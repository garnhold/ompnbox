import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ompnbox",
    version="0.0.1",
    author="Garrett Arnhold",
    author_email="garrett@arnholdsystems.com",
    description="Utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[],
    python_requires='>=3.7',
)