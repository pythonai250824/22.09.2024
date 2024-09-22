
WORLD_RECORD: float = 6.23
new_world_record: float = None
new_world_record_name: str = None
count_good_results: int = 0
sum_good_results: int = 0
max_score: float = None
MAX_COUNT: int = 7
for _ in range(MAX_COUNT):
    result: float = float(input('whats the height? '))
    if result < 5.80:
        continue
    count_good_results += 1
    sum_good_results += result
    # if max_score is None
    # if not max_score
    if max_score is None or result > max_score:
        max_score = result
    if result > WORLD_RECORD:
        # TODO: what if second world record was lower than the first
        new_world_record = result
        print('NEW WORLD RECORD !!!!!!!!!!')
        new_world_record_name = input('whats the name of the jumper? ')
else:
    avg_good_score: float = None
    print(f"number of good jumps: {count_good_results}")
    if count_good_results:
        avg_good_score: float = sum_good_results / count_good_results
    print(f"good jumps avg = {avg_good_score}")
    print(f"highest score: {max_score}")
    if new_world_record:
        print(f"new world record height: {new_world_record}")
        print(f"new world record jumper name: {new_world_record_name}")
    else:
        print("no new world record achieved. None")
