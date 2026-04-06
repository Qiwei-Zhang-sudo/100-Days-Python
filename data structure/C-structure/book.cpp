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

int main()
{
    cout<<"hello,world"<<endl;
    return 0;
}
