from os import listdir
from os.path import isfile, join

import os

import shutil

mypath = r"."
base_localisation_path = r".\english"

languages = ['french', 'german', 'braz_por', 'russian', 'spanish', 'polish']

onlyfiles = [f for f in listdir(base_localisation_path) if isfile(join(base_localisation_path, f))]

for language in languages: # Check if directory exist. If they don't, create them
	directory = mypath + "\\" + language
	if not os.path.exists(directory):
		os.makedirs(directory)


for file in onlyfiles:
	fileBaseName = file[:-11] # Remove the english.yml
	fileBaseCompleteLink = base_localisation_path + "\\" + file
	
	for language in languages:
		fileCompleteName = fileBaseName + language + ".yml"
		fileCompleteLink = mypath + "\\" + language + "\\" + fileCompleteName
		shutil.copy2(fileBaseCompleteLink, fileCompleteLink) # complete target filename given