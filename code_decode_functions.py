#!/usr/bin/env python3

# Function that is used for text decoding
def decode(code):
    i=0
    text=''
    pattern_in_code=''
    for i in range(0,len(code),1):
        pattern_in_code=pattern_in_code+code[i]
        if pattern_in_code=='000':
            text=text+'a'
            pattern_in_code=''
            continue
        elif pattern_in_code=='001':
            text=text+'o'
            pattern_in_code=''
            continue
        elif pattern_in_code=='0100':
            text=text+'i'
            pattern_in_code=''
            continue
        elif pattern_in_code=='0101':
            text=text+'e'
            pattern_in_code=''
            continue
        elif pattern_in_code=='01100':
            text=text+'n'
            pattern_in_code=''
            continue
        elif pattern_in_code=='01111':
            text=text+'s'
            pattern_in_code=''
            continue
        elif pattern_in_code=='10000':
            text=text+'r'
            pattern_in_code=''
            continue
        elif pattern_in_code=='10010':
            text=text+'t'
            pattern_in_code=''
            continue
        elif pattern_in_code=='10011':
            text=text+'j'
            pattern_in_code=''
            continue
        elif pattern_in_code=='1010':
            text=text+'u'
            pattern_in_code=''
            continue
        elif pattern_in_code=='10110':
            text=text+'d'
            pattern_in_code=''
            continue
        elif pattern_in_code=='10111':
            text=text+'v'
            pattern_in_code=''
            continue
        elif pattern_in_code=='11000':
            text=text+'m'
            pattern_in_code=''
            continue
        elif pattern_in_code=='11001':
            text=text+'k'
            pattern_in_code=''
            continue
        elif pattern_in_code=='11010':
            text=text+'l'
            pattern_in_code=''
            continue
        elif pattern_in_code=='11011':
            text=text+'p'
            pattern_in_code=''
            continue
        elif pattern_in_code=='11100':
            text=text+'g'
            pattern_in_code=''
            continue
        elif pattern_in_code=='111010':
            text=text+'z'
            pattern_in_code=''
            continue
        elif pattern_in_code=='111011':
            text=text+'b'
            pattern_in_code=''
            continue
        elif pattern_in_code=='111100':
            text=text+'š'
            pattern_in_code=''
            continue
        elif pattern_in_code=='1111010':
            text=text+'ć'
            pattern_in_code=''
            continue
        elif pattern_in_code=='1111011':
            text=text+'c'
            pattern_in_code=''
            continue
        elif pattern_in_code=='1111100':
            text=text+'č'
            pattern_in_code=''
            continue
        elif pattern_in_code=='1111101':
            text=text+'h'
            pattern_in_code=''
            continue
        elif pattern_in_code=='1111110':
            text=text+'ž'
            pattern_in_code=''
            continue
        elif pattern_in_code=='11111110':
            text=text+'đ'
            pattern_in_code=''
            continue
        elif pattern_in_code=='11111111':
            text=text+'f'
            pattern_in_code=''
            continue
        elif pattern_in_code=='11111111':
            text=text+'f'
            pattern_in_code=''
            continue
        elif pattern_in_code=='01101':
            text=text+'.'
            pattern_in_code=''
            continue
        elif pattern_in_code=='01110':
            text=text+','
            pattern_in_code=''
            continue
        elif pattern_in_code=='10001':
            text=text+' '
            pattern_in_code=''
            continue
    print('Decoded text:\n'+text)

# Function that is used for text coding
def code(text):
    i=0
    code=''
    while i!=len(text):
        if text[i]=='a'or text[i]=='A':
            code=code+'000'
            i=i+1
            continue
        elif text[i]=='o' or text[i]=='O':
            code=code+'001'
            i=i+1
            continue
        elif text[i]=='i' or text[i]=='I':
            code=code+'0100'
            i=i+1
            continue
        elif text[i]=='e' or text[i]=='E':
            code=code+'0101'
            i=i+1
            continue
        elif text[i]=='n' or text[i]=='N':
            code=code+'01100'
            i=i+1
            continue
        elif text[i]=='s' or text[i]=='S':
            code=code+'01111'
            i=i+1
            continue
        elif text[i]=='r' or text[i]=='R':
            code=code+'10000'
            i=i+1
            continue
        elif text[i]=='t' or text[i]=='T':
            code=code+'10010'
            i=i+1
            continue
        elif text[i]=='j' or text[i]=='J':
            code=code+'10011'
            i=i+1
            continue
        elif text[i]=='u' or text[i]=='U':
            code=code+'1010'
            i=i+1
            continue
        elif text[i]=='d' or text[i]=='D':
            code=code+'10110'
            i=i+1
            continue
        elif text[i]=='v' or text[i]=='V':
            code=code+'10111'
            i=i+1
            continue
        elif text[i]=='m' or text[i]=='M':
            code=code+'11000'
            i=i+1
            continue
        elif text[i]=='k' or text[i]=='K':
            code=code+'11001'
            i=i+1
            continue
        elif text[i]=='l' or text[i]=='L':
            code=code+'11010'
            i=i+1
            continue
        elif text[i]=='p' or text[i]=='P':
            code=code+'11011'
            i=i+1
            continue
        elif text[i]=='g' or text[i]=='G':
            code=code+'11100'
            i=i+1
            continue
        elif text[i]=='z' or text[i]=='Z':
            code=code+'111010'
            i=i+1
            continue
        elif text[i]=='b' or text[i]=='B':
            code=code+'111011'
            i=i+1
            continue
        elif text[i]=='š' or text[i]=='Š':
            code=code+'111100'
            i=i+1
            continue
        elif text[i]=='ć' or text[i]=='Ć':
            code=code+'1111010'
            i=i+1
            continue
        elif text[i]=='c' or text[i]=='C':
            code=code+'1111011'
            i=i+1
            continue
        elif text[i]=='č' or text[i]=='Č':
            code=code+'1111100'
            i=i+1
            continue
        elif text[i]=='h' or text[i]=='H':
            code=code+'1111101'
            i=i+1
            continue
        elif text[i]=='ž' or text[i]=='Ž':
            code=code+'1111110'
            i=i+1
            continue
        elif text[i]=='đ' or text[i]=='Đ':
            code=code+'11111110'
            i=i+1
            continue
        elif text[i]=='f' or text[i]=='F':
            code=code+'11111111'
            i=i+1
            continue
        elif text[i]=='.':
            code=code+'01101'
            i=i+1
            continue
        elif text[i]==',':
            code=code+'01110'
            i=i+1
            continue
        elif text[i]==' ':
            code=code+'10001'
            i=i+1
            continue
    print('Encoded text:\n'+code)
