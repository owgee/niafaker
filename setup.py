from setuptools import setup, find_packages

setup(
    name='niafaker',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'setuptools',
    ],
    package_data={
        'niafaker': ['data/*.json'],
    },
    description='A Faker package localized for African data',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Owden Godson (OG)',
    author_email='owdeng@gmail.com',
    url='https://github.com/owgee/niafaker',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
