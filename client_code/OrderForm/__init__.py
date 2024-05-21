
# ToDo: process the Send To Oven button at the end of this  file. Batch Publish all the pizzas in the list.
# ToDo: Add Anvil Payment Method
# ToDo: Add the Anvil Login method
# ToDo: Document! User manual/video, plus Developer
# ToDo: This uses  the Uplink code. Auto-launch if not runing,
# ToDo:    


from ._anvil_designer import OrderFormTemplate
from anvil import *
import anvil.users
import anvil.server
from anvil.tables import app_tables
# from EventzAnvilAPI import *
# import ServerModule1



class OrderForm(OrderFormTemplate):
  def __init__(self, **properties): 
  # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #anvil.users.login_with_form()
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
    self.repeating_panel_1.items = app_tables.pizzas.search()
    
   # Additional UI setup
    self.setup_price_tb()   
    
    self.calculate_price()
    self.pizza_list_show()
    




      # Use Label instead of  etxt box, to get rich formatting
  def setup_price_tb(self):
      # Assuming 'price_tb' is your Label component
      self.price_tb.text = "Price: $10"
      self.price_tb.role = 'input-lg'
      self.price_tb.foreground = '#FF5733'  # Set font color
      self.price_tb.font = 'Arial'  # Set font family
      self.price_tb.bold = True  # Make text bold
# Set the font size via the style property
      self.price_tb.style = {'font-size': '24pt', 'font-weight': 'bold', 'color': '#FF5733', 'font-family': 'Arial'}


  def setup_price_tb1(self):
    # Assuming 'price_tb' is your TextBox component and it is correctly initialized
    # Set the font size
    self.price_tb.role = 'input-lg'  # Predefined roles like 'input-lg', 'input-sm'

# Set the font color
    self.price_tb.foreground = '#FF5733'  # Any CSS color value
# Set the font style via custom CSS
    self.price_tb.style = {'font-weight': 'bold', 'font-family': 'Arial'}


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
    self.price = (self.pizza_size_price + self.crust_price + self.toppings * self.top_price)
    print('CP3', self.price)
    
    self.price_tb.text ='${:,.2f}'.format(self.price)
    
    self.pizza_list_show()
    
  
#   def account_entered(self, **event_args):
#     """This method is called when the user presses Enter in this text box"""
#     self.account = self.item['account']  # 
#     #print(self.item['account'])
#     print('892  ACCOUNT', self.account)
#     self.pizza_list_show()
#     pass


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
    """This method is called when the SUBMIT button is clicked"""
    status = 'Ordered'
    new_row = app_tables.pizzas.add_row(size = self.pizza_size, crust = self.pizza_crust, toppings =self.top_list, price=self.price,status=status)
    l = list(self.repeating_panel_1.items) + [new_row]
    self.repeating_panel_1.items = l
    
    self.clear_form_all()
    
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
    self.pizza_list.text =  self.account, self.pizza_size, self.pizza_crust, self.top_list
   
    pass

  def price_tb2_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def account_tb_lost_focus(self, **event_args):
    """This method is called when the ACCOUNT TextBox loses focus"""
    self.account = self.item['account']  # 
    #print(self.item['account'])
    print('2519  ACCOUNT', self.account)
    self.pizza_list_show()
    pass

  def send_to_oven_click(self, **event_args):
    """This method is called when SEND ORDER TO OVEN the button is clicked"""
    # Publish to RabbitMQ   

    print('1481', type(self.size), self.size)
    selected_size = self.size.selected_value
    selected_crust = self.crust.selected_value
    status = 'Ordered'
    print('1512',type(self.top_list), self.top_list, type(self.account), self.account)

#     selected_size = self.size.selected_value
#     selected_size = self.size.selected_value
    eventz_id = ''   # Don't have one now, this is a new pizza. Will be assigned by Publish. New button
    anvil.server.call('publish_pizza', 'New', self.account, eventz_id, selected_size, selected_crust, self.top_list, str(self.price), status)
  
 
    pass

  def clear_form_all(self):
    
    """This method is called when we need to CLEAR THE FORM FOR NEXT ORDER"""
    self.account_tb.text = ''
    self.size.selected_value = None
    self.crust.selected_value = None
    self.pepperoni_cb.checked = False
    self.olives_cb.checked = False
    self.mushrooms_cb.checked = False
    self.price_tb2.text = ''
    self.pizza_list.text = ''    

  def clear_form(self):
    
    """This method is called when we need to CLEAR THE FORM EXCEPT LEAVE THE ACCOUNT NUMBER FOR NEXT PIZZA"""
    # self.account_tb.text = ''
    self.size.selected_value = None
    self.crust.selected_value = None
    self.pepperoni_cb.checked = False
    self.olives_cb.checked = False
    self.mushrooms_cb.checked = False
    self.price_tb2.text = ''
    self.pizza_list.text = ''    
    
  

    























