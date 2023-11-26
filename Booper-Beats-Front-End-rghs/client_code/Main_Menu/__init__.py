from ._anvil_designer import Main_MenuTemplate
from anvil import *

class Main_Menu(Main_MenuTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main_Menu.ORDER_NOW')
    pass
