from setuptools import setup, find_packages
import pathlib


setup(
    name='CICD_PipeLine',
    version='7.1.3',
    python_requires=">=3.8",
    install_requires=[
        'pytest','labels','pandas','numpy'
    ],
    packages=find_packages(where="src")
)
