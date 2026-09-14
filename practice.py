print("Welcome to the Python Adventure Park!")
print("Today we are going to get your Python ticket ready.")
print("Then we are going to find out what rides you can go on!")



guest_name = input("What is your name?")
guest_age = int(input("How old are you?"))
guest_height = int(input("What is your height in inches?"))
ticket_type = input("What ticket did you purchase, the regular or the premium?")
your_membership = input("Are you a park member? yes/no")
visiting_with_adult = input("Are you visiting with an adult? yes/no")
visit_time = input("will you be visiting in the morning or the evening?")

def calculate_admission(guest_age):
    if guest_age <= 4:
        return 0
    elif guest_age <= 12:
        return 12
    elif guest_age <= 64:
        return 30
    else:
        return 20

def calculate_discount(price, memeber, visit_time):
    if memeber == "yes" and visit_time == "evening":
        discount = 10
    elif memeber == "yes":
        discount = 5
    elif visit_time == "evening":
        discount = 3
    else:
        discount = 0
    total_price = price - discount

    if total_price < 0:
        total_price = 0
    return total_price

def ride_level(guest_age, guest_height):
    if guest_height >= 54 and guest_age >= 16:
        return "Extreme rides"
    elif guest_height >= 48 and guest_age >= 12:
        return "Thrill ride"
    elif guest_height >= 42 and guest_age >= 8:
        return "Family Rides"
    elif guest_height >= 36:
        return "Kiddie Rides"
    else:
        return "No rides" \

def check_supervision(guest_age, has_adult):
    if guest_age < 13 and has_adult != "yes":
        return "An adult is required"
    else:
        return "you can go"
def check_supervision(guest_age, has_adult):
    if guest_age < 13 and has_adult != "yes":
        return "Adult Required"
    else:
        return "Approved"

# price and ride lvls
first_price = calculate_admission(guest_age)
final_price = calculate_discount(first_price, your_membership, visit_time)
qualifying_ride = ride_level(guest_age, guest_height)
supervision_status = check_supervision(guest_age, visiting_with_adult)


if ticket_type == "premium":
   perk_message = "Premium ticket: Free food and skip the lines"
else:
   perk_message = "Standard ticket: No free food and skip the line"


# print report
print("PYTHON ADVENTURE PARK GUEST REPORT")
print()
print("Guest Name: " + guest_name)
print()
print("Age: " + str(guest_age))
print("Height: " + str(guest_height) + " inches")
print("Ticket Type: " + ticket_type)
print("Park Member: " + your_membership)
print()
print("Base Admission: $" + str(first_price))
print("Final Admission: $" + str(final_price))
print()
print("Highest Ride Level: " + qualifying_ride)
print()
print("Supervision Status: " + supervision_status)
print()
print("Perks: " + perk_message)
print()
print("Have an awesome day at Python Adventure Park")
print()
print()


# fun little personalized message
if qualifying_ride == "Extreme Rides":
   print(guest_name + ", you can rides at the park, have fun")
elif qualifying_ride == "No Rides":
   print("Sorry " + guest_name + ", but you cannot ride any rides")
else:
   print("Have fun " + guest_name + "!")
