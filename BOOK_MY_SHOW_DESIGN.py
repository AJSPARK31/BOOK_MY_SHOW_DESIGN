#!/usr/bin/env python
# coding: utf-8

# In[115]:


#design of book my show app
#1 you have register/login
#  if register : save the users details
#  if logins verify the user name and password
#2 
"""
When I run the main.py file of your Program. It should show me this kind of interaction.
Ask the number of rows and seats per row and than show these 4 options until I choose Exit:
1.Show the seats
2. Buy a Ticket
3. Statistics
4. Show booked Tickets User Info
0. Exit


1.Show the seats
A cinema Hall with 7 Rows and 8 seats per Row should look like this.
Notice that S shows the Vacant Seat here and the counting 
in the beginning of the row and column is just for reference to the seat number. 
Reserved seat will show a B. Like here Seat at (Row No 3 ,Column 5th) is Booked.
Hint: Use nested for loops to show the cinema like this.


2. Buy a Ticket
When I buy a Ticket It should ask me row number and column number for the ticket I am booking.On the basis of the Rules it should show me the Price for that seat and ask If I want to book.
If I choose Yes, it should take details of Name,Gender,Age and Phone No.
Think about a data structure where you can save it(list ? set? Or a dict?)
Finally It should print Booked Successfully.

3. Statistics
When I choose the 3rd option for statistics.
It should show me the following things:-
1 Number of Purchased Tickets
2 Percentage of Tickets booked
3 Current Income
4 Total Income
(Please follow the rules for calculating price for each seat as shown in the next slide) 

4. Show booked Tickets User Info
When I choose the 4th option:
It should ask me the row and col number.
If that row,col is booked show the Name,gender,age,Ticket Price and Phone No


Expected Results.

1 The whole code should be modular by using proper classes and functions.
2 Using of OOP is compulsory







"""

rows= int(input("Enter number the rows:"))
columns=int(input("Enter number the columns:"))
m1=Cinema(rows,columns)
while True:
    user_input=int(input("Select options from given below:\n1. Show me the seats \n2. Buy a Ticket \n3. Statistic \n4. Show Booked Tickets user info \n0. Exit\n"))
    if user_input==1:
        m1.show_the_seats()
    elif user_input==2:
        m1.book_tickets()
    elif user_input==3:
        m1.statistics()
    elif user_input==4:
        row=int(input("Enter the row "))
        col=int(input("Enter the column "))
        m1.show_user_details(row,col)
        
        
    elif user_input==0:
        print("You have selected the Exit")
        break
    else:
        print("Option not available please choose options from below")
    


# In[114]:


class Cinema():
    def __init__(self,rows,columns):
        self.rows=rows
        self.columns=columns
        self.Booking={}
#         self.ticket_booked=0
        
    def is_booked(self,row,column):
        Ticket_no=int(str(row)+str(column))
        if Ticket_no in self.Booking:
            return True
        else:
            False
            
        
    def show_the_seats(self):
        print("Cinema:")
        for rows in range(0,self.rows+1):
            for columns in range(0,self.columns+1):
                if rows==0:
                    if columns==0:
                        print(" ",end=" ")
                    else:
                        print(columns,end=" ")
                else:
                    
                    if columns==0:
                        print()
                        print(rows,end=" ")
                    else:
                        if self.is_booked(rows,columns):
                            print("B",end=" ")
                        else:
                            print("S",end=" ")
        print()
        
        
    def book_tickets(self):
        customer_info={}
        print("Ticket Counter")
        Booking_row=int(input("Enter the row preference : "))
        Booking_column=int(input("Enter the column preference : "))
        
        if self.rows*self.columns<=60:
            price=10
            print("Price of the ticket is :" ,price , "dollars")
            m1.booking()
        else:
            if self.rows%2==0:
                if Booking_row<=self.rows/2:
                    price=8
                else:
                    price=10
            else:
                if Booking_row<=(self.rows-1)/2:
                    price=8
                else:
                    price=10
        print("Price of the ticket is :" ,price,"dollars")
        Ticket_no=int(str(Booking_row)+str(Booking_column))
        print("Do you want to book the ticket\n1. Yes \n2. No")
        user_response=int(input())   
        if user_response==1:
            print("We are booking the ticket ")
            customer_name=input("Enter your name ")
            customer_gender=input("Enter your gender ")
            customer_age=int(input("Enter your age " ))
            customer_phone_no=int(input("Enter your phone No "))
            customer_info["Name"]=customer_name
            customer_info["Gender"]=customer_gender
            customer_info["Age"]=customer_age
            customer_info["Phone no"]=customer_phone_no
            customer_info["Price"]=price
            self.Booking[Ticket_no]=customer_info
#             self.ticket_booked+=1
            print("Ticket Booked Successfully")
        else:
            print("Booking Cancelled")
    
    
    def show_user_details(self,row,col):
        Ticket_no=int(str(row)+str(col))
        if Ticket_no in self.Booking:
            info_dict = self.Booking[Ticket_no]
            print("Here is the deatils: ")
            print("Name: ",info_dict['Name'])
            print("Age: ",info_dict['Gender'])
            print("Gender: ",info_dict['Age'])
            print("Mobile number: ",info_dict['Phone no'])
            print("Ticket book for : $",info_dict['Price'])
        else:
            print(f"Seat for row: {row} and column: {col} is not booked yet")
    
            
            
            
            
            
            
    def statistics(self):
        booked_ticket=len(self.Booking)
        print("Number of purchased ticket : ", booked_ticket )
        total_ticket=self.rows*self.columns
        percentage_of_ticket_booked=round((booked_ticket/total_ticket)*100,2)
        print("Percentage of booked ticket",percentage_of_ticket_booked)
        current_income=0
        for Ticket_no in self.Booking:
            info_dict=m1.Booking[Ticket_no]
            price=info_dict["price"]
            current_income+=price
        print("Current income ",current_income)
        if total_ticket<=60:
            total_income=10*total_ticket
        else:
            row_factor=self.rows//2
            front_row_tickets=row_factor*self.columns
            back_row_tickets=(self.rows-row_factor)*self.columns
            total_income=front_row_tickets*8+back_row_tickets*10
        print("Total_income",total_income)
            
        


# m1.book_tickets()


# In[113]:


m1.Booking


# In[ ]:




