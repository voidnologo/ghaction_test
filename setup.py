from setuptools import setup

requires = []

setup(
    name='voidnologo-ghactions',
    version='0.0.1',
    setup_requires=['pytest-runner'],
    install_requires=requires,
    dependency_links=[],
    tests_require=['pytest'],
    description='Voidnologo run tests with ghactions',
    url='http://voidnologo.com',
    author='Voidnologo',
    author_email='dev@voidnologo.com',
    license='private',
)
