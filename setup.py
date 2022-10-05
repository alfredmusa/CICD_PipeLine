from setuptools import setup

requirements = [
    'pytest'
]


setup(
    name="downloader_cli",
    version='7.1.3',
    packages=find_packages(where="src"),
    install_requires=requirements
)
