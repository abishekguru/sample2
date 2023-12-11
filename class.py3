class parent():
	def _init_(self,name,rollno):
		self.name = name
		self.rollno = rollno
class parent2():
	def _init_(self,age,favsub):
		self.age = age
		self.favsub = favsub
class child(parent,parent2):
	def _init_(self,name,rollno,age,favsub):
		super()._init_(self,name,rolln,age,favsub)
	def print(self):
		print(self.name)
		print(self.rollno)
		print(self.age)
		print(self.favsub)

c1 = child()
n1 = input("Enter name")
n2 = int(input("Enter roll no"))
n3 = int(input("Enter age"))
n4 = input("Enter favourite subject")
c1.name = n1
c1.rollno = n2
c1.age = n3
c1.favsub = n4
c1.print()
