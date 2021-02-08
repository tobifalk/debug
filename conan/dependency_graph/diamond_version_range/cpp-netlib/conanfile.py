from conans import ConanFile, CMake


class TmpCppNetlib(ConanFile):
    name = 'TMP-cpp-netlib'
    version = '1.0.0'
    requires = ("TMP-boost/[>=1.65.0 <1.70]@user/testing")
