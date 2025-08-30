class Course:
    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"

    #Class attribute for head office location
    head_office = "cape town".lower()

    # Method to display contact details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    #Method to display head office location
    def head_office(self):
        print("Head office is located in", self.head_office)    


#Subclass of Course called OOPCourse.
class OOPCourse(Course):
    def __init__(self,description="OOP Fundamentals", trainer="Mr Anon A. Mouse", id_number="#12345" ):
        self.description = description
        self.trainer = trainer
        self.id_number = id_number
#creating a method in subclass called trainer_details 
    def trainer_details(self):
        print(f"The course is about{self.description} and the name of the trainer is {self.trainer}")

#creating a method in subclass called show_course_id
    def show_course_id(self):
        print(self.id_number)

#creating object called course_1
course_1 = Course("OOP Fundamentals","Mr Anon A. Mouse","#12345")
