import streamlit as st
import time
import math

st.write("Hello, Azaam Ahmed!")


def draw_clock(hour, minute, second):
    clock_radius = 6
    clock = [[" " for _ in range(2 * clock_radius + 1)] for _ in range(2 * clock_radius + 1)]

    # Draw clock border
    for angle in range(0, 360, 6):
        rad = math.radians(angle)
        x = int(clock_radius + clock_radius * math.cos(rad))
        y = int(clock_radius + clock_radius * math.sin(rad))
        clock[y][x] = "o"

    # Draw hour hand
    hour_angle = math.radians((hour % 12 + minute / 60) * 30 - 90)
    hx = int(clock_radius + (clock_radius - 3) * math.cos(hour_angle))
    hy = int(clock_radius + (clock_radius - 3) * math.sin(hour_angle))
    clock[hy][hx] = "H"

    # Draw minute hand
    min_angle = math.radians(minute * 6 - 90)
    mx = int(clock_radius + (clock_radius - 2) * math.cos(min_angle))
    my = int(clock_radius + (clock_radius - 2) * math.sin(min_angle))
    clock[my][mx] = "M"

    # Draw second hand
    sec_angle = math.radians(second * 6 - 90)
    sx = int(clock_radius + (clock_radius - 1) * math.cos(sec_angle))
    sy = int(clock_radius + (clock_radius - 1) * math.sin(sec_angle))
    clock[sy][sx] = "S"

    # Draw center
    clock[clock_radius][clock_radius] = "+"

    # Convert to string
    return "\n".join("".join(row) for row in clock)


st.header("Analog Clock Timer")

timer_running = st.checkbox("Start Timer")
timer_duration = st.number_input("Set Timer (seconds)", min_value=1, max_value=3600, value=10)
timer_placeholder = st.empty()

if timer_running:
    start_time = time.time()
    while time.time() - start_time < timer_duration:
        elapsed = int(time.time() - start_time)
        remaining = timer_duration - elapsed
        now = time.localtime()
        clock_str = draw_clock(now.tm_hour, now.tm_min, now.tm_sec)
        timer_placeholder.code(clock_str)
        timer_placeholder.info(f"Time Remaining: {remaining} seconds")
        time.sleep(1)
    timer_placeholder.success("Timer finished!")