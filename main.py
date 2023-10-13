##https://www.create-learn.us/blog/how-to-make-ai-in-python-tutorial/
import random

greetings = ["yo", "sup", "hi", "Hello" , "Hey", "What's up", "What's good", "Howdy"]
goodbyes = ["bye", "cya", "goodbye", "see you", "see you later", "adios"]
keywords = ["pet", "book", "game"]
responses = ["Do you have pets?", "What are you reading?", "What games do you like?"]

print(random.choice(greetings))
user = input("Say something(or type bye to quit): ")
user = user.lower()

while (user!= "bye"):
  keyword_found = False  
  
  for index in range(len(keywords)):
    if (keywords[index] in user):
      print("Bot: "+responses[index])
      keyword_found = True

  if (keyword_found is False):
    new_keyword = input("Bot: I'm not sure how to respond. What should I respond to? ")
    keywords.append(new_keyword)
    new_response = input("Bot: How should I respond to "+new_keyword+"?")
    responses.append(new_response)
    
  user = input("Say something(or type bye to quit): ")
  user = user.lower()

print("Bot: " + random.choice(goodbyes))