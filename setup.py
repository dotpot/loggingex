import os

import setuptools


def main():
    return setuptools.setup(
        author="Paulius Maruška",
        author_email="paulius.maruska+loggingex@gmail.com",
        name="loggingex",
        url="https://github.com/open-things/loggingex/",
        packages=["loggingex", "loggingex.context"],
        package_dir={"": "src"},
        description="Logging Extensions",
        long_description=read_file("README.rst"),
        license="MIT",
        zip_safe=False,
        use_scm_version={
            "write_to": "src/loggingex/_version.py",
            "write_to_template": VERSION_FILE_TEMPLATE,
        },
        setup_requires=["setuptools_scm"],
        python_requires=">=3.5",
        install_requires=INSTALL_REQUIRES,
    )


INSTALL_REQUIRES = ['contextvars;python_version<"3.7"']

VERSION_FILE_TEMPLATE = """\
# coding: utf-8
# file generated by setuptools_scm
# don't change, don't track in version control
version = "{version}"
"""


def read_file(name):
    """Return contents of a file as text, relative to this file."""
    full_path = os.path.join(os.path.dirname(__file__), name)
    with open(full_path, "r") as f:
        return f.read()


if __name__ == "__main__":
    main()
