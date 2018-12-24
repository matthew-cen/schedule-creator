def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    print("this is repeat, ", repeat)
    print(args)
    print(*args)
    pools = [tuple(pool) for pool in args] * repeat
    print(pools)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


def product2(something, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111

    pools = [tuple(pool) for pool in something] * repeat

    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result: # goes through the list of permutations and yields it
        yield tuple(prod)


thisTuple = (((((1,2),1000, 2000),), (((1,2),2000, 3000),), (((1,2),3000, 4000),),), ((((3,4),5000,6000),), (((3,4),0000, 7000),), (((3,4),7000,8000),),))
# for something in product2(thisTuple):
    # print(something)


def createCorrectTuple(days, timeslots):
    pass


def create_schedule(this_tuple):
    # tuple in form ((((day1, day#...), lowTime, highTime),), ....,),))

    # ex #(((((1, 2), 1000, 2000),), (((1, 2), 2000, 3000),), (((1, 2), 3000, 4000),),), ((((1, 2), 1500, 2500),), (((3, 4), 0000, 7000),), (((3, 4), 7000, 8000),),))
    total_schedules = []

    for combinations in product2(this_tuple):
        time_conflicts = {}
        good_schedule = True

        for extra_layer in combinations: # there is an extra tuple layer that this for loop goes thorugh

            for i in range(len(extra_layer[0][0])):  # gets the day number as a key
                if extra_layer[0][0][i] == 1:
                    if i not in time_conflicts.keys():  # if there is no key yet, create one
                        time_conflicts[i] = [(extra_layer[0][1], extra_layer[0][2])]  # gets the time zones of the days

                    else: # if there is a key
                        for timeslots in time_conflicts[i]:
                                # if the curr low and high time is between the curr low and high in dictionary
                            if (timeslots[0] < extra_layer[0][1] < timeslots[1]) or (timeslots[0] < extra_layer[0][2] < timeslots[1]):
                                good_schedule = False # if time conflict, flip bad schedule
                                break

        if good_schedule is True: # if no time conflicts, add it to total possible schedules
            print("This is the current combination: ", combinations)
            yield combinations

    print(len(total_schedules))
    for i in total_schedules:
        print(i)

    print("-----------------------------------------------------------")

def displaySchedule(this_tuple):
    this_dictionary = {}
    for elem in this_tuple:
        for sections in elem:
            for i in range(0, len(sections[0])):
                if sections[0][i] == 1:
                    if i not in this_dictionary:
                        this_dictionary[i] = [(sections[1],sections[2])]
                    else:
                        this_dictionary[i].append((sections[1], sections[2]))

    #for keys, args in this_dictionary.items():
        #print(keys, " ", args)

    for keys in this_dictionary: # sorts each value of the dictionary
        this_dictionary[keys].sort(key=lambda tup:tup[0])

    for i in range(0,7):
        if (i == 0):
            print("Monday:", end=" ")
        if (i == 1):
            print("Tuesday:", end=" ")
        if (i == 2):
            print("Wednesday:", end=" ")
        if (i == 3):
            print("Thursday:", end=" ")
        if (i == 4):
            print("Friday:", end=" ")
        if (i == 5):
            print("Saturday:", end=" ")
        if (i == 6):
            print("Sunday:", end=" ")

        if i in this_dictionary:
            print(this_dictionary[i])
        else:
            print("There no scheduled classes on this day :(")
    print("-----------------------------------------------------------")

def main():
    alist1 = [(1,2), (2,3), (4,5)]
    alist2 = [(1,2,3),(4,5,6),(7,8,9)]
    alist3 = [1,2,3,4,5,6]
    alist5 = [7,8,9,10,11,12]

                # (1, 2)                                      # (3, 4)
    timeslots = (((1000, 2000), (2000, 3000), (3000, 4000)), ((5000,6000), (0000, 7000), (7000,8000)))

    for i in create_schedule((((([1, 0, 1, 0, 0, 0, 0], 1000, 2000),), (([1, 0, 1, 0, 0, 0, 0], 2000, 3000),), (([1, 0, 1, 0, 0, 0, 0], 3000, 4000),),),
                              ((([0, 1, 0, 1, 0, 0, 0], 5000, 6000),), (([0, 1, 0, 1, 0, 0, 0], 0000, 7000),), (([0, 1, 0, 1, 0, 0, 0], 7000, 8000),),))):
        displaySchedule(i)

    create_schedule((((((1, 2), 1000, 2000),), (((1, 2), 2000, 3000),), (((1, 2), 3000, 4000),),),
                 ((((1, 2), 1500, 2500),), (((3, 4), 0000, 7000),), (((3, 4), 7000, 8000),),)))
                    # ((3,4), 5000, 6000)

main()
