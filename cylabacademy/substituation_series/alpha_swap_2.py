#sub 2
'''
LKOb (bwvek ove lgqkhej kwj osgx) gej g kyqj vo lvrqhkje bjlhetky lvrqjktktvu. 
Lvukjbkgukb gej qejbjukjz dtkw g bjk vo lwgssjuxjb dwtlw kjbk kwjte lejgktftky, 
kjlwutlgs (guz xvvxstux) bitssb, guz qevmsjr-bvsftux gmtstky. 
Lwgssjuxjb hbhgssy lvfje g uhrmje vo lgkjxvetjb, guz dwju bvsfjz, 
jglw ytjszb g bketux (lgssjz g osgx) dwtlw tb bhmrtkkjz kv gu vustuj blvetux bjeftlj. 
LKOb gej g xejgk dgy kv sjgeu g dtzj geegy vo lvrqhkje bjlhetky bitssb tu g bgoj, 
sjxgs juftevurjuk, guz gej wvbkjz guz qsgyjz my rguy bjlhetky xevhqb gevhuz kwj dvesz ove ohu guz qeglktlj. 
Ove kwtb qevmsjr, kwj osgx tb: qtlvLKO{OE3AH3ULY_4774LI5_4E3_L001_6J0659OM}
'''
#words of interest:
#guz x5 must be and this there is aot og just 'g' -> a
#kwj x3 the?

#vo x3

###with out a key letters would habe to be picked out i.e we know picoCTF == qtlvLKO seems like cheating
#also very unliky getting all letters this way
#maybe check a few letters and see if it is just a shift
#could work through it adding what can be seen and piece it on each run

# "x x x x x O x x x x T C x x V x P x x I x x x x x x"
# "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"


encoded_word = """LKOb (bwvek ove lgqkhej kwj osgx) gej g kyqj vo lvrqhkje bjlhetky lvrqjktktvu. 
Lvukjbkgukb gej qejbjukjz dtkw g bjk vo lwgssjuxjb dwtlw kjbk kwjte lejgktftky, 
kjlwutlgs (guz xvvxstux) bitssb, guz qevmsjr-bvsftux gmtstky. 
Lwgssjuxjb hbhgssy lvfje g uhrmje vo lgkjxvetjb, guz dwju bvsfjz, 
jglw ytjszb g bketux (lgssjz g osgx) dwtlw tb bhmrtkkjz kv gu vustuj blvetux bjeftlj. 
LKOb gej g xejgk dgy kv sjgeu g dtzj geegy vo lvrqhkje bjlhetky bitssb tu g bgoj, 
sjxgs juftevurjuk, guz gej wvbkjz guz qsgyjz my rguy bjlhetky xevhqb gevhuz kwj dvesz ove ohu guz qeglktlj. 
Ove kwtb qevmsjr, kwj osgx tb: qtlvLKO{OE3AH3ULY_4774LI5_4E3_L001_6J0659OM}"""

# Known plaintext:
# qtlvLKO -> picoCTF
# could do a frequency check to try and find a e i o u
alphabet_upper  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def frequency_check(input_word):
    input_word_len= len(input_word)
    print(f"len of input: {input_word_len}")

    alphabet_upper  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lower  = "abcdefghijklmnopqrstuvwxyz"
    index_count     = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    for x in range(input_word_len):
        for y in range(len(alphabet_upper)):
            if input_word[x] == alphabet_upper[y]:
                index_count[y] = index_count[y] + 1
            elif input_word[x]== alphabet_lower[y]:
                index_count[y] = index_count[y] + 1

    #print(index_count)
    return index_count

decode = {
    'q': 'p',
    'Q': 'P',
    't': 'i',
    'T': 'I',
    'l': 'c',
    'L': 'C',
    'v': 'o',
    'V': 'O',
    'O': 'F',
    'o': 'f',
    'g': 'a',   #assumptions
    'G': 'A',
    'u': 'n',
    'U': 'N',
    'z': 'd',
    'Z': 'D',
    'k': 't',
    'K': 'T',
    'w': 'h',
    'W': 'H',
    'j': 'e',
    'J': 'E',
    'r': 'm',
    'R': 'M',
    's': 'l',
    'S': 'L',
    'e': 'r',
    'E': 'R',
    'b': 's',
    'B': 'S',
    'm': 'b',
    'M': 'B',
    'h': 'u',
    'H': 'U',
    'o': 'f',
    'O': 'F',
    'x': 'g',
    'X': 'G',
    'y': 'y',
    'Y': 'Y',
    'd': 'w',
    'D': 'W',
    'f': 'v',
    'F': 'V',
    'i': 'k',
    'I': 'K',
    'A': 'Q'
}

output_word = ""

for char in encoded_word:
    if char in decode:
        output_word += decode[char]
    elif char.isalpha():
        output_word += "_"
    else:
        output_word += char

freq_output=frequency_check(encoded_word)

for x in range(len(freq_output)):
    print(f"{alphabet_upper[x]}:{freq_output[x]},")

print(output_word)


#this slow work through it picking out words and letters worked becasue the context of the text was clear 
#real word example with unknown contents this would be not very useful



