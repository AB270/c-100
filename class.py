class Car(object):

    def __init__(self,model,colour,company,speed_limit):
        self.color = colour
        self.model = model
        self.company = company
        self.speed_limit = speed_limit

    def start(self):
        print("Started")

    def stop(self):
        print("Stoped")

    def accelerate(self):
        print("Accelerating...")
        "accelerated functionality here"
    
    def change_gear(self,gear_type):
        print("Gear changed")
        "gear related functionality here"


audi = Car("A6","red","audi","80")

print(audi.color)