from data import *
# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.

# Part 2
   # The function for Part 2 should be within the class in data.py.
# Part 3
def time_add(time1: Time, time2: Time) -> Time:
    hours = time1.hour + time2.hour
    minutes = time1.minute + time2.minute
    seconds = time1.second + time2.second
    if seconds > 59:
        seconds -= 59
        minutes += 1
    if minutes > 59:
        minutes -= 59
        hours += 1
    return Time(hours, minutes, seconds)

# Part 4
def is_descending(list1: list[float]) -> bool:
    for i in range(len(list1) - 1):
        if list1[i] < list1[i+1]:
            return False
        else:
            return True
# [3, 2, 1]

# Part 5
def largest_between(list: list[int], lower: int, upper: int) -> any:
    if lower > upper:
        return None
    elif lower < 0 or upper > len(list) - 1:
        return None
    largest = lower
    for i in range(lower, upper):
        if list[i] > list[largest]:
            largest = i
    return largest

# Part 6
def furthest_from_origin(l: list[Point]) -> any:
    if len(l) == 0:
        return None
    greatest = round(math.sqrt((l[0].x-0)**2 + (l[0].y-0)**2), 2)
    index = 0
    for p in l:
        if round(math.sqrt((p.x-0)**2 + (p.y-0)**2), 2) > greatest:
            greatest = round(math.sqrt((p.x-0)**2 + (p.y-0)**2), 2)
            index = l.index(p)
    return index