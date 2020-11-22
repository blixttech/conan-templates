from conans import ConanFile, CMake, tools
import os
import re
import configparser


class SomeNameConan(ConanFile):
    name = "somename"
    description = "Description of what is being built goes here"
    topics = ("some topic")
    url = "https://github.com/blixttech/conan-libname"
    homepage = "https://github.com/original_author/original_lib"
    license = "	Apache-2.0"  # Use SPDX Identifiers https://spdx.org/licenses/

    exports_sources = ["CMakeLists.txt", "src/*"]
    generators = "cmake"

    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = {"shared": False}

    _cmake = None

    def set_version(self):
        if not self.version:
            git = tools.Git(folder=self.recipe_folder)
            version = re.sub(".*/", "", str(git.get_branch()))
            self.version = version

    def _configure_cmake(self):
        if not self._cmake:
            self._cmake = CMake(self)
            self._cmake.configure()
        # Do other changes to cmake in here
        return self._cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
