
def into_minutes(hh_mm_time):
    hh_mm = [int(i) for i in hh_mm_time.split(":")]
    return hh_mm[0]*60 + hh_mm[1]


def free_time(start_min, stop_min, busy_min):
    blocks = []
    start = start_min

    for pause in busy_min:
        blocks.append(pause['start']-start)
        start = pause['stop']
    
    blocks.append(stop_min-start)
    return blocks


def number_of_chunks(busy, start="09:00", stop="21:00", chunk_size=30):
    start_min, stop_min = into_minutes(start), into_minutes(stop)
    busy_min = sorted(
        [{'start': into_minutes(i['start']), 'stop': into_minutes(i['stop'])} for i in busy],
        key=lambda x: x['start'])
    free_time_blocks = free_time(start_min, stop_min, busy_min)

    return sum([i//chunk_size for i in free_time_blocks])
