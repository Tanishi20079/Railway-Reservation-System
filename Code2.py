#Railway Reservation System-
#have 4 classes- Train, Passenger, Bookings,Payment
#6 list- train_details, passenger_details, bookings, payment, availability, waiting_list
#each train have 120 seats and if all the seats are full then 20 more waitings can happen after 20 waitings no booking will be available

class Main:
  def __init__(self):
    self.__train_details={'234AR':['Rajasthan Express','1:00 PM','6:00 PM','Delhi','Jaipur',349],'583Es':['Bhopal Shatabdi','5:00 AM','12:00 AM','Delhi','Bhopal',990],'45CD5':['Duranta Express','11:30 PM','11:30 AM','Kolkata','Bangalore',1050],'6HA40':['Grand Trunk Express','3:00 PM','3:00 PM in 2 days','Delhi','Chennai',1150],'12KW1':['Lucknow Mail','7:30 PM','3:00 AM','Lucknow','Delhi',650]}      #train(pnr,train_name,start_time,end_time,start_point,destination,fare)
    self.__passenger_details={1:['Akarsh Shrivastava',22,7303764800],2:['Priyanka Ghosh',23,7550113230],3:['Maadhav Sharma',34,7003046144],4:['Nayanika Salgaokar',27,8614469829],5:['Neeta Gaikwad',42,8450056211]}        #passenger_details(id,name,age,phone_no)
    self.__availability={'234AR':117,'583Es':120,'45CD5':120,'6HA40':119,'12KW1':119}  #availability{train_id:vacant_seats}
    self.__bookings=[['234AR',1,1],['234AR',2,2],['234AR',3,3],['6HA40',4,1],['12KW1',5,1]]     #bookings[train_id,passenger_id,seat_number]
    self.__payment={1:349,2:349,3:349,4:1150,5:650}   #payment{passenger_id:fare}
    self.__waiting_list=[]
    self.__admin={'Tanishi':1997,'Drishti':1998}


class Train(Main):
  def __init__(self):
      self.train_no=0
      self.train_name=''
      self.start_time=''
      self.end_time=''
      self.source=''
      self.destination=''
      self.fare=0
      Main.__init__(self)
  #add a new train by admin only
  def __add_train(self):
      self._Main__train_details[self.train_no]=[self.train_name,self.start_time,self.end_time,self.source,self.destination,self.fare]
      self._Main__availability[self.train_no]=120
      print("Train is added")
  #remove a train by admin only
  def __remove_train(self):
      train_no=input("Enter Train no \n")
      flag=0
      for i in self._Main__bookings:
          if train_no in i:
              flag=1
              break
      if flag==0:
          self._Main__train_details.pop(train_no)
          print("Train is removed")
      else:
          print("Cannot remove the train")
          print("Their are some passenger bookings in this train")
  #displaying train details
  def __train_details(self):
      id=input("Enter train no. \n")
      print("*"*6,"Train details","*"*6)
      print("Train no-",id)
      print("Train name-",self._Main__train_details[id][0])
      print("Train start time-",self._Main__train_details[id][1])
      print("Train end time-",self._Main__train_details[id][2])
      print("Train start location-",self._Main__train_details[id][3])
      print("Train destination",self._Main__train_details[id][4])
      print("Train Fare-",self._Main__train_details[id][5])
  #checking the vacancy of the train
  def __check_availability(self,id):
      if id in self._Main__availability.keys():
        print("Availability of train having train no.",id,"is-",self._Main__availability[id])
      else:
        print("Train doesnot exists")
  #updating the details of the train
  def __update_details(self):
      train_no=input("Enter train id \n")
      train_name=input("Enter train name \n")
      start_time=input("Enter start time \n")
      end_time=input("Enter end time \n")
      source=input("Enter start location \n")
      destination=input("Enter destination station \n")
      fare=input("Enter train fare \n")
      self.train_no=train_no
      self.train_name=train_name
      self.start_time=start_time
      self.end_time=end_time
      self.source=source
      self.destination=destination
      self.fare=fare
  

class Passenger(Main):
  def __init__(self):
      self.passenger_id=0
      self.name=''
      self.age=0
      self.phone_no=0
      Main.__init__(self)
  #for adding details of the passenger while booking
  def __add_passenger(self,name,age,phone):
      for i in self._Main__passenger_details.keys():
        pid=i
      self.passenger_id=pid+1
      self.name=name
      self.age=age
      self.phone_no=int(phone)
      self._Main__passenger_details[self.passenger_id]=[self.name,self.age,self.phone_no]
      print("Stored in passenger list")
      return self.passenger_id
    #removing the stored detail of the passenger while cancelling the booking
  def __remove_passenger(self,id):
      self._Main__passenger_details.pop(id)
      print("Removed from passenger list")


