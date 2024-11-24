from setuptools import setup, find_packages

setup(
    name="iterr",
    version="0.1.0",
    description="type-checked, lazy, rust-styled iterator",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Allen Chen",
    author_email="allenchenyilun1999@gmail.com",
    url="https://github.com/YilunAllenChen/iter",
    packages=find_packages(),
    install_requires=[],  # List dependencies here
    test_requires=["pytest"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
