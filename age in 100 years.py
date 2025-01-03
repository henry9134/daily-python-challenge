print('Hello, Python Challenge!')
from datetime import date

current_year = date.today().year

name = input("What is your name? ")

age = int(input(f"How old are you, {name}? "))

year_turn_100 = current_year + (100 - age)

print(f"Hello, {name}! You will turn 100 years old in the year {year_turn_100}.")
