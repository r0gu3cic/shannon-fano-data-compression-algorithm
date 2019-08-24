from code_decode_functions import *
while True:
    print('''1-Encode text using shannon fano algorith
2-Decode encoded text
3-Exit''')
    answer=input()
    if answer=='1':
        text=input('Enter text you want to encode:\n')
        code(text)
    elif answer=='2':
        code=input('Enter code you want to decode to text:\n')
        decode(code)
    elif answer=='3':
        break #better option than exit()
    else:
        print('Wrong input')#protection against bad input
