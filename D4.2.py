total_users = 0
staff_users = 0
non_teaching_staff_users = 0

# Get input from user
num_students = int(input("Enter the number of student users in the college: "))

# Calculate total users, staff users and non-teaching staff users
total_users = num_students + staff_users
staff_users = num_students * 3
non_teaching_staff_users = staff_users / 4

# Print the results
print("Total users:", total_users)
print("Staff users:", staff_users)
print("Non-teaching staff users:", non_teaching_staff_users)