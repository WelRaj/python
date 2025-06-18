from random import randint
class train:
    def __init__(self,traino):
        self.traino=traino
    def book(self,fro,to):
        print(f"ticket is booked from {self.traino} from {fro} to {to}")
    def status(self):
        print(f"train no: {self.traino} is ruuning on time")
    def getFare(self,fro,to):
        print(f"the train no :{self.traino} the fare {fro} to {to} is {randint(223,5000)}")
a=train(12134)
a.book("gwalior","kalyan")
a.status()
a.getFare("gwalior","kalyan")
