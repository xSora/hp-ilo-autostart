import os
import time
from hpilo import Ilo
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone


ilo = None

def check_env():
    load_dotenv()
    if(os.getenv("ILO_ADDRESS") == None):
        print("ILO_ADDRESS not set")
        exit()
    if(os.getenv("ILO_USERNAME") == None):
        print("ILO_USERNAME not set")
        exit()
    if(os.getenv("ILO_PASSWORD") == None):
        print("ILO_PASSWORD not set")
        exit()
    if(os.getenv("SERVER_START_HOURS") == None):
        print("SERVER_START_HOURS not set")
        exit()
    if(os.getenv("SERVER_START_MINUTES") == None):
        print("SERVER_START_MINUTES not set")
        exit()

def start_server():
    global ilo
    print("Starting Server...")
    server_status = ilo.get_host_power_status()
    print(f"Server Status: {server_status}")
    if(server_status != "ON"):
        print("Powering On Server...")
        ilo.press_pwr_btn()
        time.sleep(10)
        print(f"Server Status: {server_status}")

def wait_timer():
    now = datetime.now()
    time_goal = datetime(now.year, now.month, now.day, int(os.getenv("SERVER_START_HOURS")), int(os.getenv("SERVER_START_MINUTES")), 0) # 20 Uhr
    print(f"Current Time:  {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Waiting Until: {time_goal.strftime('%Y-%m-%d %H:%M:%S')}")

    if(now > time_goal):
        time_goal = time_goal + timedelta(days=1)

    if(now < time_goal):
        wait_time = time_goal - now
        time.sleep(wait_time.seconds)

def wait_loop():
    global ilo
    # Connect to ILO
    try:
        ilo = Ilo(os.getenv("ILO_ADDRESS"), os.getenv("ILO_USERNAME"), os.getenv("ILO_PASSWORD"))
        ilo.get_product_name()
        print("ILO Login Success")
    except:
        print("ILO Login Failed")
        exit()
    # ILO Login Success
    while(True):
        wait_timer()
        start_server()

def main():
    print("HP ILO Script by xSora")
    check_env()
    wait_loop()

if __name__ == "__main__":
    main()
