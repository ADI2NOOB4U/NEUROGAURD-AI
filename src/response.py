def format_response(process_info):
    cpu = round(process_info.get("cpu", 0), 2)
    memory = round(process_info.get("memory", 0), 2)

    confidence = min(max(process_info.get("confidence", 0), 0), 100)

    prediction = process_info.get("prediction", "SAFE")

    status_emoji = "✅" if prediction == "SAFE" else "⚠️"

    return {
        "Process": process_info.get("name", "unknown"),
        "PID": process_info.get("pid", -1),
        "CPU (%)": cpu,
        "Memory (%)": memory,
        "Threads": process_info.get("threads", 0),
        "Status": f"{prediction} {status_emoji}",
        "Confidence": confidence,
        "Threat Level": process_info.get("threat", "LOW"),
        "Reason": process_info.get("reason", "normal")
    }


def format_multiple(process_list):
    return [format_response(process) for process in process_list if process]