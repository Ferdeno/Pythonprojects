#
# class Oombu:
#     def __init__(self):
#         print("Nakku")
#
#
# a = Oombu()
# a.name="Ferdeno"
# a.age=20
# # using object the attributes of the class can be created
# print("Name : ",a.name)
# print("Age : ",a.age)
#
# b=Oombu()
# b.name="deno"
# print(b.name)


class Study:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.section=0
        self.marks=0
    def names(self,mark):
        self.marks+=10
        mark.section+=10

student1=Study("Ferdi",20)
student2=Study("Deno",19)
student1.names(student1)
print(f"Student 1 mark : {student1.marks}")
print(f"Student 1 section : {student1.section}")
print(f"Student 2 mark : {student2.marks}")
print(f"Student 2 section : {student2.section}")



