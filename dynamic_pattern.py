# *
# **
# ***     *
# **********
# ***     *
# **
# *

n=7
for i in range(0,n):
    for j in range(0,n):
        if(i<n//2 and j<=i) or (i>n//2 and j<n-i) or (i==n//2 and j<=n):
            print("*",end='')
        else:
            print(" ",end='')

    if (i==n//2-1 or i==n//2+1):
        print(" *",end='')
    if(i==n//2):
        print("***",end='')
    print()


#      @
#     @@@
#    @@@@@
#   @@@@@@@
#   *     *
#  **     **
# ***@@@@@***
#  **     **
#   *     *

n = 5
for i in range(n//2+2):
    for j in range(n-i):
        print(" ",end='')
    for j in range(2*i+1):
        print("@",end='')
    print()
for i in range(n):
    for j in range(n//2+1):
        if (j>=n//2-i and j>=i-n//2):
            print("*",end='')
        else:
            print(" ",end='')

    for j in range(n):
       if i==n//2:
           print("@",end='')
       else:
           print(" ",end='')

    for j in range(n//2+1):
        if(j>=n//2-i and j>=i-n//2):
            print("*",end='')
    print()


#    @@@@@@@
#     @@@@@
#      @@@
#       @
# *******
# *     *
# *     *
# *     *
# *     *
# *     *
# *     *

n = 7
for i in range(1,n//2+2):
    for j in range(1,n//2+1):
        print(" ",end='')
    for j in range(1,n+1):
        if j>=i and j<=(n+1)-i:
            print("@",end='')
        else:
            print(" ",end='')
    print()

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==1 or j==n:
            print("*",end='')
        else:
            print(" ",end='')
    print()


#        *
#       ***
#      *****
#      @   @
#      @   @
#      @   @
# *****@   @*****
#  ***       ***
#   *         *

n=5
for i in range(1,n//2+2):
    for j in range(1,n+1):
        print(" ",end='')
    for j in range(1,n+1):
        if j>=n//2+2-i and j<=n//2+i:
            print("*",end='')
        else:
            print(" ",end='')
    print()

for i in range(1,n-1):
    for j in range(1,n+1):
        print(" ",end='')
    for j in range(1,n+1):
        if j==1 or j==n :
            print("@",end='')
        else:
            print(" ",end='')
    print()

for i in range(1,n//2+2):
    for j in range(1,n+1):
        if j>=i and j<=(n+1)-i:
            print("*",end='')
        else:
            print(" ",end='')

    for j in range(1,n+1):
        if  i==1 and (j==1 or j==(n+1)-1):
            print("@",end='')
        else:
            print(" ",end='')

    for j in range(1,n+1):
        if j>=i and j<=(n+1)-i:
            print("*",end='')
        else:
            print(" ",end='')
    print()


#            e
#            e
#            e
#            e
#            e
#            e
#            e
#            e
#    eeeeeeeee
#    @
#   @@@
#  @@@@@
# @@@@@@@

n=7
for i in range(n+2):
    for j in range(n+3):
        print(" ",end='')
    for j in range(n+3):
        if j==i-1:
            print("e",end='')
    print()

for i in range(1):
    for j in range(n//2):
        print(" ",end='')
    for j in range(n+2):
        print("e",end='')
    print()

for i in range(1,n//2+2):
    for j in range(1,n+1):
        if j>=n//2+2-i and j<=n//2+i:
            print("@",end='')
        else:
            print(" ",end='')
    print()


# *
# *   *
# *   *   *
# *eee*eee*eee
# *   *   *
# *   *
# *

n=3
for i in range(1,n*2+2):
    for j in range(1):
        print("*",end='')
    for j in range(1,n+1):
        if i==n+1:
            print("e",end='')
        else:
            print(" ",end='')

    for j in range(1):
        if i>=2 and i<=n*2:
            print("*",end='')
    for j in range(n):
        if i==n+1:
            print("e",end='')
        else:
            print(" ",end='')

    for j in range(1):
        if i>=3 and i<=n*2-1:
            print("*",end='')
    for j in range(n):
        if i==n+1:
            print("e",end='')
        else:
            print(" ",end='')
    print()


#    *
#   * *
#  * * *
# * * * *
n = int(input("Ener a Number: "))
for i in range(n):
    for j in range(n-1-i):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=' ')
    print()

# * * * *
#  * * *
#   * *
#    *
n = int(input("Enter a Number: "))
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    print()


#    *
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *
n = int(input("Enter a Number: "))
for i in range(n):
    for j in range(n-1-i):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=' ')
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    print()


# ALPHABET STAR PATTERN

#  ***
# *   *
# *   *
# *****
# *   *
# *   *
# *   *

for i in range(7):
    for j in range(5):
        if ((j==0 or j==4)  and i!=0) or ((i==0 or i==3) and (j>0 and j<4)):
            print("*",end='')
        else:
            print(" ",end='')
    print()

# ****
# *   *
# *   *
# ****
# *   *
# *   *
# ****
for i in range(7):
    for j in range(5):
        if (j==0) or (j==4 and(i!=0 and i!=3 and i!=6)) or ((i==0 or i==3 or i==6) and (j>0 and j<4)):
            print("*",end='')
        else:
            print(" ",end='')
    print()

# *****
# *
# *
# *
# *
# *
# *****
for i in range(7):
    for j in range(5):
        if j==0 or (i==0 or i==6):
            print("*",end='')
        else:
            print(" ",end='')
    print()

# ****
# *   *
# *   *
# *   *
# *   *
# *   *
# ****
for i in range(7):
    for j in range(5):
        if (j==0) or (j==4 and (i!=0 and i!=6)) or ((i==0 or i==6) and (j>0 and j<4)):
            print("*",end='')
        else:
            print(" ",end='')
    print()

# *****
# *
# *
# *****
# *
# *
# *****
for i in range(7):
    for j in range(5):
        if (i==0 or j==0) or (i==3 or i==6):
            print("*",end='')
        else:
            print(" ",end='')
    print()

# *****
# *
# *
# *****
# *
# *
# *
for i in range(7):
    for j in range(5):
        if (i==0 or j==0 or i==3):
            print("*",end='')
        else:
            print(" ",end='')
    print()

# *****
# *
# *
# *  ***
# *   *
# *   *
# *****

for i in range(7):
    for j in range(6):
        if ((i==0 or i==6 or j==0) and j<5) or ((i==3) and j>2) or ((j==4 and i>3) and j>2):
            print("*",end='')
        else:
            print(" ",end='')
    print()


# *   *
# *   *
# *   *
# *****
# *   *
# *   *
# *   *

for i in range(7):
    for j in range(5):
        if (j==0 or j==4) or (i==3):
            print("*",end='')
        else:
            print(" ",end='')
    print()

# *****
#   *
#   *
#   *
#   *
#   *
# *****

for i in range(7):
    for j in range(5):
        if (i==0 or i==6) or j==2:
            print("*",end='')
        else:
            print(" ",end='')
    print()

# *****
#   *
#   *
#   *
#   *
#   *
# ***
for i in range(7):
    for j in range(5):
        if (i==0 or (i==6 and j<3)) or j==2:
            print("*",end='')
        else:
            print(" ",end='')
    print()

# *   *
# *  *
# * *
# **
# * *
# *  *
# *   *
k=0
l=4
for i in range(7):
    for j in range(5):
        if j==0 or (i==j+2 and j>1):
            print("*",end='')
        elif (i==k and j==l) and j>0:
            print("*",end='')
            k=k+1
            l=l-1
        else:
            print(" ",end='')
    print()

# *
# *
# *
# *
# *
# *
# *****

for i in range(7):
    for j in range(5):
        if j==0 or i==6:
            print("*",end='')
        else:
            print(" ",end='')
    print()

# *     *
# **   **
# * * * *
# *  *  *
# *     *
# *     *
# *     *
for i in range(7):
    for j in range(7):
        if (j==0 or j==6) or (i==j and i<4) or (i==1 and j==5) or (i==2 and j==4):
            print("*",end='')
        else:
            print(" ",end='')
    print()

# *     *
# **    *
# * *   *
# *  *  *
# *   * *
# *    **
# *     *

for i in range(7):
    for j in range(7):
        if (j==0 or j==6) or (i==j):
            print("*",end='')
        else:
            print(" ",end='')
    print()

#  ***
# *   *
# *   *
# *   *
# *   *
# *   *
#  ***
for i in range(7):
    for j in range(5):
        if (j==0 and i>0 and i<6) or (j==4 and i>0 and i<6) or (i==0 and j>0 and j<4) or (i==6 and j>0 and j<4):
            print("*",end='')
        else:
            print(" ",end='')
    print()

# ****
# *   *
# *   *
# ****
# *
# *
# *

for i in range(7):
    for j in range(5):
        if ((j==0) or (j==4 and i>0 and i<3)) or (i==0 and j<4) or (i==3 and j<4):
            print("*",end='')
        else:
            print(" ",end='')
    print()

#  ***
# *   *
# *   *
# *   *
# *   *
# **  *
#  ***
#    *

for i in range(8):
    for j in range(5):
        if (j==0 and i>0 and i<6 or j==4 and i>0 and i<6) or (i==0 and j>0 and j<4 or i==6 and j>0 and j<4)\
                or (i==5 and j<2) or (j==3 and i==7):
            print("*",end='')
        else:
            print(" ",end='')
    print()

# ****
# *   *
# *   *
# ****
# *   *
# *   *
# *   *

for i in range(7):
    for j in range(5):
        if (j==0) or (j==4 and( i!=0 and i!=3)) or (i==0 and j<4) or (i==3 and j<4):
            print("*",end='')
        else:
            print(" ",end='')
    print()


#  ***
# *
# *
#  ***
#     *
#     *
#  ***
for i in range(7):
    for j in range(5):
        if ((i==1 and j<1) or (i==2 and j<1)) or ((i==4 and j>3) or (i==5 and j>3)) or ((i==0 or i==3 or i==6) and j>0 and j<4):
            print("*",end='')
        else:
            print(" ",end='')
    print()

# *****
#   *
#   *
#   *
#   *
#   *
#   *

for i in range(7):
    for j in range(5):
        if i==0 or j==2:
            print("*",end='')
        else:
            print(" ",end='')
    print()

# *   *
# *   *
# *   *
# *   *
# *   *
# *   *
#  ***

for i in range(7):
    for j in range(5):
        if ((j==0 and i!=6) or (j==4 and i!=6)) or (i==6 and j!=0 and j!=4):
            print("*",end='')
        else:
            print(" ",end='')
    print()

# *     *
#  *   *
#   * *
#    *

for i in range(4):
    for j in range(7):
        if (i==j) or (i==0 and j==6) or (i==1 and j==5) or (i==2 and j==4):
            print("*",end='')
        else:
            print(" ",end='')
    print()


# *  *  *
# * * * *
# **   **
# *     *
k=0
l=3
for i in range(4):
    for j in range(7):
        if (j==0 or j==6) or ( j==4 and i==1 or j==5 and i==2) or ():
            print("*",end='')
        elif (i==k and j==l):
            print("*",end='')
            k=k+1
            l=l-1
        else:
            print(" ",end='')
    print()


# *   *
#  * *
#   *
#  * *
# *   *
k=0
l=4
for i in range(5):
    for j in range(5):
        if i==k and j==l:
            print("*",end='')
            k=k+1
            l=l-1
        elif i==j:
            print("*",end='')
        else:
            print(" ",end='')
    print()


# *   *
#  * *
#   *
#   *
#   *

k=0
l=4
for i in range(5):
    for j in range(5):
        if (j==2 and i>1) or (i==j and j<2) or (i==0 and j==4) or (i==1 and j==3):
            print("*",end='')
        else:
            print(" ",end='')
    print()


# ******
#     *
#    *
#   *
#  *
# ******
k=1
l=4
for i in range(6):
    for j in range(6):
        if (i==0 or i==5):
            print("*",end='')
        elif i==k and j==l:
            print("*",end='')
            k+=1
            l-=1
        else:
            print(" ",end='')
    print()