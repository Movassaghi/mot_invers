################"
#################ecrire un mot à l'envers###################################
word = input("entert le mot:")
len(word)

# creer une liste qui contient des lettres du mot
word_list = [lettre for lettre in word]
print(word_list)


invers_word = []

## les element de la liste de invers_word commence par la derniere element
## de la liste de word_list jusqu'au debut. la fin vers le debut

for i in range(0, len(word)):
    #print(word_list[(-i+len(word))-1])
    invers_word.append(word_list[(-i+len(word))-1])
    i +=i

# on attache les lettre pour avoir un mot    
invers_word = "".join(invers_word)
print(invers_word)





    
        
    
