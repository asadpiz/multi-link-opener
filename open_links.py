#! /usr/bin/env python
import sys
import webbrowser

try:
    browser_path = 'C:/Program Files/Opera/launcher.exe'
    # browser_path = "\"C:\Program Files\Opera\launcher.exe\""
    #webbrowser.register('opera', None, webbrowser.BackgroundBrowser(browser_path))
    links = open ("link.txt", "r")
    #browser = webbrowser.get("C:/Program Files/Opera/launcher.exe %s")
    for line in links:
        browser.open(line,new=2,)
    links.close()
except Exception as e:
    print (e)
    links.close()
