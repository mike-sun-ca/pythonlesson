student ={'name':'john', 'age':25, 'courses':['math','sci']}
print(student.get('age','apu'))
student['courses'].append('gym')
print(student['courses'])
student.update({'name':'adam'})
print(student)
del student['age']
student.pop('name')
student['phone']='555-5555'
print(student)