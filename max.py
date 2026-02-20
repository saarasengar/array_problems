array=[3,7,3,9]

maximum=array[0]
minimum=array[0]

for num in array:

    if num>maximum:
        maximum=num
    
    if num < minimum:

        minimum=num

    print("max:",maximum)

    print("min:",minimum)