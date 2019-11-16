import pyperclip

def getClip():
  return pyperclip.paste()
def setClip(clipData):
  pyperclip.copy(clipData)
  return clipData
def updateClip():
  