#!/usr/bin/python
#  Joel Gurnett
#  Converts ts files to mp4
#  June 21, 2019

from pyunpack import Archive
import globalFunc
def convertedList(path):
	# define an empty list
	places = []

	# open file and read the content in a list
	with open(path, 'r') as filehandle:
		for line in filehandle:
			# remove linebreak which is the last character of the string
			currentPlace = line[:-1]

			# add item to the list
			places.append(currentPlace)
	
	if len(places) > 0:
		return places
	return None

# execute program
def main():
	convPath = "/Users/joelgurnett/Desktop/convertedFiles.txt"
	# main path to start on 
	dirPath = "/Users/joelgurnett/Desktop/another/"
	convList = convertedList(convPath)
	# get list of ts files
	files = globalFunc.getFiles(dirPath)
	# iterate through the list
	if files != None:
		if (convList != None):
			f = open(convPath, "a+")
		else:
			f = open(convPath, "w+")
		for rar in files:
			if (rar not in convList):
				filename, file_extension = os.path.splitext(rar)
				infile = rar
				Archive(rar).extractall("/Users/joelgurnett/Desktop/another/")
				f.write("\n" + filename + file_extension)

		f.close()
	else:
		print("no files")

main()