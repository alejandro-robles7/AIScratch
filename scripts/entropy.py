from math import log

def ent(p):
	if p == 0 or p==1:
		return 0
	else:
		p2 = 1 - p
		return -p*log(p, 2) - p2*log(p2, 2)

def entg(start, a1, p1, a2, p2):
    return ent(start) - (a1* ent(p1) + a2* ent(p2))


# Wind
n = 14.0
start_num = 9
a11, a22 = 8, 6
b11, b22 = 6, 3
start = start_num/n
a1 = a11/n
a2 = a22/n
p1 = b11/a11
p2 = b22/a22
print(entg(start, a1, p1, a2, p2))

# Humidity
a11, a22 = 7, 7
b11, b22 = 3, 6
a1 = a11/n
a2 = a22/n
p1 = b11/a11
p2 = b22/a22
print(entg(start, a1, p1, a2, p2))


# Temp
a11, a22, a33 = 4, 6, 4
b11, b22, b33 = 2, 4, 3
a1 = a11/n
a2 = a22/n
a3 = a33/n
p1 = b11/a11
p2 = b22/a22
p3 = b33/a33
print(ent(start) - (a1* ent(p1) + a2* ent(p2) + a3*ent(p3)))


# Outlook

a11, a22, a33 = 5, 4, 5
b11, b22, b33 = 2, 4, 3
a1 = a11/n
a2 = a22/n
a3 = a33/n
p1 = b11/a11
p2 = b22/a22
p3 = b33/a33
print(ent(start) - (a1* ent(p1) + a2*ent(p2) + a3*ent(p3)))

