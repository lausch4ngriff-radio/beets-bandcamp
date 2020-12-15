from setuptools import setup

setup(
    name='beets-bandcamp',
    version='0.1.4',
    description='Forked and updated Plugin for beets (http://beets.io) to use bandcamp as an autotagger source.',
    long_description=open('README.rst').read(),
    author='Erik Milach',
    author_email='emilach82@gmail.com',
    url='https://github.com/lausch4ngriff-radio/beets-bandcamp.git',
    download_url='https://github.com/lausch4ngriff-radio/beets-bandcamp/archive/v0.1.4.tar.gz',
    license='GPL-2.0',
    platforms='ALL',

    packages=['beetsplug'],

    install_requires=[
        'beets>=1.4.6',
        'six>=1.9'
        'requests',
        'beautifulsoup4',
        'isodate'
    ],

    classifiers=[
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Players :: MP3',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)
