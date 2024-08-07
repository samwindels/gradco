from setuptools import setup, Extension, find_packages
import os
import sysconfig
import numpy as np


def main():

    c_module = Extension("gradco_c_routines",
                         sources=["c_module/directed_graph.cpp",
                                  "c_module/gradco_module.cpp",
                                  "c_module/sparse_matrix.cpp",
                                  "c_module/dense_matrix.cpp",
                                  "c_module/symmetric_dense_matrix.cpp",
                                  ],
                         depends=["c_module/unordered_dense.h",
                                  "c_module/sparse_matrix.hh",
                                  "c_module/dense_matrix.hh",
                                  "c_module/symmetric_dense_matrix.hh",
                                  "c_module/directed_graph.hh"],
                         include_dirs=[np.get_include(), "."],
                         language='c++',
                         extra_compile_args=['-std=c++17', '-O3'],
                         )
    # c++20
    # gnu++20
    # c++2b => 23 working draft
    # gnu++2b => working draft with GNU extensions

    setup(
        ext_modules=[c_module],
        py_modules=["gradco", "tests"],
    )


if __name__ == "__main__":
    main()
