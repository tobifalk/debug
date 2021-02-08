from conans import ConanFile, CMake


class TmpUtilLib(ConanFile):
    name = 'TMP-util-lib'
    version = '1.0.0'
    requires = ("TMP-boost/[>=1.65.0]@user/testing")
