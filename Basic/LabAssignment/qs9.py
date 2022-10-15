
from operator import index


def replace_word():
    replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]

    s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."
    browken_words=s.split(" ")
    # print(browken_words)
    output=""

    for word in browken_words:
      
      if word in replace_with:
            indexrep=replace_with.index(word)
            # print(indexrep)
            output+=replace_with[indexrep+1]+" "  
            # return indexrep
      else:
        output+=word+" "       

    return output

       


words=replace_word()

print(words)

