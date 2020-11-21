# tsConverter
- Converts ts file to mp4 

# unrar
- extracts all rar files within a given path

# Dependacies
- there is a script to run if on ubuntu linux
- chmod +x depend.sh
- ./depend.sh <br /><br />
- if on mac install ffmpeg, python pip3, and with pip3 ffmpy, pyunpack, patool 

# crontab
- I run unrar with the below crontab to run everyday at 8PM<br />
`0 16 * * * /home/joel/Desktop/converter-extractor/unrar.py`
