#task one
import numpy as np

encode_0= [102,105,114,101,99,108,105,99,107,58,102,97,115,116]
encode_1= [108,97,98,121,114,105,110,116,104,105,99,115]

book_0=[112,97,52,115,115,51,99,111,53,100,101,53]
output_word=""

input_word=book_0
for x in range(len(input_word)):
    output_word = output_word + chr(input_word[x])

output_word = output_word + " "

print(output_word)

#decoded_0=fireclick:fast
#decoded_1= the second xeses     # dpols

