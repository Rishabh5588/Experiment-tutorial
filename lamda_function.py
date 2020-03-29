numbers=[1,2,3,4,5,6]
even_num = filter(lambda num:num%2 == 0,numbers)
odd = filter(lambda num:num%2 !=0,numbers)
list(even_num)
