import itertools

def create_schedule(nestedlist):
    # nested list of sections
    total_schedules = []

    for combinations in itertools.product(*nestedlist):
        time_conflicts = {}
        good_schedule = True

        for sections in combinations: # there is an extra tuple layer that this for loop goes thorugh
            for i in range(7):  # gets the day number as a key
                if sections.days[i] == 1:
                    if i not in time_conflicts.keys():  # if there is no key yet, create one
                        time_conflicts[i] = [(sections.timeslot[0], sections.timeslot[1])]  # gets the time zones of the days

                    else: # if there is a key
                        for timeslots in time_conflicts[i]:
                                # if the curr low and high time is between the curr low and high in dictionary
                            if (timeslots[0] < sections.timeslot[0] < timeslots[1]) or (timeslots[0] < sections.timeslot[1] < timeslots[1]):
                                good_schedule = False # if time conflict, flip bad schedule
                                break

        if good_schedule is True: # if no time conflicts, add it to total possible schedules
            #print("This is the current combination: ", combinations)
            total_schedules.append(combinations)

    return total_schedules


# def main():
#     alist1 = [(1,2), (2,3), (4,5)]
#     alist2 = [(1,2,3),(4,5,6),(7,8,9)]
#     alist3 = [1,2,3,4,5,6]
#     alist5 = [7,8,9,10,11,12]
#
#                 # (1, 2)                                      # (3, 4)
#     timeslots = (((1000, 2000), (2000, 3000), (3000, 4000)), ((5000,6000), (0000, 7000), (7000,8000)))
#
#     for i in create_schedule((((([1, 0, 1, 0, 0, 0, 0], 1000, 2000),), (([1, 0, 1, 0, 0, 0, 0], 2000, 3000),), (([1, 0, 1, 0, 0, 0, 0], 3000, 4000),),),
#                               ((([0, 1, 0, 1, 0, 0, 0], 5000, 6000),), (([0, 1, 0, 1, 0, 0, 0], 0000, 7000),), (([0, 1, 0, 1, 0, 0, 0], 7000, 8000),),))):
#         displaySchedule(i)
#
#     create_schedule((((((1, 2), 1000, 2000),), (((1, 2), 2000, 3000),), (((1, 2), 3000, 4000),),),
#                  ((((1, 2), 1500, 2500),), (((3, 4), 0000, 7000),), (((3, 4), 7000, 8000),),)))
#                     # ((3,4), 5000, 6000)


