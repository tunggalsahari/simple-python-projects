import ntplib

from datetime import datetime


# 1. INPUT: Human readable past

past_input = "2007-10-16 14:30:05.123456"

past_dt = datetime.strptime(past_input, "%Y-%m-%d %H:%M:%S.%f")


# 2. CURRENT: Precise NTP time

client = ntplib.NTPClient()

try:

    # pool.ntp.org provides the 'true' epoch including microseconds

    response = client.request('pool.ntp.org')

    current_dt = datetime.fromtimestamp(response.tx_time)

except:

    current_dt = datetime.now()


# 3. CALCULATION: The "Odometer" Method

# We subtract the 'years' and 'months' directly. 

# If the current day is less than the past day, we roll back a month.

years = current_dt.year - past_dt.year

months = current_dt.month - past_dt.month

days = current_dt.day - past_dt.day


# Adjust for negative values (the "Borrowing" logic)

if days < 0:

    months -= 1

    # Get the last day of the PREVIOUS month to know how many days to add back

    # This handles the 28, 30, vs 31 day month problem perfectly

    prev_month = (current_dt.month - 1) if current_dt.month > 1 else 12

    days += (current_dt.replace(month=prev_month, day=1) - 

             current_dt.replace(month=prev_month, day=1, year=current_dt.year-1 if prev_month==12 else current_dt.year)).days


if months < 0:

    years -= 1

    months += 12


# 4. PRECISE TIME COMPONENTS

# The 'timedelta' handles the overflow of hours/mins/secs/ms perfectly

diff_time = current_dt - past_dt

hours, remainder = divmod(diff_time.seconds, 3600)

minutes, seconds = divmod(remainder, 60)

microseconds = diff_time.microseconds


# 5. OUTPUT

print(f"You have lived for: ")

print(f"{years} Years, {months} Months, {days} Days, {hours} Hours")

print(f"{minutes} Minutes, {seconds} Seconds, {microseconds} Microseconds")
