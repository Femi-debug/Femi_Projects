# student_register.py

# Ask the user how many students are registering
num_students = int(input("How many students are registering? "))

# Open reg_form.txt for writing (will create or overwrite)
with open("reg_form.txt", "w") as file:
    # Loop for each student
    for i in range(num_students):
        student_id = input(f"Enter student ID number for student {i+1}: ")
        # Write ID to file with a dotted line for signing
        file.write(f"{student_id} ........................................\n")

print("All student IDs registered. The register is saved in 'reg_form.txt'.")