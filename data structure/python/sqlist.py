class Seqlist:
    """顺序表"""

    def __init__(self,capacity=10):
        """初始化顺序表"""
        self.capacity = capacity
        self.data = [None] * self.capacity
        self.length = 0

    def is_empty(self):
        """是否为空"""
        return self.length == 0

    def is_full(self):
        """是否满溢"""
        return self.length == self.capacity

    def add(self,item):
        """尾部添加元素"""
        if self.is_full():
            raise OverflowError("顺序表已满")
        self.data[self.length] = item
        self.length +=1

    def insert(self,index,item):
        """向指定位置添加元素"""
        if index < 0 or index > self.length:
            raise IndexError("插入位置非法")
        for i in range(self.length,index,-1):
            self.data[i] = self.data[i-1]
        self.data[index] = item
        self.length += 1

    def remove(self,index):
        """删除指定位置元素，并返回元素"""
        if index < 0 or index >= self.length:
            raise IndexError("插入位置非法")
        item = self.data[index]
        for i in range(index,self.length-1):
            self.data[i] = self.data[i+1]
        self.length -= 1
        return item

    def get(self,index):
        """获取指定位置的元素"""
        if index < 0 or index >= self.length:
            raise IndexError("索引越界")
        return self.data[index]

    def set(self,index,item):
        """更新指定位置的元素"""
        if index < 0 or index >= self.length:
            raise IndexError('索引越界')
        self.data[index] = item

    def find(self,item):
        """查找元素首次出现的位置，未找到返回-1"""
        for i in range(self.length):
            if self.data[i] == item:
                return i
        return -1

    def display(self):
        """展示顺序表元素"""
        print(self.data[:self.length])


if __name__ == "__main__":
    L = Seqlist(100)