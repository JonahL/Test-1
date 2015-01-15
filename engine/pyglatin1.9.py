# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 23:08:18 2015

@author: Jonah
"""
import datetime as time
now = str(time.datetime.now())
last_run
print("PygLatin 1.9 by JonahJ // Last run on {0}".format(now))
while True:
    text = input("Enter text here:").lower()
    original = text.split()
    # splits sentence into a list of words, uncomment next line to see
    # print(original)
    new_sent = []
    # initialize new list before the for loop
    for i in original:
        first = i[0]
        # isolates the first letter
        pyg = "ay"
        # adds ay
        new_word = i + first + pyg
        # adds them all together
        new_word = new_word[1:len(new_word)]
        # gets rid of the first letter
        new_sent.append(new_word)
    # adds them into the new list of words "new_sent"
    new_sent[0] = new_sent[0].capitalize()
    # capitalizes the first word
    final_sent = " ".join(new_sent)
    # joins list of words separated by space
    if text == "exit":
        print("Okay")
        quit()
    elif len(original) > 0 and original[0].isalpha():
        # checks to see if the word is there and *only contains letters* (cant figure this one out, hence the 1.9)
        print(final_sent)
    elif text == "who is the best?":
        print ("Clayton is the best")
    # eureka
    else:
        print("Not acceptable")
