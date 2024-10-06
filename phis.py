from math import sqrt
def form(I):
    m0 = 12.6 * 10**(-7)
    L = 0.18
    N = 550
    R = 0.025
    V1 = (m0*I*N)/(2*L)
    z = 0.00
    c = 0
    while z <= 0.19:
        ans = V1*( ((L-z)/(sqrt(R**2 + (L - z)**2))) + (z/(sqrt(R**2 + z**2))))
        print(f"B{c} = {round(ans*1000, 1)}мТл")
        z += 0.01
        c += 1
        
I = int(input("I:\n"))
form(I)
