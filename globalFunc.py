#!/usr/bin/python
#  Joel Gurnett
#  Converts ts files to mp4
#  June 21, 2019

import os
# gets all ts files that are in given path
#
# dirPath = string of path given
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
				tmpList = innerFolder(dirPath, file)
				videoFiles.extend(tmpList)

		if file_extension == ".rar":
			videoFiles.append(dirPath + file)

	if len(videoFiles) > 0:
		return videoFiles
	return None

# recusive function to go through folders within folder to get a list of .ts files
def innerFolder(path, file):
	tmpList = []
	inner = os.listdir(path + file)
	# print(path + file)
	for tmp in inner:
		if (os.path.isdir(path + file + "/" + tmp)):
			tList = innerFolder(path + file +"/", tmp)
			tmpList.extend(tList)
			
		tmpname, tmp_extension = os.path.splitext(tmp)
		if tmp_extension == ".rar":
			tmpList.append(path + file + "/" + tmp)

	return tmpList