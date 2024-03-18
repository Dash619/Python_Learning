date = input("Enter today's date (YYYY-MM-DD) : ")
mood = input("How do you rate your mood today from 1 to 10 : ")
thoughts = input("Let your thoughts flow : \n")

with open(rf"Journal\{date}.txt", 'w') as file:
    file.write(mood + 2 * '\n')
    file.write(thoughts)

