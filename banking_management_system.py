import mysql.connector
cnx=mysql.connector.connect(user='root', password='server', database='Bank')
cur=cnx.cursor(buffered=True)
########################################################################################################################


try:
    cur.execute('create table accounts(Account_num int(20),Name varchar(20),Mobile_No int(20),Email_ID varchar(20),Residence_address varchar(20),City varchar(20),Country varchar(20),Balance int(20))')
except:
    pass
try:
    cur.execute('create table transactions(Account_number int(20), Transactions_left_today int(20),Current_Transaction_Limit int(20), Foreign Key(Account_number) references ACCOUNTS(Account_num)')
except:
    pass
def menu():
    print('#'*170)
    print('        --MAIN MENU--'.center(110))
    print('(1) VIEW USER')
    print('    -- Sort With Respect To Account Number')
    print('    -- Sort With Respect To Name')
    print('    -- Sort With Respect To Balance')
    print('(2) ADD USER')#CHANGE TO 1
    print('(3) SEARCH FOR AN ACCOUNT')
    print('(4) MODIFY ACCOUNT DETAILS')
    print('(5) MAKE TRANSACTIONS')
    print('    -- Credit Into An Account')
    print('    -- Debit Into An Account')
    print('(6) DELETE USER')
    print('(7) QUIT')
    print("                                      # CHOOSE AND ENTER A NUMBER BETWEEN 1 AND 7 #")
    print('#'*170)


def sortwithaccount():
    cur.execute("select * from Accounts order by Account_num")
    print('-'*170)
    Head="%20s %20s %20s %20s %20s %15s %18s %18s"
    print(Head%("ACCOUNT_NO,", "NAME", "MOBILE_NO","EMAIL_ID", "RESIDENCE_AREA", "CITY", "COUNTRY", "BALANCE"))
    print('-'*170)
    for i in cur:
        for j in i:
            print("%20s" % j, end='')
        print()
    print('-'*170)
def sortwithname():
    cur.execute('select * from accounts order by Name')
    print('-'*170)
    Head = "%20s %20s %20s %20s %20s %15s %18s %18s"
    print(Head % ("ACCOUNT_NO,", "NAME", "MOBILE_NO", "EMAIL_ID", "RESIDENCE_AREA", "CITY", "COUNTRY", "BALANCE"))
    print('-' * 170)
    for i in cur:
        for j in i:
            print("%20s" % j, end='')
        print()
    print('-' * 170)
def sortwithbalance():
    cur.execute('select * from accounts order by Balance')
    print('-'*170)
    Head = "%20s %20s %20s %20s %20s %15s %18s %18s"
    print(Head % ("ACCOUNT_NO,", "NAME", "MOBILE_NO", "EMAIL_ID", "RESIDENCE_AREA", "CITY", "COUNTRY", "BALANCE"))
    print('-' * 170)
    for i in cur:
        for j in i:
            print("%20s" % j, end='')
        print()
    print('-' * 170)

def Insertval():
    inp='y'
    while inp=='y':
        Acc=int(input('Enter Account Number: '))
        name=input('Enter Name: ')
        mobile=int(input('Enter Your Mobile Number: '))
        Email_id=input("Enter Your Email Id: ")
        Residence=input("Enter Your Residence Area(in less than 15 characters)")
        city=input('Enter The City Name')
        Country=input('Enter The Country Name')
        Balance=int(input('Enter The balance amount'))
        stm="insert into accounts values(%s,%s,%s,%s,%s,%s,%s,%s)"
        noni=[Acc, name, mobile, Email_id, Residence, city, Country, Balance]
        cur.execute(stm,noni)
        cnx.commit()
        print("ENTRY ADDED!")
        inp=input('Do You Want To Enter Another Entry?(y/n):')
        if inp=='n' or inp=='N':
            break

def displaywhole():
    try:
        cur.execute('select * from accounts')
        print('#' * 170)
        Head = "%20s %20s %20s %20s %20s %15s %18s %18s"
        print(Head % ("ACCOUNT_NO", "NAME", "MOBILE_NO", "EMAIL_ID", "RESIDENCE_AREA", "CITY", "COUNTRY", "BALANCE"))
        print('#' * 170)
        for i in cur:
            for j in i:
                print("%20s" % j, end='')
            print()
        print('#' * 170)
    except:
        print('EMPTY TABLE')

