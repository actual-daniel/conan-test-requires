from conans import ConanFile, CMake, tools

class PkgC(ConanFile):
    name = "PkgC"

    def requirements(self):
        self.requires("PkgB/1.0.0")

    def build_requirements(self):
        self.test_requires("PkgA/1.0.0")
    
    def build(self):
        pass