# This script automatically checks the battery percentage and updates us the action required.


import psutil
import pyttsx3



done='Hey Mani Please charge only'


# Voice Engine
def voice(message):
    engine = pyttsx3.init()

    engine.say(message)
    engine.runAndWait()

battery = psutil.sensors_battery()

# To know whether the charger is plugged in or not
print(psutil.sensors_battery().power_plugged)
while True:
#checking the battery percentage
    if battery.percent < 20:
        if psutil.sensors_battery().power_plugged:
            pass
        else:
            print('Please charge')
            done=done + str(battery.percent) +'left'
            voice(done)
    elif battery.percent == 100 or battery.percent >95:
        if psutil.sensors_battery().power_plugged:
            print('charging completed')
            done = 'Hey Mani Please turn off the charging, battery percent is ' + str(battery.percent)
            voice(done)


