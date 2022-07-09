import robotop as op
from gtts import gTTS 
from pydub import AudioSegment
import robotMove as move
import random as rnd

def make_wav(text:str, output_file_path='temp.wav', slow=False) -> int:
    gTTS(text=text, lang='en', slow=slow).save('temp.mp3')
    sound = AudioSegment.from_mp3('temp.mp3')
    sound.export(output_file_path, format='wav')
    return sound.duration_seconds

def say_text(ip:str, port:int, text:str) -> int:
    d = make_wav(text)
    op.play_wav(ip, port, 'temp.wav')
    return d

def listenBack(ip:str, port:int, msg_obj:dict, text:str):
    robot_response_rules = ["could you say that again", "pardon", "excuse", "what did you say"]
    if msg_obj['topic'] == 'recognizing':
        if msg_obj['result'] in robot_response_rules:
            d = say_text(ip, port, text)
            move.tiltHead(ip, port)
            move.timeSleep(d)



def getConversation(ip:str, port:int, text:str, msg_obj:dict):
    d = say_text(ip, port, text)
    n = rnd.randint(0, 1)
    if text == "good morning":
        move.hi(ip, port)
    elif n == 0:
        move.pointing(ip, port)
    else:
        move.tiltHead(ip, port)
    move.timeSleep(d)


    listenBack(ip, port, msg_obj, text)


def hi(ip:str, port:int, text:str):
    d = say_text(ip, port, text)
    move.hi(ip, port)
    move.timeSleep(d)

def random_say(ip:str, port:int, text:str):
    d = say_text(ip, port, text)
    move.randomMove(ip, port)
    move.timeSleep(d)
    move.reset(ip, port)
    return d

def question(ip:str, port:int, text:str):
    d = say_text(ip, port, text)
    Question = [move.pointing(ip, port), move.pointing(ip, port)]
    n = rnd.randint(0, 1)
    Question[n]
    move.timeSleep(d)
    move.reset(ip, port)


def nodding(ip:str, port:int, text:str):
    d = say_text(ip, port, text)
    Nodding = ["move.nod(ip, port)", "move.Isee(ip, port)", "move.bothRaise(ip, port)", "move.rightRaise(ip, port)"]
    n = rnd.randint(0, 3)
    eval(Nodding[n])
    move.timeSleep(d)

    

def YesNo(ip:str, port:int,user_response:list, robot_response_rules:dict):
    if "yes" in user_response:
        nodding(ip, port, robot_response_rules["yes"])
    elif "no" in user_response:
        nodding(ip, port, robot_response_rules["no"])
    else:
        nodding(ip, port, "uh-huh")

def happy(ip:str, port:int, text:str):
    d = say_text(ip, port, text)
    move.bothRaise(ip, port)
    move.timeSleep(d)
    move.reset(ip, port)

