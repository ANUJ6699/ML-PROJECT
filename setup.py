from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """This function returns the list of requirements."""
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='MLPROJECT1',
    version='0.0.1',
    author='Anuj Chhetri',
    author_email='anuj.chhetri261@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
