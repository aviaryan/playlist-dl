# playlist-dl

Youtube playlist downloader


### Features

* Resumable downloading
* Video resolution, video format, audio bitrate, audio format can be configured
* Video Output format (via conversion) can also be specified


### Tutorial

* To start a new playlist download, create a new folder and open terminal (cmd) in it.
* Then run `playlist-dl`
* Give the playlist link and playlist-dl (youtube-dl actually) will start scanning the playlists.
* After that it will create a config.json file in that folder. Edit that if needed.
* Download will begin soon after.
* You can close the terminal at any time. Reopening the terminal at that folder and running `playlist-dl` will resume the downloads.


### Config.json

* `start` - The item in playlist from where the download will be started.
* `end` - The item in playlist till where downloading will be done.
* `output_format` - The format to convert the downloaded video to. (eg > mkv,mp4,flv,webm)
* `download.resolution` - The height of the video to download. If set to 0, then bestvideo will be downloaded.
* `download.video_format` - The format of the video stream to download. Note that this is different from `output_format` (eg > flv,webm,mp4).
* `download.bitrate` - The bitrate of the audio to download. If set to 0, then bestaudio will be downloaded.
* `download.audio_format` - The format of the audio stream to download. (eg > webm,m4a)

**NOTE** - If the downloader finds no match with your `download.` settings, then it will automatically settle with the next preferable audio/video.