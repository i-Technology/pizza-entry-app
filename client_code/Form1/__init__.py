from ._anvil_designer import Form1Template
from anvil import *


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    size = 'Small'

    # Any code you write here will run before the form opens.
    
  def calculate
  
  def account_entered(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    print(self.item['account'])
    pass

#   def text_box_3_show(self, **event_args):
#     """This method is called when the TextBox is shown on the screen"""
#     print(self.item['size'])
#     pass

  def top1_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    print(self.top1.selected)
    
    if self.top1.selected == True:
      self.top1.selected = False
    else:
      self.top1.selected= True
      
    print(self.top1.selected)
    pass

  def size_change(self, **event_args):
    """This method is called when an item is selected"""
    print(self.item['size'])
    
    pass

  def size_show(self, **event_args):
    """This method is called when the DropDown is shown on the screen"""
    self.size.selected_value = "Small"
    pass

  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    pass

  def top2_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    print(self.top1.selected)
    
    if self.top2.selected == True:
      self.top2.selected = False
    else:
      self.top2.selected= True
      
    print(self.top2.selected)
    pass

  def pepperoni_cb_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    print(self.pepperoni_cb.checked)
    pass

  def submit_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Publish to RabbitMQ
    
    pass













