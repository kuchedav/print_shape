"""

Quick way:
pip install cookiecutter
cookiecutter gh:ionelmc/cookiecutter-pythonlibrary


follow the manual under this link:
https://dzone.com/articles/executable-package-pip-install

Great but long video:
https://www.youtube.com/watch?v=GIF3LaRqgXo

After you have filled you the setup.py file, wrote your README.md and 
copied all your functions into ./src you can run the command to create the packge.

Command to create package
    python setup.py bdist_wheel

in the same directory run this commadn to test install the package
    pip install -e .

Git ignore some files:
https://www.toptal.com/developers/gitignore

Create a licence file for the package:
https://choosealicense.com
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='forlong',  
    version='0.0.1',
    py_modules=['forlong'] ,
    author="David Kuchelmeister",
    author_email="kuchelmeister.david@gmail.com",
    description="for_long facilitates long running loops",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kuchedav/for_long.git",
    package_dir={"":"src"},
    # find good classifiers under this link: https://pypi.org/classifiers/
    classifiers=[
        
    ],
    # list all used packages in this section!
    install_requires=[
        "package_name ~= 1.7"
    ],
)