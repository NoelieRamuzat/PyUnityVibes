from setuptools import setup
from codecs import open
from os import path


with open(path.join(path.abspath(path.dirname(__file__)), 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='PyUnityVibes',
    version='1.0.0',
    description='A Graphical library for Python using Unity3d',
    long_description=long_description,
    url='https://github.com/NoelieRamuzat/PyUnityVibes',
    author='Rémi Rigal',
    author_email='remi.rigal@ensta-bretagne.org',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: User Interfaces',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='Unity GUI Library UnityVibes',
    packages=['PyUnityVibes', 'PyUnityVibes.Animation', 'PyUnityVibes.Network', 'PyUnityVibes.UI'],
    install_requires=['numpy'],
    project_urls={ 'Source': 'https://github.com/NoelieRamuzat/PyUnityVibes' }
)