from os import path

from setuptools import find_packages, setup

root = path.abspath(path.dirname(__file__))
with open(path.join(root, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="metadata_filter",
    version="0.1.0",
    description="Metadata filters for scrobblers",
    url="https://github.com/YodaEmbedding/metadata-filter",
    author="Mateen Ulhaq",
    author_email="mulhaq2005@gmail.com",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    tests_require=["pytest"],
    zip_safe=False,
)