def searchit():
    try:
        cur.execute('select * from accounts')
        lj=int(input('ENTER THE ACCOUNT NUMBER YOU WANT TO SEARCH FOR: '))
        for i in cur:
            if i[0]==lj:
                print('FOUND!')
                print('#'*170)
                Head = "%20s %20s %20s %20s %20s %15s %18s %18s"
                print(Head % ("ACCOUNT_NO,", "NAME", "MOBILE_NO", "EMAIL_ID", "RESIDENCE_AREA", "CITY", "COUNTRY", "BALANCE"))
                print('#' * 170)
                for j in i:
                    print("%20s" % j, end='')
                print()
                print('#' * 170)
                break
        else:
            print('RECORD NOT FOUND!')
    except:
        print('TABLE DOES NOT EXIST')
def updateit():
        cur.execute('select * from accounts')
        jk=int(input('ENTER THE ACCOUNT NUMBER YOU WANT TO CHANGE DETAILS FOR: '))
        for i in cur:
            i=list(i)
            if i[0]==jk:
                inp=input('DO YOU WANT TO CHANGE NAME?(y/n): ')
                if inp=='y' or inp=='Y':
                    i[1]=input('ENTER THE NEW NAME: ')
                inp = input('DO YOU WANT TO CHANGE MOBILE NUMBER?(y/n): ')
                if inp=='y' or inp=='Y':
                    i[2]=int(input("ENTER THE NEW MOBILE NUMBER: "))
                inp = input('DO YOU WANT TO CHANGE EMAIL_ID?(y/n): ')
                if inp=='y' or inp=='Y':
                    i[3]=input('ENTER THE NEW EMAIL ID: ')
                inp = input('DO YOU WANT TO CHANGE RESIDENCE AREA?(y/n): ')
                if inp=='y' or inp=='Y':
                    i[4]=input('ENTER THE NEW RESIDENCE: ')
                inp = input('DO YOU WANT TO CHANGE CITY?(y/n): ')
                if inp=='y' or inp=='Y':
                    i[5]=input('ENTER THE CITY NAME: ')
                inp=input('DO YOU WANT TO CHANGE COUNTRY?(y/n): ')
                if inp=='y' or inp=='Y':
                    i[6]=input("ENTER THE COUNTRY NAME: ")
                vcv='update accounts set name=%s, Mobile_No=%s, Email_id=%s, Residence_address=%s, city=%s, country=%s where account_num=%s'
                dsf=[i[1], i[2], i[3], i[4], i[5], i[6], i[0]]
                cur.execute(vcv,dsf)
                cnx.commit()
                print('Your Details Have been Updated!')
                break
        else:
            print('NO SUCH ACCOUNT!')


def displaysortmenu():
    print('*'*170)
    print("            1. SORT WITH RESPECT TO ACCOUNT NUMBER")
    print("            2. SORT WITH RESPECT TO NAME")
    print("            3. SORT WITH RESPECT TO BALANCE")
    print("            4. GO BACK TO MAIN MENU")
    print('*'*170)
def displaytransactionmenu():
    print('*'*170)
    print("            1. CREDIT(ADD MONEY TO ACCOUNT)")
    print("            2. DEBIT(TAKE MONEY OUT FROM ACCOUNT)")
    print("            3. GO BACK TO MAIN MENU")
    print('*'*170)

def deleterecord():
    try:
        cur.execute('select * from accounts')
        lel=int(input('Enter the account number of the account you want to delete: '))
        for i in cur:
            i=list(i)
            if i[0]==lel:
                cur.execute("delete from accounts where Account_num=%s"%(lel,))
                cnx.commit()
                print("ACCOUNT DELETED!")
                break
        else:
            print("NO SUCH RECORD FOUND!")
    except:
        print("TABLE DOES NOT EXIST")

