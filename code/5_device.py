class Device:
    """
    Base IOT device
    기반 사물인터넷 장치
    """
    
    def __init__ (self, name:str) -> None:
        self.name = name
    
    def connect(self) -> None:
        print(f"{self.name} connecting...")
        
    def status(self) -> str:
        return "Unknown"

class SensorDevice (Device):
    """
    A device that reads data.
    데이터를 읽을 수 있는 장치.
    """
    
    def read(self) -> float:
        """
        센서 값을 반환
        """
        return 0.0
    
    def status(self) -> str:
        return "Reading data..."
    
class ActuatorDevice (Device):
    """
    A device that
    작동할 수 있는 장치
    """
    
    def status(self) -> str:
        return "Performing action..."
    
class TemperatureSensor (SensorDevice):
    """
    Simulated temperature sensor
    온도 센서 시뮬레이션
    """
    
    def __init__(self, name:str) -> None:
        super().__init__(none)
        
    def read(self) -> float:
        """
        가짜 온도 값을 반환
        """
        return round(random.uniform(20.0,30.0))