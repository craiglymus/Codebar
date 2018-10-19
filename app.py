class Member:
    def __init__(self, full_name):
        self.name = full_name

    def introduce(self):
        print(f'Hi, my name is {self.name}')


class Student(Member):
	def __init__(self, reason, full_name):
		super().__init__(full_name)
		self.reason = reason

class Instructor(Member):
	def __init__(self, full_name, bio):
		super().__init__(full_name)
		self.bio = bio
		self.skills = []

	def add_skill(self, new_skill):
		self.skills.append(new_skill)


class Workshop:
	def __init__(self, date, subject):
		self.date = date
		self.subject = subject
		self.instructors = []
		self.students = []

	def add_participant(self, participant):
		if isinstance(participant, Instructor):
			self.instructors.append(participant)
		elif isinstance(participant, Student):
			self.students.append(participant)

PRINT DETAILS FORMULA



Kevin = Instructor('Kevin Smith', 'I have been coding in Python for 5 years and want to share the love!')
print(Kevin)








