#x = 20
#y = 5
# x += y  
#x = x + y 
#print(x)

#x = 54 + 6 
#y = 59
#print(x+y) 

#a = 7
#b = 500
#if b >= 335: 
    #print(a) 
    
#x = 10
#y = 10
#print(f"{x} == {y}: {x == y}")  # True

#y = 20
#print(f"{x} == {y}: {x == y}")  # False


x = 10
y = 30
print(f"{x} < = {y}: {x > y}")  # True

y = 10
print(f"{x} == {y}: {x == y}")  # False

# 2. Not Equal (!=) - checks if two values are not equal
a = 10
b = 20
print(f"{a} != {b}: {a != b}")  # True

a = 15
b = 15
print(f"{a} != {b}: {a != b}")  # False

# 3. Greater Than (>) - checks if left value is greater than right
num1 = 50
num2 = 30
print(f"{num1} > {num2}: {num1 > 
      num2}")  # True

# 4. Less Than (<) - checks if left value is less than right
num1 = 20
num2 = 40
print(f"{num1} < {num2}: {num1 < num2}")  # True

# 5. Greater Than or Equal (>=) - checks if left value is greater than or equal to right
score = 85
passing_score = 70
print(f"{score} >= {passing_score}: {score >= passing_score}")  # True

# 6. Less Than or Equal (<=) - checks if left value is less than or equal to right
age = 25
max_age = 30
print(f"{age} <= {max_age}: {age <= max_age}")  # True

# Practical Examples

# Example 1: Checking eligibility for voting
age = 18
voting_age = 18
if age >= voting_age:
    print(f"Age {age}: Eligible to vote")
else:
    print(f"Age {age}: Not eligible to vote")

# Example 2: Grade system
marks = 75
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Marks {marks}: Grade {grade}")

# Example 3: Temperature check
temperature = 25
if temperature > 30:
    print("It's hot outside!")
elif temperature < 15:
    print("It's cold outside!")
else:
    print("The weather is pleasant!")

# Example 4: Comparing strings (lexicographical comparison)
word1 = "apple"
word2 = "banana"
print(f"'{word1}' < '{word2}': {word1 < word2}")  # True (a comes before b)

# Example 5: Multiple comparisons
number = 15
if 10 <= number <= 20:
    print(f"{number} is between 10 and 20 (inclusive)")

# Example 6: Comparing lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 4]
print(f"list1 == list2: {list1 == list2}")  # True
print(f"list1 == list3: {list1 == list3}")  # False

# Important Note: Difference between = and ==
# = is assignment operator (gives a value to a variable)
# == is comparison operator (checks if two values are equal)

# Correct usage:
value = 10  # Assignment
if value == 10:  # Comparison
    print("Value is 10")

# Common mistake:
# if value = 10:  # This will cause an error!
#     print("This won't work")

 #arithmetic operatore 
wilmot = 10
wilmot = wilmot +40
print(f"{wilmot} ") 

wilmot += 50
print(f"{wilmot} ")

# subtraction
cash_received = 10000
cash_spend =  8000
balance = cash_received - cash_spend
print(f"Balance: {balance}")

wilmot = 90
wilmot = wilmot -10
print(f"{wilmot}")

wilmot -= 50
print(f"{wilmot} ") 

#multipication

wilmot = 90
wilmot = wilmot *3
print(f"{wilmot}")

wilmot *= 3
print(f"{wilmot} ") 


# Division
wilmot = 90
wilmot = wilmot /2
print(f"{wilmot}")

wilmot /= 2
print(f"{wilmot} ") 

#exponent
wilmot = 5
wilmot = wilmot **5
print(wilmot) 

wilmot **= 5
print(wilmot) 

#Modulus
remainder = 5
remainder = wilmot %2
print(remainder) 

wilmot %= 2
print(remainder) 



