import json
import youtube_dl
from platform import subprocess

class Video():
	'''
	Video class
	Get video info, parse them and download videos
	'''

	def __init__(self, vobj, oext=''):
		'''
		Inits the Video class
		'''
		self.vobj = vobj
		self.url = vobj['webpage_url']
		self.oext = oext


	def getVStream(self, height, ext=''):
		'''
		Gets the format id of the required video stream
		Searches only DASH video
		'''
		retid = 0
		csize = 2**64

		for item in self.vobj['formats']:
			if item['format_note'] != 'DASH video' and item['format'].find('DASH video') == -1:
				continue
			if ext:
				if item['ext'] != ext:
					continue
			if item['height'] != height:
				continue
			if item['filesize'] < csize: # in many extension with same resolution cases, use the one with least size
				retid = item['format_id']
				csize = item['filesize']

		return int(retid)


	def getAStream(self, abr, ext=''):
		'''
		Gets the format id of the required audio stream
		Searches only in DASH audio
		'''
		retid = 0
		csize = 2**64

		for item in self.vobj['formats']:
			if item['format_note'] != 'DASH audio' and item['format'].find('DASH audio') == -1:
				continue
			if ext:
				if item['ext'] != ext:
					continue
			if item['abr'] != abr:
				continue
			if item['filesize'] < csize: # in many extension with same resolution cases, use the one with least size
				retid = item['format_id']
				csize = item['filesize']

		return int(retid)


	def getBestDL(self, res='', bitrate='', vext='', aext=''):
		'''
		Gets the best possible download combination for you
		If return has one item in array, that means it is a complete video
		If 2 items, then video+audio stream. 0 in these values means let yt-dl choose automatic
		'''
		v,a = res,bitrate
		if not res:
			v = 0
		else:
			v = 0
			for item in self.vobj['formats']:
				if item['format_note'].find('DASH') == -1 and item['format'].find('DASH') == -1 and item['height'] == res:
					v = int(item['format_id']) # optimize min size technique here
					if item['ext'] == vext:
						return [v] # both resolution and format match, return immediately
			v2 = self.getVStream(res, vext)
			if not vext and v: # no vext but got a full video
				return [v]
			else:
				v = v2
				if vext and v==0:
					v = self.getVStream(res) # one more try but without extension

		if not bitrate:
			a = 0
		else:
			a = self.getAStream(bitrate, aext)
			if aext and a==0:
				a = self.getAStream(bitrate)

		return [v , a]


	def download(self, res='', bitrate='', vext='', aext=''):
		'''
		Starts the video download in the specified format
		'''
		o = self.getBestDL(res, bitrate, vext, aext)
		if len(o) == 1:
			if o[0] == 0:
				pstr = 'youtube-dl'
			else:
				pstr = 'youtube-dl -f ' + o[0]
		else:
			if o[0] == 0:
				o[0] = 'bestvideo'
			if o[1] == 0:
				o[1] = 'bestaudio'
			pstr = 'youtube-dl -f ' + o[0] + '+' + o[1]
			if o[0] == 0 and o[1] == 0:
				pstr = 'youtube-dl' # make it back in case both 0
			subprocess.call(pstr
				+ ' '
				+ self.url
				+ '--merge-output-format '
				+ this.oext
			)



# ydl = youtube_dl.YoutubeDL()
# url = 'https://www.youtube.com/watch?v=InF16sp7J0M'
# res = ydl.extract_info(url, download=False)
# ptr = open('video.json', 'r')
# res = json.loads(ptr.read())
# ptr.close()


# obj = res
# res = json.dumps(res, indent=4)
# # print(res)
# ptr = open('video.json', 'w')
# ptr.write(res)
# ptr.close()

# vc = Video(obj)

# print( vc.getVStream(720) )
# print( vc.getAStream(128))
# print( vc.getBestDL(480) )