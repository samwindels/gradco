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
    extra_compile_args = sysconfig.get_config_var('CFLAGS').split()
    extra_compile_args += ["-Wall", "-Wextra"]
    if _DEBUG:
        extra_compile_args += ["-g3", "-O0", "-DDEBUG=%s" % _DEBUG_LEVEL, "-UNDEBUG"]
    else:
        extra_compile_args += ["-DNDEBUG", "-O2"]  # careful, does this compile for current system architecture only?

    print(extra_compile_args)
    setup(name="gradco",
          version="1.0.0",
          description="Python interface for the fputs C library function",
          author="<your name>",
          author_email="your_email@gmail.com",
          ext_modules=[Extension("gradco", 
                                 ["gradco_module.c"],
                                 include_dirs=[np.get_include()],
                                 extra_compile_args=extra_compile_args
                                 )
                       ]
          )

if __name__ == "__main__":
    main()

