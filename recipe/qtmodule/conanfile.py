from conans import ConanFile, tools


class QtModuleConan(ConanFile):
    name = "qtmodule"
    description = "Description of the module"
    topics = ("sometopic")
    url = "https://github.com/blixttech/conan-qtmodule.git"
    homepage = "https://code.qt.io/cgit/qt/qtmodule.git"
    license = "LGPL-3.0"

    python_requires = "qtmodulepyreq/0.1.0"
    python_requires_extend = "qtmodulepyreq.QtModuleConanBase"

    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = {"shared": True}
