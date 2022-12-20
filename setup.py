from setuptools import find_packages,setup


def get_requirements():
    pass

setup(
    name="sensor",
    version="0.01",
    author="ineuron",
    author_email="dharavathdas101@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),
)