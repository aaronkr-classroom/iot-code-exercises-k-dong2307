class RoomSensor:
  
    def __init__ (self, name:str, temperature:int, humidity:int, light:int) -> None:
        self.name = name
        self.temperature = temperature
        self.humidity = humidity
        self.light = light
    
    
    def show_info(self):
        print(f"Sensor: {self.name}")
        print(f"Temperature: {self.temperature}")
        print(f"Humidity: {self.humidity}")
        print(f"Light: {self.light}")
    
    
    def comfort_level (self):
        if (20 <= temperature <= 26 & 40 <= humidity <= 60):
            print ("Comfortable")
        elif (30 <= temperature | 70 <= humidity):
            print ("Warning")
        else:
            print ("Normal")
            
    def light_status (self):
        if (light < 200):
            light = print("Dark")
        elif (light > 200):
            light = print("Bright")
   
name = str(input("이름입력: "))
temperature = int(input("온도입력: "))
humidity = int(input("습도입력 "))
light = int(input("밝기입력: "))