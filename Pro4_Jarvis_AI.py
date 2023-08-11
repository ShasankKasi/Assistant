import speech_recognition as sp
import os
import win32com.client
import webbrowser
import time as t
import openai
import random
import json
import requests

chatStr=""
speaker = win32com.client.Dispatch("Sapi.Spvoice")
file_path=r"https://wynk.in/music/song/levitating/wm_A10302B00055145532?q=levitating"
# file_path2=r"C:\Users\SHASANK REDDY\OneDrive\Desktop\LTspice XVII.lnk"
def say(text):
    speaker.Speak(text)
def chat(query):
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    global chatStr
    # print(chatStr)
    chatStr +=f"Shasank:{query}\n Jarvis :"
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=chatStr,
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    say(response["choices"][0]["text"])
    chatStr=chatStr+f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]
    
    if not os.path.exists("OpenAI"):
        os.mkdir("OpenAI")
    with open(f"OpenAI/prompt-{random.randint(1,100000000)}","w") as fd:
              fd.write(text)

def ai(prompt):
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    text="The response for my Open AI prompt is  \n ***************************************************\n"

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    print(response["choices"][0]["text"])
    text=text+response["choices"][0]["text"]
    
    if not os.path.exists("OpenAI"):
        os.mkdir("OpenAI")
    with open(f"OpenAI/prompt-{random.randint(1,100000000)}","w") as fd:
              fd.write(text)
def takeCommand():
    r = sp.Recognizer()
    stop_listening = False

    with sp.Microphone() as source:
        r.pause_threshold = 1

        while not stop_listening:
            audio = r.listen(source)

            try:
                query = r.recognize_google(audio, language='en-in')
                print(f"User said: {query}")
                k=query.split(" ")
                if "music" in k:
                        # os.startfile(file_path)
                        webbrowser.open(f"https://wynk.in/music/song/levitating/wm_A10302B00055145532?q=levitating")
                        say("playing music sir")
                
                if "open" in k:
                    
                    # say(f"opening {k[1]} sir")
                    # elif "Lt" in k:
                    #     os.startfile(file_path2)
                        
                
                        webbrowser.open(f"https://www.{k[1]}.com")
                        say(f"opening {k[1]} sir")
                    # say(f"opening {query.upper()} sir")
                
                elif "stop" in query.lower():
                    stop_listening = True
                elif "time" in k:
                    timer=t.strftime( "%H %M %S" )
                    say(f"Sir The time is{timer}")
                    print(f"The time is{timer}")
                
                # elif "news" in query:
                #     say("Tell the topic you are interested in")
                #     r = sp.Recognizer()
                #     r.pause_threshold = 1
                #     audio = r.listen(source)
                #     print(f"User said: {q}")
                #     q = r.recognize_google(audio, language='en-in')
                #     url=f"https://newsapi.org/v2/everything?q={q}&from=2023-06-07&sortBy=publishedAt&apiKey=ceea1fbb09f64105860483b7c7a9b796"

                #     r=requests.get(url) 
                #     news=json.loads(r.text)
                #     # for article in news['articles']:
                #     print(news['articles'][0]['title'])
                #     say(news['articles'][0]['title'])
                #     print( news['articles'][0]['description'])
                #     say( news['articles'][0]['description'])
                #     print("_____________________________________________________________________________________________________")
                        
                elif "using artificial intelligence" in query.lower():
                    say("Writing sir")
                    ai(prompt=query)
                elif "reset chat" in query.lower():
                    chatStr=""
                    say("Chat reset sir")
                    print("Chat reset sir")
                else :
                    chat(query)
            except sp.UnknownValueError:
                print("Could not understand audio")
            except sp.RequestError as e:
                print(f"Request error: {e}")

        return query

say("Hello, I am Jarvis")
print("Hello, I am Jarvis")
print("To open any website say in the format \"Open Website or use stop at the end to exit")
print("Listening")
text = takeCommand()
say("Thanks for spending time with me       This is Jarvis  Signing off")
