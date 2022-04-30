from setuptools import setup, find_packages


VERSION = '0.0.2'
DESCRIPTION = 'SQLITE tools'
LONG_DESCRIPTION = 'this package is designed to manage the database'

# Setting up
setup(
    name="sqllite3tools1",
    version=VERSION,
    author="SanjarbekDev",
    author_email="<sanjarbeksodiqov0302@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    keywords=['eexecute','commit','fetchone','fetchall','create_table','info','select'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)