text = input("Enter your text: \n")

if ("subscribe" in text):                                   
    spam = True
elif("click" in text):
    spam = True
elif("make a lot of money" in text):
    spam = True
elif("buy" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")