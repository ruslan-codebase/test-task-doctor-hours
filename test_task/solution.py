
def into_minutes(hh_mm_time):
    hh_mm = [int(i) for i in hh_mm_time.split(":")]
    return hh_mm[0]*60 + hh_mm[1]


def into_hh_mm(min_time):
    hours, minutes = min_time//60, min_time%60
    return f"{hours:02d}:{minutes:02d}"


def free_time(start_min, stop_min, busy_min):
    start = start_min
    
    for pause in busy_min:
        yield {"start": start, "stop": pause["start"]}
        start = pause['stop']
    
    yield {"start": start, "stop": stop_min}


def list_of_open_windows(busy, start="09:00", stop="21:00", window_size=30):
    busy_min = sorted(
        [{'start': into_minutes(i['start']), 'stop': into_minutes(i['stop'])} for i in busy],
        key=lambda x: x['start'])

    result = []
    for block in free_time(into_minutes(start), into_minutes(stop), busy_min):
        current = block["start"]
        nxt = current+window_size

        while nxt <= block["stop"]:
            result.append({"start": into_hh_mm(current), "stop": into_hh_mm(nxt)})
            current = nxt
            nxt = current+window_size
    
    return result