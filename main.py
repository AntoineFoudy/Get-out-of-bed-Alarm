import time
import alarm

a = alarm.Alarm()
a.start_alarm()

time.sleep(60)
a.stop_alarm()