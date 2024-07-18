#!/usr/bin/env sh
#
# all possible wheels: https://github.com/pypa/cibuildwheel/blob/main/cibuildwheel/resources/build-platforms.toml
# default cibuildwheel settings: https://github.com/pypa/cibuildwheel/blob/main/cibuildwheel/resources/defaults.toml

# numpy supports (from their docs):
    # Windows: 32-bit and 64-bit wheels built using Github actions;
    # OSX: x64_86 and arm64 OSX wheels built using Github actions;
    # Linux: x64_86 and aarch64 Manylinux2014 wheels built using Github actions.
    # (Mussle linux aarch64 seems to fail here as no binary is provied)


# build wheels

# MACOS
# pipx run cibuildwheel --only "cp310-macosx_arm64"
# pipx run cibuildwheel --only "cp311-macosx_arm64"
pipx run cibuildwheel --only "cp312-macosx_arm64"
# pipx run cibuildwheel --only "cp313-macosx_arm64" # FAILS: numpy compilation

# pipx run cibuildwheel --only "cp310-macosx_x86_64"
# pipx run cibuildwheel --only "cp311-macosx_x86_64"
# pipx run cibuildwheel --only "cp312-macosx_x86_64"
# pipx run cibuildwheel --only "cp313-macosx_x86_64" # FAILS: numpy compilation

# pipx run cibuildwheel --only "cp310-macosx_universal2"
# pipx run cibuildwheel --only "cp311-macosx_universal2"
# pipx run cibuildwheel --only "cp312-macosx_universal2"
# pipx run cibuildwheel --only "cp313-macosx_universal2" # FAILS: numpy compilation

# pipx run cibuildwheel --only "pp310-macosx_x86_64" # FAILS: scipy compilation
# pipx run cibuildwheel --only "pp310-macosx_arm64"  # FAILS: scipy compilation


# MANYLINUX (glibc)

# pipx run cibuildwheel --only "cp310-manylinux_x86_64"
# pipx run cibuildwheel --only "cp311-manylinux_x86_64"
# pipx run cibuildwheel --only "cp312-manylinux_x86_64"
# pipx run cibuildwheel --only "cp313-manylinux_x86_64"  # FAILS: does not show up in wheelhouse
# pipx run cibuildwheel --only "cp313t-manylinux_x86_64" # FAILS: gradco does not compile

# pipx run cibuildwheel --only "cp310-manylinux_i686"   # FAILS: does not show up in wheelhouse
# pipx run cibuildwheel --only "cp311-manylinux_i686"   # FAILS: does not show up in wheelhouse
# pipx run cibuildwheel --only "cp312-manylinux_i686"  # FAILS: does not show up in wheelhouse
# pipx run cibuildwheel --only "cp313-manylinux_i686"  # not tested
# pipx run cibuildwheel --only "cp313t-manylinux_i686" # not tested

# pipx run cibuildwheel --only "pp310-manylinux_x86_64" 

# pipx run cibuildwheel --only "cp310-manylinux_aarch64"
# pipx run cibuildwheel --only "cp311-manylinux_aarch64"
# pipx run cibuildwheel --only "cp312-manylinux_aarch64"
# pipx run cibuildwheel --only "cp313-manylinux_aarch64"  # not tested 
# pipx run cibuildwheel --only "cp313t-manylinux_aarch64" # not tested

# pipx run cibuildwheel --only "cp310-manylinux_ppc64le"
# pipx run cibuildwheel --only "cp311-manylinux_ppc64le"
# pipx run cibuildwheel --only "cp312-manylinux_ppc64le"
# pipx run cibuildwheel --only "cp313-manylinux_ppc64le"  # not tested
# pipx run cibuildwheel --only "cp313t-manylinux_ppc64le" # not tested

# pipx run cibuildwheel --only "cp310-manylinux_s390x"
# pipx run cibuildwheel --only "cp311-manylinux_s390x"
# pipx run cibuildwheel --only "cp312-manylinux_s390x"
# pipx run cibuildwheel --only "cp313-manylinux_s390x"  # not tested
# pipx run cibuildwheel --only "cp313t-manylinux_s390x" # not tested

# pipx run cibuildwheel --only "pp310-manylinux_aarch64" # FAILS: scipy compilation
# pipx run cibuildwheel --only "pp310-manylinux_i686" # FAILS: scipy compilation

# MUSLLINUX (musl)


# DOCKER issues

# pipx run cibuildwheel --only "cp310-musllinux_x86_64"
# pipx run cibuildwheel --only "cp311-musllinux_x86_64"
# pipx run cibuildwheel --only "cp312-musllinux_x86_64"
# pipx run cibuildwheel --only "cp313-musllinux_x86_64" # not tested
# pipx run cibuildwheel --only "cp313t-musllinux_x86_64" # not tested

# pipx run cibuildwheel --only "cp310-musllinux_i686"  # not tested
# pipx run cibuildwheel --only "cp311-musllinux_i686" # not tested
# pipx run cibuildwheel --only "cp312-musllinux_i686" # not tested
# pipx run cibuildwheel --only "cp313-musllinux_i686" # not tested
# pipx run cibuildwheel --only "cp313t-musllinux_i686" # not tested

# pipx run cibuildwheel --only "cp310-musllinux_aarch64" # fails on numpy
# pipx run cibuildwheel --only "cp311-musllinux_aarch64" # fails on numpy
# pipx run cibuildwheel --only "cp312-musllinux_aarch64" # fails on numpy
# pipx run cibuildwheel --only "cp313-musllinux_aarch64" # not tested
# pipx run cibuildwheel --only "cp313t-musllinux_aarch64" # not tested

# pipx run cibuildwheel --only "cp310-musllinux_ppc64le"
# pipx run cibuildwheel --only "cp311-musllinux_ppc64le"
# pipx run cibuildwheel --only "cp312-musllinux_ppc64le"
# pipx run cibuildwheel --only "cp313-musllinux_ppc64le" # not tested
# pipx run cibuildwheel --only "cp313t-musllinux_ppc64le" # not tested

# pipx run cibuildwheel --only "cp310-musllinux_s390x"  # failed on numpy
# pipx run cibuildwheel --only "cp311-musllinux_s390x"  # failed on numpy
# pipx run cibuildwheel --only "cp312-musllinux_s390x"  # failed on numpy
# pipx run cibuildwheel --only "cp313-musllinux_s390x" # not tested
# pipx run cibuildwheel --only "cp313t-musllinux_s390x" # not tested

# WINDOWS
# pipx run cibuildwheel --only "cp310-win32"
# pipx run cibuildwheel --only "cp310-win_amd64"
# pipx run cibuildwheel --only "cp311-win_32"
# pipx run cibuildwheel --only "cp311-win_amd64"
# pipx run cibuildwheel --only "cp312-win32"
# pipx run cibuildwheel --only "cp312-win_amd64"
# pipx run cibuildwheel --only "cp313-win32"
# pipx run cibuildwheel --only "cp313-win_amd64"
# pipx run cibuildwheel --only "cp313t-win32"
# pipx run cibuildwheel --only "cp313t-win_amd64"
# pipx run cibuildwheel --only "cp310-win_arm64"
# pipx run cibuildwheel --only "cp311-win_arm64"
# pipx run cibuildwheel --only "cp312-win_arm64"
# pipx run cibuildwheel --only "cp313-win_arm64"
# pipx run cibuildwheel --only "cp313t-win_arm64"
# pipx run cibuildwheel --only "pp310-win_amd64"
