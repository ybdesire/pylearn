# evaluated success
# ref: https://stackoverflow.com/questions/492519/timeout-on-a-function-call

import multiprocessing
import time

ret = {"foo": False}


def worker(queue):
    """worker function"""

    ret = queue.get()

    time.sleep(1)

    ret["foo"] = True
    queue.put(ret)


if __name__ == "__main__":
    queue = multiprocessing.Queue()
    queue.put(ret)

    p = multiprocessing.Process(target=worker, args=(queue,))
    p.start()
    p.join(timeout=10)# time out after 10s, modify worker() sleep to test

    if p.exitcode is None:
        print("The worker timed out.")
    else:
        print(f"The worker completed and returned: {queue.get()}")
