guess_me = 5
number = 1
for number in range(10):
    if number < guess_me:
      print(number)
      print('too low')
    elif number == guess_me:
      print(number)
      print('found it!')
    else:
      print(number)
      print('oops')