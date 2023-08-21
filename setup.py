from distutils.core import setup, Extension
import os
import sysconfig
import numpy as np


def main():

    _DEBUG = False
    # Generally I write code so that if DEBUG is defined as 0 then all optimisations
    # # are off and asserts are enabled. Typically run times of these builds are x2 to x10
    # # release builds.
    # # If DEBUG > 0 then extra code paths are introduced such as checking the integrity of
    # # internal data structures. In this case the performance is by no means comparable
    # # with release builds.
    # _DEBUG_LEVEL = 0
    #
    # # Common flags for both release and debug builds.
    # extra_compile_args = sysconfig.get_config_var('CFLAGS').split()
    # extra_compile_args += ["-Wall", "-Wextra"]
    # if _DEBUG:
    #     extra_compile_args += ["-g3", "-O0",
    #                            "-DDEBUG=%s" % _DEBUG_LEVEL, "-UNDEBUG"]
    # else:
    #     # careful, does this compile for current system architecture only?
    #     extra_compile_args += ["-DNDEBUG", "-O2"]

    # print(extra_compile_args)
    
    gradco_module = Extension("gradco",
                              sources=["directed_graph.cpp", 
                                       "gradco_module.cpp",
                                       "matrix.cpp"],
                              depends=["unordered_dense.h", 'matrix.hh'],
                              # headers=["unordered_dense.h", 'matrix.hh'],
                              # library_dirs=['/opt/local/lib/boost'],
                              # library_dirs=['/opt/local/libexec/boost/1.76/lib/'],
                              # runtime_library_dirs=['/opt/local/libexec/boost/1.76/lib/'],
                              # runtime_library_dirs=['/opt/local/lib/boost'],
                              # libraries=['boost_python'],
                              # include_dirs=['/opt/local/include', np.get_include()],
                              # include_dirs=['/opt/local/include/boost/', np.get_include()],
                              include_dirs=[ np.get_include(), "."],
                              language='c++',
                              # extra_compile_args=['-std=c++17', "-O3", "-march=native"]
                              extra_compile_args=['-std=c++20', "-O3", "-march=native"]
                              # extra_compile_args=['-std=c++20', '-g', '-O0']
                              # extra_compile_args=['-std=c++20', "-O2"]
                              )

    # c++20 
    # gnu++20 
    # c++2b => 23 working draft 
    # gnu++2b => working draft with GNU extensions 


    setup(name="gradco",
          version="0.0.2",
          description="Orbit adjacency counter.",
          author="Sam Windels",
          author_email="sam.windels@gmail.com",
          # setup_requires=["numpy"],  # Just numpy here
          # install_requires=["numpy"],  # Add any of your other dependencies here
          ext_modules=[gradco_module]
          )


if __name__ == "__main__":
    main()
