#Q6

faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
               
fk = faculty_dict.keys()

for i in list(fk)[0:min(3,len(fk))]:
    print(i)
    print("  ")
    print(faculty_dict[i])
    print("\n")
    
    
#Q7
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']}

pk = professor_dict.keys()

for i in list(pk)[0:min(3,len(pk))]:
    print(i)
    print("  ")
    print(professor_dict[i])
    print("\n")

    
#Q8
srted=sorted(pk, key=lambda x: x[0]+x[1])
for s in srted:
    print(s)
    print("  ")
    print(professor_dict[s])
    print("\n")

