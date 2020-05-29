#Дан текстовий файл f. Отримати в файлі g кількість букв, що знаходяться в файлі f
#Курдупов Олексій Леонідович 122Г
f=open('f.txt', 'w')#Створюємо файли
list=([input("Введіть елемент: ") for i in range(int(input("Скільки чисел ви хочите ввести? ")))])#Проходимся по списку
f.write(''.join(map(str,list)))#щоб не повторялися елементи
f=open('f.txt', 'r')
x=f.read()
f.close()
def reverse(x):#тут ми міняєм текст наоборот
    return x[::-1]
b=reverse(x)

def povt(b):
    n=[]
    for i in b:
        if i not in n:
            n.append(i)
    return n
g=open('g.txt', 'w')
g.write(' '.join(map(str, povt(b))))
g.close()