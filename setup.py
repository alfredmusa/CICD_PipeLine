import os
import sys
import setuptools
import pkg_resources
from setuptools import setup

classifiers = [
    "Development Status :: 6 - Mature",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: POSIX",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: MacOS :: MacOS X",
    "Topic :: Software Development :: Testing",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
] + [
    ("Programming Language :: Python :: %s" % x)
    for x in "2 2.7 3 3.4 3.5 3.6 3.7".split()
]

def get_environment_marker_support_level():
    try:
        version = pkg_resources.parse_version(setuptools.__version__)
        if version >= pkg_resources.parse_version("36.2.2"):
            return 2
        if version >= pkg_resources.parse_version("0.7.2"):
            return 1
    except Exception as exc:
        sys.stderr.write("Could not test setuptool's version: %s\n" % exc)

    # as of testing on 2018-05-26 fedora was on version 37* and debian was on version 33+
    # we should consider erroring on those
    return 0


def main():
    extras_require = {}
    install_requires = [
        "py>=1.5.0",
        "six>=1.10.0",
        "setuptools",
        "attrs>=17.4.0",
        "more-itertools>=4.0.0",
        "atomicwrites>=1.0",
    ]
    # if _PYTEST_SETUP_SKIP_PLUGGY_DEP is set, skip installing pluggy;
    # used by tox.ini to test with pluggy master
    if "_PYTEST_SETUP_SKIP_PLUGGY_DEP" not in os.environ:
        install_requires.append("pluggy>=0.5,<0.7")
    environment_marker_support_level = get_environment_marker_support_level()
    if environment_marker_support_level >= 2:
        install_requires.append('funcsigs;python_version<"3.0"')
        install_requires.append('colorama;sys_platform=="win32"')
    elif environment_marker_support_level == 1:
        extras_require[':python_version<"3.0"'] = ["funcsigs"]
        extras_require[':sys_platform=="win32"'] = ["colorama"]
    else:
        if sys.platform == "win32":
            install_requires.append("colorama")
        if sys.version_info < (3, 0):
            install_requires.append("funcsigs")

    setup(
        name="CICD_PipeLine",
        version='7.1.3',
        license="MIT license",
        platforms=["unix", "linux", "osx", "cygwin", "win32"],
        entry_points={"console_scripts": ["pytest=pytest:main", "py.test=pytest:main"]},
        classifiers=classifiers,
        # the following should be enabled for release
        setup_requires=["setuptools-scm"],
        package_dir={"": "src"},
        python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
        install_requires=install_requires,
        extras_require=extras_require,
        packages=[
            "_pytest",
            "_pytest.assertion",
            "_pytest._code",
            "_pytest.mark",
            "_pytest.config",
        ],
        py_modules=["pytest"],
        zip_safe=False,
    )


if __name__ == "__main__":
    main()
