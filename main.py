# Temperature Converter
# Converts between Celsius and Fahrenheit

# Title
print('------------------------------------------------------------------------------')
print(' Temperature Converter')
print('------------------------------------------------------------------------------')
print(' What would you like to do?:')
print('------------------------------------------------------------------------------')
print(' [1] (°C) Celsius     ->  (°F) Fahrenheit')
print(' [2] (°F) Fahrenheit  ->  (°C) Celsius')
print('------------------------------------------------------------------------------')
print('')

# Choose what will happen
while True:
    method_option = input('What would you like to do?: ')

    # (°C) Celsius -> (°F) Fahrenheit
    if method_option == '1':
        while True:
            try:
                print('')
                method = '(°C) Celsius -> (°F) Fahrenheit'
                old_unit = '°C'
                new_unit = '°F'
                current_temperature = float(input('How many degrees Celsius (°C) is it?: '))

                new_temperature = (current_temperature * (9 / 5)) + 32

                break
            
            except ValueError:
                print('That is not a valid number! Try again.')

    # (°F) Fahrenheit -> (°C) Celsius
    elif method_option == '2':
        while True:
            try:
                print('')
                method = '(°F) Fahrenheit -> (°C) Celsius'
                old_unit = '°F'
                new_unit = '°C'
                current_temperature = float(input('How many degrees Fahrenheit (°F) is it?: '))

                new_temperature = (current_temperature - 32) * (5 / 9)

                break
            
            except ValueError:
                print('That is not a valid number! Try again.')

    # If user does not input a valid option
    else:
        print('Please enter either 1 or 2')
        continue

    break

# Output
print('')
print('------------------------------------------------------------------------------')
print(f' {method}')
print(f' {current_temperature} {old_unit} -> {round(new_temperature, 1)} {new_unit}')
print('------------------------------------------------------------------------------')
print('')
input('Press the Enter Key to Exit...')