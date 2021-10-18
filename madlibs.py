# string concatenation (aka how to put strings together)
# suppose we want to create string that says "subscribe to _________"

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer Programming is so {adj}! It makes me so excited all time because \
I love to {verb1}. Stay hydrated and and {verb2} like you are {famous_person}"

print(madlib)
