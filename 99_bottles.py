import random

bottle = 'bottles'
for num_bottles in range(10, 0, -1):
    if num_bottles > 1:
        bottle = 'bottles'
        print(f'{num_bottles} ' + bottle + ' on the wall')
    else:
        bottle = 'bottle'
        print(f'{num_bottles} ' + bottle + ' on the wall')
    if num_bottles == 1:
        print('There is the last bottle on the table...')
    else:
        print('Take the next bottle...')
