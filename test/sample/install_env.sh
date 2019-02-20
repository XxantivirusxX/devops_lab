#!/bin/bash




pyenv install 2.7.15
pyenv install 3.7.1

pyenv global 3.7.1

mkdir python-virtual-environments && cd python-virtual-environments

virtualenv -p python2 --no-site-packages --prompt="(Test)" venvpython2
virtualenv -p python3 --no-site-packages --prompt="(Test)" venvpython3

pip install twine

virtualenv --no-site-packages --prompt="(Test)" envname

