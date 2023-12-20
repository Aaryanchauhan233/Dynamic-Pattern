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


