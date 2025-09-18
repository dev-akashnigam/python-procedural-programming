def temperatureConvertor(temp, unit):
    ALPHABET_C = 'C'
    ALPHABET_F = 'F'
    ALPHABET_K = 'K'
    if unit.upper() == ALPHABET_C:
        fahrenheitTemp = ((9*temp)/5)+32
        kelvinTemp = temp + 273.15
        print(f"{temp} in celcius = {fahrenheitTemp} in fahrenheit")
        print(f"{temp} in celcius = {kelvinTemp} in kelvin")
    elif unit.upper() == ALPHABET_F:
        celciusTemp = ((temp - 32)*5)/9
        kelvinTemp = celciusTemp + 273.15
        print(f"{temp} in fahrenheit = {celciusTemp} in celcius")
        print(f"{temp} in fahrenheit = {kelvinTemp} in kelvin")
    elif unit.upper() == ALPHABET_K:
        celciusTemp = temp - 273.15
        fahrenheitTemp = (((temp - 273.15)*9)/5)+32
        print(f"{temp} in kelvin = {celciusTemp} in celcius")
        print(f"{temp} in kelvin = {fahrenheitTemp} in fahrenheit")
    else:
        print("Please enter correct unit of temperature (C/F/K)")


def main():
    print("Please enter the temperature to be converted: ")
    temperature = float(input())

    print("Please enter the unit of temperature (C for Celcius, F for Fahrenheit and K for Kelvin): ")
    unit_of_temp = input()

    temperatureConvertor(temperature, unit_of_temp)

main()
    