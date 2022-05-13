# print("Day 1")
# the_file = open("um-deliveries-day-1.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-day-2.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-day-3.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()

def delivery_summary(a): # creating my function
    """ Prints the summary of watermelons sold and for how much """

    print(a) # shows which delivery day list
    the_file = open(a) # opens the file
    for line in the_file: # lists everything 
        line = line.rstrip() # takes away white space
        words = line.split('|') # tokenizes

        melon = words[0] 
        count = words[1] # creates variable for where each indice goes
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")
        # prints the summary statement
    the_file.close() # closes file
delivery_summary("um-deliveries-day-1.txt") # calls the function for the first one
delivery_summary("um-deliveries-day-2.txt") # calls second day
delivery_summary("um-deliveries-day-3.txt") # calls third day