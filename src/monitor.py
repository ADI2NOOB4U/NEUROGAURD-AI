import psutil
import time
from ai_detector import analyze_process
import logging

logging.basicConfig(
    filename='monitoring.log',
    level=logging.INFO,
    format='%(asctime)s: %(message)s'
)

def get_process_data(limit=20):
    process_list = []

    try:
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'num_threads']):
            try:
                info = proc.info

                process_data = {
                    "cpu": info.get('cpu_percent', 0.0),
                    "memory": info.get('memory_percent', 0.0),
                    "threads": info.get('num_threads', 0)
                }

                name = info.get('name', 'unknown')
                pid = info.get('pid')

                prediction_data = analyze_process(process_data, name)

                if prediction_data and prediction_data["prediction"] == "SUSPICIOUS":
                    logging.info(f"Suspicious Process Detected -> {name} (PID: {pid})")

                process_list.append({
                    "name": name,
                    "pid": pid,
                    "cpu": process_data["cpu"],
                    "memory": process_data["memory"],
                    "threads": process_data["threads"],
                    **(prediction_data or {})
                })

            except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess):
                continue

    except Exception as e:
        logging.critical(f"Critical Error Occurred -> {str(e)}")

    process_list = sorted(process_list, key=lambda k: k.get('cpu', 0), reverse=True)[:limit]

    timestamp = time.time()
    for proc in process_list:
        proc["timestamp"] = timestamp

    return process_list


def monitor_loop(interval=5):
    while True:
        get_process_data()
        time.sleep(interval)