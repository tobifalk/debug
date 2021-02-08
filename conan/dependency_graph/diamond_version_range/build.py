import os
# adapted from:
#  https://github.com/memsharded/tools_build_requires


def run(cmd):
    ret = os.system(cmd)
    if ret != 0:
        raise Exception(cmd)


run("cd boost && conan create . TMP-boost/1.69.0@user/testing")
run("cd boost && conan create . TMP-boost/1.75.0@user/testing")
run("cd cpp-netlib && conan create . user/testing")
run("cd util-lib && conan create . user/testing")
run("cd app && conan create . user/testing")