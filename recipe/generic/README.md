# Structure of a generic conan recipe

This directory contains the structure of a generic conan recipe for ``cmake`` based projects.
Note that the ``conanfile.py`` file is only a skeleton that highlights important functions.
Refer the conan [reference](https://docs.conan.io/en/latest/reference/conanfile.html) for more details.

## Build with ``build.py``

The ``build.py`` file is a script that uses Conan Package Tools (CPT) for creating conan packages with different build configurations.
Refer the documentation of [CPT](https://github.com/conan-io/conan-package-tools) for more details.

``cpt-helpers`` is a python package which provides additional helper classes and functions to be used in the ``build.py`` file.
``cpt-helpers`` package can be installed using the following command. 

```bash
pip install git+https://github.com/blixttech/cpt-helpers.git
```

Refer documentation of [cpt-helpers](https://github.com/blixttech/cpt-helpers) for more details.


If build parameters are not set in the ``build.py`` file, they have to be set using environmental variables.

Following shows settings for the environmental variables for a release build on Linux using a docker image.
```bash
# Set environmental variables
$ export CONAN_GCC_VERSIONS=7 
$ export CONAN_ARCHS="x86_64" 
$ export CONAN_BUILD_TYPES="Release" 
$ export CONAN_USER="" 
$ export CONAN_CHANNEL="" 
$ export CONAN_DOCKER_IMAGE="conanio/gcc7" 
$ export CONAN_REMOTES="https://api.bintray.com/conan/blixttech/conan-packages@True@blixttech"
# Run build script
$ python build.py
```

## Build with ``conan create`` command

As ``conan create`` command builds only for a specific build configuration, environmental variable settings are not required.
Instead conan profiles can be used to specify the build configurations.

```bash
conan create . user/channel
```

Refer the documentation of [conan profiles](https://docs.conan.io/en/latest/reference/profiles.html) for more details.

## Git repository branching and versioning

Version of the conan package being built depends on the branch of the recipe's git repository unless it is specified in the ``conanfile.py`` file explicitly.

For example, if the branch of the recipe's git repository is ``testing/x.y.z``, the version of the conan package will be ``x.y.z``.
In other words, everything before and including ``/`` is removed when constructing the conan package version.
This convention can also be applied when both source and recipe in the same repository.
