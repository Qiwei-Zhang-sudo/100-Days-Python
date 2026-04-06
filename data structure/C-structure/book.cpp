#include<iostream>
using namespace std;
 
#define OK 0
#define ERROR -1
#define OVERFLOW -2

typedef int Status;

#define MAXSIZE 100

struct Book
{
    char ISDN[10];
    char name[20];
    float price;
};

typedef struct 
{
    Book *p;
    int length;
}Sqlist;

Status InitList(Sqlist &L)
{
    L.p = new Book[MAXSIZE];
    if(!L.p)
    {
        exit(OVERFLOW);
        cout<<"overflow"<<endl;
    }
    L.length = 0;
    return OK;
}

//获取元素
Status GetElem(Sqlist L, int i, Book &e)
{
    if(i<1 || i>L.length)
    {
        cout<<"error"<<endl;
        return ERROR;
    }
    e = L.p[i - 1];
    return OK;
}

//获取位置
int LocateElem(Sqlist L, float e)
{
    for (int i = 0; i < L.length; i++)
    {
        if(L.p[i].price == e)
            return i + 1;
    }
    return 0;
}

//插入元素
Status ListInsert(Sqlist &L,int i, Book e)
{
    if(L.length == MAXSIZE)
    {
        cout << "overflow" << endl;
        return ERROR;
    }
        
    if(i<1 || i>L.length + 1)
    {
        cout << "error" << endl;
        return ERROR;
    }
    for (int j = L.length - 1; j >= i - 1; j--)
        L.p[j + 1] = L.p[j];
    L.p[i - 1] = e;
    ++L.length;
    return OK;
}

//删除元素
Status ListDelete(Sqlist &L, int i)
{
    if (i<1 || i>L.length)
    {
        cout << "error" << endl;
        return ERROR;
    }
    for (int j = i; j < L.length; j++)
        L.p[j - 1] = L.p[j];
    --L.length;
    return OK;
}
int main()
{
    cout<<"hello,world"<<endl;
    return 0;
}
