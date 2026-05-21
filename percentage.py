# 1) Ask the user to enter marks for 4 subjects: math, english, science, and hindi.
#    Store each mark in its own variable.

# 2) Add all 4 subject marks and store the total in `sum`.

# 3) Print the total marks stored in `sum`.

# 4) Calculate the percentage:
#    - Divide `sum` by 400 (total maximum marks for 4 subjects, assuming each is out of 100)
#    - Multiply the result by 100
#    Store the final value in `perc`.

# 5) Print the percentage stored in `perc`.
math = int(input("Enter marks for math: "))
english = int(input("Enter marks for english:"))
science = int(input("Enter marks for science:"))
hindi = int(input("Enter marks for hindi:"))
sum = math + english + science + hindi
print("Total marks:", sum)
perc = (sum/400) * 100
print("Percentage:", perc, "%")


