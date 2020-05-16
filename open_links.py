#! /usr/bin/env python
import sys
import webbrowser

try:
    links = open ("link.txt", "r")
    browser = webbrowser.get("C:/Program Files/Opera/launcher.exe %s")
    #browser = webbrowser.get('opera')
    for line in links:
        browser.open(line,new=2,)
    links.close()
except Exception as e:
    print (e)
    links.close()
