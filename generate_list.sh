#! /usr/bin/env bash

function process_subdir {
  if [[ $# -ne 1 ]]
  then
    echo "Subfolder name missing. "
    exit 1
  fi
  #ls ./$1/* #TMP
  cd $1
  for video_file in ./*.mp4
  do
    duration=$(ffprobe -v error -select_streams v:0 \
	    -show_entries stream=duration \
	    -of default=noprint_wrappers=1:nokey=1 "${video_file}")
    CWD=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)
    echo "$CWD/${video_file} ::: ${duration}" >> ../list_$1.txt
  done
}

function main {
  videos_subfolder="videos"
  if [[ $# -ge 1 ]]
  then
    videos_subfolder=$1
  fi
  process_subdir ${videos_subfolder}
}

sudo apt-get update
sudo apt install ffmpeg -y

main "$@"

