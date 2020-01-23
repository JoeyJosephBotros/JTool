import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler



def task2():

    print("press 1 to show the logs or 2 to save in file ")
    x = int(input("enter 1 or 2 : "))

    if x == 1:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
    elif x == 2:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S', filename='/root/python/Dirlog.txt' )
    try:
        path = input("enter the full path: ")

        event_handler = LoggingEventHandler()
        observer = Observer()
        observer.schedule(event_handler, path, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            exit
    except:
        print("Invalid input ya man ...")
        exit(1)
    
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()