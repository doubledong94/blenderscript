
import requests
import json
import time
from wf000script_data_structure import *
from wf001script1 import scriptObj


s = requests.session()

def getAudioLink(text):
    x = s.post("http://new.text-to-speech.cn/wp-content/plugins/speech-tts/getSpeek.php", data={"language": "%E4%B8%AD%E6%96%87%EF%BC%88%E6%99%AE%E9%80%9A%E8%AF%9D%EF%BC%8C%E7%AE%80%E4%BD%93%EF%BC%89", "voice": "zh-CN-YunxiNeural", "text": text, "role": "0", "style": "0", "rate": "3", "pitch": "0", "kbitrate": "audio-16khz-32kbitrate-mono-mp3", "silence": None, "styledegree": "1", "volume": "75", "predict": "0", "user_id": "15327", "backgroundaudio_url": None, "backgroundaudio_fadein": None, "backgroundaudio_fadeout": None, "yzm": None, "replice": "1"}, headers={"X-Requested-With": "XMLHttpRequest"}, cookies={"wordpress_dc294d1089fc92d04291e72879a2741f": "mpweixin_29845631%7C1722198651%7Cb3m43OsNFdXazvUaAbBTMKHXdcyhxipJbp142UwxjqO%7Cfccc3c3cf0c4a8cebb04f3c0cdc52d784c746beec04541b8f7f4179d5a713721", "Hm_lvt_b38a22175a63114a18d55183d7ddb4c4": "1719805315,1720982259,1720987890", "wordpress_logged_in_dc294d1089fc92d04291e72879a2741f": "mpweixin_29845631%7C1722198651%7Cb3m43OsNFdXazvUaAbBTMKHXdcyhxipJbp142UwxjqO%7C7477a96d1fc0a31f0553de7bd11d6d558e0b8207222f7fe5ea59d4fa5cd420c9"})
    a = json.loads(x.text)
    return a["download"]


def ttsImpl(text,mp3filepath):
    print("sleep 2")
    time.sleep(2)
    print(text)
    audio_link = getAudioLink(text)
    audio_response = s.get(audio_link, headers={"Range": "bytes=0-"}, cookies={"wordpress_logged_in_dc294d1089fc92d04291e72879a2741f": "mpweixin_29845631%7C1722198651%7Cb3m43OsNFdXazvUaAbBTMKHXdcyhxipJbp142UwxjqO%7C7477a96d1fc0a31f0553de7bd11d6d558e0b8207222f7fe5ea59d4fa5cd420c9", "Hm_lvt_b38a22175a63114a18d55183d7ddb4c4": "1719805315,1720982259,1720987890,1722053589", "HMACCOUNT": "3A98716D11045E97", "Hm_lpvt_b38a22175a63114a18d55183d7ddb4c4": "1722053611"})
    open(mp3filepath, "wb").write(audio_response.content)

def tts(text,id):
    ttsImpl(text,textToMp3FileName(text,id))

size = len(scriptObj)

for i,t in enumerate(scriptObj):
    if i > 216:
        print(str(i) + " / " + str(size))
        tts(t[1],i)