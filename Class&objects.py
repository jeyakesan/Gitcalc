class Person:
    def __init__(self, name):
        self.name= name
    def talk(self, last):
        self.last=last
        print(f"Hi this is {self.name , self.last}")


jeyakesan=Person("deva")
jeyakesan.talk("Paramasamy")

deva=Person("Goldman")
deva.talk("JK")

