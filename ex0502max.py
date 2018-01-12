# ch5 exercise2
# Write another program that prompts for a list of numbers as above and at the
# end prints out both the maximum and minimum of the numbers instead of the average.

print('Provide a list a number here; start to enter numbers')
print('Enter "done" when you entered all the numbers.')

my_list = []
count = 0

while True:
    inp_num = input('Enter a number: ')
    if inp_num == 'done':
        break
    try:
        finp = float(inp_num)
    except:
        print('Invalid value')
        continue
    my_list.append(finp)
    count += 1

print('You have entered {} numbers; they are {}' .format(count, my_list))
print('You have entered {} numbers; they are {}' .format(len(my_list), my_list))  # build-in function

largest = my_list[0]
smallest = my_list[0]

for num in my_list:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print('Largest: {} / Smallest: {}'.format(largest, smallest))
print('Largest: {} / Smallest: {}'.format(max(my_list), min(my_list)))  # build-in function
