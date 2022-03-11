import mysql.connector as sq
import matplotlib.pyplot as plt
con=sq.connect(host='localhost',user='root',passwd='122004')
cur=con.cursor()
cur.execute('create database if not exists a76')
cur.execute('use a75')
cur.execute('create table if not exists places (pid varchar(10) primary key,pname char(25) not null,category char(25),days int(15))')
print(' TABLE NAME: PLACES')

cur.execute('insert into places values("P001","Yercaud","Hill station",5)')
cur.execute('insert into places values("P002","Kodaikanal","Hill station",4)')
cur.execute('insert into places values("P003","Ooty","Hill station",6)')
cur.execute('insert into places values("P004","Kumbakonam","Temple town",5)')
cur.execute('insert into places values("P005","Mahabalipuram","Historic town",4)')
cur.execute('insert into places values("P006","Rameshwaram","Temple town",7)')
cur.execute('insert into places values("P007","Chennai","Capital city",5)')
cur.execute('insert into places values("P008","Auroville","Peace town",4)')
cur.execute('insert into places values("P009","Kanyakumari","View town",7)')
cur.execute('insert into places values("P010","Madurai","Temple town",6)')
cur.execute('insert into places values("P011","Tuticorin","Pearl city",5)')
cur.execute('insert into places values("P012","Thiruvannamalai","Temple town",5)')
cur.execute('insert into places values("P013","Thanjavur","Heritage centre",3)')
cur.execute('insert into places values("P014","Chidambaram","Temple town",5)')
con.commit()
cur.execute('select * from places')
d=cur.fetchall()
for i in d:
     print(i)

cur.execute('create table if not exists hotels (hid varchar(10) primary key,hname char(25) not null,address varchar(50),phno varchar(10),email varchar(50),rating varchar(15))')
print(' TABLE NAME: HOTELS')
cur.execute('insert into hotels values("CV007","Clouds Valley","2/B Garden street, Salem,600107",9400343687,"mail@cloudsvalley.com","4 star")')
cur.execute('insert into hotels values("CN001","Casa Montana","7/19,Norwood street,Dindigul,600092",0486523264,"mail@casamountana.com","4 star")')
cur.execute('insert into hotels values("EG005","Elysium garden resort","57/16,Joshi Gardens,Coimbatore,600047",9946824665,"info@elysiumgarden.com","3 star")')
cur.execute('insert into hotels values("KU007","Sana Resorts","55/32,Pillayar street,Kumbakonam,600017",7563825688,"svresorts@gmail.com","3 star")')
cur.execute('insert into hotels values("LV007","Lorenz villa","18/4,Salve street,Mahabalipuram,600026",4653782910,"lorenz@villa.com","4 star")')
cur.execute('insert into hotels values("JR008","Jiwan residency","74/17,Kalam street,Rameshwaram,600012",4963172810,"jiwan@gmail.com","4 star")')
cur.execute('insert into hotels values("ITC01","ITC Grand Chola","23/10,MG street,Guindy,Chennai,600002",1029384756,"itcgc@gmail.com","6 star")')
cur.execute('insert into hotels values("LT009","La Taara","10/12,Pondy street,Pondicherry,600345",9840115567,"lataara@gmail.com","4.5 star")')
cur.execute('insert into hotels values("SR003","Sparsa Resort","15/30,Skyark street,Kanyakumari,600890",9070836369,"sparsa@gmail.com","5 star")')
cur.execute('insert into hotels values("FR006","Fortune Residency","67/45,Pheonx street,Madurai,601015",9940501462,"fr@gmail.com","3.5 star")')
cur.execute('insert into hotels values("SV072","Sea Villa","23/4,Samudram street,Tuticorin,600423",9880045625,"seavilla@gmail.com","4.5 star")')
cur.execute('insert into hotels values("IR089","Iswaran Resorts","67/75,Anamalaiyar street,Thiruvanamalai,607080",8940501462,"iswaran.in","5.5 star")')
cur.execute('insert into hotels values("SR90","Sastra Resorts","23/14,Tarangini street,Thanjavur,630423",9876543211,"sr@gmail.com","5 star")')
cur.execute('insert into hotels values("HCR02","HoneyComb Resorts","55/11,Natrajan street,Chidambaram,600425",9846745625,"hcr@gmail.com","5 star")')
con.commit()
cur.execute('select * from hotels')
d=cur.fetchall()
for i in d:
     print(i)


cur.execute('create table if not exists rooms (rid varchar(25) primary key,type char(50) not null,facilities char(50),tariff int(10))')
print(' TABLE NAME: ROOMS')

