import time

def sleep_timer(minutes):
    # Implement sleep timer logic here
    time.sleep(minutes * 60)

def remaining_sleep_time(end_time):
    # Implement remaining sleep time calculation logic here
    remaining_time = end_time - time.time()
    minutes = int(remaining_time // 60)
    seconds = int(remaining_time % 60)
    return minutes, seconds
