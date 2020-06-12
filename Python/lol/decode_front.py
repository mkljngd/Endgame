from tkinter import *
import string

msg=''
d={}

def init(base):
    l=[str(x) for x in range(min(base,10))]
    l=''.join(l)
    if base>10:
        l+=string.ascii_uppercase[0:base-10]
    count=0
    for i in l:
        d[i]=count;count+=1
    return d

def decode(n,base):
    d=init(base)
    n=n[::-1]
    sum=0
    for i in range(len(n)):
        sum+=int(base**i)*int(d[n[i]])
    return sum

def lol(msg,base):
    l=msg.split(',')
    op=[decode(x,base) for x in l]
    print(op)
    op1=[chr(int(x)) for x in op]
    print(op1)
    op2=''.join(op1)
    print(op2)
    front_end.decode_text.insert(END,op2)



def front_end(master):
    title_label=Label(master,text="Prototype 1.0",font=("Arial",40))
    front_end.decode_text=Text(master,height=5)
    encode_text=Text(master,height=5)
    encode_text.insert(END,'Paste your encrypted message in this box')
    #print('message=',message)
    #decode_button=Button(master,text="Decode",command=lambda:decode(message.strip(),30))
    decode_button=Button(master,text="Decode",command=lambda:lol(encode_text.get(1.0,END).strip(),30))
    r=0;c=0
    title_label.grid(row=r,column=c);r+=1;
    encode_text.grid(row=r,column=c);r+=1;
    front_end.decode_text.grid(row=r,column=c);r+=1;
    decode_button.grid(row=r,column=c);r+=1



root=Tk()

front_end(root)

root.mainloop()
