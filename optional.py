#implementation of "word stemming"
word = input("Enter the word:") 
x = 'ing'
y = 'ed' 
z = 's' 
first = word[:1] 
last = word[-1:] 
uppercase = first.upper 
if word == uppercase: 
 print("")

elif (x in word) == True: 
 word = (word.replace('ing',''))
 print(word)

elif (y in word) == True: 
 word = (word.replace('ed',''))
 print(word)

elif (z in word) == True: 
 word = (word.replace('s',''))
 print(word)
 #%%
 # implementation of "stop words"
 query = 'What is hello'
 stopwords = ['what', 'who', 'is', 'a', 'at', 'is', 'he'] 
 querywords = query.split() 
 resultwords = [word for word in querywords if word.lower() not in stopwords] 
 result = ' '.join(resultwords) 
 print(result)

 
