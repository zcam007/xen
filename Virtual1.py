
import os.path
import sys
import json
import speech_recognition
import pyttsx
import pocketsphinx
import apiai
speech_engine = pyttsx.init('sapi5') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
speech_engine.setProperty('rate', 230)
#voices = speech_engine.getProperty('voices')
#for voice in voices:
speech_engine.setProperty('voice', 1)
 #  speech_engine.say('The quick brown fox jumped over the lazy dog.')
#speech_engine.runAndWait()

CLIENT_ACCESS_TOKEN = '093e0a8432ab4441939015c7696939ff'
song_name=""
def speak(text):
	speech_engine.say(text)
	speech_engine.runAndWait()
recognizer = speech_recognition.Recognizer()

def router(response_obj):
    parameters =response_obj["result"]["parameters"]
    parameters_list= parameters.keys()
    if 'website' and 'music-artist' in parameters_list:
        play_music(parameters)
    elif 'news' in parameters_list:
        fetch_news(parameters)
  
def play_music(parameters):
    song_name =parameters['music-artist']
    if parameters['website']=='youtube' or parameters['website']=='':
        execfile('youtube.py')
      
        
def fetch_news(parameters):
    #print "Here's what I got for you.."
    speak("Here's what I got for you")
    execfile('headlines.py')        
def main():
    while 1:
        ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

        request = ai.text_request()

        request.lang = 'en'  # optional, default value equal 'en'

    #request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"
        query=raw_input("User:")
        request.query = query

        response = request.getresponse()

        responsestr = response.read().decode('utf-8')
        response_obj = json.loads(responsestr)
        bot_response=response_obj["result"]["fulfillment"]["speech"]
        
        #print _param['website']
        print bot_response
        router(response_obj)
        speak(bot_response)
        if(query=="bye"):
            break
        

if __name__ == '__main__':
    main()