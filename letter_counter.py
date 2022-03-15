
def counter(word,a_bet):
    Word = str(word)
    letter = str(a_bet)
    
    count = 0
    for let in Word:
        if let == letter:
          count+=1
    print ("your letter ",letter, "comes up in ", Word," ",count,"times")


counter('carnavan','n')