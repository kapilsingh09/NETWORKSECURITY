from setuptools import find_packages, setup
from typing import List

def get_requriements(filepath) ->[str]:
    """
    This function will return the list of requirements
     mentioned in the file passed as argument
    """
    try:
        with open('requirements.txt') as f:
            return f.read().splitlines()

setup(
    name="networksecurity",
    version="0.1.0",
    packages=find_packages(),

)