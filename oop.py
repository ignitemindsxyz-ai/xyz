# STATIC METHODS

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9
    
    @staticmethod
    def celcius_to_kelvin(c):
        return c +273.15
    
    @staticmethod
    def is_valid_celsius(c):
        return c >= -273.15
    
print(TemperatureConverter.celsius_to_fahrenheit(100))
print(TemperatureConverter.fahrenheit_to_celsius(212))
print(TemperatureConverter.is_valid_celsius(-300))

tc = TemperatureConverter()
print(tc.celsius_to_fahrenheit(36))