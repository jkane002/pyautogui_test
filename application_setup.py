#!/usr/bin/env python
import pyautogui as pag
pag.PAUSE = .5

test = pag.confirm("Which cover letter?", buttons=['cg', 'swe'])
if test == 'cg':
    pag.hotkey("command", "space")
    pag.typewrite(['delete'])
    pag.typewrite("coverletter1_cg")
    pag.typewrite(["enter"])

    pag.hotkey("command", "space")
    pag.typewrite(['delete'])
    pag.typewrite("resume master")
    pag.typewrite(["enter"])
else:
    pag.hotkey("command", "space")
    pag.typewrite(['delete'])
    pag.typewrite("coverletter1_mobile")
    pag.typewrite(["enter"])

    pag.hotkey("command", "space")
    pag.typewrite(['delete'])
    pag.typewrite("resume master")
    pag.typewrite(["enter"])
