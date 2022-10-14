def replace_comma_with_space(text):
    output=" "
    for i in text:
        if i!=',':
            output+=i
        else:
            output+=" "

    return output         

   





s = "I,have,been,practising,python,since,the,course,started"
output = replace_comma_with_space(s)
print(output)

