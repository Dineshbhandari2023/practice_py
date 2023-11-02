age = input ("What is your age?")
age_int = int (age)


# if we live upto 90 years old

years_left = 90 - age_int
days_left = years_left * 365
months_left = years_left * 12
weeks_left = years_left * 52

message = f"you have left {days_left} days, {weeks_left} weeks and {months_left} months in your life."

print(message)

