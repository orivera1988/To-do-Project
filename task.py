class Task(object):
	def __init__(self, due_date, content):
		self.due_date = due_date 
		self.content = content


print "Hey give me a due date"
due = raw_input()
print "Hey now tell me the actual task"
task = raw_input()
x = Task(due, task)