cur.execute('insert into rooms values("R101","Deluxe room,valley view room","restaurant,free wifi, lockers",5750)')
cur.execute('insert into rooms values("R102","casa mountana suite,premium club, deluxe double","restaurant,free wifi, parking",11000)')
cur.execute('insert into rooms values("R103","executive room,garden view cottage","cable tv,tea/coffee maker,wifi,view",7400 )')
cur.execute('insert into rooms values("R104","Deluxe room,temple view cottage","room service,parking,free wifi",6250)')
cur.execute('insert into rooms values("R105","Double Deluxe room,sea view villa","dining,recreation,airport access",9000)')
cur.execute('insert into rooms values("R106","Mini suite room,temple-view room","free wifi,free breakfast,ac room",1200)')
cur.execute('insert into rooms values("R107","King size room,premium club","spa,massage center",4000)')
cur.execute('insert into rooms values("R108","Junior suite room,sea view room","gym,parlor,free wifi",3500)')
cur.execute('insert into rooms values("R109","Terrace suite,nature view setup room","car parking,complimentary breakfast",5600)')
cur.execute('insert into rooms values("R110","Deluxe suite,temple view room","free wifi,lockers,free room service",3700)')
cur.execute('insert into rooms values("R111","Executive rooms","meeting rooms,free wifi,bar",8900)')
cur.execute('insert into rooms values("R112","Royal suite,sea view room","free wifi,parking facilities",23000)')
cur.execute('insert into rooms values("R113","Double deluxe room,temple view rooms","free wifi,parking,lockers",2000)')
cur.execute('insert into rooms values("R114","Penthouse suite,magnificent view","fine dining,health club,steam bath",7900)')
con.commit()
cur.execute('select * from rooms')
d=cur.fetchall()
for i in d:
     print(i)

cur.execute('create table if not exists bill(billid int(10) primary key,destination_chosen varchar(50),hotel_chosen varchar(50),room_chosen varchar(50),tariff int(50))')



