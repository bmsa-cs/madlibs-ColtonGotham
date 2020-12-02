"""
MadLibs
Author: Colton Gotham
Period/Core: 5


"""

name = input("Enter a Name: ")

country = input("Enter a Country: ")

food_1 = input ("Enter a Food: ")

food_2 = input ("Enter another Food: ")

cost = int(input("Enter a Dollar Amout: $"))

city = (input("Enter a City: "))

emotion = (input("Enter a Emotion: ")) 

famous_animal = (input("Enter a Animal: "))

def location():
  print(city + (", ") + country+("."))

transportation = (input("Enter a Way of Transportation: "))


print(" ")
 
print(f"{name} is wanting to move to {country}!\n{name} is very excited to try {country}'s {food_1} but they are curious about the world famous {food_2} too.")

print(f"However, {name} doesn't know if they can afford it because it is ${cost}.\nAlso {name} wants to experience the culture of {country}.\n{name} is {emotion} when they were learning the language of {country}.")

print(f"{name} has booked a hotel in")

location()

print(f"Which is the home of the famous {famous_animal} The Second. The {famous_animal} The Second exibit is a block away from the hotel.\n When {name} was finished packing {name} got into a {transportation} and went to {country}. THE END")