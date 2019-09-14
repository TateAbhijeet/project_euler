def pythagorean_triplet():
    for a in range(1,1000):
        for b in range(a,1000):
            c = 1000-a-b
            if (a*a+b*b) == c**2:
                print(a, b, c)
                print(a*b*c)
                
pythagorean_triplet()