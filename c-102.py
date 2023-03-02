import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

Hi = '/Users/luvpreetsinghcheema/Downloads/c-102'
class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Created: {event.src_path} has been created!")
        
    def on_deleted(self, event):
        print(f"Oops! Someone deleted: {event.src_path}!")

event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, Hi,  recursive=True)
observer.start()
print(f"Watching directory {Hi}...")

try:
    while True:
        time.sleep(2)
        print("running....")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()
