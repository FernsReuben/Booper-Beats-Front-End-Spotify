from ._anvil_designer import Create_A_PizzaTemplate
from anvil import *

class Create_A_Pizza(Create_A_PizzaTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
