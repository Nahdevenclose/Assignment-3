#Student Information
print("Full name: Jordan Smith")
print("Student email: jsmith@ncat.edu")
print("Hometown: Charlotte, NC")
print("Graduation semester: Spring 2028")
print("Major: Computer Science")

#Academic Data in Lists
current_course_list = ["COMP 163", "MATH 150", "ENG 101", "HIS 105"]
completed_course_list = ["Biology", "Chemistry", "Calculus", "Spanish II", "World History"]
credit_hour_list = [3, 3, 3, 3]
gpa_history = [3.2, 3.6, 3.4, 3.7]

print("Current courses list: ", current_course_list)
print("Completed courses list: ", completed_course_list)
print("Credit hour list: ", credit_hour_list)
print("GPA history list: ", gpa_history)

#Contact Info in tuples
e_contact = ("Mom", "Hannah Smith", "704-555-0199")
home_address = ("456 Oak Street", "Charlotte", "NC", "28202")
insta_info = ("Instagram", "@jordan_codes", 312)
twitter_info = ("Twitter", "@jordandev", 127)
birthday = ("Birthday", "5, 22, 2006")

print("Emergency contact tuple: ", e_contact)
print("Home address tuple: ", home_address)
print("Instagram info tuple: ", insta_info)
print("Twitter info tuple: ", twitter_info)
print("Birthday info tuple: ", birthday)

#Interests Tracking in Sets
current_skills = {"Python basics", "HTML", "Problem Solving", "Time Management", "Photography"}
skills_to_learn = {"JavaScript", "Data Structures", "Git", "Web design","Public Speaking"}
career_interests = {"Software Development", "Web development", "Data Science", "Game development"}
hobbies = {"Gaming", "Photography", "Reading", "Soccer", "Music"}
entertainment = {"One Piece", "Barry", "Life", "Incantation", "Memento"}

print("Current skills set: ", current_skills)
print("Skills to learn set: ", skills_to_learn)
print("Career interests set: ", career_interests)
print("Hobbies set: ", hobbies)
print("Entertainment backlog set: ", entertainment)

#Organizational mapping in dictionaries
course_credits = {"COMP 163": 3, "MATH 150": 3, "ENG 101": 3, "HIS 105": 3}
course_professors = {"COMP 163": "Prof. Rhodes", "MATH 150": "Dr. Lee", "ENG 101": "Dr. Martinez", "HIS 105": "Dr. Brown"}
course_room = {"COMP 163": "M-Eric 300", "MATH 150": "Marteena 201", "ENG 101": "Crosby 121", "HIS 105": "Crosby 210"}
monthly_budget = {"Food": 450, "Entertainment": 200, "Books": 125, "Transportation": 100}
study_hours = {"Programming": 10, "Math": 8, "English": 4, "History": 3}
contact_info = {"Mom": "704-555-0199", "Roommate": "336-555-781", "Academic Advisor": "336-334-5000"}

print("Course credits dictionary: ", course_credits)
print("Course professors dictionary: ", course_professors)
print("Course room dictionary: ", course_room)
print("Monthly budget dictionary: ", monthly_budget)
print("Study hours per subject dictionary: ", study_hours)
print("Contact directory dictionary: ", contact_info)


#Calculations 
total_credits = sum(credit_hour_list)
average_gpa = sum(gpa_history) / len(gpa_history)
completed_courses = len(completed_course_list)
total_study_hours = sum(study_hours.values())
academic_load_credits = sum(course_credits.values()) 
all_mothly_budget = sum(monthly_budget.values())
daily_food_budget = monthly_budget["Food"] / 30
annual_budget = all_mothly_budget * 12
study_cost = monthly_budget["Books"] / total_study_hours
total_sm_followers = insta_info[2] + twitter_info[2]
skills_comparison1 = len(current_skills)
skills_comparison2 = len(skills_to_learn)
contact_directory = len(contact_info)

print("Total credits this semester: ", total_credits)
print("Cumulative GPA: ", average_gpa)
print("Count of completed courses: ", completed_courses)
print("Total weekly study hours: ", total_study_hours)
print("Academic load: ", academic_load_credits)
print("Monthly budget total: $", all_mothly_budget)
print(f"Daily food budget: ${daily_food_budget:.2f}")
print("Annual budget: $", annual_budget)
print(f"Study cost per hour: ${study_cost:.2f}")
print("Total social media followers: ", total_sm_followers)
print("Current skills count: ", skills_comparison1, " vs. Skills to learn count: ", skills_comparison2)
print("Contact directory size: ", contact_directory)
