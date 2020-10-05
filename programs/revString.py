def rev_sentence(sentence): 
  
    # first split the string into words 
    words = sentence.split(' ')  
  
    # then reverse the split string list and join using space 
    reverse_sentence = ' '.join(reversed(words))  
  
    # finally return the joined string 
    return reverse_sentence   
  
if __name__ == "__main__": 
    string = input("enter the word ")
    print(rev_sentence(string))

