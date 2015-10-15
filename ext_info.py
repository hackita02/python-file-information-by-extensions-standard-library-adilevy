__author__ = 'Adi Levy'
import sys
from pathlib import Path
from collections import defaultdict

(_,dir)=sys.argv
path=Path(dir)

def new_file_type():
    return {
        'count': 0,
        'size': 0,
    }
types_count=defaultdict(new_file_type)


for file in path.iterdir():
    if file.is_file():
        types_count[file.suffix[1:].rjust(1,'.')]['count']+=1
        types_count[file.suffix[1:].rjust(1,'.')]['size']+=file.stat().st_size

for type in sorted(types_count):
    print(type,types_count[type]['count'],types_count[type]['size'])