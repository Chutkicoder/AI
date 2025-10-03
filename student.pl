Q2 Students details
student(rahul,math,85).
student(sita,math,92).
student(amit,science,78).
student(rina,science,89).
student(karan,english,76).
student(sita,english,88).

high_score(Name):-student(Name,_,Marks),Marks>80.
math_student(Name):-student(Name,math,_).
topper(Subject,Name,Marks):-student(Name,Subject,Marks),\+ (student(_,Subject,Marks2),Marks2>Marks).


Query:
| ?- high_score(Name).
| ?- math_student(Name).
| ?- topper(Subject,Name,Marks).