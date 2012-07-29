#!/usr/bin/env python
#  This file is part of Headphones.
#
#  Headphones is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Headphones is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Headphones.  If not, see <http://www.gnu.org/licenses/>.

import os

from lib.beets.mediafile import MediaFile

music_dir = raw_input("Enter the path to your music directory: ")
    
for r,d,f in os.walk(music_dir):
    for files in f:
        if any(files.lower().endswith('.' + x.lower()) for x in ["mp3", "aac", "ogg", "ape", "m4a", "flac"]):

            song = os.path.join(r, files)

            print "Reading file: " + song
            try:
                f = MediaFile(song)

            except:
                print 'Cannot read file: ' + song
                continue
                
            print f.bitrate
            print f.albumartist
            print f.artist
            print f.title
            print f.mb_trackid

