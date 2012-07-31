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
import locale

from lib.beets.mediafile import MediaFile

music_dir = raw_input("Enter the path to your music directory: ")

music_dir = unicode(music_dir)

# Try to mimic the encoding/decoding done in the original librarysync
SYS_ENCODING = None

try:
    locale.setlocale(locale.LC_ALL, "")
    SYS_ENCODING = locale.getpreferredencoding()
    print "SYS_ENCODING is: " + SYS_ENCODING
except (locale.Error, IOError):
    print "Could not get SYS_ENCODING"
    pass

# for OSes that are poorly configured I'll just force UTF-8
if not SYS_ENCODING or SYS_ENCODING in ('ANSI_X3.4-1968', 'US-ASCII', 'ASCII'):
    SYS_ENCODING = 'UTF-8'
    
print "Configured SYS_ENCODING is: " + SYS_ENCODING

music_dir = music_dir.encode(SYS_ENCODING)
print "Encoded music_dir is " + repr(music_dir)
raw_input("Press Enter to start scan\n")
    
for r,d,f in os.walk(music_dir):
    for files in f:
        if any(files.lower().endswith('.' + x.lower()) for x in ["mp3", "aac", "ogg", "ape", "m4a", "flac"]):

            song = os.path.join(r, files)

            print "Reading file: " + song.decode(SYS_ENCODING)
            try:
                f = MediaFile(song)

            except:
                print 'Cannot read file: ' + song.decode(SYS_ENCODING)
                continue
                
            print f.bitrate
            print f.albumartist
            print f.artist
            print f.title
            print f.mb_trackid

