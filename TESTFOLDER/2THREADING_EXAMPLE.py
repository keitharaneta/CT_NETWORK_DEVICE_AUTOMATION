from concurrent.futures import ThreadPoolExecutor
import urllib.request
import time

x2 = [2, 4]


def fn_takes_time(x1):
    print("***BEFORE CALLING SLEEP")
    time.sleep(x1)
    print("***AFTER SLEEP")
    return f"DONE @ {x1}"


# EDIT MAX_WORKERS to see the THREADING EFFECT
with ThreadPoolExecutor(max_workers=2) as ex:
    future = ex.map(fn_takes_time, [the_time for the_time in x2])
    print("\nCALLING RESULT")
    for value in future:
        print(value)
