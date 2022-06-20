#1. Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо. Используйте знания с последней лекции. 
#Выполните ее в виде функции. 
#Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»
text = "абвгдеж рабав копыто аБв фабв Абкн абрыволк аБволк аБвв dfyx"
data=text.split()
print (text)
data = [i.lower() for i in data ]
subtext='абв'
data2 = [i for i in data if subtext not in i]
print (data2) 
#===================================================================
#Отфильтруйте его, чтобы этот текст можно было нормально прочесть. 
# Предусмотрите вариант, что мусорные слова могли быть написаны без использования запятых.
text=[]
path='text.txt'
data=open (path,'r')
for i in data:
    text.append(i)
data.close()
print (text)
list=[]
a=''
j=0
while j< len(text):
    for i in text[j]:
        if (i!=',') and(i!='.')and (i!='\n'):
            a+=i
        else:
            list.append(a)
            a=''
    j+=1
print(list)
z=' in short'
s=' uh '
for i in list:
    if i==z:
        list.remove(i)
    if i==s:
        list.remove(i)
print(list)
#===================================================================

# "Крестики-нолики"
board = [1,2,3,
        4,5,6,
        7,8,9]

victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]   
def print_board():
    print(board[0], end = " ")
    print(board[1], end = " ")
    print(board[2])
 
    print(board[3], end = " ")
    print(board[4], end = " ")
    print(board[5])
 
    print(board[6], end = " ")
    print(board[7], end = " ")
    print(board[8]) 
def step_board(step,symbol):
    ind = board.index(step)
    board[ind] = symbol
def get_result():
    win = ""
 
    for i in victories:
        if board[i[0]] == "X" and board[i[1]] == "X" and board[i[2]] == "X":
            win = "X"
        if board[i[0]] == "O" and board[i[1]] == "O" and board[i[2]] == "O":
            win = "O"   
             
    return win
game_over = False
player1 = True
 
while game_over == False:
    print_board()
    if player1 == True:
        symbol = "X"
        step = int(input("игрок 1, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("игрок 2, ваш ход: "))
 
    step_board(step,symbol) 
    win = get_result() 
    if win != "":
        game_over = True
    else:
        game_over = False
    player1 = not(player1)        
print_board()
print("Победил", win) 





