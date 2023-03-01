from conans import ConanFile, CMake, tools

class PkgB(ConanFile):
    name = "PkgB"

    def requirements(self):
        self.requires("PkgA/1.0.0")

    def build_requirements(self):
        pass
    
    def build(self):
        pass