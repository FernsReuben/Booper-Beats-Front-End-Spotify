from ._anvil_designer import MusicPlayerTemplate
from anvil import *

class MusicPlayer(MusicPlayerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main_Menu.ORDER_NOW.Create_A_Pizza')
    pass
