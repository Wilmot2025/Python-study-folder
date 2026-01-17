#Some methods in string :
# 1. len() => it is used to find the length of string
# 2. lower() => it is used to convert the string to lowercase
# 3. upper() => it is used to convert the string to uppercase
# 4. title() => it is used to convert the first character of each word to uppercase
# 5. strip() => it is used to remove the leading and trailing whitespace from the string
# 6. replace() => it is used to replace a substring with another substring
# 7. split() => it is used to split the string into a list of substrings based
# 8. join() => it is used to join a list of strings into a single string with a specified separator
# 9. find() => it is used to find the index of the first occurrence of a substring
# 10. count() => it is used to count the number of occurrences of a substring in the string
# 14. startswith() => it is used to check if the string starts with a specified substring
# 15. endswith() => it is used to check if the string ends with a specified substring
# # 16. index() => it is used to find the index of the first occurrence of a substring (raises an error if not found)
# 17. capitalize() => it is used to convert the first character of the string to uppercase and the rest to lowercase

name = "wilmot Togar Okai"
print(len(name)) 

name = "wilmot Togar Okai"
print(name.upper())    # WILMOT TOGAR OKAI
print(name.lower())    # wilmot togar okai
print(name.title())    #  Wilmot Togar Okai


name = "Ritchie Okai"
name_parts = name.split()
print(name_parts)      # ['wilmot', 'Togar', 'Okai']
first_name = name_parts[0]
last_name = name_parts[-1]  

name = "Ritchie Okai"
print(name.count('i')) 

name = "Ritchie Okai"
print(name.count('i')) 

school_name = name.replace('Ritchie Okai', 'Shobhit')
print(school_name)

name = "John Brown"
print(name.find('B'))


name = "John Brown"
result = "-".join(name)
print(result)

name = "John Brown"
combined = "".join(name.split())
print(combined)





 