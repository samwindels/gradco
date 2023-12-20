from setuptools import setup, Extension, find_packages
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
    
    c_module = Extension("gradco_c_routines",
                              sources=["c_module/directed_graph.cpp", 
                                       "c_module/gradco_module.cpp",
                                       "c_module/matrix.cpp"],
                              depends=["c_module/unordered_dense.h", 
                                       'c_module/matrix.hh', 
                                       "c_module/directed_graph.hh"],
                              include_dirs=[ np.get_include(), "."],
                              language='c++',
                              extra_compile_args=['-std=c++17', "-O2"]
                              )

    # c++20 
    # gnu++20 
    # c++2b => 23 working draft 
    # gnu++2b => working draft with GNU extensions 

    setup(name="gradco",  # Name of the package. Used e.g. by pip to install the package.
          version="0.0.2",
          description="Orbit adjacency counter.",
          author="Sam Windels",
          author_email="sam.windels@gmail.com",
          ext_modules=[c_module],
          py_modules=["gradco"],  # Refers to gradco.py. Name of the module.
          )


if __name__ == "__main__":
    main()
