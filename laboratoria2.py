print('Zadanie 1')
print('0>1 = ',0>1)
print('0<=1 = ',0<=1)
print('0>=1 = ',0>=1)
print('1==0 = ',1==0)
print('1==1 = ',1==1)
print('1!=0 = ',1!=0)
print('1!=1 = ',1!=1)

print('Zadanie 2')
x,y = int(input('Podaj x ')),int(input('Podaj y '))
print(2*x+5*y)

print('Zadanie 3')

print('Zadanie 4')
a,b,d = input('Podaj imie '),input('Podaj nazwisko '),input('Podaj kierunek ')
c = int(input('Podaj wiek '))
print('Jestem ',a,' ',b,' mam ',c,' lat studiuje ',d)

print('Zadanie 5')

print('true') if(1+2+10+20000001+4+347586970885 == 321784560456434534646) else print('false')

print('Zadanie 6')
x,y = int(input('Podaj x ')), int(input('Podaj y '))
print('Suma ',x," + ",y,' jest parzysta') if((x+y)%2==0) else print('Suma ',x," + ",y,' jest nieparzysta')

print('Zadanie 7')
x,y= int(input('Podaj x ')),int(input('Podaj y '))
print('1 - dodawanie\n2 - odejmowanie\n3 - mnozenie\n4 - dzielenie')
choice = int(input('Wybierz opcje'))

match choice:
  case 1:
    print(x+y)
  case 2:
    print(x-y)
  case 3:
    print(x*y)
  case 4:
    print(x/y)

print('Zadanie 8')
x = int(input('Podaj x '))
print((x > 3)&(x < 13))
print((x != 5)|(x < 0))
