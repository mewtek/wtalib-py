from setuptools import find_packages, setup

setup(
    name="wtalib",
    packages=find_packages(include=['wtalib']),
    version="0.0.1",
    description="Asynchronous python library for the Whatcom Transit Authority API",
    author="mewtek",
    install_requires=['aiohttp'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-asyncio'],
    test_suite='tests'
)