import os

from setuptools import setup, find_packages

requirements = [
    "logging",
    "colorama",
]

def get_requirements():
    if not os.path.exists("requirements.txt"): return None
    requirements = []
    with open("requirements.txt") as f:
        _requirements = f.read().splitlines()
        for requirement in _requirements:
            rq = requirement.split("=")[0].replace("~", "").replace(">", "").replace("<", "")
            if rq in requirements or rq == "setuptools":
                continue
            requirements.append(rq)
    return requirements

requirements = get_requirements() or requirements

_version = "0.1.1"

with open(__file__.rstrip("setup.py") + "README.md", "r") as f:
    long_description = f.read().replace("> [!WARNING]", "WARNING")

setup(
    name="dantools",
    version=_version,
    author="Daniil10295",
    author_email="chernyak.daniil.2010@gmail.com",
    url="https://github.com/Daniil10295/dantools",
    description="dantools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    entry_points={"console_scripts": ["Daniil10295 = dantools.main:main"]},
)
