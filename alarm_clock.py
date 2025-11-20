import datetime, time, winsound


user_input = input("Set the alarm: xx:xx ")
alarm_hour, alarm_minute = map(int, user_input.split(":"))
print(f"Alarm set for {user_input}")


while True:
    now = datetime.datetime.now()
    current_hour = now.hour
    current_minute = now.minute

    if current_hour == alarm_hour and current_minute == alarm_minute:
        print("Wakie wakie eggs ang bakey")
        winsound.Beep(1000, 1000)
        break

time.sleep(20)
