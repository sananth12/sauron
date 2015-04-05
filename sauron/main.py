from sys import version_info
from time import sleep
import argparse
if version_info.major is 2:
    import pynotify
    notifyModule = "pynotify"
    if version_info.major is 3:
        try:
            from gi.Repository import Notify
            notifyModule = "Notify"
        except ImportError:
            import notify2
            notifyModule = "notify2"

Interrupt = False
            
def pop(title, message, logo):
    if notifyModule is "pynotify":
                pynotify.init("Scorer")
                pynotify.Notification(title, message, logo).show()
    elif notifyModule is "Notify":
                Notify.init("Scorer")
                Notify.Notification.new(title, message, logo).show()
    else:
                notify2.init("Scorer")
                notify2.Notification(title, message, logo).show()
    return True

def get_args():
    parser = argparse.ArgumentParser(
                            description='Downloads images from given URL')
    parser.add_argument('-t', '--time', type=int, default=1200,
                                                    help="No. of seconds to alert\n")
    args = parser.parse_args()
    time = args.time
    return time
             
def console_main():
    print ("Souron : Sauron reminds you to take regular break and follow the 20-20-20 rule")
    alert_time = get_args()
    while True:
        try:
            pop("Sauron sees you!", "Time to rest those eyes!\n Look away from the screen for 20s!",
                "path/to/image")
            sleep(alert_time)
            
        except KeyboardInterrupt:
            if Interrupt:
                print("Bye bye")
                exit
            else:
                print("Press Ctrl+C again to quit")
                Interrupt =  True
    