class Booking(Passenger):
  def __init__(self,train_id):
      self.train_id=train_id
      self.passenger_id=0
      self.seat_no=0
      Passenger.__init__(self)
  #booking the train
  def __book_train(self,name,age,phone):
      seat_no=0
      pid=self._Passenger__add_passenger(name,age,phone)
      ticket_cost=self._Main__train_details[self.train_id][5]
      n=input("Are you sure for booking? Enter 'y' for yes otherwise 'n'")
      if n=='n':
        return
      Payment._Payment__add_payment(self,pid,ticket_cost)
      if self._Main__availability[self.train_id]>=-20 and self._Main__availability[self.train_id]<0:
          self._Main__bookings.append([self.train_id,pid,9999999])    #asigning deafult seat no. 999999 which means you are in waiting list
          self._Main__waiting_list.append([self.train_id,pid,self._Main__availability[self.train_id]-1])
          self._Main__availability[self.train_id]-=1
          print("Your Booking has been successfully done in Waiting")
          #generating the print of the waiting ticket
          with open('C:\\Users\\hp\\Desktop\\Ticket.txt','w') as file:
              file.write("              -----------------Railway Ticket----------------")
              file.write("\n")
              file.write("*************Your ticket is in Waiting with booking id-")
              file.write(pid)
              file.write("**************\n")
              file.write("Your train number is-")
              file.write(self.train_id)
              file.write("           ")
              file.write("Your seat number is- Not yet given \n")
              file.write("Source station-")
              file.write(self._Main__train_details[self.train_id][3])
              file.write("              Destination station-")
              file.write(self._Main__train_details[self.train_id][4])
              file.write("\n")
              file.write("Start time-")
              file.write(self._Main__train_details[self.train_id][1])
              file.write("               Reaching Time-")
              file.write(self._Main__train_details[self.train_id][2])
              file.write("\n")
              file.write("\n")
              file.write("Passenger Details-")
              file.write("\n")
              file.write("Passenger Name-")
              file.write(name)
              file.write("      Age-")
              file.write(str(age))
              file.write("       Phone Number-")
              file.write(str(phone))
              file.write("\n")
              file.write("Paid-")
              file.write(str(ticket_cost))
              file.write("\n")
              file.write("                 ********Happy Journey*********")
              file.write("\n")
              file.write("*"*77)
          file.close()
      else:
          for i in self._Main__bookings:
              if i[0]==self.train_id:
                  seat_no=max(i[2],seat_no)
          self._Main__bookings.append([self.train_id,pid,seat_no+1])
          self._Main__availability[self.train_id]-=1
          print("Your Booking has been successfully done")
          #generating the print of the Confirmed ticket
          with open('C:\\Users\\hp\\Desktop\\Ticket.txt','w') as file:
              file.write("              -----------------Railway Ticket----------------")
              file.write("\n")
              file.write("*************Your booking has been Confirmed with booking id-")
              file.write(str(pid))
              file.write("**************\n")
              file.write("Your train number is-")
              file.write(self.train_id)
              file.write("           ")
              file.write("Your seat number is-")
              file.write(str(seat_no+1))
              file.write("\n")
              file.write("Source station-")
              file.write(self._Main__train_details[self.train_id][3])
              file.write("              Destination station-")
              file.write(self._Main__train_details[self.train_id][4])
              file.write("\n")
              file.write("Start time-")
              file.write(self._Main__train_details[self.train_id][1])
              file.write("               Reaching Time-")
              file.write(self._Main__train_details[self.train_id][2])
              file.write("\n")
              file.write("\n")
              file.write("Passenger Details-")
              file.write("\n")
              file.write("Passenger Name-")
              file.write(name)
              file.write("      Age-")
              file.write(str(age))
              file.write("       Phone Number-")
              file.write(str(phone))
              file.write("\n")
              file.write("Paid-")
              file.write(str(ticket_cost))
              file.write("\n")
              file.write("                 ********Happy Journey*********")
              file.write("\n")
              file.write("*"*77)
          file.close()
      print("Ticket has been generated on your system")
      print("Your passenger id is-",pid)
      print("-------------Happy Journey------------\n")
        
  #cancelling the train        
  def __cancel_train(self,pid):
      yn=input("Are you sure for cancelling the booking? Enter 'y' for yes otherwise 'n' \n")
      if yn=='y':
        train_id=''
        for i in self._Main__bookings:
          if i[1]==int(pid):
              train_id=i[0] #train id
        self._Passenger__remove_passenger(pid)
        self._Main__availability[train_id]+=1
        Payment._Payment__return_payment(self,pid)
        for i in range(len(self._Main__bookings)):
            if self._Main__bookings[i][1]==int(pid):
               self._Main__bookings.pop(i)
               break
              
        print("Your booking has been successfully cancelled")

  #for checking the booking details
  def __booking_info(self,pid):
      info=[]
      for i in self._Main__bookings:
          if i[1]==int(pid):
              info.append(i[0]) #train id
              info.append(i[2]) #seat no
              #print(info)
              break
      #print(self._Main__train_details[info[0]])
      info.append(self._Main__train_details[info[0]][0])#train name
      info.append(self._Main__passenger_details[int(pid)][0])
      print("Hey",info[3],"your booking info is-")
      print("You have booked seat number-",info[1],"of train",info[2],"having train id",info[0])
  

