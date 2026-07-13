import webbrowser
import datetime

def jarvis():
    print("Hello !!! I am Jarvis...")
    print("Available commands...")
    print("1. google")
    print("2. youtube")
    print("3. time")
    print("4. exit")

    while True:
        command = input("\n Enter the command:").lower()

        if command == "google":
            print("Opening google...")
            webbrowser.open("http://www.google.com")
        elif(command == "exit"):
            break
        elif command == "youtube":
            print("Opening youtube...")
            webbrowser.open("http://www.youtube.com")
        elif command == "time":
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Current time is: {current_time}")
        else:
            print("Command Not Found")
jarvis()