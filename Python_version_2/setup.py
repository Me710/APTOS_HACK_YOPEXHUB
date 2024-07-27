from setuptools import setup, find_packages

setup(
    name="yopex",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "aptos-sdk==0.5.0",
        "PyYAML==6.0",
    ],
    entry_points={
        "console_scripts": [
            "yopex=main:main",
        ],
    },
)