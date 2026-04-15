class Book:
    '''这是关于图书信息的一个类'''
    def __init__(self, isbn: str, name: str, price: float):
        '''初始化图书的基本信息'''
        self.isbn = isbn
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"《{self.name}》-({self.isbn})-$'{self.price}'"
    

class BookSeqlist:
    '''这是一个顺序表的图书管理系统'''
    def __init__(self, maxsize: int = 100):
        '''初始化基本属性'''
        if maxsize <= 0:
            raise ValueError("maxsize必须大于0")
        self.maxsize = maxsize
        self.data = [None] * maxsize
        self.length = 0

    def get_elem(self, i: int):
        '''取值'''
        if i < 1 or i > self.length:
            raise IndexError("位置错误")
        return self.data[i-1]
    
    def locate_elem(self, bookname: str):
        '''查找'''
        for i in range(0,self.length):
            if self.data[i].name == bookname:
                return i+1
            else:
                return False
            
    def insert(self, i: int, book: Book):
        """插入"""
        if self.length >= self.maxsize:
            print('错误，顺序表已满')
            return False
        if i < 1 or i > self.length + 1:
            raise IndexError("位置不合法")
        for j in range(self.length-1,i-2,-1):
            self.data[j+1] = self.data[j]
        self.data[i-1] = book
        self.length += 1
        return True
    


        

        