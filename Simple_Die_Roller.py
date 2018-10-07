import random

def dieroller():
    plsroll=random.randint(1,6)
    print('You rolled a',plsroll)

def main():
    roller=True
    while roller:
        ans=str(input('Ready to Roll? Y=ROLL . Q=QUIT:'))
        if ans.lower()=='y':
            dieroller()
        elif ans.lower()=='q':
            print('Thankyou for Playing......')
            break
        else:
            print('INVALID INPUT')

main()
