#!/usr/bin/env sh

python3 -m twine upload dist/*
python3 -m twine upload wheelhouse/*
