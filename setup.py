import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="optimization-ahujaradhika", 
    version="0.0.1",
    author="Radhika Ahuja",
    author_email="ahujaradhika18@gmail.com",
    description="A package for common optimization techniques",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ahujaradhika/optimization",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)