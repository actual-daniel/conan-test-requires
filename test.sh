#!/bin/bash -e

rm -rf /tmp/conan
mkdir /tmp/conan
export CONAN_USER_HOME=/tmp/conan
conan remote remove conancenter

conan create a/conanfile.py PkgA/1.0.0@_/_
conan create a/conanfile.py PkgA/2.0.0@_/_

conan create b/conanfile.py PkgB/1.0.0@_/_

conan create c/conanfile.py PkgC/1.0.0@_/_

conan create x/conanfile.py PkgX/1.0.0@_/_ --build missing --build PkgC