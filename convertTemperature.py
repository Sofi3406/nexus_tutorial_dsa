class Solution(object):
    def convertTemperature(self, celsius):
        # Convert Celsius to Kelvin
        kelvin = celsius + 273.15
        
        # Convert Celsius to Fahrenheit
        fahrenheit = celsius * 1.80 + 32.00
        
        
        return [kelvin, fahrenheit]
