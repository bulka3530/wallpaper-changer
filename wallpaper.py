#!/usr/bin/env python3
import os
import requests
from xml.dom import minidom

url = "https://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1"

response = requests.get(url)

if response.status_code == 200:
	xml_content = response.content
	
	file = minidom.parseString(xml_content)
	
	models = file.getElementsByTagName("url")
	
	if models:
		print("found todays wallpaper url!")
		print("its " + "https://www.bing.com" + models[0].firstChild.data)
		os.system("gsettings set org.gnome.desktop.background picture-uri " + "https://www.bing.com" + models[0].firstChild.data)
		print("installed new wallpaper")
	else:
		print("dammit")
else:
	print("dammit")




