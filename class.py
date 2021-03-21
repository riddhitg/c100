class Car(object):

    def __init__(self, model, colour, company, speed_limit):
        self.colour = colour
        self.model = model
        self.company = company
        self.speed_limit = speed_limit

    def start(self):
        print("started")
    
    def stop(self):
        print("stoped")

    def accelarate(self):
        print("accelarated")

    def change_gear(self):
        print("change gear")

audi = Car("Audi RS7 Sportscar", "red", "Audi", 280)
print(audi.start())