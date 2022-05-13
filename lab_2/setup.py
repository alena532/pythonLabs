from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="fpars",
    version="5.2.3",
    description="Demo library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alena532?tab=projects",
    author="Alena Vorobey",
    author_email="alena.vorobey.03@mail.ru",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(),
    include_package_data=True,
)