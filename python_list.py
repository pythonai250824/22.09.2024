
# input grades from user until entered -999
# save all grades
# print the max grade
# print the lowest grade
# print the average
# if a grade is not between 0-100 ignore

grades: list[int] = []
SENTINEL: int = -999
while True:
    grade: int = int(input('enter next grade:'))
    if grade == SENTINEL:
        break
    if not 0 <= grade <= 100:
        continue
    grades.append(grade)  # adding a value to the end of the list

# if len(grades) != 0
# if grades
# if len(grades):
if len(grades) >= 1:
    print(f"max value == {max(grades)}")  # gets the maximum value
    print(f"min value == {min(grades)}")  # gets the minimum value
    print(f"avg == {sum(grades) / len(grades)}")  # calculates the avg
    import statistics
    #print(f"mean == {statistics.mean(grades)}")
else:
    print("empty list ...")