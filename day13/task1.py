"""
WAP to prompt the user for hours and rate per hour using input to compute gross pay.
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours
worked above 40 hours
"""

hours = float(input("Enter total hours"))
rate = float(input("Enter rate per hour "))
if hours <= 40:
    pay = hours * rate
else:
    overtime = hours - 40  # overtime = 5
    normal_pay = 40 * rate  # 40 * 10.5
    ot_pay = overtime * rate * 1.5   # 5 * 10.5 * 1.5
    pay = normal_pay + ot_pay
print(f"Total pay is {pay}")

