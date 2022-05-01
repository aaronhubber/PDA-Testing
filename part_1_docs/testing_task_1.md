### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
#class not set up, no __init__ or contructors 

  def check_for_ace(self, card):
    if card.value = 1: # missing the second = to compare
      return True
    else # missing colon 
      return False
   
#def misspelled as dif
  dif highest_card(self, card1 card2): # missing comma
  if card1.value > card2.value:
    return card #missing number1 to denote which card.
  else:
    return card2
  


def cards_total(self, cards):
  total # total not set
  for card in cards:
    total += card.value
    return "You have a total of" + total #return in wrong place in loop
  
```
