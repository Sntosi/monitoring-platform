from fastapi import FastAPI
import time
import random

app = FastAPI(title="Monitoring Demo App")

@app.get("/")
def home():
    return {"status": "healthy", "app": "monitoring-demo"}

@app.get("/metrics")
def metrics():
    return {
        "cpu_usage_percent": round(random.uniform(10, 95), 2),
        "memory_usage_percent": round(random.uniform(20, 90), 2),
        "active_requests": random.randint(5, 150),
        "error_rate": round(random.uniform(0.1, 4.5), 2),
        "uptime_seconds": int(time.time() - 1720000000),
        "timestamp": time.time()
    }
