import random
import string

st = input("Enter Message: ")
words = st.split(" ")
coding = input("1 for Coding and 0 for Decoding")
coding = True if (coding == "1") else False

if coding:
    nwords = []
    for word in words:
        if (len(word) >= 3):
            # Remove the first character and append it to the end
            word_new = word[1:] + word[0]
            r1 = ''.join(random.choices(string.ascii_letters, k=3))
            r2 = ''.join(random.choices(string.ascii_letters, k=3))
            stnew = r1 + word_new + r2
            
            nwords.append(stnew)
        else:
            # Reverse short words
            nwords.append(word[::-1])

    # Print final message
    print(" ".join(nwords))
else:
    nwords = []
    for word in words:
        if (len(word) >= 3):
            word_new = word[3:-3]
            word_new =  word_new[-1] + word_new[:-1]
            nwords.append(word_new)
        else:
            # Reverse short words
            nwords.append(word[::-1])
    # Print final message
    print(" " .join(nwords))
