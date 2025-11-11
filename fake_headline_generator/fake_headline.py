#import the random module
import random

#2 - create lists of  Subjects, Actions and Objects(Places) 
subjects = [
    "Shahrukh khan",
    "Virat Kohli",
    "Nirmala Sitaraman",
    "A Mumbai Cat",
    "A Group of Monkeys",
    "Prime Minister Modi",
    "Auto Ricksaw Driver From Delhi",
]

actions = [
    "launches",
    "cancels all events",
    "dances with her Partner",
    "eats",
    "declares war on Pakistan",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai Local Train",
    "at the press of Sillicon valley",
    "inside Indian Parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India Gate"
]

#Steps the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    
    headline = f" BREAKING NEWS : {subject} {action} {place_or_thing} "
    print("\n"+headline)
    
    user_input = input("\nDo you want another headline? (yes/no)").strip().lower()
    if user_input == "no":
        break
    
#print a goodbye message
print("\nThanks for using the Fake News Headline Generator. Have a fun day")
