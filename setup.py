from setuptools import find_packages, setup

setup(
    name='sentence2tags',
    version='1.0.0',
    description='Python package for joint neural lemmatization and tagging',
    author='Martin Mirakyan',
    author_email='mirakyanmartin@gmail.com',
    python_requires='>=3.6.0',
    url='https://github.com/MartinXPN/sentence2tags',
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'Keras>=2.2.4',
        'scikit-learn>=0.20.3',
        'tqdm>=4.31.1',
        'tensorflow>=1.13.1',
        'numpy>=1.16.1',
    ],
    extras_require={},
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Full list of Trove classifiers: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)
