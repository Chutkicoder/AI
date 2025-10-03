Q.Batsman → Cricketer → Sportsman → Famous person
Facts: Define at least 4 batsman (Ex: Sachin, Virat, Dhoni, Rohit)
Rules:
If X is a Batsman, then X is cricketer
If X is a cricketer, then X is sportsman
If X is a sportsman, then X is a famous person
Queries:
Check if sachin is a cricketer
Check if virat is a sportsman
List all famous persons

Code:
batsman(sachin).
batsman(virat).
batsman(rohit).
batsman(dhoni).

cricketer(X):-batsman(X).
sportsman(X):-cricketer(X).
famous(X):-sportsman(X).


Query:
| ?- cricketer(sachin).
| ?- sportsman(virat).
| ?- famous(X).
