#!/usr/local/bin/python3

send_count_max = None
prolific_sender = None
senders = dict()

fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
  words_in_line = []
  for word in line.split():
    words_in_line.append(word)
  if len(words_in_line) > 0 and words_in_line[0] == 'From':
    senders[words_in_line[1]] = senders.get(words_in_line[1], 0) + 1
  else:
    continue
fh.close()

for sender, count in senders.items():
  if send_count_max is None or senders[sender] > send_count_max:
    prolific_sender = sender
    send_count_max = senders[sender]

print(prolific_sender, send_count_max)