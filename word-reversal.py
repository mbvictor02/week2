phrase = (input("Enter the phrase: "))  #Asks user a phrase and stores it as text in a string variable

phrase2 = phrase.split()                
#string.split(separator, maxsplit)
#separator	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
#maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
phrase2.reverse()          
#list_name.reverse()
#Returns: The reverse() method does not return any value but reverses the given object from the list.             
phrase2 = "".join(phrase2)
#string_name.join(iterable) 
#Iterable – objects capable of returning their members one at a time. Some examples are List, Tuple, String, Dictionary, and Set
#Return Value: The join() method returns a string concatenated with the elements of iterable.              

print(phrase2)  #Prints the reversed initial phrase