import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tk-oddbox",
    version="0.0.1",
    author="Andrew Allaire",
    author_email="andrew.allaire@gmail.com",
    description="A few odd tkinter utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aallaire/python_tk_oddbox",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)