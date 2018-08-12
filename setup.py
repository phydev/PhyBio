"""
this setup will check for dependencies and install PhyBio on your computer
"""
from setuptools import setup, find_packages

setup(
    name = "PhyBio",
    version = "0.0.1",
    url = "https://gitlab.com/phydev/phybio.git",
    author = "Mauricio Moreira",
    author_email = "mmsoares@uc.pt",
    description = "Easing the study of phase-field models in biology",
    license = "GNU GPLv3",
    platform = "Python 3.6",
    packages = find_packages(),
    install_requires = ["numpy >= 1.14.3"],
)
