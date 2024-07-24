from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return list of requirements
    from requirements.txt file
    '''
    # Initializing blank requirements list
    requirements = []

    # Opening the file
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        # Remove hyphen_e_dot if present in requirements
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name = 'Gemstone Price Prediction',
    version= '0.0.1',
    author='Raju Meher',
    author_email='minitable2023@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)