ans='y'
while ans=='y':
     ch=input('enter your login- admin or user')
     if ch=='admin':
          pw=input('enter password')
          if pw=='0419':
               print('$ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $')
               print('$                                                                                             $')
               print('$                                  WELCOME TO TOURS AND TRAVELS                               $')
               print('$                                                                                             $')
               print('$ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $')
               print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
               print('|                        1. Add place                         |')
               print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
               print('|                        2. Add hotel                         |')
               print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  ')
               print('|                        3.Add room                           |')
               print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
               print('|                        4.Remove place                       |')
               print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
               print('|                        5.Remove hotel                       |')
               print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  ')
               print('|                        6.Remove room                        |')
               print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
               print('|                        7.Exit                               |')
               print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
               x=int(input('enter your choice'))
               if x==1:
                    print('You are going to add a place')
                    pid=input('enter pid')
                    pname=input('enter pname')
                    cat=input('enter category')
                    day=input('enter days')
                    cur.execute('insert into places values("{}","{}","{}","{}")'.format (pid,pname,cat,day))
               con.commit()       
               if x==2:
                     print('You are going to add a hotel')
                     hid=input('enter hotel id')
                     hname=input('enter hotel name')
                     add=input('enter address')
                     ph=input('enter phone number')
                     em=input('enter email id')
                     rat=input('enter rating of the hotel')
                     cur.execute('insert into hotels values("{}","{}","{}","{}","{}","{}")'.format (hid,hname,add,ph,em,rat))
               con.commit()
               if x==3:
                     print('You are going to add a room')
                     rid=input('enter room id')
                     typ=input('enter room type')
                     fac=input('enter room facilities available')
                     tar=input('enter room tariff')
                     cur.execute('insert into rooms values("{}","{}","{}","{}")'.format (rid,typ,fac,tar))
               con.commit()
               if x==4:
                    print('You are going to remove a place')
                    p=input('enter place to be removed')
                    trial=('select * from places where pname=%s')
                    cur.execute(trial,[(p)])
                    res=cur.fetchall()
                    if res:
                         for i in res:
                              x=('delete from places where pname=%s')
                              cur.execute(x,(p,))
                              con.commit()
                              print('place deleted successfully')
                    else:
                         print('place does not exist')
               if x==5:
                    print('You are going to remove a hotel')
                    h=input('enter hotel id to be removed')
                    check=('select * from hotels where hid=%s')
                    cur.execute(check,[(h)])
                    res=cur.fetchall()
                    if res:
                         for i in res:
                              x=('delete from hotels where hid=%s')
                              cur.execute(x,(h,))
                              con.commit()
                              print('hotel deleted successfully')
                    else:
                         print('hotel does not exist')
               if x==6:
                      print('You are going to remove a room')
                      r=input('enter room id to be removed')
                      trial=('select * from rooms where rid=%s')
                      cur.execute(trial,[(r)])
                      res=cur.fetchall()
                      if res:
                           for i in res:
                                x=('delete from rooms where rid=%s')
                                cur.execute(x,(r,))
                                con.commit()
                                print('room deleted successfully')
                      else:
                           print('room does not exist')
               if x==7:
                    print('you are going to exit the program')
                    print('exit')
               else:
                    print('invalid choice')
          else:
              print('Incorrect password')

     if ch=='user':
           print('$ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $')
           print('$                                                                                              ')
           print('$                                  WELCOME TO TOURS AND TRAVELS                               $')
           print('$                                         Come,stay,and enjoy your day                        $')
           print('$                                                                                             $')
           print('$ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $')               
           print('Hello Customer....You can customise by selecing the following options')
           print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  ')
           print('|                        1. Choose your destination                           |')
           print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  ')
           print('|                        2. Choose your dream Inn                             |')
           print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  ')
           print('|                        3.Choose your comfort zone                           |')
           print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  ')
           print('|                        4. Hotel reviews                                     |')
           print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  ')
           print('|                        5. Category reviews                                  |')
           print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  ')
           print('|                        6. People interest                                   |')
           print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  ')
           print('|                        7.Exit                                               |')
           print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  ')
           y=int(input('enter your choice'))
           bid=random.randint(0,9)
           if y==1:
               p=input('enter destination to be reached')
               trial=('select * from places where pname=%s')
               cur.execute(trial,[(p)])
               res=cur.fetchall()
               if res.rowcount==0:
                         print('Hurray!.....Your Destination is reachable')
               else:
                    print('Alas!......Your Destination is not reachable')
                    cur.execute('insert into bill values(bid,p,null,null,0')
           elif y==2:
               h=input('enter your Dream Inn')
               nd=int(input('enter number of days of stay'))
               trial=('select * from hotels where hname=%s')
               cur.execute(trial,[(h)])
               res=cur.fetchall()
               if res.rowcount==0:
                         print('Alas!......Your Dream Inn is not available')
               else:
                    print('Alas!......Your Dream Inn is available')
                    cur.execute('update bill set hname=h where billid=bid')
           elif y==3:
               r=input('enter your best-suited accomodation')
               trial=('select * from rooms where type=%s')
               cur.execute(trial,[(r)])
               res=cur.fetchall()
               if res.rowcount==0:
                         print('Alas!......Your Dream Inn is not available')
               else:
                    print('Alas!......Your Dream Inn is available')
               '''if res:
                    for i in res:
                         print('Hurray!.....Your room is available')
               else:
                    print('Oo No!......Your room is not available')'''
                    cur.execute('update bill set type=r where billid=bid')
           if y==4:
                print('You are going to view the hotel wise report')
                x=['Clouds Valley','Casa Montana','Elysium garden resort','Sana Resorts','Lorenz villa','Jiwan Residency','ITC Grand Chola','La Taara','Sparsa resort','Fortune residency','Sea villa','Iswaran resorts','Sastra resorts','Honeycomb resorts']
                y=[20,35,57,49,68,25,54,43,31,77,89,45,30,98]
                plt.bar(x,y,color=['r','b','k','m','c'])
                plt.xlabel('NAME OF THE HOTELS')
                plt.ylabel('RATING OF THE HOTELS')
                plt.title('HOTEL WISE REPORT')
                plt.show()
           if y==5:
                print('You are going to view the category wise report')
                x=['Hill station','Temple town','Historic town','Capital city','Peace town','View town','Pearl city','Heritage centre']
                y=[8,9,7,5,10,7,6,8]
                plt.bar(x,y,color=['orange','pink','violet','brown','yellow'])
                plt.xlabel('CATEGORY OF THE PLACES')
                plt.ylabel('RATINGS')
                plt.title('CATEGORY WISE REPORT')
                plt.show()
           if y==6:
                print('You are goimg to view customer\'s review')
                x=['Pretty good','Good','Satisfied','Bad','Very bad']
                y=[4.7,3.8,4.5,2.3,0.4]
                plt.bar(x,y,color=['m','b','orange','k','r'])
                plt.xlabel('REVIEWS OF THE CUSTOMER')
                plt.ylabel('RATINGS GIVEN BY THE CUSTOMER')
                plt.title('CUSTOMER"S REVIEW')
                plt.show()
           if y==7:
                    print('you are going to exit this website')
                    print('exit')
     else:
          print('invalid choice')

                
                
          

        
     
