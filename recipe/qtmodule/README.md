# Structure of the conan recipe for building a Qt module

This folder contains structure the conan recipe for building a Qt module.
Note that the recipe in the ``conanfile.py`` file is an extended recipe from ``QtModuleConanBase``.
This requires the followings to be added to the ``conanfile.py``.

```python
    python_requires = "qtmodulepyreq/0.1.0"
    python_requires_extend = "qtmodulepyreq.QtModuleConanBase"
```