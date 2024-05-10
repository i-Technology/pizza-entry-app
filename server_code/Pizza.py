import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from EventzAnvilAPI import DS_Init, DS_Logger, LibrarianClient, SubscriberFactory, RecordAction, QueryTerm, dsQuery, DS_Utility, RecordAction



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

class Pizza(object):
  def __init__(self,action,size,crust,toppings,price):
    self.record_id  = ''
    self.action = action
    self.size = size
    self.crust = crust
    self.toppings = toppings
    self.price = price
    
  def load_pizza(self,size,crust,toppings,price):
    self.size = size
    self.crust = crust
    self.toppings = toppings
    self.price = price
    
  def make_tuple(self):
    record_tuple = (size,crust,toppings,price)
    return record_tuple
  
  
  def submit_pizza(self,action):
    record_tuple = self.make_tuple()
    if action == 'New':
      publish_event = self.dsparam.the_publisher.publish(500001.00, record_tuple, RecordAction.INSERT.value)
    elif action == 'Update':
      publish_event = self.dsparam.the_publisher.publish(500001.00, record_tuple, RecordAction.UPDATE.value,self.record_id)
    elif action == 'Delete':
      publish_event = self.dsparam.the_publisher.publish(500001.00, record_tuple, RecordAction.DELETE.value,self.record_id)
    else:
      print('Invalid action!')
    
      
      
      
      
      