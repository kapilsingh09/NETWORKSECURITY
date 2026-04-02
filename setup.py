from setuptools import find_packages, setup
from typing import List

def get_requriements() ->List[str]:
    """
    This function will return the list of requirements
     mentioned in the file passed as argument
    """
    requirement_list: List[str] = []
    try:
        with open('requirements.txt','r') as f:
            #read lines from the file
            lines = f.readlines()
            for line in lines:

                requirement = line.strip()

                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)

    except FileNotFoundError as e:
        print("requirements.txt not found - ",e)


    return requirement_list

# print(get_requriements())

setup(
    name='NetworkSecutiry',
    version='0.0.01',
    author='Kapil',
    author_email="karan404katyura@gamil.com",
    packages=find_packages(),
    install_requires=get_requriements()
)