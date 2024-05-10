from setuptools import setup, find_packages

setup(
    name='FinderZ',
    version='2.1.2',
    description='A tool for gathering information about files and directories',
    author='Vivek Shravan Tate',
    author_email='vivektate.developer@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'finderz = FinderZV2:main'
        ]
    },
    install_requires=[
        'sphinx-rtd-theme',
    ],
)
