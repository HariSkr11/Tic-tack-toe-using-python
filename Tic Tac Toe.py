import random
column=row=[1,2,3]
display = [['-' for i in range(3)] for j in range(3)]
def check_dash(display):
    for i in display:
        if '-' in i:
            return True
    return False
def get_diagonals(display):
    diagonals = [[display[0][0],display[1][1],display[2][2]],[display[0][2],display[1][1],display[2][0]]]
    return diagonals
def check_diagonals(display):
    diagonals = get_diagonals(display)
    for i in diagonals:
        if i==['x','x','x'] or i==['o','o','o']:
            return False
    return True
def print_current(display):
    for i in range(3):
       print(*display[i],sep=" ")
       print()
def row_checker(display):
    for i in range(3):
        if(display[i]==['x','x','x'] or display[i]==['o','o','o']):
            return False
    return True
def get_columns(display):
    columns = []
    for i in range(3):
        c1 = []
        for j in range(3):
            c1.append(display[j][i])
        columns.append(c1)
    return columns
def check_columns(display):
    columns = get_columns(display)
    for i in columns:
        if i == ['x','x','x'] or i ==['o','o','o']:
            return False
    return True
def init1(display):
    i=1
    a=1
    print("Simple tic tac toe game using python without using the concepts od object oriented programming")
    for j in display:
        print((a,i),(a,i+1),(a,i+2),sep=' ')
        print(*j,sep='\t\t ')
        a+=1
    print("The above figure show the index of the 3x3 grid. The Two players should input the correponding row column pair to mark at that position")
def main():
 while check_dash(display) :
    move_x = tuple((input("Enter the move of x ").split()))
    display[int(move_x[0])-1][int(move_x[1])-1]='x'
    print_current(display)
    if (not row_checker(display) and not check_columns(display)):
        if (not row_checker(display)):
         for i in range(3):

              if (display[i] == ['o', 'o', 'o']):
                  print('o wins the game')
                  break
              elif (display[i] == ['x', 'x', 'x']):
                  print('x wins the game')
                  break
              else:
                  a = 0
        break
    elif (not check_columns(display)):
        columns = get_columns(display)
        for i in columns:
            if i==['x','x','x']:
                print('x wins the game')
                break
            elif i==['o', 'o', 'o']:
                print('o wins the game')
                break
            else:
                a=0
        break
    elif (not check_diagonals(display)):
        diagonals = get_diagonals(display)
        for i in diagonals:
            if i==['x','x','x']:
                print('x wins the game')
                break
            elif i==['o', 'o', 'o']:
                print('o wins the game')
                break
            else:
                a=0
        break
    if(not check_dash(display)):
        print('tie')
        break
    move_o = tuple((input("Enter the move of o ").split()))
    display[int(move_o[0])-1][int(move_o[1])-1]='o'
    print_current(display)
    if (not row_checker(display) and not check_columns(display)):
        if (not row_checker(display)):
            for i in range(3):
                if (display[i] == ['o', 'o', 'o']):
                    print('o wins the game')
                    break
                elif (display[i] == ['x', 'x', 'x']):
                    print('x wins the game')
                    break
                else:
                    a = 0
        break
    elif (not check_columns(display)):
        columns = get_columns(display)
        for i in columns:
            if i == ['x', 'x', 'x']:
                print('x wins the game')
                break
            elif i == ['o', 'o', 'o']:
                print('o wins the game')
                break
            else:
                a = 0
        break
    elif (not check_diagonals(display)):
        diagonals = get_diagonals(display)
        for i in diagonals:
            if i==['x','x','x']:
                print('x wins the game')
                break
            elif i==['o', 'o', 'o']:
                print('o wins the game')
                break
            else:
                a=0
        break
    if (not check_dash(display)):
        print('tie')
        break
init1(display)
try:
    main()
except:
    print('Error occured')
