#! /usr/bin/env python

""" Parse video-list text file into a dictionary Title:duration. """

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


def main():
    """ Receives name of text file. """
    video_list_file_name = sys.argv[1]
    pairs = parse_into_dictios(video_list_file_name)
    display_list_pairs(pairs) #TMP
#


if __name__ == '__main__':
    main()
#


