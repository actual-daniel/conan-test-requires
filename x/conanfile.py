from conans import ConanFile, CMake, tools

class PkgX(ConanFile):
    name = "PkgX"

    def requirements(self):
        self.requires("PkgA/2.0.0")
        self.requires("PkgC/1.0.0")
    
    def build(self):
        pass