def debitit():
    cur.execute("select * from accounts")
    yo=int(input("ENTER THE ACCOUNT NUMBER FOR ACCOUNT TO BE DEBITED: "))
    for i in cur:
        i=list(i)
        if i[0]==yo:
            print("THE BALANCE IN YOUR ACCOUNT IS:", i[7])
            cur.execute("select balance from accounts ")
            ko=int(input("ENTER THE AMOUNT TO BE DEBITED: "))
            if (i[7]-ko)>2500:
                if ko<i[7]:
                    a="update accounts set balance=balance-%s where account_num=%s"
                    b=(ko,yo)
                    cur.execute(a,b)
                    cnx.commit()
                    print("AMOUNT DEBITED!")
                    break
                else:
                    print('NOT ENOUGH BALANCE!')
                    break
            else:
                print("YOU HAVE TO LEAVE ATLEAST 2500 IN THE ACCOUNT!")
                break
    else:
        print('NO RECORD FOUND!')
def credit():
    cur.execute("select * from accounts")
    lp=int(input("ENTER THE ACCOUNT TO BE CREDITED TO: "))
    for i in cur:
        i=list(i)
        if i[0]==lp:
            nb=int(input("ENTER THE AMOUNT YOU WANT TO CREDIT: "))
            a='update accounts set balance=balance+%s where account_num=%s'
            b=[nb,lp]
            cur.execute(a,b)
            cnx.commit()
            print("AMOUNT CREDITED!")
            break
    else:
        print("NO RECORD FOUND!")


########################################################################################################################

#EXECUTION BLOCK

print("@"*170)
print("                                   BANKING MANAGEMENT SYSTEM")
print("                                     MADE BY- SAKSHAM DUA")
print("@"*170)

while True:
    menu()
    get=int(input("ENTER YOUR CHOICE: "))
    if get==1:
        displaywhole()
        get2=input("DO YOU WANT TO SEE A SORTED LIST?(Y/N): ")
        if get2=='y' or get2=='Y':
            while True:
                displaysortmenu()
                try:#these try and except for every input statement(with integer input) are added so that if any character is given in input by mistake error does not pop up and the program does not stop
                    get3=int(input("ENTER WHICH SORT WOULD YOU WANT?: "))
                except:
                    print("DO NOT ENTER A CHARACTER!, ONLY ENTER NUMBER")
                    break
                if get3==1:
                    sortwithaccount()
                elif get3==2:
                    sortwithname()
                elif get3==3:
                    sortwithbalance()
                elif get3==4:
                    break
                else:
                    print("ENTER A VALID NUMBER!")
        elif get2=='n' or get2=='N':
            print("OKAY!")
            continue
    elif get==7:
        print('BBYE!')
        break
    elif get==2:
        Insertval()
    elif get==3:
        while True:
            searchit()
            imk=input("DO YOU WANT TO SEARCH FOR ANY OTHER ACCOUNT?(Y/N): ")
            if imk=='n' or imk=='N':
                break
    elif get==4:
        while True:
            updateit()
            jgjg=input("DO YOU WANT TO MODIFY ANY OTHER ACCOUNT?(Y/N): ")
            if jgjg=='n' or jgjg=='N':
                break
    elif get==5:
        while True:
            displaytransactionmenu()
            try:
                jojo=int(input("ENTER YOUR CHOICE: "))
            except:
                print("ENTER A NUMBER, NO CHARACTERS ALLOWED!")
                break
            if jojo==1:
                while True:
                    credit()
                    lk=input("DO YOU WANT TO CREDIT AGAIN?(Y/N): ")
                    if lk=='n' or lk=='N':
                        break
            elif jojo==2:
                while True:
                    debitit()
                    bv=input("DO YOU WANT TO DEBIT AGAIN?(Y/N): ")
                    if bv=='n' or bv=='N':
                        break
            elif jojo==3:
                break
            else:
                print("PLEASE ENTER A VALID CHOICE! ")
                break
    elif get==6:
        while True:
            deleterecord()
            rf=input("DO YOU WANT TO DELETE ANOTHER ENTRY?(Y/N): ")
            if rf=='n' or rf=='N':
                break
    else:
        print("ENTER A VALID NUMBER FROM 1-7")












