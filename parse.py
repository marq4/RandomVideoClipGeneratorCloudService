#! /usr/bin/env python

""" Parse video-list text file into a dictionary Title:duration. """

import json
import sys


def parse_into_dictios(path: str) -> list:
    """
    Store pairs from text file into array of dictionaries, splitting 
    the lines by the last occurrence of '.mp4 ::: '.
    """
    result = list()
    with open(path) as file:
        while True:
            line = file.readline()
            if not line:
                break
            pair = dict()
            (key, val) = line.rsplit('.mp4 ::: ', 1)
            pair[key] = val
            result.append(pair)
        #
    #
    return result
#

def display_list_pairs(pairs: list) -> None:
    """ Simply display in webpage. """
    print("<div>[")
    print("  <ul>")
    for pair in pairs:
        for key in pair:
            print("    <li>{"+key+' ====> '+pair[key]+"}</li>")
    print("  </ul>")
    print("]</div>")
#

def generate_playlist_form(filename: str) -> None:
    """ Generate HTML form with button to generate playlist. """
    form_html = """ <form method="get" enctype="multipart/form-data"
        action="call_playlist_generator.php"> """
    print(form_html)
    print(""" <input value="Generate Playlist" name="submit" type="submit" /> """)
    print(f"<input type=\"hidden\" value=\"{filename}.json\" name=\"jsonfilename\" />")
    print("</form>")
#

def save_pairs_to_disk(pairs: list, filename: str) -> bool:
    """ Save list of dictionaries (to Instance Store). """
    try:
        with open(f"{filename}.json", 'w') as file:
            json.dump(pairs, file)
            return True
    except:
        return False
#

def main():
    """ Receives name of text file. """
    video_list_file_name = sys.argv[1]
    pairs = parse_into_dictios(video_list_file_name)
    display_list_pairs(pairs) #TMP
    write_suc = save_pairs_to_disk(pairs, video_list_file_name)
    if not write_suc:
        print("<p>Unable to write video list to disk!</p>")
        exit(1)
    generate_playlist_form(video_list_file_name)
#


if __name__ == '__main__':
    main()
#


