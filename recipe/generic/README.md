# Structure of the generic conan recipe

This folder contains the structure of a generic conan recipe.
Note that the ``conanfile.py`` file is only a skeleton that highlights important functions.
Refer the documentation of [``conanfile.py``](https://docs.conan.io/en/latest/reference/conanfile.html) for the complete reference.

## Use of ``build.py`` file

The ``build.py`` file is a script that uses Conan Package Tools (CPT) for creating conan packages with different build configurations.
Refer the documentation of [CPT](https://github.com/conan-io/conan-package-tools) for more details.

``cpt-helpers`` is a python package which provides additional helper classes and functions to be used in the ``build.py`` file.
``cpt-helpers`` can be installed using the following command. 

```bash
pip install git+https://github.com/blixttech/cpt-helpers.git
```