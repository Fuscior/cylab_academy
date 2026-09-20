#sub 
'''
ZGSOCXPQUYHMILERVTBWNAFJDK 

Qctcnrel Mcptzlo ztebc, fuwq z ptzac zlo bwzwcmd zut, zlo gtenpqw ic wqc gccwmc
xtei z pmzbb szbc ul fqusq uw fzb clsmebco. Uw fzb z gcznwuxnm bsztzgzcnb, zlo, zw
wqzw wuic, nlhlefl we lzwntzmubwb—ex sentbc z ptczw rtukc ul z bsuclwuxus reulw
ex aucf. Wqctc fctc wfe tenlo gmzsh brewb lczt elc cjwtciuwd ex wqc gzsh, zlo z
melp elc lczt wqc ewqct. Wqc bszmcb fctc cjsccoulpmd qzto zlo pmebbd, fuwq zmm wqc
zrrcztzlsc ex gntlubqco pemo. Wqc fcupqw ex wqc ulbcsw fzb actd tcizthzgmc, zlo,
wzhulp zmm wqulpb ulwe selbuoctzwuel, U senmo qztomd gmzic Ynruwct xet qub eruluel
tcbrcswulp uw.

Wqc xmzp ub: ruseSWX{5NG5717N710L_3A0MN710L_357GX9XX}
'''

key_upper="ZGSOCXPQUYHMILERVTBWNAFJDK"
key_lower="zgsocxpquyhmilervtbwnafjdk"
exp=      "ABCDEFGHIJKLMNOPQRSTUVQXYZ"
#exp="A B C D E F G H I J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z"
#     1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
#expecting to swap poistions
#maybe some loop char check with a index swap
#have to account for upper and lower case.. hummmm
#could have key1 in lower and key two in upper shifting should be the same
#could add an asssci range check to minimize
corrected_index= [26,7,19,15,3,24,16,22,21,25,8,13,9,12,5,18,22,20,2,23,14,1,6,10,4,11]

encoded_word = "Qctcnrel Mcptzlo ztebc, fuwq z ptzac zlo bwzwcmd zut, zlo gtenpqw ic wqc gccwmc xtei z pmzbb szbc ul fqusq uw fzb clsmebco. Uw fzb z gcznwuxnm bsztzgzcnb, zlo, zw wqzw wuic, nlhlefl we lzwntzmubwb—ex sentbc z ptczw rtukc ul z bsuclwuxus reulw ex aucf. Wqctc fctc wfe tenlo gmzsh brewb lczt elc cjwtciuwd ex wqc gzsh, zlo z melp elc lczt wqc ewqct. Wqc bszmcb fctc cjsccoulpmd qzto zlo pmebbd, fuwq zmm wqc zrrcztzlsc ex gntlubqco pemo. Wqc fcupqw ex wqc ulbcsw fzb actd tcizthzgmc, zlo, wzhulp zmm wqulpb ulwe selbuoctzwuel, U senmo qztomd gmzic Ynruwct xet qub eruluel tcbrcswulp uw. Wqc xmzp ub: ruseSWX{5NG5717N710L_3A0MN710L_357GX9XX}"


key_upper = "ZGSOCXPQUYHMILERVTBWNAFJDK"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

decode = {}

for i in range(26):
    decode[key_upper[i]] = alphabet[i]
    decode[key_upper[i].lower()] = alphabet[i].lower()

output_word = ""

for char in encoded_word:
    if char in decode:
        output_word += decode[char]
    else:
        output_word += char

print(output_word)

