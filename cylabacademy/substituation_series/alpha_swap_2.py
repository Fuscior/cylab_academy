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
# i a the should be easy to spot

decode = {
    'q': 'p',
    't': 'i',
    'l': 'c',
    'v': 'o',
    'L': 'C',
    'K': 'T',
    'O': 'F',
    'e': 'r'
}

output_word = ""

for char in encoded_word:
    if char in decode:
        output_word += decode[char]
    elif char.isalpha():
        output_word += "_"
    else:
        output_word += char

print(output_word)


