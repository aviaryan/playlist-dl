import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    install_requires = ['youtube-dl'],

    name = "playlist-dl",
    version = "0.1",
    author = "Avi Aryan",
    author_email = "avi.aryan123@gmail.com",
    description = "Configurable Youtube Playlist downloader",
    license = "Apache",
    keywords = "youtube playlist download youtube-dl ytd",
    url = "http://github.com/aviaryan/playlist-dl",
    packages=['playlist_dl'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Beta",
        "Topic :: Utilities",
        "License :: Apache License v2.0",
    ],
    include_package_data=True, # needed for MANIFEST

    entry_points={
        'console_scripts': [
            'playlist-dl = playlist_dl.playlist_dl:start'
        ]
    }
)