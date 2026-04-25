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
        if (20 <= temperature <= 26 and 40 <= humidity <= 60):
            return "Comfortable"
        elif (30 <= temperature or 70 <= humidity):
            return "Warning"
        else:
            return "Normal"
            
    def light_status (self):
        if self.light < 200:
            return "Dark"
        elif (light > 200):
            return "Bright"