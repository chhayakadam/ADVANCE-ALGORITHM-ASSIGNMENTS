#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Function to perform merge sort
def merge_sort(students, key):
    if len(students) > 1:
        mid = len(students) // 2
        left_half = students[:mid]
        right_half = students[mid:]

        # Recursively sort both halves
        merge_sort(left_half, key)
        merge_sort(right_half, key)

        # Merge the sorted halves
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i][key] < right_half[j][key]:
                students[k] = left_half[i]
                i += 1
            else:
                students[k] = right_half[j]
                j += 1
            k += 1

        # Copy the remaining elements
        while i < len(left_half):
            students[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            students[k] = right_half[j]
            j += 1
            k += 1

# Function to display the sorted student data
def display_student_data(students):
    print("\nSorted Student Data:")
    print(f"{'Name':<15} {'Roll No':<10} {'Entrance Marks':<15}")
    print("-" * 40)
    for student in students:
        print(f"{student['Name']:<15} {student['Roll No']:<10} {student['Entrance Marks']:<15}")

# Main function to collect data and sort it
def main():
    # Collect student data
    students = []
    num_students = int(input("Enter the number of students: "))

    for _ in range(num_students):
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")
        entrance_marks = float(input("Enter entrance marks: "))
        
        student = {
            'Name': name,
            'Roll No': roll_no,
            'Entrance Marks': entrance_marks
        }
        students.append(student)

    # Ask the user to choose the field for sorting
    print("\nChoose the field for sorting:")
    print("1. Name")
    print("2. Roll No")
    print("3. Entrance Marks")
    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        key = 'Name'
    elif choice == 2:
        key = 'Roll No'
    elif choice == 3:
        key = 'Entrance Marks'
    else:
        print("Invalid choice! Sorting by Name as default.")
        key = 'Name'

    # Sort the students using merge sort based on the chosen field
    merge_sort(students, key)

    # Display the sorted data
    display_student_data(students)

# Run the program
if __name__ == "__main__":
    main()


# In[ ]:




