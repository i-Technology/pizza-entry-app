from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    #-------------

  def link_1_click(self, **event_args):
    """This method is called when the TRASH link is clicked"""
    self.item.delete()
    self.remove_from_parent()
    print('Line 18 delete')
    pass
  
  def form_refreshing_data_bindings(self, **event_args):
    
    """This method is called when refreshing_data_bindings is called"""
  
    pass

# class RowTemplate1(RowTemplate1Template):
#     def __init__(self, **properties):
#         # Make sure all inherited properties are initialized properly.
#         self.init_components(**properties)
        
#         # Example of setting item, assuming this RowTemplate is used in a RepeatingPanel
#         # This should be set outside this class, typically where the RepeatingPanel's items are assigned.
#         # self.item = {'size': 'Medium', 'price': 20}  # Example dictionary

#     # Use this method to handle specific initialization for each row.
#     def set_item_data(self, item_data):
#         self.item = item_data
#         try:
#             print(self.item['size'])  # Correctly accessing the size if item is a dictionary
#         except TypeError as e:
#             print(f"Error: {str(e)} - Check that 'item' is a dictionary with a 'size' key.")
#         except KeyError as e:
#             print(f"Missing key: {str(e)} in item")

#     # Any code you write here will run before the form opens.

    def form_refreshing_data_bindings(self, **event_args):
      """This method is called when refreshing_data_bindings is called"""
#     pass

