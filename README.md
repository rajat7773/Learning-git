# Learning-git


#Download python environmnt through these commands
python3 -m venv ./venv
source venv/bin/activate

#then install fastapi
pip3 install fastapi

#This lets you run the code #main.py on local host
fastapi dev main.py

#all can see
uvicorn app:app --host 0.0.0.0

Then use IP Address of the Latop's connection to view the same on other devices connected through the same network.