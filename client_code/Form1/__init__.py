from ._anvil_designer import Form1Template
from anvil import *


class Form1(Form1Template):
  def __init__(self, **properties): 
  # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.pizza_size = 'Small'
    self.pizza_size_price = 10.0
    self.item['crust'] = 'Thin'
    self.pizza_crust = 'Thin'
    self.crust_price = 1.0
    self.toppings = 0 # Integer # of toppings selected now
    self.top_price = 0.1
    self.calculate_price()
    self.pizza_list_show()
    

    # Any code you write here will run before the form opens.
    
  #def calculate_price (self, size_price, crust_price, toppings, top_price):
  def calculate_price(self):
    self.toppings = 0
    if self.pepperoni_cb.checked:
      self.toppings += 1
    if self.olives_cb.checked:
      self.toppings += 1
    if self.mushrooms_cb.checked:
      self.toppings += 1
  
    
    print ('CP1',self.pizza_size_price,self.crust_price, self.toppings)
    print ('CP2', self.pizza_size, self.pizza_crust, self.toppings)
    price = (self.pizza_size_price + self.crust_price + self.toppings * self.top_price)
    print('CP3', price)
    
    self.price_tb.text ='${:,.2f}'.format(price)
    self.pizza_list_show()
    
  
  def account_entered(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    print(self.item['account'])
    pass


  def size_change(self, **event_args):
    """This method is called when a SIZE is selected"""
    print(self.item['size'])
    if self.item['size'] == 'Small':
      self.pizza_size = 'Small'
      self.pizza_size_price = 10.0
    if self.item['size'] == 'Medium':
      self.pizza_size = 'Medium'
      self.pizza_size_price = 15.0
    if self.item['size'] == 'Large':
      self.pizza_size = 'Large'
      self.pizza_size_price = 20.0
    
    self.item['price_show'] = self.pizza_size_price
    
    
    print (type(self.pizza_size_price),self.pizza_size_price)
    
    self.calculate_price()
    #self.price_tb.text = 'L64',self.pizza_size_price
    self.pizza_list_show()
    pass

  def size_show(self, **event_args):
    """This method is called when the SIZE DropDown is shown on the screen"""
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


  def submit_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Publish to RabbitMQ
    
    pass

  def crust_change(self, **event_args):
    """This method is called when a CRUST item is selected"""
    #global crust_price, size_price
    crust = self.item['crust']
    print(crust)
    if self.item['crust'] == 'Thin':
      crust_price = 1.0
    if self.item['crust'] == 'Crispy':
      crust_price = 1.50
    if self.item['crust'] == 'Thick':
      crust_price = 2.0
    print(crust_price)
    #self.calculate_price(size_price, crust_price, toppings, top_price)
    self.calculate_price()
    self.pizza_crust = crust
    self.pizza_list_show()
    pass

  def price_tb_show(self, **event_args):
    """This method is called when the TextBox is shown on the screen"""
    self.calculate_price()
    
#     if self.price_tb.text:
#       try:
#         # Convert text to a float, format as a dollar amount
#         value = float(self.price_tb.replace('$', '').replace(',', ''))
#         self.price_tb.text = '${:,.2f}'.format(value)
#       except ValueError:
#         # Handle the case where the text is not a valid number
#         self.price_tb.text = 'Invalid input'
    #self.price_tb.text = '0.00'
    
    pass

  def crust_show(self, **event_args):
    """This method is called when the DropDown is shown on the screen"""
    self.crust.selected_value = "Thin"
    crust = self.item['crust']
    pass

  def price_tb_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass
  
  def pepperoni_cb_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    print(self.pepperoni_cb.checked)
    self.calculate_price()
    pass

  def olives_cb_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    print(self.olives_cb.checked)
    self.calculate_price()
    pass

  def mushrooms_cb_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    print(self.mushrooms_cb.checked)
    self.calculate_price()
    pass

  def price_tb_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""

    if self.price_tb.text:
      try:
        # Convert text to a float, format as a dollar amount
        value = float(self.price_tb.replace('$', '').replace(',', ''))
        self.price_tb.text = '${:,.2f}'.format(value)
      except ValueError:
        # Handle the case where the text is not a valid number
        self.price_tb.text = 'Invalid input'
    pass

  def pizza_list_show(self, **event_args):
    """This method is called when the pizza_list TextBox is shown on the screen"""
    self.top_list = ''
    if self.pepperoni_cb.checked:
      self.top_list += 'Pepperoni, '
    if self.olives_cb.checked:
      self.top_list += 'Olives, '
    if self.mushrooms_cb.checked:
      self.top_list += 'Mushrooms, '
    # Remove the last comma and space from the top_list if it's not empty
    if self.top_list:
        self.top_list = self.top_list[:-2]
    self.pizza_list.text =   self.pizza_size, self.pizza_crust, self.top_list
   
    pass





















