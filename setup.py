from setuptools import find_packages, setup

setup(
    name="wtalib",
    packages=find_packages(include=['wtalib-py']),
    version="0.0.1",
    description="Asynchronous python library for the Whatcom Transit Authority API",
    author="mewtek",
    install_requires=['aiohttp'],
    tests_require=['pytest', 'pytest-asyncio'],
    test_suite='tests'
)