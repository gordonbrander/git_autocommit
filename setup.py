from setuptools import setup, find_packages
from os import path

readme_path = path.join(path.dirname(__file__), "README.md")
with open(readme_path) as f:
    readme = f.read()

setup(
    name='git_autocommit',
    version='0.0.1',
    author='Gordon Brander',
    description='Automatically commit to git whenever changes occur.',
    long_description=readme,
    license="MIT",
    url="https://github.com/gordonbrander/git_autocommit",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.7",
    ],
    packages=find_packages(exclude=("tests", "tests.*")),
    install_requires=[],
    extras_require={},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'autocommit=git_autocommit:main'
        ]
    }
)
