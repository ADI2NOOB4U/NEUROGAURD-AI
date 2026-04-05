import streamlit as st
import psutil
from ai_detector import analyze_process   # ✅ FIXED
import pandas as pd
import time

st.set_page_config(layout="wide")

# Sidebar
menu = st.sidebar.radio("Navigation", ["Dashboard", "Logs"])
auto_refresh = st.sidebar.toggle("Auto Refresh", value=True)
refresh_interval = st.sidebar.slider("Refresh Interval (sec)", 1, 60, 2)


def get_process_data():
    data = []

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'num_threads']):
        try:
            info = proc.info

            process_data = {
                "cpu": info.get("cpu_percent", 0),
                "memory": info.get("memory_percent", 0),
                "threads": info.get("num_threads", 0)
            }

            # ✅ USE CORRECT FUNCTION
            result = analyze_process(process_data, info.get("name"))

            if not result:
                continue

            data.append({
                "Name": info.get("name", "unknown"),
                "PID": info.get("pid", 0),
                "CPU %": process_data["cpu"],
                "Memory %": process_data["memory"],
                "Threads": process_data["threads"],
                "Prediction": result.get("prediction", "SAFE"),
                "Confidence": result.get("confidence", 0),
                "Threat": result.get("threat", "LOW")
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    return pd.DataFrame(data)


def highlight(row):
    if row["Threat"] == "HIGH":
        return ['background-color: red; color: white'] * len(row)
    else:
        return ['background-color: green; color: white'] * len(row)


def dashboard():
    st.title("🧠 NeuroGuard AI - Dashboard")

    df = get_process_data()

    if not df.empty:
        styled_df = df.style.apply(highlight, axis=1)
        st.dataframe(styled_df, use_container_width=True)

        suspicious = (df["Threat"] == "HIGH").sum()   # ✅ FIXED COUNT
        total = len(df)

        st.success(f"Total: {total} | High Threat: {suspicious}")
    else:
        st.warning("No data")


def logs():
    st.title("📜 Logs")

    try:
        with open("monitoring.log", "r") as f:
            logs = f.readlines()[-50:]
        st.text("".join(logs))
    except:
        st.warning("No logs found")


# Routing
if menu == "Dashboard":
    dashboard()
elif menu == "Logs":
    logs()

# Auto refresh
if auto_refresh:
    time.sleep(refresh_interval)
    st.rerun()