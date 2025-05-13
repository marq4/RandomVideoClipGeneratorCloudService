#! /usr/bin/env python

""" 
Generate XML playlist from dictionaries(title:duration) and send to user. 
"""

import os
import random
import subprocess
import json
import sys
import xml.etree.ElementTree as ET
from subprocess import Popen


XML_PLAYLIST_FILE = '/var/www/rvcg/clips.xspf'
NUMBER_OF_CLIPS = 5
INTERVAL_MIN = 4
INTERVAL_MAX = 8


def display_as_unorderedlist(pairs: list) -> None:
    """ Code pasted from parse.py. """
    print("<div>[")
    print("  <ul>")
    for pair in pairs:
        for key in pair:
            print("    <li>{"+key+' ====> '+pair[key]+"}</li>")
    print("  </ul>")
    print("]</div>")
#

def read_json(filename: str) -> list:
    """ Imports and returns pairs from json. """
    with open(filename, 'r', encoding='utf-8') as file:
        json_str = file.read()
    loaded_data = json.loads(json_str)
    return loaded_data
#

def verify_intervals_valid() -> None:
    """ Music video clips should be between at most 15 to 25 seconds long. """
    assert 15 >= INTERVAL_MIN >= 1
    assert 25 >= INTERVAL_MAX >= 1
#

def generate_random_video_clips_playlist(video_list: list) -> ET.Element:
    """
    * Create playlist as an xml element tree.
    * Create tracklist as subelement of playlist. This contains the clips.
    * For each clip to be generated:
        + Select a video at random.
        + Choose beginning and end of clip from selected video.
        + Add clip to playlist.
    """
    assert video_list

    playlist = ET.Element("playlist", version="1", xmlns="http://xspf.org/ns/0/")
    tracks = ET.SubElement(playlist, "trackList")

    assert 1 <= NUMBER_OF_CLIPS < sys.maxsize, \
        "Invalid number of clips: {NUMBER_OF_CLIPS} "

    for iteration in range(NUMBER_OF_CLIPS):
        pair = select_video_at_random(video_list)
        video_file = list(pair.keys())[0]
        video_file += '.mp4'
        #print(f"Video selected at random: {video_file}")#TMP
        duration = int(float(list(pair.values())[0].rstrip()))
        #print(f"Duration: {duration}")

        begin_at = choose_starting_point(duration)
        clip_length = random.randint(INTERVAL_MIN, INTERVAL_MAX)
        play_to = begin_at + clip_length

        add_clip_to_tracklist(tracks, video_file, begin_at, play_to)

    return playlist
#

def add_clip_to_tracklist(track_list: ET.Element, \
    video: str, start: int, end: int) -> None:
    """ Add clip (track) to playlist.trackList sub element tree and mute.
        :param: track_list: Contains the clips.
        :param: video: The name of the video file to be cut.
        :param: start: Begin clip from.
        :param: end: Stop clip at. """
    assert track_list is not None and video and start >= 0
    track = ET.SubElement(track_list, 'track')
    ET.SubElement(track, 'location').text = f"file:///{video}"
    extension = ET.SubElement(track, 'extension', \
        application='http://www.videolan.org/vlc/playlist/0')
    ET.SubElement(extension, 'vlc:option').text = f"start-time={start}"
    ET.SubElement(extension, 'vlc:option').text = f"stop-time={end}"
    ET.SubElement(extension, 'vlc:option').text = 'no-audio'
#

def create_xml_file(playlist_et: ET.Element) -> None:
    """ Finally write the playlist tree element as an xspf file to disk. """
    ET.ElementTree(playlist_et).write(XML_PLAYLIST_FILE)
    prepend_line(XML_PLAYLIST_FILE, '<?xml version="1.0" encoding="UTF-8"?>')
#

def choose_starting_point(video_length: int) -> int:
    """ Choose beginning of clip.
    :return: Starting point from beginning of video to end of video - max. """
    assert video_length > 0
    return random.randint(0, video_length - INTERVAL_MAX)
#

def select_video_at_random(list_of_files: list) -> dict:
    """ Choose a video. :return: Video {filename:duration} pair. """
    assert list_of_files
    #print(f"select_video_at_random() list_of_files => {list_of_files}")#TMP
    #print(type(list_of_files))#TMP
    selected = random.randint(0, len(list_of_files) - 1)
    video_pair = list_of_files[selected]
    #print(type(video_pair))#TMP
    return video_pair
#

def prepend_line(filename: str, line: str) -> None:
    """ Append line to beginning of file. """
    assert filename, f"Cannot prepend line: '{line}' to invalid {filename}. "
    if line is not None and len(line) > 0:
        with open(filename, 'r+', encoding='utf-8') as file:
            content = file.read()
            file.seek(0,0)
            file.write( line.rstrip("\r\n") + "\n" + content )
#

def generate_playlist(pairs: list) -> str:
    """ Returns XSPF as string. """
    verify_intervals_valid()
    top_element = generate_random_video_clips_playlist(pairs)
    create_xml_file(top_element)
    return XML_PLAYLIST_FILE
#

def generate_download_button(xml_path: str) -> None:
    """ Generate HTML form and button to download playlist. """
    form_html = """ <form method="get" enctype="multipart/form-data"
        action="download_playlist.php"> """
    print(form_html)
    print(""" <input value="Download Playlist" name="submit" type="submit" /> """)
    print(f"<input type=\"hidden\" value=\"{xml_path}\" name=\"xml_path\" />")
    print("</form>")
#

def main():
    """ Read JSON from disk, parse it, generate XML. """
    #print("<h2>Parse!</h2>") #TMP
    filename = sys.argv[1]
    pairs = read_json(filename)
    display_as_unorderedlist(pairs)
    xml = generate_playlist(pairs)
    print("<p>The playlist for VLC has been generated. ")
    #print(f"<div>{xml}</div>") #TMP
    print("</p>")
    generate_download_button(xml)
#


if __name__ == '__main__':
    main()
#

