from setuptools import setup, find_packages

setup(
    name='idm-brand',
    version='0.1',
    description='Branding for an IdM that looks kinda Oxfordy',
    #long_description=open('README.rst').read(),
    author='Alexander Dutton',
    author_email='idm@alexdutton.co.uk',
    url='https://github.com/alexsdutton/idm-brand',
    license='BSD',
    packages=find_packages(exclude=("test*", )),
    install_requires=['Django'],
)
