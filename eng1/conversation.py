from itertools import count
import re
import dialog
import robotsp as sp
import subscriber
import threading
import time
import datetime


ROBOT_IP = '192.168.50.76'
ROBOT_PORT = 22222
DIALOG = dialog.DIALOG_1
ROBOT_RESPONSED = []
def get_day():
    dt_now = datetime.datetime.now()
    now_month = dt_now.month
    if 5 <= now_month <= 10:
        asking = "Is it hot today?"

    else:
        asking = "Is it cold today?"
    sp.question(ROBOT_IP, ROBOT_PORT, asking)
    ROBOT_RESPONSED.append(asking)
    print("doing function get_day")


def run_dialog():
    asr_sub = subscriber.TCPSubscriber('127.0.0.1', 10001)
    asr_sub.subscribe()
    for line in DIALOG:
        if isinstance(line, str):
            if line.startswith("$"):
                # 関数として処理をする
                eval(line[1:])
                continue

            if line.endswith("?"):
                sp.question(ROBOT_IP, ROBOT_PORT, line)
                ROBOT_RESPONSED.append(line)
                print("Robot asked you.")
                continue

            if line.endswith("!"):
                sp.happy(ROBOT_IP, ROBOT_PORT, line)
                ROBOT_RESPONSED.append(line)
                print("You made Robot happy!")
                continue

            d = sp.random_say(ROBOT_IP, ROBOT_PORT, line)
            ROBOT_RESPONSED.append(line)
            print(line)
            time.sleep(d + 1)
            continue
        
        if isinstance(line, dict):
            recognition_start_time = time.time()
            robot_response_rules = ["Could you say that again?", "Pardon.", "Excuse me", "What did you say?"]

            while True:
                speech_recognitions = asr_sub.get_memory_between(recognition_start_time, time.time())

                if speech_recognitions != []:
                    if str(speech_recognitions[-1]['result']) in robot_response_rules:
                        print("You listened back!")
                        listenback_line = ROBOT_RESPONSED[-1]
                        sp.random_say(ROBOT_IP, ROBOT_PORT, "i said," + listenback_line)
                        speech_recognitions[-1]['result'] = ""
                        
                
                speech = get_matched_speech(line, speech_recognitions)
                if speech is None:
                    time.sleep(0.1)
                    continue

                if speech.endswith("?"):
                    sp.question(ROBOT_IP, ROBOT_PORT, speech)
                    ROBOT_RESPONSED.append(speech)
                    print("Robot asked you.")
                    break

                if speech.endswith("!"):
                    sp.happy(ROBOT_IP, ROBOT_PORT, speech)
                    ROBOT_RESPONSED.append(speech)
                    print("You made Robot happy!")
                    break                

                d = sp.random_say(ROBOT_IP, ROBOT_PORT, speech)
                ROBOT_RESPONSED.append(speech)
                print(speech)
                time.sleep(d + 1)
                break
            continue
    #asr_sub.close()


def get_matched_speech(line:dict, speech_recognitions:list) -> str:
    for recognition in reversed(speech_recognitions):
        if recognition['topic'] != 'recognized':
            continue
        if recognition['result'] == '':
            continue
        for pattern, speech in line.items():
            if re.search(pattern, recognition['result']):
                return speech
    return None


if __name__ == '__main__':
    threading.Thread(target=run_dialog, daemon=True).start()
    try:
        while True:
            input('Ctrl-cで終了\n')
    except KeyboardInterrupt:
        pass
