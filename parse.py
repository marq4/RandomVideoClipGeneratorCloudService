#! /usr/bin/env python

""" Parse video-list text file into a dictionary Title:duration. """

import json
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
    result = list()
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            #line = bytes_read.decode('utf-8')
            #print(f"<p>LINE: ___{line}___ </p>")#TMP
            line = line.replace('\r', '').replace('\0', '')
            line = line.replace('\n', '')
            line = line.replace('\ufeff', '') # Removing BOM causes problems later?
            #line = line.replace('~', '&#126;') #XXX: can't add special chars!
            if '.mp4' in line:
                pair = dict()
                (key, val) = line.rsplit('.mp4 ::: ', 1)
                #key = encode_to_html_entities(key) #XXX: win filenames too long!
                #key = key.replace('&amp;', '&')
                pair[key] = val
                result.append(pair)
        #
    #
    #print(f"<p>RESULT (pairs): ___{result}___ </p>")#TMP
    #TMP
    #for pair in result:
    #    for key in pair:
    #        print(f"Pair repr: __{key.encode()}:{pair[key].encode()}__")
    #\TMP
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

def generate_persist_crate_form(filename: str) -> None:
    """ Generate HTML form with button to persist crate to DB. """
    form_html = """ <form method="post" enctype="multipart/form-data" 
        action="save_to_db.php"> """
    print(form_html)
    print(""" <input value="Save crate" name="submit" type="submit" /> """)
    print(f"<input type=\"hidden\" value=\"{filename}.json\" name=\"jsonfilename\" />")
    print("</form>")

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
    #print(f"Try open w {filename} \n")#TMP
    try:
        with open(f"{filename}.json", 'w', encoding='utf-8') as file:
            #print(f"<p>SAVE TO JSON: ___{pairs}___</p>")#TMP
            json.dump(pairs, file, ensure_ascii=False)
            return True
    except: #Exception as e: #PermissionError as e:
        #print(e)#TMP
        return False
#

def main():
    """ Receives name of text file. """
    video_list_file_name = sys.argv[1]
    #print("<h1>" + repr(encode_to_html_entities("&")) +"</h1>")#TMP
    #with open('/var/www/OwnedByUbuntu/amp.txt', 'w') as tmp:#TMP
    #    tmp.write("&")#TMP
    pairs = parse_into_dictios(video_list_file_name)
    display_list_pairs(pairs)
    write_suc = save_pairs_to_disk(pairs, video_list_file_name)
    if not write_suc:
        print("<p>Unable to write video list to disk!</p>")
        exit(1)
    generate_playlist_form(video_list_file_name)
    generate_persist_crate_form(video_list_file_name)
    #print(f"<p>MAIN COMPLETE!!!!</p>")#TMP
#


if __name__ == '__main__':
    main()
#


