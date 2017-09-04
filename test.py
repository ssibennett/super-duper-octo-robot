class HelloWorld():
  """Hello World program in Python using classes."""
  
  def __init__(self, person="Bob Marley"):
    self.person = person
    
  def print(self):
    ret = "Hello World! I'm %s." % (self.person,)
    return ret

if __name__ == "__main__":
  hw = HelloWorld()
  hw.print()
