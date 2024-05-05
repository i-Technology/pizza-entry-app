from ._anvil_designer import Form1Template
from anvil import *


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    size = 'Small'
    size_price = 10.0
    self.item['crust'] = 'Thin'
    crust = 'Thin'
    crust_price = 1.0
    toppings = []
    top_price = 0.0
    
    self.calculate_price(size_price, crust_price, toppings, top_price)

    # Any code you write here will run before the form opens.
    
  def calculate_price (self, size_price, crust_price, toppings, top_price):
    
    price = size_price + crust_price + len(toppings)*top_price
    price = 12.34
    print (price)
    
    self.price_tb.text = price
  
  
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
    """This method is called when a Size is selected"""
    print(self.item['size'])
    if self.item['size'] == 'Small':
      size_price = 10.0
    if self.item['size'] == 'Medium':
      size_price = 15.0
    if self.item['size'] == 'Large':
      size_price = 20.0
    
    self.item['price_show'] = size_price
    
    print (type(size_price),size_price)
    self.price_tb.text = size_price
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

  def crust_change(self, **event_args):
    """This method is called when an item is selected"""
    crust = self.item['crust']
    print(crust)
    if self.item['crust'] == 'Thin':
      crust_price = 1.0
    if self.item['crust'] == 'Crispy':
      crust_price = 1.50
    if self.item['crust'] == 'Thick':
      crust_price = 2.0
    print(crust_price)
    pass

  def price_tb_show(self, **event_args):
    """This method is called when the TextBox is shown on the screen"""
    self.price_tb.text = '987.56'
    
    pass

  def crust_show(self, **event_args):
    """This method is called when the DropDown is shown on the screen"""
    self.crust.selected_value = "Thin"
    crust = self.item['crust']
    pass

  def price_tb_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

















