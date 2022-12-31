#'nohup python3 watcher.py &'
import pyinotify
import os
import subprocess
import logging

folder_to_watch = '.'

# Set up logging
logging.basicConfig(level=logging.INFO, filename='watch_folder.log', filemode='w', format='%(asctime)s - %(message)s')

# Create a watch manager
wm = pyinotify.WatchManager()

# Add a watch on the specified folder for the IN_CREATE event
wm.add_watch(folder_to_watch, pyinotify.IN_CREATE)

# Define a custom event handler class
class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        file_path = event.pathname
        file_name = os.path.basename(file_path)
        # Log a message
        logging.info('Adding file {} to rain client'.format(file_name))
        # Run the rain client add -t command with the file name as an argument
        subprocess.run(['rain', 'client', 'add', '-t', file_name])

# Create an event handler
handler = EventHandler()

# Create a notifier
notifier = pyinotify.Notifier(wm, handler)

# Loop indefinitely and process events as they occur
notifier.loop()
