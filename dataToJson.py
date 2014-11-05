import json
import sys

entries = []

for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	split = line.split('\t', 1)
	record = None
	if(len(split)==2):
		date = split[0]
		count = split[1]
		record = {"date": date, "count": int(count)}
		entries.append(record)

print json.dumps(entries, sort_keys=True, indent=4, separators=(',', ': '))