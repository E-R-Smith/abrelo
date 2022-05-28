#!/usr/bin/env python

from datetime import date, datetime
import webbrowser

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
firefox_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'
edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
url = ''
now = 0

print("This program will open a URL in Firefox, Chrome, and Edge at a given time.")
url = input('Enter the URL to open: ')
print("Open it when?")
hour = str(input('Hour (00-23): ')).zfill(2)
minute = str(input('Minute (00-59): ')).zfill(2)

print(f"\n\n{url} will launch at {hour}:{minute}")
print("\nThis terminal will remain open until then. Close this terminal to stop the program")

while (now != f"{hour}:{minute}:00"):
    now = datetime.now()
    now = now.strftime("%H:%M:%S")

#register Firefox
webbrowser.register('firefox',
	None,
	webbrowser.BackgroundBrowser(firefox_path))
#register Chrome
webbrowser.register('chrome',
    None,
    webbrowser.BackgroundBrowser(chrome_path))
#register Edge
webbrowser.register('edge',
    None,
    webbrowser.BackgroundBrowser(edge_path))

print('opening...')
webbrowser.get('firefox').open_new(url)
webbrowser.get('chrome').open(url)
webbrowser.get('edge').open(url)
print('done')
