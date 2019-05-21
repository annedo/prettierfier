import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="prettierfier-anne_do",
    version="1.0.0",
    author="Anne Do",
    author_email="anne.do.designs@gmail.com",
    description="Intelligently pretty-print HTML/XML with inline tags.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/annedo/prettierfier",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows 10",
    ],
)