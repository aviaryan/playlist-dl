import json
import os

from Video import Video
from Playlist import Playlist

CONF = {}
PL = ''


def readConfig():
	'''
	Reads the config file config.json
	'''
	ptr = open('config.json', 'r')
	CONF = json.loads(ptr.read())
	for i in CONF:
		print(i)
	ptr.close()


def saveConfig():
	'''
	Saves the CONF variable back to config.json
	'''
	ptr = open('config.json', 'w')
	ptr.write(json.dumps(CONF, indent=4))
	ptr.close()


def start():
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
		CONF = {
			'output_format': '',
			'start': 0,
			'end': 0,
			'download': {
				'resolution': 720,
				'video_format': '',
				'bitrate': '',
				'audio_format': '',
			},
			'url': url
		}
		saveConfig()
		PL = Playlist(CONF['url'])



def getin(msg):
	'''
	gets the input. Doesn't accept empty input
	'''
	t = ''
	while not t:
		t = input(msg + '\n> ')
	return t


if __name__ == '__main__':
	start()