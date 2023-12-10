import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    

if __name__=='__main__':
    print('Hello this is robo speaker 1.1')
    while True:
        x = input('type what do you want me to speak: ')
        if x=='q':
            break
        speak(x)
        
