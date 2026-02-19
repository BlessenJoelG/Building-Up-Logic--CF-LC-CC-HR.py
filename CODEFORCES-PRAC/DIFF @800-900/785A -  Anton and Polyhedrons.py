alpha,alphia  = input(),set()
list_alpha = list(alpha)
for _ in list_alpha:
    if "a"<= _ <= "z":
        alphia.add(_) 
print(len(alphia))
shapes,faces = [],0
n = int(input())
for x in range(n):
    shapes.append(input())
for _ in shapes:
    if _ == "Tetrahedron":
        faces = faces + 4
    elif _ == "Cube":
        faces = faces + 6
    elif _ == "Octahedron":
        faces = faces + 8
    elif _ == "Dodecahedron":
        faces = faces + 12
    elif _ == "Icosahedron":
        faces = faces + 20
print(faces)