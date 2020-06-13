import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FixtureGenerator",
    version="0.1",
    author="Germán Henríquez",
    author_email="germanandres.hv@gmail.com",
    description="Generates pytest fixtures that allow the use of type hinting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/G-HenriquezV/FixtureGenerator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': ['pytest-factoryboy-fixtures=fixturegenerator.command:main'],
    }
)