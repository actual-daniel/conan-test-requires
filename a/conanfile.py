from conans import ConanFile, CMake, tools

class PkgA(ConanFile):
    name = "PkgA"

    def requirements(self):
        pass 
    def build_requirements(self):
        pass
    
    def build(self):
        pass