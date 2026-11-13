
from datetime import date, datetime
from zoneinfo import ZoneInfo
import calendar

START_DATE = date(2026, 7, 27)

today = datetime.now(ZoneInfo("Asia/Kolkata")).date()

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

result = f"{years} Years • {months} Months • {days} Days"

with open("README.md", "r", encoding="utf-8") as file:
    content = file.read()

replacement = f"""<!-- START_CODING_COUNTER -->
Started Posting on Github on **27 July 2026**

**{result}**
<!-- END_CODING_COUNTER -->"""

if "<!-- START_CODING_COUNTER -->" in content:
    import re
    content = re.sub(
        r"<!-- START_CODING_COUNTER -->.*?<!-- END_CODING_COUNTER -->",
        lambda m: replacement,
        content,
        flags=re.DOTALL
    )
else:
    content += "\n\n" + replacement + "\n"

with open("README.md", "w", encoding="utf-8") as file:
    file.write(content)

print("Updated journey:", result)
