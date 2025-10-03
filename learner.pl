Q.Student → Learner → Knowledge Seeker → Future Professional
Facts: Define at least 4 students (Ex: Riya, Amit, Sam, Neha)
Rules:
If X is a student, then X is a learner.
If X is a learner, then X is a knowledge seeker.
If X is a knowledge seeker, then X is a future professional.
Queries:
Check if Riya is a learner
Prove that Amit is a future professional
List all knowledge seekers

Code:
student(riya).
student(amit).
student(sam).
student(neha).

learner(X):-student(X).
knowledge_seeker(X):-learner(X).
future_professional(X):-knowledge_seeker(X).


Query:
?-learner(riya).
?-future_professional(amit).
?-knowledge_seeker(X).
