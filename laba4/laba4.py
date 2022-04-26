
class Set:   #elem
    def __init__(self):
        self.mn = []
        self.size = 0

    def File(self):
        pois:int
        f = open('text.txt','r')
        for line in f:
            pois = line.find('\n')
            if pois == -1:
                pass
            else:
                line = line[0:pois]

            self.Add(line)


    def Add(self,atr):
        i = 0
        flag = True
        for a in self.mn:
            if a == atr:
                flag = False
                break

        if flag == True:
            if self.size == 0:
                self.mn.append(atr)
                self.size += 1
            else:
                for k in self.mn:
                    if k > atr:
                        i += 1
                    else:
                        break
                self.mn.insert(i,atr)
                self.size += 1


    def Del(self,el):
        flag = False
        for elem in self.mn:
            if elem == el:
                flag = True
        if flag == True:
            i = self.mn.index(el)
            self.mn.pop(i)
            self.size -= 1      
       

    def Poisk(self,el):
        i = 0
        flag = -1
        for elem in self.mn:
            if elem == el:
                return i
            i += 1
        return flag

    def Union(self,E):
        U = Set()   
        for i in self.mn:
            U.Add(i)
        for j in E.mn:
            U.Add(j)
        return U

    def Cross(self,L,E,mno):
        C = Set()
        if mno == '1':
            for i in L.mn:
                flag = True
                for j in E.mn:
                    if i == j:
                         flag = False
                if flag == 1:
                    C.Add(i)
        else:
            for i in E.mn:
                flag = True
                for j in L.mn:
                    if i == j:
                         flag = False
                if flag == 1:
                    C.Add(i)


        return C

    def Show(self):
        print('Размер множества: ', self.size)
        for i in self.mn:
            print(i)


L = Set()
E = Set()
U = Set()
C = Set()
el: int
while True:
    print('С каким множеством хотите работать?(1/2)')
    mno = input()
    if((mno != '1') & (mno != '2')):
        print('Недопустимый символ')
        continue
    
    print('Что вы хотите сделать?')
    print('0: Ввод из файла')
    print('1: Включить элемент')
    print('2: Исключить элемент')
    print('3: Объединить множества')
    print('4: Вычесть множества')
    print('5: Найти элемент')
    print('6: Вывести множество')
    print('7: Выйти')
    vvod = input()

    if vvod == '0':
        if mno == '1':
            L.File()
        elif mno == '2':
            E.File()
    elif vvod == '1':
        atr = input('Введите элемент: ')
        if mno == '1':
            L.Add(atr)
        elif mno == '2':
            E.Add(atr)
    elif vvod == '2':
        atr = input('Введите элемент: ')
        if mno == '1':
            L.Del(atr)
        elif mno == '2':
            E.Del(atr)
    elif vvod == '3':
        U = L.Union(E)
        U.Show()
    elif vvod == '4':
        if mno == '1':
            C = L.Cross(L,E,mno)
        if mno == '2':
            C = E.Cross(L,E,mno)
        C.Show()
    elif vvod == '5':       
        atr = input('Введите элемент: ')
        if mno == '1':
            el = L.Poisk(atr)
        elif mno == '2':
            el = E.Poisk(atr)

        if el == -1:
            print('такой элемент не найден')
        else:
            print('элемент найден ')
    elif vvod == '6':
        if mno == '1':
            L.Show()
        elif mno == '2':
            E.Show()
    elif vvod == '7':
        break
    else:
        print('Недопустимый символ')  
        continue


