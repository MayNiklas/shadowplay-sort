from setuptools import setup

setup(
    name='shadowplay_sort',
    version='1.0.0',
    url='https://github.com/MayNiklas/shadowplay-sort',
    license='',
    author='MayNiklas',
    author_email='info@niklas-steffen.de',
    description='sort shadowplay files after date',
    packages=['shadowplay_sort'],
    entry_points={
        'console_scripts': ['shadowplay-sort=shadowplay_sort:__main__']
    },
)
