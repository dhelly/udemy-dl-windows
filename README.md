# udemy-dl for Windows
A windows utility to download videos from udemy for personal offline use, based on <https://github.com/nishad/udemy-dl>.

For Windows (XP, Vista, 7, 8, 10) 32 & 64 bit

### Download

You can get the latest release from here.  
https://github.com/nishad/udemy-dl-windows/releases/latest  
Download `udemy-dl-win-X.X.X.zip`

[![Total downloads](https://img.shields.io/github/downloads/nishad/udemy-dl-windows/total.svg)](https://github.com/nishad/udemy-dl-windows/releases/latest) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/b94bce94629e4971ac537660f93345a1)](https://www.codacy.com/app/rimpoche/udemy-dl-windows?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=nishad/udemy-dl-windows&amp;utm_campaign=Badge_Grade)

### Version
**2.1.2** [![Latest version downloads](https://img.shields.io/github/downloads/nishad/udemy-dl-windows/latest/total.svg)](https://github.com/nishad/udemy-dl-windows/releases/latest)

### Usage

Simply call `udemy-dl.exe` with the full URL to the course page.
```
udemy-dl.exe https://www.udemy.com/COURSE_NAME
```
`udemy-dl.exe` will ask for your udemy username (email address) and password then start downloading the videos.

By default, `udemy-dl.exe` will create a subdirectory based on the course name.  If you wish to have the files downloaded to a specific location, use the `-o \path\to\directory\` parameter.

If you wish, you can include the username/email and password on the command line using the -u and -p parameters.

```
udemy-dl.exe -u user@domain.com -p $ecRe7w0rd https://www.udemy.com/COURSE_NAME
```

For information about all available parameters, use the `--help` parameter
```
udemy-dl.exe --help
```

### Advanced Usage

```
usage: udemy-dl [-h] [-u USERNAME] [-p PASSWORD]
                [--lecture-start LECTURE_START] [--lecture-end LECTURE_END]
                [-o OUTPUT] [-d {aria2c,axel,httpie,curl}] [--use-ffmpeg]
                [-q VIDEO_QUALITY] [-s] [--safe-file-names] [-l] [--debug]
                [-v]
                link

Fetch all the lectures for a udemy course

positional arguments:
  link                  Link for udemy course

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Username / Email
  -p PASSWORD, --password PASSWORD
                        Password
  --lecture-start LECTURE_START
                        Lecture to start at (default is 1)
  --lecture-end LECTURE_END
                        Lecture to end at (default is last)
  -o OUTPUT, --output OUTPUT
                        Output directory / text file path (if saving links)
  -d {aria2c,axel,httpie,curl}, --external-downloader {aria2c,axel,httpie,curl}
                        Download with external downloader [aria2c, axel,
                        httpie, curl] (default is aria2c)
  --use-ffmpeg          Download videos from m3u8/hls with ffmpeg
                        (Recommended)
  -q VIDEO_QUALITY, --video-quality VIDEO_QUALITY
                        Select video quality [default is 654321(highest)]
  -s, --save-links      Do not download but save links to a file
  --safe-file-names     Use safe cross-platform filenames
  -l, --list            Just list all of the possible lectures and their ids
  --debug               Enable debug mode
-v, --version Display the version of udemy-dl and exit
```


### Updating

For updating components or to latest development version, run `update.cmd` in the same folder of `udemy-dl.exe` and `curl.exe`

### Support

[![ nishad/udemy-dl-windows at Baikal](https://s3-us-west-2.amazonaws.com/nerpa-static/baikal-banner.svg)](https://baikal.io/nishad/udemy-dl-windows)

[![Baikal](https://baikal.io/badges/nishad/udemy-dl-windows)](https://baikal.io/nishad/udemy-dl-windows)


### Downloader 
By default `udemy-dl.exe` uses `aria2c.exe` to download the video file. If it is missing it will try `curl.exe`, and if both these downloaders are missing it will use built in `wget` function. You can delete `area2c.exe` if it is not working or wants to use `curl.exe`.

### Versioning 
This tool will use  MINOR and PATCH version of <https://github.com/nishad/udemy-dl>, as MAJOR and MINOR versions, and its own changes as PATCH version. Which will be a dirty approach with <http://semver.org/>.

For example `v 0.2.1` of `udemy-dl` will be used in `v 2.1.X` of `udemy-dl.exe`.
