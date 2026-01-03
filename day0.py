class Robot:
  def __init__(self, name: str, model: int, generation: int):
    self.name = name
    self.model = model
    self.generation = generation
  def status(self):
    print(f"the robot {self.name} is now active")
  def intro(self):
    print(f"the name of the robot is {self.name} , model: {self.model} it belongs to a generation {self.generation}")
bot1 = Robot("pavan", 2345, 6)
class WarRobot(Robot):
  def __init__(self, name, model, generation, weapon: str):
    super().__init__(name, model, generation)
    self.weapon = weapon
  def weapon_name(self):
    print(f"the weapon with the {self.name} is {self.weapon}")
  def intro(self):
    print("I will attack you!! run, run!!")
bot2 = WarRobot("harshith", 123, 222, "nuclear bomb")  
bot2.weapon_name()
bot2.intro()
