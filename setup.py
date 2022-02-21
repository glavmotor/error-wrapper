from setuptools import find_packages, setup
setup(
    name='error-wrapper',
    packages=find_packages(include=['error_wrapper']),
    version='0.9.4',
    url='https://github.com/glavmotor/error-wrapper',
    description='Error wrapper with auto logging',
    long_description=open('README.rst').read(),
    author='Dmitry Kravtsov',

    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner==5.*'],
    tests_require=['pytest==4.*', 'pylint==2.*'],
    test_suite='tests',
)
