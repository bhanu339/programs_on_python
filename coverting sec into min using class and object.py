class Time:
    def read(self,seconds):
        self.seconds=seconds
    def to_convert(self):
        self.minutes=self.seconds//60
        self.hours=self.seconds//3600
        self.day=self.seconds//86400
    def display(self):
        print("hours:",self.hours)  
        print("minutes:",self.minutes)  
        print("days:",self.day)    
t=Time()
t.read(86400)
t.to_convert()
t.display()
        