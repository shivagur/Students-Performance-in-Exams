

from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'

'''here below in setup function we have install_requires and we may not be able to specify all the packages what we need explicitly so 
    this func will take care of that for us'''


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='MachineLearning_Project',
    version='0.0.1',
    author='omshivasai',
    author_email='shivasaigurrapu@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)
