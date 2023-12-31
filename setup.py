from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="isopsephism",
    description="null",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="null",
    url="https://github.com/uggerus/isopsephism",
    project_urls={
        "Issues": "https://github.com/uggerus/isopsephism/issues",
        "CI": "https://github.com/uggerus/isopsephism/actions",
        "Changelog": "https://github.com/uggerus/isopsephism/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["isopsephism"],
    install_requires=[],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.7",
)
