#This is the implementation of the python object oriented approach for the teacher
if __name__ == "__main__":
    print("running the file as the main")
else:
    class teacher:
        def __init__(self,name,skills):
            self.name = name
            self.skills = skills
        def count_skills(self):
            count=0
            for i in self.skills:
                count+=1
            return count
        def show(self):
            print(f"My name is {self.name}")
            print("My skills are:")
            for skill in self.skills:
                print(skill,end=" ")
            print("\nTotal no of skills {}".format(self.count_skills()))
        def teaching(self):
            print(f"Myself teaching {self.skills[0]} as {self.name}")
            print("Hey Hey Hey")
