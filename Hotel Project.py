#!/usr/bin/env python
# coding: utf-8

# In[1]:


class RMS:

    def __init__(self,restaurant_name,restaurant_menu):
        self.user_bill=0
        self.menu=restaurant_menu
        self.user_order=''
        self.user_pay=0
        self.rest_name=restaurant_name    
        self.user_rep=''
    def Welcome_user(self):
        #Welcome User
        print("Welcome  To", self.rest_name)
    
    def Display_menu(self):
        #display menu
        print("Menu:")
        for i in self.menu:
            print(i.title(),self.menu[i])
    
    def Take_order(self):
        #Take order
        self.user_order=input('Please  place youre order here:')
    
    def Prepare_order(self):
        #Prepare order
        print('Preparing youre order',self.user_order)
        import time
        time.sleep(1)
        self.user_bill=self.user_bill+self.menu[self.user_order]
    
    def Sereve_order(self):
        #Sereve order
        print('Your order is ready')
        print('Please enjoy your',self.user_order)
    
    def Display_bill(self):
        #Display Bill
        #user_bill=menu[user_order]
        print('Total bill',self.user_bill)
    
    def Verify_payment(self):
        #verify payment
        self.user_pay=int(input('Please pay youre bill here:'))
        
        while self.user_pay<self.user_bill:
            print('Payment unsuccessful')
            self.user_bill=self.user_bill-self.user_pay
            print('please pay reamaining',self.user_bill)
            self.user_pay=int(input('Please pay youre bill here:'))
    
        if self.user_pay>self.user_bill:
            print('Here is youre change',self.user_pay-self.user_bill)
            print('Payment succcessfull')
        else:
            print('Payment succcessfull')
    
    def Thank_user(self):
        #thank user
        print('Thank You For Visiting 3D Cafe')
    
    def Order_process(self):
        self.Display_menu()
        self.Take_order()
        if self.user_order in self.menu:
            self.Prepare_order()
            self.Sereve_order()
            self.user_rep=input('Do you want to order anything else?')
            while self.user_rep=='yes':
                self.Repeat_order()
                self.user_rep=input('Do you want to order anything else?')
            self. Display_bill()
            self.Verify_payment()
            self.Thank_user()
        else:
            print('Invalid Order..!')
            self.Order_process()
    
    def Repeat_order(self):
        self.Display_menu()
        self.Take_order()
        if self.user_order in self.menu:
            self.Prepare_order()
            self.Sereve_order()
        else:
            print('Invalid Order..!')
            self.Repeat_order()


# In[ ]:





# In[3]:


if __name__=='__main__':
    Rm={"Pizza":599,"Burger":150,"Fries":100,"Cold Coffee":199,"Choco":200  ,"Nuggets":349,"Shake":279,"Sandwitch":99,"Lassi":80,"Brownie":149}
    Rn='3D Cafe'

    cafe_rest=RMS(Rn,Rm)

    import tkinter as tk 
    
    #Create Window 
    window=tk.Tk()
    #Changing Title 
    window.title('Pruthvi Patil')
    #Changing size 
    window.geometry('400x400')
    #adding lable
    tk.Label(window,text='Welcome To 3D Cafe',font=('Times New Roman',18)).place(x=100,y=30)
    tk.Button(window,text='Start',command=cafe_rest.Order_process,width=20).place(x=140,y=200)
    # so if u want write this , window want be visible 
    window.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




