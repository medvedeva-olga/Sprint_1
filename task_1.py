str ='1h 45m,360s,25m,30m 120s,2h 60s'
times = str.replace(',', ' ').split()
total_min = 0
sum_of_sec = 0
for t in times:
    if "h" in t:
        total_min += int(t.replace('h',''))*60
    elif "m" in t:
        total_min += int(t.replace('m',''))
    elif "s" in t:
        sum_of_sec += int(t.replace('s',''))
total_min += sum_of_sec // 60
print(total_min)