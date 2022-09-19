from setuptools import find_packages, setup

setup(
    name="SeAPI",
    packages=find_packages(),
    version="0.0.2",
    description="ShipEngine API Library",
    author="Rolando Diaz Cruz",
    license="MIT",
    install_requires=["aiohttp"],
)
