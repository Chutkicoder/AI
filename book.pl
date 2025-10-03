Q.Book → Knowledge Source → Educational Material → Valuable Resource
Facts: Define at least 4 books (Ex: physic,math,history,computer)
Rules:
If X is a book, then X is a knowledge source
If X is a knowledge source, then X is an educational material
If X is an educational material, then X is a valuable resource
Queries:
Check if math is a educational material
Check if physics is an valuable resources
List all valuable resources

Code:
book(physics).
book(math).
book(history).
book(computers).

knowledge_source(X):-book(X).
educational_material(X):-knowledge_source(X).
valuable_resources(X):-educational_material(X).


Query:
?-educational_material(math).
?-valuable_resources(physics).
?-valuable_resources(X).
