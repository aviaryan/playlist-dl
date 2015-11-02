#!/usr/bin/env python

import json
import os

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
	if not CONF or not CONF['url']:
		return
	ptr = open('config.json', 'w')
	ptr.write(json.dumps(CONF, indent=4))
	ptr.close()


def run():
	'''
	Starts the app
	'''
	global CONF, PL

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
		confirm = input('Config saved as config.json. Edit it if you please. Then press ENTER ')
		readConfig()

	# CONFIG read/create done. Now downloading

	while CONF['start'] <= CONF['end']:
		PL.download( CONF['start'],
		**{
			'res': CONF['download']['resolution'],
			'bitrate': CONF['download']['bitrate'], 
			'vext': CONF['download']['video_format'],
			'aext': CONF['download']['audio_format'], 
			'oext': CONF['output_format'],
			'more': CONF['download']['more_options']
		})
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


if __name__ == '__main__':
	run()