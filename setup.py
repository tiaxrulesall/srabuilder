from distutils.core import setup
from setuptools import find_packages
import distutils.text_file
import sys
from pathlib import Path
from typing import List

def _parse_requirements(filename: str) -> List[str]:
    """Return requirements from requirements file."""
    # Ref: https://stackoverflow.com/a/42033122/
    return distutils.text_file.TextFile(filename=str(Path(__file__).with_name(filename))).readlines()

install_requires= [
    "dfly-breathe", 
    "git+https://github.com/tiaxrulesall/kaldi-active-grammar/releases/download/mac-build-hotfix/kaldi_active_grammar-3.1.0-py2.py3-none-macosx_13_0_arm64.whl"
]

setup(
    name='srabuilder',
    version='0.0.1',
    packages=find_packages(),
    install_requires=install_requires,
    license='MIT',
    long_description='placeholder',
)