#!/usr/bin/env python3
#  Joel Gurnett
#  Converts ts files to mp4
#  June 21, 2019 - edited April 29, 2020

import subprocess
import os
import globalFunc
from ffmpy import FFmpeg
from datetime import date

# save the list of all .ts files to a log 
def output(files):
	today = date.today()
	f =  open("/home/joel/Desktop/converted/converted_" + str(today) + ".txt", 'w+')
	for item in files:
		f.write("%s\n" % item)
	f.close()

# execute program
def main():
	# main path to start on 
	dirPath = "/home/joel/media/shows/"
	# get list of ts files
	vids = globalFunc.getFiles(dirPath)
	output(vids)
	# iterate through the list
	if vids != None:
		for video in vids:
			filename, file_extension = os.path.splitext(video)
			infile = video
			outfile = filename + ".mp4"

			# convert ts to mp4
			p = subprocess.call(["ffmpeg", "-i", infile, "-s", "hd720", outfile])
			# rmove ts file
			os.remove(infile)
	else:
		print("no files")

main()
