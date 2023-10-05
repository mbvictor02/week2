temperature_celsius = float(input("Temperature in Celsius: "))      #Asks temperature in Celsius and stores it as a float value
temperature_farenheit = float(temperature_celsius*9/5)+32           #Calculates the equivalent temperature in Farenheit and Kelvin 
temperature_kelvin = float(temperature_celsius+273.15)              #and stores it as a float value in a new variable.
print("Temperature in Farenheit: ", temperature_farenheit, "\n",
      "Temperature in Kelvin: ", temperature_kelvin)                #Prints Farenheit and Kelvin equivalent temperatures previously calculated.