#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name="pygments-style-beamertrek",
    version='0.1',
    description='Pygments theme for default beamer-trek colors',
    keywords='pygments style beamertrek',
    license='BSD',

    author='Jonathan Merritt',
    author_email='j.s.merritt@gmail.com',

    packages=find_packages(),
    install_requires=['pygments >= 1.6'],

    entry_points='''[pygments.styles]
                    beamertrek=pygments_style_beamertrek:BeamerTrekStyle''',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
