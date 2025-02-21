def greeting(name, age=28, color='red'):
    #Greets user with 'name' from 'input box' and 'age', if available, default age is used
    name = name.capitalize()
    color = color.lower()
    age = int(age)
    print('Hello '  +  name + ', you are ' + str(age) +'!')
    print(f'Hello {name}, you will be {age + 1} years old next birthday!')
    print(f'We heard you like the color {color}!')
    

name = input('Enter your name: ')
age = input('Enter your age: ')
color = input('Enter your favorite color: ')
greeting(name, age, color)