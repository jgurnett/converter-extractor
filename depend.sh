chmod +x convertTS.py
sudo apt --assume-yes install ffmpeg
sudo apt --assume-yes install python-pip
pip --assume-yes install ffmpy
echo 0 0 * * 0 /convertTS.py >> crontab -e