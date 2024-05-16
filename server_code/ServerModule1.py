import anvil.users
# ServerModule1  May 6-24

import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from EventzAnvilAPI import Publisher, Subscriber

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

publisher = Publisher()

@anvil.server.callable
def set_session_id(s):
  print(f'Setting Session Id: {s}')
  anvil.server.session['session_id'] = s
  
@anvil.server.callable
def launch_subscriber_task():
  print("Launching the subscriber task")
  #subscriber = Subscriber()
  subscriber_task = anvil.server.launch_background_task('background_subscriber_task')
  if subscriber_task: 
    print(f"I have a subscriber_task: {subscriber_task}")
#     subscriber_task.run
  return subscriber_task

@anvil.server.background_task
def background_subscriber_task():
  subscriber = Subscriber()
  return subscriber.subscriber_task()