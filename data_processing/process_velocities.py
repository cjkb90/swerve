import json
import math
from collections import defaultdict

def mag(x): 
  return math.sqrt(sum(i**2 for i in x))

fname = 'distrupt_hackathon_data'
with open(fname) as f:
  content = f.readlines()

content = [x.strip() for x in content] 
content = [json.loads(x) for x in content]

objects = defaultdict(list)

for c in content:
  objects[c['object_id']].append(c)

for object_id, data in objects.iteritems():
  print 'OBJECT ID: ', object_id
  for data_point in data:
#    print data_point
    #print data_point['time'], mag(data_point['world_velocity'])
    print mag(data_point['world_velocity'])
