# name = "John Smith";
# age = 20;
# patient_type = "old";
# print( + " is " + str(age) + " years old. He is an " + patient_type + " patient.")

# weight = float(input("Weight: "));
# units =  input("(K)gs or (L)bs:").upper();
# if units == "L":
#     print("Your weight in Kgs is: " + str(.453592 * weight))

# else:
#     print("Your weight in Lbs is: " + str(2.20462 * weight))
    
# def factorial(n):
#   if n < 2:
#     return 1
#   return n * factorial(n-1)

# print(factorial(1000))

def student_grade(name, grade):
	return "{name} received {grade}% on the exam".format(name = name, grade = grade)

print(student_grade("Reed", 80))
