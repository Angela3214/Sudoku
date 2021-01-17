import random


class t:
    def __init__(self, n=3):
        self.n = n
        self.table = [[((i * n + i // n + j) % (n * n) + 1) for j in range(n * n)] for i in range(9)]
        self.pere()

    def pokaz(self):
        for j in range(self.n ** 2):
            print(self.table[j])

    def trans(self):
        self.table = list(map(list, zip(*self.table)))

    def swap_rows_1(self):
        a = random.randrange(0, self.n, 1)
        b = random.randrange(0, self.n, 1)
        str1 = a * self.n + b
        c = random.randrange(0, self.n, 1)
        str2 = a * self.n + c
        while str1 == str2:
            str2 = random.randrange(0, self.n, 1)
        self.table[str1], self.table[str2] = self.table[str2], self.table[str1]

    def swap_col_1(self):
        self.trans()
        self.swap_rows_1()
        self.trans()

    def swap_rows_3(self):
        a = random.randrange(0, self.n, 1)
        b = random.randrange(0, self.n, 1)
        while a == b:
            b = random.randrange(0, self.n, 1)
        for i in range(0, self.n):
            k1 = a * self.n
            k2 = b * self.n
            d, c = k1 + i, k2 + i
            self.table[d], self.table[c] = self.table[c], self.table[d]

    def swap_col_3(self):
        self.trans()
        self.swap_rows_3()
        self.trans()

    def pere(self):
        for i in range(40):
            ap = random.randrange(0, 4)
            if ap == 0:
                self.trans()
            if ap == 1:
                self.swap_rows_1()
            if ap == 2:
                self.swap_col_1()
            if ap == 3:
                self.swap_rows_3()
            if ap == 4:
                self.swap_col_3()


class g:
    def __init__(self, n):
        self.n = 3
        self.matr = t()
        self.m = n
        self.sozd()
        self.sozdnew()
        self.pokaz()
        self.shag()

    def pokaz(self):
        for j in range(self.n ** 2):
            print(self.t[j])

    def sozd(self):
        self.t = []
        for i in range(9):
            k = []
            for j in range(9):
                k.append(0)
            self.t.append(k)
        lst = list(range(0, 81))
        random.shuffle(lst)

        for i in range(self.m):
            self.t[lst[i] // 9][lst[i] % 9] += self.matr.table[lst[i] // 9][lst[i] % 9]

    def sozdnew(self):
        self.g = []
        for i in range(9):
            r = list()
            for j in range(9):
                s = set()
                for k in range(9):
                    s.add(self.t[i][k])
                    s.add(self.t[k][j])
                for m in range(3):
                    for er in range(3):
                        s.add(self.t[(i // 3) * 3 + m][(j // 3) * 3 + er])
                r.append(s)
            self.g.append(r)

    def obnov(self, x, y, z):
        self.sozdnew()

    def shag(self):
        print('Введите координаты клетки')
        x = int(input()) - 1
        y = int(input()) - 1
        print('Введите значение клетки')
        z = int(input())
        if z in self.g[y][x]:
            print('Вы проиграли')
        else:
            self.t[y][x] = z
            self.obnov(x, y, z)
            self.pokaz()
            self.shag()


print('Введите количество заполненных клеток')
h = int(input())
w = g(h)
