from conans import ConanFile, CMake


class TmpApp(ConanFile):
    name = 'TMP-app'
    version = '1.0.0'

    def requirements(self):
        self.requires("TMP-cpp-netlib/1.0.0@user/testing")
        self.requires("TMP-util-lib/1.0.0@user/testing")
        # This avoids the issue:
        #self.requires("TMP-boost/[>=1.65.0 <1.70]@user/testing", override=True)
