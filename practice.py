class car:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def start(self):
        print(f'{self.a} is the brand and its color is {self.b}')
    
    def stop(self):
        print(f'{self.a} stoped')

a=car('bmw','red')
b=car('skoda','black')
# c=car('telsa','stop')

a.start()
b.start()
a.stop()