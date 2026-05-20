import time
from datetime import datetime, timedelta
import threading
from flask import Flask, request
import alarm

app = Flask(__name__)

alarm_instance = alarm.Alarm() # Create an instance of the Alarm class
client_IP_address = "192.168.0.x" # Stop the alarm from being shut off from different IP addresses

def schedule_alarm():
    while True:
        now = datetime.now()
        wake_up_time = now.replace(hour=5, minute=0, second=0, microsecond=0)

        if now >= wake_up_time:
            wake_up_time += timedelta(days=1)

        time_until_alarm = (wake_up_time - now).total_seconds()

        time.sleep(time_until_alarm)
        alarm_instance.start_alarm()

threading.Thread(target=schedule_alarm, daemon=True).start() # Start the alarm scheduling in a separate thread


@app.route('/stop_alarm', methods=['POST']) # Define a route to stop the alarm
def stop_alarm():
    if request.remote_addr == client_IP_address:
        alarm_instance.stop_alarm()
        return "", 204
    return "", 403

app.run(host="0.0.0.0", port=5000)



