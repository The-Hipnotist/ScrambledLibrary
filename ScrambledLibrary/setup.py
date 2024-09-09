from setuptools import setup, find_packages

setup(
    name="scrambled_library",
    version="0.1",
    packages=find_packages(),
    description="A library that takes a sentence and turns it into a completely new one using 3 methods.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="The-Hipnotist",
    url="https://github.com/The-Hipnotist/ScrambledLibrary",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'
)