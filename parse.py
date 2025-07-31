#! /usr/bin/env python

""" Parse video-list text file into a dictionary Title:duration. """

import json
import ntpath
import sys

#def encode_to_html_entities(text: str) -> str:
#    """ Replace every single characted with its HTML entity. """
#    result = ''.join(f'&#{ord(char)};' for char in text)
#    #t = type(result)
#    #print(f"<h3>Result: __{result}__ </h3>")#TMP
#    #print(f"<h3>TYPE:{t}</h3>")#TMP
#    return result

def parse_into_dictios(path: str) -> list:
    """
    Store pairs from text file into array of dictionaries, splitting 
    the lines by the last occurrence of '.mp4 ::: '.
    """
    result = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.replace('\r', '').replace('\0', '')
            line = line.replace('\n', '')
            line = line.replace('\ufeff', '') # Removing BOM causes problems later?
            if '.mp4' in line:
                pair = {}
                (key, val) = line.rsplit('.mp4 ::: ', 1)
                pair[key] = val
                result.append(pair)
    return result
#

def display_list_pairs(pairs: list) -> None:
    """ Simply display in webpage. """
    print("<div>")
    print("<ul>")
    for pair in pairs:
        for key in pair:
            video_title = ntpath.basename(key)
            print(f"<li>{video_title}</li>")
    print("</ul>")
    print("</div>")
#

def generate_persist_crate_form(filename: str) -> None:
    """ Generate HTML form with button to persist crate to DB. """
    form_html = """ <form method="post" enctype="multipart/form-data"
        action="save_to_db.php"> """
    print(form_html)
    print(""" <input value="Save crate" name="submit" type="submit" /> """)
    print(f"<input type=\"hidden\" value=\"{filename}.json\" name=\"jsonfilename\" />")
    print("</form>")

def generate_playlist_form(filename: str) -> None:
    """ Generate HTML form with button to generate & download playlist. """
    form_html = """ <form method="get" enctype="multipart/form-data"
        action="generate_and_download.php"> """
    print(form_html)
    print(""" <input value="Generate & Download Playlist" name="submit" type="submit" /> """)
    print(f"<input type=\"hidden\" value=\"{filename}.json\" name=\"jsonfilename\" />")
    print("</form>")
#

def save_pairs_to_disk(pairs: list, filename: str) -> bool:
    """ Save list of dictionaries (to Instance Store). """
    try:
        with open(f"{filename}.json", 'w', encoding='utf-8') as file:
            json.dump(pairs, file, ensure_ascii=False)
            return True
    except PermissionError as pe:
        print(pe)
        return False
#

def main():
    """ Receives name of text file. """
    video_list_file_name = sys.argv[1]
    pairs = parse_into_dictios(video_list_file_name)
    display_list_pairs(pairs)
    write_suc = save_pairs_to_disk(pairs, video_list_file_name)
    if not write_suc:
        print("<p>Unable to write video list to disk!</p>")
        sys.exit(1)
    generate_playlist_form(video_list_file_name)
    generate_persist_crate_form(video_list_file_name)
#


if __name__ == '__main__':
    main()
#
