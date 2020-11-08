# coding: utf8
"""
**PESEL** is the national identification number used in Poland since 1979.

Having a PESEL in the form of *abcdefghijk*, one can check the validity of the number by computing
the following expression:

1×*a* + 3×*b* + 7×*c* + 9×*d* + 1×*e* + 3×*f* + 7×*g* + 9×*h* + 1×*i* + 3×*j*

Then the last digit of the result should be subtracted from 10. If the result of the last operation
is not equal to the last digit of a given PESEL, the PESEL is incorrect. This system works reliably
well for catching one-digit mistakes and digit swaps.

Checking validity of PESEL: 44051401358 (number 8, the last digit, is the check digit for this PESEL):

    1×4 + 3×4 + 7×0 + 9×5 + 1×1 + 3×4 + 7×0 + 9×1 + 1×3 + 3×5 = 101

Getting the last digit of the result (101 % 10):

101 % 10 = 1

In order to get the check digit one need to take the 10s complement of the number. It is 0 if the modulo
result is 0, and it is 5 when the modulo is equal to 5, otherwise it means the modulo result has to
be subtracted from 10.

10 - 1 = 9

9 is not equal to the last digit of PESEL, which is 8, so the PESEL contains errors.

### Date of birth

PESEL also a encodes birthdate. It is stored in the first six digits os the number in the form
`YYMMDDxxxxxx`, where YYMMDD is the date of birth (with century encoded in month field).
The PESEL system has been designed to cover five centuries. To distinguish people born in
different centuries, numbers are added to the MM field:

- for birthdates between 1900 and 1999: no change to `MM` field is made
- for other birthdates:
  - 2000–2099: month field number is increased by 20
  - 2100–2199: month + 40
  - 2200–2299: month + 60
  - 1800–1899: month + 80

For example, a person born on *December 24, 2002* would have a PESEL number starting with `023224`
and person born on *December 24, 1902* would have a PESEL number starting with `021224`.

### Your task (`pesel.py`)

1. Write a function `check_pesel` that will verify the PESEL number and the date of birth of the person
identified by this number.

   The function is supposed to take the PESEL number as a text string and return:

   - None if PESEL is incorrect
   - date of birth in the format `September 5, 1971` if the PESEL number is correct

2. Write the function `check_pesel_file`, which takes the file name as an argument and reads PESEL numbers
   from this file (one on each line). The function must create a file with the same name as the original file name
   with the extension changed to `.out`, containing each line of the person's date of birth, or the sign "-"
   in the case of an incorrect PESEL number.

   For example, calling `check_pesel_file("pesels.txt")` will create the file `pesels.out`. If the file
   `pesels.txt` contains

        90090515836
        87832165581

   This `pesels.out` will be as follows:

        May 5, 1990
        -

   It is worth considering how to use the function from the first point.
"""

def check_pesel(pesel):
    if pesel == None or len(pesel)!=11: return None
    sum=0
    lastnumer=int(pesel[10])
    x=False

    sum=int(pesel[0])+int(pesel[1])*3+int(pesel[2])*7+int(pesel[3])*9+int(pesel[4])+int(pesel[5])*3+int(pesel[6])*7+int(pesel[7])*9+int(pesel[8])+int(pesel[9])*3
    modulo=sum%10
    if modulo==0 and lastnumer==0:x=True
    if 10-modulo==lastnumer:x=True
    if x==False: return None

    primernumero=int(pesel[2])
    segundonumero=int(pesel[3])
    numerototal=primernumero*10+segundonumero
    año=0
    if numerototal<=12:
        año=1900+int(pesel[0])*10+int(pesel[1])
        mesnum=int(pesel[2])*10+int(pesel[3])
        daynum=int(pesel[4])*10+int(pesel[5])
        if mesnum==1: mes="January"
        if mesnum==2: mes="February"
        if mesnum==3: mes="March"
        if mesnum==4: mes="April"
        if mesnum==5: mes="May"
        if mesnum==6: mes="June"
        if mesnum==7: mes="July"
        if mesnum==8: mes="August"
        if mesnum==9: mes="September" 
        if mesnum==10: mes="October"
        if mesnum==11: mes="November"
        if mesnum==12: mes="December"
        final=str(mes)+" "+str(daynum)+", "+str(año)
        return final
    mes1=""
    if (numerototal<=32 and numerototal>12):
        año=2000+int(pesel[0])*10+int(pesel[1])
        mesnum=(int(pesel[2])*10+int(pesel[3])-20)
        daynum=int(pesel[4])*10+int(pesel[5])
        if mesnum==1: mes1="January"
        if mesnum==2: mes1="February"
        if mesnum==3: mes1="March"
        if mesnum==4: mes1="April"
        if mesnum==5: mes1="May"
        if mesnum==6: mes1="June"
        if mesnum==7: mes1="July"
        if mesnum==8: mes1="August"
        if mesnum==9: mes1="September" 
        if mesnum==10: mes1="October"
        if mesnum==11: mes1="November"
        if mesnum==12: mes1="December"
        final=str(mes1)+" "+str(daynum)+", "+str(año)
        return final
    else:
        año=1800+int(pesel[0])*10+int(pesel[1])
        mesnum=(int(pesel[2])*10+int(pesel[3])-80)
        daynum=int(pesel[4])*10+int(pesel[5])
        if mesnum==1: mes2="January"
        if mesnum==2: mes2="February"
        if mesnum==3: mes2="March"
        if mesnum==4: mes2="April"
        if mesnum==5: mes2="May"
        if mesnum==6: mes2="June"
        if mesnum==7: mes2="July"
        if mesnum==8: mes2="August"
        if mesnum==9: mes2="September" 
        if mesnum==10: mes2="October"
        if mesnum==11: mes2="November"
        if mesnum==12: mes2="December"
        final=str(mes2)+" "+str(daynum)+", "+str(año)
        return final
        
        
"""
Line: 90090515836 bueno
Line: 87832165181 bueno
Line: 01261031813 malo
Line: 01261051813 bueno
Line: 123456789   malo
"""
def check_pesel_file(filename):
    other=[]
    with open("data.txt", "r") as file: 
         for line in file:
             x=line.rstrip()
             l=check_pesel(x)
             if l==None: l="-"
             other.append(l)
         
         with open('data.out', 'w') as fillee:
            for x in other:
               print(x)
               fillee.write(x)
        
            
                
             
check_pesel_file("test")