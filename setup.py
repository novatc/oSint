"""
Setup file for building binaries
"""
from setuptools import setup, find_packages

setup(name='oSint',
    version='1.0',
    packages=find_packages(include=['oSint', 'oSint.*']),
    classifiers=[
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    ]
    )
