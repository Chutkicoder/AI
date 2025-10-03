print("===Arithmetic Associative Law===")
a=int(input("Enter value for a:"))
b=int(input("Enter value for b:"))
c=int(input("Enter value for c:"))
lhs_add=(a+b)+c
rhs_add=a+(b+c)
print(f"(a+b)+c=({a}+{b})+{c}={lhs_add}")
print(f"a+(b+c)={a}+({b}+{c})={rhs_add}")

if lhs_add==rhs_add:
    print("Addition Associative Law holds")
else:
    print("Addition Associative Law does not holds")

lhs_mul=(a*b)*c
rhs_mul=a*(b*c)
print(f"(a*b)c=({a}{b})*{c}={lhs_mul}")
print(f"a*(b*c)={a}({b}{c})={rhs_mul}")

if lhs_mul==rhs_mul:
    print("Multiplication Associative Law holds")
else:
    print("Multiplication Associative Law does not holds")
print("\n")

print("===Boolean Associative Law===")
print("Enter Boolean values as 1 (True) or 0 (False): ")
A=bool(int(input("Enter value for A:")))
B=bool(int(input("Enter value for B:")))
C=bool(int(input("Enter value for C:")))
lhs_or=(A or B) or C
rhs_or=A or (B or C)
print(f"(A or B) or C=({A} or {B}) or {C}={lhs_or}")
print(f"A or (B or C)={A} or ({B} or {C})={rhs_or}")

if lhs_or==rhs_or:
    print("OR Associative Law holds")
else:
    print("OR Associative Law does not holds")

lhs_and=(A and B) and C
rhs_and=A and (B and C)
print(f"(A and B) and C=({A} and {B}) and {C}={lhs_and}")
print(f"A and (B and C)={A} and ({B} and {C})={rhs_and}")

if lhs_and==rhs_and:
    print("AND Associative Law holds")
else:
    print("AND Associative Law does not holds")
