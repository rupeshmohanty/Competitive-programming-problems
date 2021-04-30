if __name__ == "__main__":
    n = int(input())
    faces = 0

    for i in range(n):
        ip = input()
        if(ip == "Tetrahedron"):
            faces = faces + 4
        elif(ip == "Cube"):
            faces = faces + 6
        elif(ip == "Octahedron"):
            faces = faces + 8
        elif(ip == "Dodecahedron"):
            faces = faces + 12
        else:
            faces = faces + 20
    
    print(faces)