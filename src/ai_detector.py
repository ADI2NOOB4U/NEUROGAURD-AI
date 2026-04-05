import logging
from detector import predict

logger = logging.getLogger(__name__)

safe_processes = [
    "system", "system idle process", "svchost.exe",
    "csrss.exe", "wininit.exe", "services.exe",
    "lsass.exe", "dwm.exe", "explorer.exe",
    "registry", "smss.exe"
]

suspicious_keywords = ["crypto", "miner", "hack", "inject", "temp"]


def analyze_process(process_data, process_name):
    process_name = (process_name or "").lower().strip()

    # ✅ Whitelist
    if any(safe in process_name for safe in safe_processes):
        return {
            "prediction": "SAFE",
            "confidence": 5,
            "threat": "LOW",
            "reason": "trusted_system_process"
        }

    if not all(key in process_data for key in ("cpu", "memory", "threads")):
        return {
            "prediction": "SAFE",
            "confidence": 0,
            "threat": "LOW",
            "reason": "invalid_data"
        }

    cpu = process_data["cpu"]
    memory = process_data["memory"]
    threads = process_data["threads"]

    # Ignore low activity
    if cpu < 5 and memory < 5:
        return {
            "prediction": "SAFE",
            "confidence": 10,
            "threat": "LOW",
            "reason": "low_activity"
        }

    # 🔽 RULES
    rule_checks = []

    if cpu > 90:
        rule_checks.append("high_cpu")

    if memory > 85:
        rule_checks.append("high_memory")

    if threads > 300:
        rule_checks.append("high_threads")

    for keyword in suspicious_keywords:
        if keyword in process_name:
            rule_checks.append(f"suspicious_keyword_{keyword}")

    # ML (optional, low weight)
    try:
        ml_result = predict(process_data)
        ml_prediction = ml_result["prediction"]
    except:
        ml_prediction = "SAFE"

    # ✅ ONLY VERY HIGH = RED
    if len(rule_checks) >= 2:
        threat = "HIGH"
        final_prediction = "SUSPICIOUS"
        confidence = 80
    elif len(rule_checks) == 1:
        threat = "MEDIUM"
        final_prediction = "SAFE"   # 👈 still GREEN
        confidence = 50
    else:
        threat = "LOW"
        final_prediction = "SAFE"
        confidence = 20

    return {
        "prediction": final_prediction,
        "confidence": confidence,
        "threat": threat,
        "reason": ", ".join(rule_checks) if rule_checks else "normal"
    }