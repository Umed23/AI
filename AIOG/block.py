def bow(n,m,f,t,au):
    if(n==1 and m==1):
        print("move for 1 box is from place"+f+"to place"+au)
        print("move for 2 box is from place"+t+"to place"+f)
        print("move for 3 box is from place"+au+"to place"+t)
        print("move for 4 box is from place"+f+"to place"+t)
    if(n==1):
        print("move for 1 box is from place"+f+"to place"+t)
        return
    if(m==1):
        print("move for 1 box is from place"+f+"to place"+t)
        return
    bow(n-1,m-1,f,au,t) 
    print("move for"+str(n)+" box is from place"+f+"to place"+t) 
    bow(n-1,m-1,t,f,au) 
print("Enter the no of box in P1:") 
n=int(input()) 
print("Enter the no of box in P2:") 
m=int(input()) 
print("its done!!!!:\n") 
bow(n,m,'P1','P3','P2')
print("SHIVAM PATEL")
