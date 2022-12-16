num_1=int(input('first number: '))
num_2=int(input('second number: '))
op = input('Chose one operator: |+  to add| - to subtract | *  to multiply | /  to division: ')

if op == '+':
  print(num_1 + num_2)
elif op == '-':
  print(num_1 - num_2)
elif op == '*':
  print(num_1 * num_2)
elif op == '/':
  print(num_1 / num_2)
elif op == '@':
  print('hi! my @ on instagram : @study_lostmind')
else:
 print ('Try again')
 