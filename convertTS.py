#!/usr/bin/python
import subprocess
import os
from ffmpy import FFmpeg

def getFiles(dirPath):
	videoFiles = []
	files = os.listdir(dirPath)
	for index, file in enumerate(files):
		filename, file_extension = os.path.splitext(file)
		# print("file " + str(index) +" : " + filename)
		if(os.path.isdir(dirPath + file)):
			if(file[0] != "."):
				inner = os.listdir(dirPath + file)
				for tmp in inner:
					tmpname, tmp_extension = os.path.splitext(tmp)
					if tmp_extension == ".ts":
						videoFiles.append(dirPath + file + "/" + tmp)
		if file_extension == ".ts":
			videoFiles.append(dirPath + file)

	if len(videoFiles) > 0:
		return videoFiles

	return None


def main():
	dirPath = "/Users/joelgurnett/Downloads/show/"
	vids = getFiles(dirPath)
	if vids != None:
		for index, video in enumerate(vids):
			filename, file_extension = os.path.splitext(video)
			infile = video
			outfile = filename + ".mp4"
			print("file: " + infile)
			print("outfile: " + outfile)
			for file in vids:
				print(file)

			p = subprocess.call(["ffmpeg", "-i", infile, outfile])
			os.remove(infile)
	else:
		print("no files")

main()