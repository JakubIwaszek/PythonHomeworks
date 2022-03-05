class TV():
    is_on = False
    volume = 0
    
    def __init__(self):
        self.is_on = False
    
    def turn_on(self):
        self.is_on = True
        
    def turn_off(self):
        self.is_on = False
        
    def increase_volume(self):
        if self.volume < 10:
            self.volume += 1
    
    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1
    
    def show_status(self):
        print(f"Volume: {self.volume}")
        if self.is_on:
            print("TV is on")
        else:
            print("TV is off")
        
tv1 = TV()
tv1.show_status()
tv1.increase_volume()
tv1.turn_on()
tv1.show_status()
tv1.turn_off()
tv1.decrease_volume()
tv1.show_status()
