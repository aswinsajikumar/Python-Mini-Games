import os
s=[[4,3,9],[6,1,2],[5,7,8],
   [6,7,1],[5,8,3],[4,2,9],
   [2,5,8],[4,9,7],[6,1,3],
   [8,2,5],[7,4,1],[3,9,6],
   [7,6,4],[2,3,9],[1,8,5],
   [1,9,3],[8,6,5],[7,4,2],
   [3,1,6],[9,2,4],[8,5,7],
   [5,8,2],[1,7,6],[9,3,4],
   [9,4,7],[3,5,8],[2,6,1]]
p=[[4,3,0],[0,0,0],[0,0,8],
   [0,7,0],[0,0,3],[0,0,9],
   [2,0,0],[4,9,0],[0,0,0],
   [0,2,0],[7,4,1],[0,0,6],
   [0,0,0],[0,0,0],[0,0,0],
   [1,0,0],[8,6,5],[0,4,0],
   [0,0,0],[0,2,4],[0,0,7],
   [5,0,0],[1,0,0],[0,3,0],
   [9,0,0],[0,0,0],[0,6,1]]
def precheck():
    z=0
    for i in p:
        for j in i:
            if j==0:
                z=1
                break
        if z==1:
            break
    else:
        check()
def check():
    if s==p:
        print "CONGRATULATION!\nYOU SOLVED THE PUZZLE!!"
        quit()
    print 'YOU LOST!\nEnter 1 to show the solution\nEnter 2 to quit'
    op=input('Enter the choice:')
    if op==1:
        print '-------------------------'
        c=0
        for i in range(0,25,3):
            print '|',
            for j in range(i,i+3):
                for k in range(0,3):
                    print s[j][k],
                print "|",
            print ''
            c+=1
            if c==3:
                print '-------------------------'
                c=0
        quit()
    elif op==2:
         quit()
def display(x,y,z,f):
    c=0
    print '-------------------------'
    for i in range(0,25,3):
        print '|',
        for j in range(i,i+3):
            for k in range(0,3):
                if x==k and j==(y+z):
                    print '#',
                    if p[j][k]==0:
                        if f=='0' or f=='1' or f=='2'or f=='3'or f=='4'or f=='5'or f=='6'or f=='7'or f=='8'or f=='9':
                            p[j][k]=int(f)
                else:
                    print p[j][k],
            print "|",
        print ''
        c+=1
        if c==3:
            print '-------------------------'
            c=0
    precheck()
    return x,y,z
for i in range(0,100,1):
    def enter(x1,y1,z1):
        sd=0
        ch=raw_input()
        if ch=='w':
            y1-=3
        elif ch=='s':
            y1+=3
        elif ch=='a':
            x1-=1
        elif ch=='d':
            x1+=1
        if x1==3:
            x1=0
            z1+=1
        elif x1==-1:
            z1-=1
            x1=2
        if ch.isdigit():
            sd=ch
        if y1==27:
            y1=0
        if y1==-3:
            y1=24
        if ch=='q':
            if (raw_input("DO YOU WANT TO QUIT?? y/n:")=='y'):
                quit()
        os.system('clear')
        p,o,i=display(x1,y1,z1,sd)
        enter(p,o,i)
print '###########SUDOKU PUZZLE###########\nINSTRUCTIONS:-\n1.# is the cursor\n2.Enter w,s,a,d to move the cursor up,down,left,right respectively\n3.Try to enter numbers from 1 to 9\n4.Replace 0 with appropriate digits\n5.press q to quit\n6.A NUMBER CANNOT BE CHANGED AFTER ENTERING, SO BE CAREFUL\n'
c=0
print '\n\n-------------------------'
for i in range(0,25,3):
    print '|',
    for j in range(i,i+3):
        for k in range(0,3):
            print p[j][k],
        print "|",
    print ''
    c+=1
    if c==3:
        print '-------------------------'
        c=0
print 'Press s to start\n'
enter(0,0,0)

