# playlist-dl

Youtube playlist downloader. Based on the majestic [youtube-dl](http://youtube-dl.org/)


### Features

* Resumable downloading
* Video resolution, video format, audio bitrate, audio format can be configured
* Video Output format (via conversion) can also be specified


### Installation

Python 3 only.  
Get it from pip
```
pip install playlist-dl
```

or download the zip and execute the following
```
python setup.py install
```


### Tutorial

* To start a new playlist download, create a new folder and open terminal (cmd) in it.
* Then run `playlist-dl`
* Give the playlist link and playlist-dl (actually youtube-dl) will start scanning the playlist.
* After that it will create a config.json file in that folder. Edit that if needed.
* Videos will start downloading one by one.
* You can close the terminal any time. Reopening the terminal in that folder and running `playlist-dl` will resume the downloads.


### Config.json

* `start` - The item in playlist from where the download will be started.
* `end` - The item in playlist till where downloading will be done.
* `output_format` - The format to convert the downloaded video to. (eg > mkv,mp4,flv,webm)
* `download.resolution` - The height of the video to download. If set to 0, then bestvideo will be downloaded.
* `download.video_format` - The format of the video stream to download. Note that this is different from `output_format` (eg > flv,webm,mp4).
* `download.bitrate` - The bitrate of the audio to download. If set to 0, then bestaudio will be downloaded.
* `download.audio_format` - The format of the audio stream to download. (eg > webm,m4a)
* `download.more_options` - More download options. See [youtube-dl README](https://github.com/rg3/youtube-dl/blob/master/README.md) for the complete list.

**NOTE** - If the program finds no match with your `download.` settings, then it will automatically settle with the most preferable audio/video options.

##### Example of a config.json

```json
{
    "start": 37,
    "output_format": "mkv",
    "url": "https://www.youtube.com/watch?v=6m44ul3fzH4&list=PLfP-5ohlBRxXUWCJRrR0i4Eft02OB_XkE&index=1",
    "download": {
        "video_format": "webm",
        "more_options": "-o \"%(title)s.%(ext)s\" --external-downloader aria2c --external-downloader-args \"-x 8 -s 8 -k 8M\"",
        "audio_format": "webm",
        "bitrate": 128,
        "resolution": 480
    },
    "end": 49
}
```
