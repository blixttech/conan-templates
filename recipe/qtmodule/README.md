# Structure of a conan recipe for building a Qt module

This directory contains structure of a conan recipe for building a Qt module.
Note that this recipe is an extended recipe from ``QtModuleConanBase`` which is provided by the conan package [``qtmodulepyreq``](https://github.com/blixttech/conan-qtmodulepyreq).

Extending conan recipes is provided by [Python requires](https://docs.conan.io/en/latest/extending/python_requires.html) feature and it requires the followings to be added to the ``conanfile.py``.

```python
class SomeNameConan(ConanFile):
    # Add the followings as class attributes
    python_requires = "qtmodulepyreq/x.y.z"
    python_requires_extend = "qtmodulepyreq.QtModuleConanBase"
```