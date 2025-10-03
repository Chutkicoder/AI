Q.Teacher → Employee → Human → Living Being
Facts: Define at least 4 teachers (Ex: Anita, Raj, Meera, Rahul)
Rules:
If X is a teacher, then X is an employee.
If X is an employee, then X is a human.
If X is a human, then X is a living being.
Queries:
Prove that Anita is a human
Prove that Rahul is a living being
List all humans

Code:
teacher(anita).
teacher(raj).
teacher(meera).
teacher(rahul).

employee(X):-teacher(X).
human(X):-employee(X).
livingbeing(X):-human(X).


Query:
?-human(anita).
?-livingbeing(rahul).
?-human(X).
