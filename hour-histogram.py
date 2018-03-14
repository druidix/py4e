#!/usr/local/bin/python3

send_count_max = None
prolific_hour = None
times = dict()

fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
  words_in_line = []
  for word in line.split():
    words_in_line.append(word)
  if len(words_in_line) > 0 and words_in_line[0] == 'From':
    time_of_day = words_in_line[5]
    hour = time_of_day.split(':')[0]
    times[hour] = times.get(hour, 0) + 1
  else:
    continue
fh.close()

for hour, count in sorted( [(hour, count) for hour, count in times.items()] ):
  print(hour, count)