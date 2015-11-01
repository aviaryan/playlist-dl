import json
import youtube_dl
from .Video import Video

class Playlist():
	'''
	Playlist class
	'''

	def __init__(self, url):
		'''
		Initialises the class
		url is the playlist url
		If url = playlist.json, then it loads from the local playlist data.
		'''
		if url == 'playlist.json':
			ptr = open('playlist.json', 'r')
			self.res = json.loads(ptr.read())['entries']
			ptr.close()
		else:
			ydl = youtube_dl.YoutubeDL()
			res = ydl.extract_info(url, download=False)
			if 'entries' in res:
				self.res = res['entries']
			self.makeSimpleList()
			ptr = open('playlist.json', 'w')
			ptr.write(json.dumps(res, indent=4))
			ptr.close()


	def download(self, index, res='', bitrate='', vext='', aext='', oext=''):
		'''
		Resumes the download of item at index 'index' from the playlist
		'''
		vobj = self.res[index-1]
		video = Video(vobj)
		video.download(res, bitrate, vext, aext, oext) # params


	def makeSimpleList(self):
		'''
		Saves a simple json file for users to see what they have in the playlist
		'''
		ptr = open('videolist.json', 'w')
		dic = {}
		c = 1
		for i in self.res:
			dic[c] = {
				'title': i['title'],
				'url': i['webpage_url']
			}
			c+=1
		ptr.write(json.dumps(dic, indent=4))
		ptr.close()