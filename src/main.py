import psutil
from ai_detector import analyze_process

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

                result = analyze_process(process_data, name)

                if result is None:
                    continue

                process_list.append({
                    "name": name,
                    "pid": pid,
                    "cpu": process_data["cpu"],
                    "memory": process_data["memory"],
                    "threads": process_data["threads"],
                    "prediction": result.get("prediction", "SAFE"),
                    "confidence": result.get("confidence", 0),
                    "threat": result.get("threat", "LOW"),
                    "reason": result.get("reason", "normal")
                })

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

        process_list = sorted(process_list, key=lambda x: x.get("cpu", 0), reverse=True)[:limit]
        return process_list

    except Exception as e:
        print("Monitor Error:", e)
        return []


def main():
    processes = get_process_data(limit=20)
    for proc in processes:
        print(proc)


if __name__ == "__main__":
    main()