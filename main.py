import psutil
from playsound import playsound

def powersound():
    while not psutil.sensors_battery().power_plugged:
        pass
    if psutil.sensors_battery().power_plugged:
        playsound('power.mp3')
    while psutil.sensors_battery().power_plugged:
        pass
    if not psutil.sensors_battery().power_plugged:
        powersound()

powersound()