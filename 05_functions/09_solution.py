def even_numbers(number):
    for i in range(2, number + 1, 2):
        yield i


for num in even_numbers(10):
    print(num)
