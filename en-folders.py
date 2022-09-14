import calendar
from pathlib import Path

#printlist(calendar.month_name[1:])
month_names = list(calendar.month_name[1:])
days = ['Day 1', 'Day 10', 'Day 20', 'Day 30']

for i, month in enumerate(month_names):
    for day in days:
        Path(f'2022/{i+1}.{month}/{day}').mkdir(parents=True, exist_ok=True)

# testing if we can create the folder
# Path('2022/January').mkdir(parents=True, exist_ok=True)