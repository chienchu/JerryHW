
# coding: utf-8

# In[ ]:


first = int(input('請輸入數字:'))
c = input('請輸入符號:')
second = int(input('請輸入數字:'))
def calculator(a,b,c):
    if c=="+":
        return a+b
    elif c=="-":
        return a-b
    elif c=="*":
        return a*b
    elif c=="/":
        return a/b
calculator(first,second,c)

