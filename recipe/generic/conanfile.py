from conans import ConanFile, CMake, tools
import os
import re
import configparser


class SomeNameConan(ConanFile):
    name = "somename"
    description = "Description of what is being built goes here"
    topics = ("some topic")
    # URL of the conan recipe repository
    url = "https://github.com/blixttech/conan-libname"
    # Homepage of the original source repository
    homepage = "https://github.com/original_author/original_lib"
    # License of the package being built. Use SPDX Identifiers https://spdx.org/licenses/
    license = "	Apache-2.0"

    exports_sources = ["CMakeLists.txt", "src/*"]
    generators = "cmake"

    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = {"shared": False}

    _git_is_dirty = False
    _git_commit = "unknown"
    _cmake = None

    def set_version(self):
        git = tools.Git(folder=self.recipe_folder)
        if not self.version:
            output = git.run("describe --all").splitlines()[0].strip()
            self.version = re.sub("^.*/v?|^v?", "", output)
        output = git.run("diff --stat").splitlines()
        self._git_is_dirty = True if output else False
        self._git_commit = git.run("rev-parse HEAD").splitlines()[0].strip()

        self.output.info("Version: %s, Commit: %s, Is_dirty: %s" %
                         (self.version, self._git_commit, self._git_is_dirty))

    def _configure_cmake(self):
        if not self._cmake:
            self._cmake = CMake(self)
            # Use the followings to pass versions, commit hash, etc to the source of the
            # package being built. 
            """
            self._cmake.definitions["SOURCE_VERSION"] = self.version
            self._cmake.definitions["SOURCE_COMMIT"] = self._git_commit
            self._cmake.definitions["SOURCE_DIRTY"] = self._git_is_dirty
            """
            # Use the something similar to the following to load conanbuildinfo.cmake in the
            # CMakeLists.txt file 
            self._cmake.definitions["USE_CONAN_BUILD_INFO"] = "ON"
            self._cmake.configure()
        return self._cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
