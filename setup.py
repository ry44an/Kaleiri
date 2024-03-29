from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Bruteforcing Hashes'
LONG_DESCRIPTION = 'A package that allows programmers to bruteforce hashes that are SHA-256, SHA-512, SHA-1, MD5, SHA-224, SHA-384, and all SHA3 hashing algorithms.'

# Setting up
setup(
    name="kaleiri",
    version=VERSION,
    author="ry44an",
    author_email="ry44an.bot@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'hashing', 'cryptography', 'bruteforce', 'cracking', 'secret'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)