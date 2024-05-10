from ._anvil_designer import OvenTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Oven(OvenTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

    self.pizza_size = 'Small'
    self.pizza_size_price = 10.0
    self.item['crust'] = 'Thin'
    self.pizza_crust = 'Thin'
    self.crust_price = 1.0
    self.toppings = 0 # Integer # of toppings selected now
    self.top_price = 0.1
    self.price = 0.00
    #self.item['account'] = 0
    
    self.account = 0  # Initialize the account variable
    self.repeating_panel_1.items = app_tables.ovenpizzas.search()
    
   # Additional UI setup

    self.pizza_list_show()
    
    def submit_click(self, **event_args):
      """This method is called when the button is clicked"""
    
    new_row = app_tables.pizzas.add_row(size = self.pizza_size, crust = self.pizza_crust, toppings =self.top_list, price=self.price)
    l = list(self.repeating_panel_1.items) + [new_row]
    self.repeating_panel_1.items = l
  
    
    pass