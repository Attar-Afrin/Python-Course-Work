# Course Details as Input (E-Learning Platform)

course_id = input("Enter Course ID: ")
course_name = input("Enter Course Name: ")
course_price = float(input("Enter Course Price: "))
course_categories = input("Enter Categories (Using comma to seperate): ")
available_slots = int(input("Enter Available Slots: "))
discount_percent = float(input("Enter Discount Percentage: "))
course_features = input("Enter Course Features: ")
instructor_name = input("Enter Instructor Name: ")
instructor_contact = int(input("Enter Instructor Contact: "))
instructor_location = input("Enter Instructor Location: ")

# Display Course Details Using Different Formatting Methods

print("\n--- E-Learning Course Information ---\n")

# Comma-separated categories
print("Categories:", course_categories)

# Percentage format using f-string
print(f"Discount: {discount_percent:.2f}%")

# Price using .format() method
print("Course Price: ₹{:.2f}".format(course_price))

# General details using f-strings
print(f"Course ID: {course_id}")
print(f"Course Name: {course_name}")
print(f"Available Slots: {available_slots}")
print(f"Course Features: {course_features}")
print(f"Instructor Info: {instructor_name}, Contact: {instructor_contact}, Location: {instructor_location}")
'''
--- E-Learning Course Information ---

Categories: programming,softskills
Discount: 5.00%
Course Price: ₹40000.00
Course ID: PFS-31
Course Name: Python
Available Slots: 10
Course Features: video recording, exams,weekly tests
Instructor Info: Sowmya Mam, Contact: 280750505071, Location: hyderabad
'''