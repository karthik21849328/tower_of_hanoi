def Toh(n,a,b,c):
    if n>0:
        Toh(n-1,a,c,b)
        print(f"move disc from {a} to {c}")
        Toh(n-1,b,a,c)

if __name__=="__main__":
    Toh(2,1,2,3)