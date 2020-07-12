import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='print_structure',  
    version='0.0.1',
    py_modules=['print_structure'] ,
    author="David Kuchelmeister",
    author_email="kuchelmeister.david@gmail.com",
    description="Print structure of any arbitrary python object",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kuchedav/print_structure.git",
    package_dir={"":"src"},
    # find good classifiers under this link: https://pypi.org/classifiers/
    # list all used packages in this section!
    install_requires=[
        "pandas ~= 1.0.1",
	"numpy ~= 1.14.5"
    ],
)
