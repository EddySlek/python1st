# LEARNING PYTHON

# VARIABLES:
integer_age = 30
float_price = 20.55
String_name = "ArtWeek"
Boolean_isPriceless = True
Boolean_isCheaper = False

print(integer_age)
integer_age = 40
print(integer_age)

print(type(integer_age))
print(type(float_price))
print(type(String_name))
print(type(Boolean_isCheaper))

print("It is your age: " + str(integer_age))
print(integer_age + float_price)

# INPUT - Get data from user
nbr1 = input("What is your best number? ")
print(nbr1)


# TYPE CONVERSION
birthYear = input("Enter your birth year: ")
age = 2024 - int(birthYear)
print(age)