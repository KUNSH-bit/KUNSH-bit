from datetime import date
from zoneinfo import ZoneInfo
import calendar
import re

START_DATE = date(2026, 8, 1)

today = date.today()

def add_months(d, months):
    month = d.month - 1 + months
    year = d.year + month // 12
    month = month % 12 + 1
    day = min(d.day, calendar.monthrange(year, month)[1])
    return date(year, month, day)

years = today.year - START_DATE.year

if (today.month, today.day) < (START_DATE.month, START_DATE.day):
    years -= 1

year_date = add_months(START_DATE, years)

months = (today.year - year_date.year) * 12 + today.month - year_date.month

if today.day < year_date.day:
    months -= 1

month_date = add_months(year_date, months)

days = (today - month_date).days

result = f"{years} Year • {months} Months • {days} Days"

with open("README.md", "r", encoding="utf-8") as file:
    content = file.read()

pattern = r"(<!-- START_CODING_COUNTER -->).*?(<!-- END_CODING_COUNTER -->)"

replacement = f"""<!-- START_CODING_COUNTER -->
## ⏱ Journey

Started coding on 23 June 2025

**{result}**
<!-- END_CODING_COUNTER -->"""

content = re.sub(pattern, lambda m: replacement, content, flags=re.DOTALL)

with open("README.md", "w", encoding="utf-8") as file:
    file.write(content)

print("Updated journey:", result)
