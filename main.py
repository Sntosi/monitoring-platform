from fastapi import FastAPI
import time
import random
import psutil

app = FastAPI(title="Monitoring Demo App")

@app.get("/")
def home():
    return {"status": "healthy", "message": "Monitoring Demo App is running!"}

@app.get("/metrics")
def metrics():
    # Real system metrics
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    
    return {
        "cpu_usage_percent": round(cpu, 2),
        "memory_usage_percent": round(memory, 2),
        "disk_usage_percent": round(disk, 2),
        "active_requests": random.randint(10, 200),
        "error_rate": round(random.uniform(0.5, 3.5), 2),
        "uptime_seconds": int(time.time() - 1720000000),
        "timestamp": time.time(),
        "service_name": "voting-app"
    }
