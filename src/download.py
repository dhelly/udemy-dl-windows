#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Download files for udemy-dl."""
from __future__ import unicode_literals
from __future__ import print_function

import os
import subprocess
import sys
import colorlog

import requests

logger = colorlog.getLogger('udemy_dl.download')
# User Agent String
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0'


class DLException(Exception):

    """Raise if some lectured failed to download."""

    pass


def download(link, filename, update_progress, downloader='aria2c'):
    """Download files to given destination file-name."""
    try:
        if 'aria2c' in downloader:
            aria2c_dl(link, filename)
        elif 'axel' in downloader:
            axel_dl(link, filename)
        elif 'httpie' in downloader:
            httpie_dl(link, filename)
        elif 'curl' in downloader:
            curl_dl(link, filename)
        elif 'ffmpeg' in downloader:  # only for hls
            ffmpeg_dl(link, filename)
        elif 'yt_dl' in downloader:  # only for youtube link
            youtube_dl(link, filename)
        else:
            requests_dl(link, filename, update_progress)
    except OSError as exc:
        if not os.path.exists(filename):
            logger.critical('%s not found. Downloading with builtin downloader', downloader)
            requests_dl(link, filename, update_progress)
        else:
            logger.critical('Failed to download: %s', exc)
            download_status = 'failed'
            return download_status


def httpie_dl(link, filename):
    """Use httpie as the downloader."""
    command = ['http', '--continue', '--download', link, '-o', filename]
    subprocess.call(command)


def axel_dl(link, filename):
    """Use axel as the downloader."""
    command = ['axel', '-U', USER_AGENT, link, '-o', filename]
    subprocess.call(command)


def curl_dl(link, filename):
    """Use curl as the downloader."""
    command = ['curl', '-C', '-', link, '-o', filename]

    cert_path = requests.certs.where()
    if cert_path:
        command.extend(['--cacert', cert_path])
    else:
        command.extend(['--insecure'])
    subprocess.call(command)


def aria2c_dl(link, filename):
    """Use aria2c as the downloader."""
    command = ['aria2c', '--continue', '--file-allocation=none', '--auto-file-renaming=false', '-k', '1M', '-x', '4', '-U', USER_AGENT, link, '-o', filename]
    subprocess.call(command)


def ffmpeg_dl(link, filename):
    """Download m3u8/hls videos."""
    command = ['ffmpeg', '-i', link, '-bsf:a', 'aac_adtstoasc', '-vcodec', 'copy', '-c', 'copy', '-crf', '50', '-f', 'mp4', filename]
    subprocess.call(command)


def dl_progress(num_blocks, block_size, total_size):
    """Show a decent download progress indication."""
    progress = num_blocks * block_size * 100 / total_size
    if num_blocks != 0:
        sys.stdout.write(4 * '\b')
    sys.stdout.write('{0:3d}%'.format((progress)))


def youtube_dl(link, filename):
    """Use youtube-dl as the downloader if videos are in youtube.com."""
    try:
        # ffmpeg automatically replace ext, this cause rename problem
        # (only if ffmpeg is installed and aria2 is not installed)
        # if ffmpeg is installed, user must install aria2 to avoid crash.
        subprocess.call(['youtube-dl', '-o', filename, link, '--external-downloader', 'aria2c'])
    except OSError:
        raise DLException('Install youtube-dl to download this lecture')


def requests_dl(link, filename, update_progress):
    """Download file with requests."""
    response = requests.get(link, stream=True)

    with open(filename, 'wb') as file:
        file_size = int(response.headers['content-length'])
        file_size_dl = 0
        block_size = 1024 * 512

        for buffer_ in response.iter_content(block_size):
            file_size_dl += len(buffer_)
            file.write(buffer_)
            progress = float(file_size_dl) / file_size
            update_progress(progress, 'Downloading', 30)
        file.close()
