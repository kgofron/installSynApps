import setuptools

with open('requirements.txt') as reqf:
    requirements = reqf.read().split()


setuptools.setup(
    name='installSynApps',
    description='A Python program for building EPICS and synApps',
    version='0.2.3',
    author='Jakub Wlodek',
    author_email=None,
    license='BSD (3-clause)',
    url='https://github.com/epicsNSLS2-deploy/installSynApps',
    packages='installSynApps',
    python_requires='>=3.4',
)
