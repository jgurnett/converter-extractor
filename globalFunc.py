#!/usr/bin/python
#  Joel Gurnett
#  Converts ts files to mp4
#  June 21, 2019 - edited April 29, 2020

import os
# recursively gets all ts files that are in given path
#
# dirPath: string of path given
def getFiles(dirPath):
	videoFiles = []
	files = os.listdir(dirPath)
	# go through all files in directory
	for file in files:
		filename, file_extension = os.path.splitext(file)
		# if the file is a directory then iterate through that
		if(os.path.isdir(dirPath + file)):
			# don't look at hidden files
			if(file[0] != "."):
				tmpList = getFiles(dirPath + file + "/")
				if tmpList != None:
					videoFiles.extend(tmpList)

		if file_extension == ".rar":
			videoFiles.append(dirPath + file)

	if len(videoFiles) > 0:
		return videoFiles
	return None