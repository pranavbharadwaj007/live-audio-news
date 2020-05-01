#NEWS READING  PROGRAMME,
#####INTERNET CONNECTION REQUIRED
from win32com.client import  Dispatch
def speak(str):
    speak = Dispatch(("SAPI.spvoice"))
    speak.speak(str)

if __name__ == '__main__':
    import requests
    import json
    url = ('https://newsapi.org/v2/top-headlines?'
           'sources=bbc-sport&'
           'apiKey=49e391e7066c4158937096fb5e55fb5d')

    pranav = requests.get(url)
    text = pranav.text
    cc = json.loads(text)
    print("#############CURRENT NEWS HEAD LINES#############")
    speak("welcome to pranav news agency")
    speak("current head lines")
    for i in range(0, 9):
        speak(cc['articles'][i]['title'])
        print("++++++++++BREAKING NEWS++++++++++ ")

