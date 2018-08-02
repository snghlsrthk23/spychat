#####name="Deepanshu Lamba"
#####spy_salutation="Mr."
#####full_name=spy_salutation + " " + name
#####spy_age=21
#####spy_rating=4
#####status = "You are in..."

#####spy = {"Name": "Deepanshu Lamba", "Salutation": "Mr.", "age": 21, "Rating": 4.5, "Status": "You are in...."}

#####class for storing details
from datetime import datetime
class Spy:
    def __init__(self, Name, Salutation, age, Rating):
        self.Name = Name
        self.Salutation = Salutation
        self.age = age
        self.Rating = Rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

#####for an existing user
spy = Spy("Deepanshu Lamba", "Mr.", 21, 4.5)

#####existing friends
#friend_one = Spy("Kriti", "Ms.", 21, 4.1)
#friend_two = Spy("Jake", "Mr.", 21, 4.2)
#friend_three = Spy("Ryan", "Mr.", 20, 4)

#Friends = [friend_one, friend_two, friend_three]

#####chat class
class ChatMessage:
    def __init__(self, spy_name, friend_name, message, time, sent_by_me):
        self.spy_name = spy_name
        self.friend_name = friend_name
        self.message = message
        self.time = time
        self.sent_by_me = sent_by_me