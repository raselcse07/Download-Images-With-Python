#! /usr/bin/python3 

import os 
import random
import urllib.request


def create_or_get_directory(dirName):
	'''
	I will create a directory to store
	all of downloaded images. Directory
	name will be the parameter that we will 
	pass to this function. If the directory 
	with this name is already exists then this 
	function will return that directory .Otherwise 
	create a new directory & return the directory.
	'''
	if not os.path.exists(dirName):
	    os.mkdir(dirName) # create the directory
	return dirName 


def get_image_ext(filepath):
	'''
	This function will check the file
	extensions.If there is no file extensions,
	then it will provide ".jpg" as default.
	'''
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	if ext == "":
		ext = ".jpg"
	return name, ext


def downloader(image_url):
    # Generate random numbers from 1 to 10000
    randnumber = random.randrange(1,10000)

    # Get the images extention
    name, ext = get_image_ext(image_url)

    # Full image name
    images_name = str(randnumber) + ext 

    # Downloading path 
    dirName = create_or_get_directory("Images")

    # Images name with directory
    upload_path = "{dirName}/{images_name}".format(
    				dirName = dirName,
    				images_name = images_name
  				)

    # Finally send a HTTP request to the server & download the image.
    urllib.request.urlretrieve(image_url, upload_path)


def main(filename):
	try:
		file = open(filename,"r") # Open the file with read mode
		images_url = file.readlines() 
		for i in images_url:
			downloader(i) # Downloading ...
		file.close() 
		return True # Successfully downloaded
	except IOError:
		return False # File does not exists
