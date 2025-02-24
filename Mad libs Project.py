# """Author: Sister Jhenifer
# Purpose: Mad Libs Project
# """
# #The program should begin by asking the user for each of the words. 
# # It should then, fill those words into the appropriate places in the story.
print("Let's play a game called Mad Libs. First I need to gather some information from you.")
print()
adjective = input("Give me an adjective: ")
animal = input("Now I need you to tell me an animal: ")
verb = input("Now a verb: ")
exclamation = input("A surprise reaction: ")
print()
print()
print("Your story is: ")

print(f'The other day, I was really in trouble. It all started when I saw a very\n{adjective.lower()} {animal.lower()} {verb.lower()} down the hallway. "{exclamation.capitalize()}!" I yelled. But all \nI could think to do was to {verb.lower()} over and over. Miraculously,\nthat caused it to stop, but not before it tried to\n{verb} right in front of my family. ')
#NOT FINISHED
#ADD STUFF FOR EXTRA POINTS