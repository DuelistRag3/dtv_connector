# Python steam connector

takes a given hostname/ip and port and connverts it to a steam connection link: steam://connect/{host}:{port}, then redirects user to it

if given a hostname it will lookup the ip first, because hostnames doesnt work for the connect link.

i only made this tool, because discord only allows http/https/discord links in buttons, but its very general purpos

## Install

clone the repo
```
git clone https://github.com/DuelistRag3/dtv_connector.git
```

change .env values if needed
```
HOST=0.0.0.0
PORT=8080
```

then either run it with docker
```
docker compose up -d
```

or without docker
```
pip install --no-cache-dir -r requirements.txt
py app.py
```
