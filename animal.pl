Q.Dog → Animal → Pet → Living Being
Facts:Define at least 4 dogs (Ex: Tommy, Bruno, Lucky, Rocky).
Rules:
If X is a dog, then X is an animal.
If X is an animal, then X can be a pet.
If X is a pet, then X is a living being.
Queries:
Prove that Tommy is a pet.
Prove that Bruno is a living being.
List all living beings.

Code:
dog(tommy).
dog(bruno).
dog(lucky).
dog(rocky).

animal(X):-dog(X).
pet(X):-animal(X).
livingbeing(X):-pet(X).


Query:
?-pet(tommy).
?-livingbeing(bruno).
?-livingbeing(X).
