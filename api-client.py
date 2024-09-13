from datetime import timedelta
import time
import requests

if __name__ == "__main__":
    INTERVAL = 1
    while True:
        try:
            start = time.perf_counter()
            resp = requests.post("http://localhost:8000/predict")
            end = time.perf_counter()
            time.sleep(max(0, INTERVAL - (end - start)))
            print(f"{resp.status_code=}, {timedelta(seconds=end-start)=}")
        except Exception as e:
            print(e)
