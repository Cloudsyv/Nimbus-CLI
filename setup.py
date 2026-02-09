from setuptools import setup, find_packages

setup(
    name="nimbus-cli",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'nimbus=src.main:run',
        ],
    },
)