#!/usr/bin/python
#  Joel Gurnett
#  unrars files, checks if they are already part of an extracted file
#  April 29, 2020

from pyunpack import Archive
import globalFunc

# create a list of files that have been extracted in the past
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
	# path to converted files list
	convPath = "/Users/joelgurnett/Desktop/convertedFiles.txt"
	# main path to start on 
	dirPath = "/Users/joelgurnett/Desktop/another/"
	# save the file to a list
	convList = convertedList(convPath)
	# get list of ts files
	files = globalFunc.getFiles(dirPath)
	# iterate through the list
	if files != None:
		# if the file already exists append to it, else create a new one
		if (convList != None):
			f = open(convPath, "a+")
		else:
			f = open(convPath, "w+")
		for rar in files:
			if (rar not in convList):
				filename, file_extension = os.path.splitext(rar)
				infile = rar
				
				# extract the file to this folder
				Archive(rar).extractall("/Users/joelgurnett/Desktop/another/")
				# write it to the file with the extracted files
				f.write("\n" + filename + file_extension)

		f.close()

main()
