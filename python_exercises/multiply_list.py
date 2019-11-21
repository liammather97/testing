def anti_vowel(text):
    t=""
    for c in text:
        for i in "ieaouIEAOU":
            if c==1:
                c=""
            else:
                c=c

        t=t+c
    return t
                
