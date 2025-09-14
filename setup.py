from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> list[str]:
    """This function will return the list of requirements"""
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    return requirements






setup(
    name="python_project",
    version="0.1.0",
    author="prernakansal",
    author_email="prerna4857@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)