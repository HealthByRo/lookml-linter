import pathlib
import setuptools


setuptools.setup(
    name="lookml-linter",
    version="1.0.0",
    author="Ro Data Infra",
    author_email="datainfra@ro.co",
    description="Linting tool to enforce LookML best practices",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/rudo-ro/lookml-linter",
    packages=setuptools.find_packages(),
    py_modules=["linter"],
    scripts=["scripts/lookmllint"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "attrs==21.4.0",
        "cattrs==22.1.0",
        "certifi==2021.10.8",
        "charset-normalizer==2.0.12",
        "exceptiongroup==1.0.0rc5",
        "idna==3.3",
        "importlib-resources==5.7.1",
        "iniconfig==1.1.1",
        "jsonschema==4.5.0",
        "lkml==1.2.0",
        "looker-sdk==22.4.0",
        "packaging==21.3",
        "pluggy==1.0.0",
        "py==1.11.0",
        "pyparsing==3.0.8",
        "pyrsistent==0.18.1",
        "pytest==7.1.2",
        "pyyaml==6.0",
        "requests==2.27.1",
        "tomli==2.0.1",
        "typing-extensions==4.2.0",
        "urllib3==1.26.9",
    ],
     entry_points={
        'console_scripts': [
            'lookml-linter = linter:main',
        ]
    }
)
