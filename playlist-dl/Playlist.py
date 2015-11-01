import json
import youtube_dl
import Video

class Playlist():
	'''
	Playlist class
	'''

	def __init__(self, url):
		'''
		Initialises the class
		url is the playlist url
		If url = video.json, then it loads from the local playlist data.
		'''
		if url == 'video.json':
			ptr = open('video.json', 'r')
			self.res = json.loads(ptr.read()).entries
			ptr.close()
		else:
			ydl = youtube_dl.YoutubeDL()
			res = ydl.extract_info(url, download=False)
			if 'entries' in res:
				self.res = res['entries']
			ptr = open('video.json', 'w')
			ptr.write(json.dumps(res, indent=4))
			ptr.close()


	def download(index):
		'''
		Resumes the download of item at index 'index' from the playlist
		'''
		vobj = self.res[index-1]
		video = Video(vobj)
		video.download() # params