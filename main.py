class Device:
    def __init__(self, price, model, color):
        self.price = price
        self.model = model
        self.color = color

class CoffeMachine(Device):
    pass

class Blender(Device):
    pass

class MeatGrinder(Device):
    pass

x = CoffeMachine(50, "IDK55", "black")
print(x.price)