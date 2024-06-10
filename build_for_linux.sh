#!/usr/bin/env sh

# to install the docker image
# docker pull quay.io/pypa/manylinux_2_28_x86_64


# Run docker image, mounting the current directory to /io

# docker run -ti -v $(pwd):/io quay.io/pypa/manylinux_2_28_x86_64 /bin/bash

# Inside the docker image
# cd /io

# X86_64 build manylinux
docker  run -it -v $(pwd):/io quay.io/pypa/manylinux_2_28_x86_64 /opt/python/cp310-cp310/bin/python3 -m build /io

docker  run -it -v $(pwd):/io quay.io/pypa/manylinux_2_28_x86_64 /opt/python/cp311-cp311/bin/python3 -m build /io

docker  run -it -v $(pwd):/io quay.io/pypa/manylinux_2_28_x86_64 /opt/python/cp312-cp312/bin/python3 -m build /io

# AARCH64 build manylinux
# docker pull quay.io/pypa/manylinux_2_28_aarch64

docker  run -it -v $(pwd):/io quay.io/pypa/manylinux_2_28_aarch64 /opt/python/cp310-cp310/bin/python3 -m build /io

docker  run -it -v $(pwd):/io quay.io/pypa/manylinux_2_28_aarch64 /opt/python/cp311-cp311/bin/python3 -m build /io

docker  run -it -v $(pwd):/io quay.io/pypa/manylinux_2_28_aarch64 /opt/python/cp312-cp312/bin/python3 -m build /io
