#!/usr/bin/env sh

python3 -m twine upload --repository testpypi dist/*
python3 -m twine upload --repository testpypi wheelhouse/*
