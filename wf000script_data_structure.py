from enum import Enum

def textToMp3FileName(text,id):
    return str(id).zfill(5)+text+".mp3"

class SceneType(Enum):
    VIDEO = 1
    IMG = 2
    TEXT = 3
    COLOR = 4

class TransitionType(Enum):
    NONE = 1
    FADE = 2
    WIPE = 3

class Transform:
    scale = [1,1]
    position = [0,0]
    rotation = 0
    def __init__(self,scale,position,rotation):
        self.scale = scale
        self.position = position
        self.rotation = rotation

class ScriptItem:
    mp3 = ""
    img_src = ""
    transform = None
    transition_type = TransitionType.NONE