class Payment(Booking):
  def __init__(self):
    Booking.__init__(self)

  #call for the payment
  def __add_payment(self,pid,ticket_cost):
      self._Main__payment[pid]=ticket_cost
      print("Payment successfully done")
      return
  #returning back the amount after cancelling the booking
  def __return_payment(self,pid):
      self._Main__payment.pop(pid)
      print("Payment has returned back to your account")
      return 
  

main=Main()
print("*"*8,"Welcome to Railway Reservation System","*"*8)
while True:
  p=int(input("Select your option \n 1. Login as Admin person \n 2. You are a user \n 3. Exit the system \n"))
  if p==1:
     print("*"*8,"Write Login details","*"*8)
     name=input("Enter your name \n")
     password=int(input("Enter the password \n"))
     if main._Main__admin[name]==password and name in main._Main__admin.keys():
       while True:
         #print(train_details)
         print("Select option from menu-")
         s1='1. Want to add a train'
         s2='2. Want to remove a train'
         s4='3. Want to exit'
         print(s1,s2,s4,sep='\n')
         s=int(input())
         train=Train()
         if s==1:
            train._Train__update_details()
            train._Train__add_train()
         elif s==2:
            train._Train__remove_train()
         else:
          # print("invalid option")
          
            break
     else:
         print("Invalid option")
  elif p==2:
    while True:
      print("Select option from the menu-")
      s1='1. Want information about train'
      s2='2. Checking Availability of a train'
      s3='3. Want to book a seat in a train'
      s4='4. Want to cancel the booking'
      s6='5. Check Booking Info'
      s5='6. Exit the menu'
      print(s1,s2,s3,s4,s6,s5,sep='\n')
      s=int(input())
      if s==1:
        train=Train()
        train._Train__train_details()
      elif s==2:
        train=Train()
        n=input('Enter train number\n')
        train._Train__check_availability(n)
      elif s==3:
        train_id=input("Enter train id \n")
        if train_id not in main._Main__availability.keys():
           print("Invalid train number")
           break
        elif main._Main__availability[train_id]==-21:
           print("No seat available")
           break
        elif main._Main__availability[train_id]>=-20 and main._Main__availability[train_id]<0:
           print("All seats are booked. You will be added in waiting list")
           yn=input("Wanted to be in waiting list enter 'y' otherwise enter 'n' \n")
           if yn=='n':
               break              
        name=input("Enter passenger name \n")
        age=int(input("Enter passenger age \n"))
        phone=input("Enter passenger phone number of 10 digits \n")
        if len(phone)!=10:
          print("*"*6,"ALERT","*"*6)
          print("Invalid phone number")
          phone=input("Enter valid phone number of 10 digits \n")
          if len(phone)!=10:
             print("Exiting the system")
             break
        book=Booking(train_id)
        book._Booking__book_train(name,age,phone)
      elif s==4:
        book=Booking(None)
        pid=int(input("Enter your passenger id"))
        book._Booking__cancel_train(pid)
      elif s==5:
        book=Booking(None)
        pid=input("Enter passenger id \n")
        book._Booking__booking_info(pid)
      else:
        break
  else:
    print("Exiting the system")
    break
    

