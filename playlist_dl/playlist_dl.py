#!/usr/bin/env python

import json
import os
from sys import argv
from sys import exit as sysexit

try:
	from .Video import Video
except SystemError:
	from Video import Video
try:
	from .Playlist import Playlist
except SystemError:
	from Playlist import Playlist

CONF = {}
PL = ''
VERSION = 'v0.2 beta'

# python C:\Users\Avi\Documents\GitHub\playlist-dl\playlist_dl\playlist_dl.py

def readConfig():
	'''
	Reads the config file config.json
	'''
	global CONF
	ptr = open('config.json', 'r')
	CONF = json.loads(ptr.read())
	ptr.close()


def saveConfig():
	'''
	Saves the CONF variable back to config.json
	'''
	# global CONF
	ptr = open('config.json', 'w')
	ptr.write(json.dumps(CONF, indent=4))
	ptr.close()


def showHelp():
	'''
	Shows the help
	'''
	printexit(
		(
		"\n"
		"playlist-dl helps you download youtube playlists.\n"
		"Just run playlist-dl without any arguments to start the program\n"
		"\n"
		"OPTIONS\n"
		"\n"
		"-h or --help:     Show help\n"
		"-v or --version:  Show version information"
		)
	)


def run():
	'''
	Starts the app
	'''
	global CONF, PL

	if len(argv) > 1:
		if argv[1] == '-h' or argv[1] == '--help':
			showHelp()
		elif argv[1] == '-v' or argv[1] == '--version':
			printexit(VERSION)
		else:
			showHelp()


	if os.path.isfile('config.json'):
		readConfig()
		if os.path.isfile('playlist.json'):
			PL = Playlist('playlist.json')
		else:
			PL = Playlist(CONF['url'])
	else:
		url = getin('You are creating a new project. Give URL of the playlist')
		PL = Playlist(url)
		CONF = {
			'output_format': '',
			'start': 1,
			'end': len(PL.res),
			'download': {
				'resolution': 720,
				'video_format': '',
				'bitrate': 0,
				'audio_format': '',
				'more_options': '-o "%(title)s.%(ext)s"'
			},
			'url': url
		}
		saveConfig()
		print()
		confirm = input('Config saved as config.json. Edit it if you please. Then press ENTER ')
		readConfig()

	# CONFIG read/create done. Now downloading

	while CONF['start'] <= CONF['end']:
		retcode = PL.download( CONF['start'],
			**{
				'res': CONF['download']['resolution'],
				'bitrate': CONF['download']['bitrate'], 
				'vext': CONF['download']['video_format'],
				'aext': CONF['download']['audio_format'], 
				'oext': CONF['output_format'],
				'more': CONF['download']['more_options']
			}
		)
		if retcode != 0: # if failed, try again
			continue
		CONF['start']+=1
		saveConfig()



def getin(msg):
	'''
	gets the input. Doesn't accept empty input
	'''
	t = ''
	while not t:
		t = input(msg + '\n> ')
	return t


def printexit(msg, code=0):
	'''
	Prints and exists
	'''
	print(msg)
	sysexit(code)


if __name__ == '__main__':
	run()