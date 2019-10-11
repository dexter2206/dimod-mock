"""Setup file for dimodmock package"""
from setuptools import setup, find_packages

with open("README.md") as description_file:
    long_description = description_file.read()


setup(
    name="dimodmock",
    use_scm_version=True,
    description="Utilities for mocking dimod Samplers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Konrad Jałowiecki",
    author_email="dexter2206@gmail.com",
    packages=find_packages(exclude="tests"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["dimod"],
    tests_require=["dimod", "pytest", "pytest-mock"],
    setup_requires=["setuptools_scm"],
    keywords="dimod mock testing"
)
