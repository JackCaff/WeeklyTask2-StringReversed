# Program allows a user enter a sentance and output every second later of the sentence in reverse

sentence = str (input("Please enter your sentence: "))
sentence = sentence[::-1] # reverses users sentence (String)

print (sentence[::2]) # outputs the every second letter of the users input 
