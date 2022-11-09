def check_anagram(angrams):
    grouped_anagram={}
    for word in angrams:
        sorted_word=str(sorted(word))
        if sorted_word in grouped_anagram:
            grouped_anagram[sorted_word].append(word)
        else:
            grouped_anagram[sorted_word]=[word]
    
    return grouped_anagram
   


anagrams=['eat', 'ate', 'done', 'tea', 'soup', 'node']
verify_anagrams=check_anagram(anagrams)

print(list(verify_anagrams.values()))