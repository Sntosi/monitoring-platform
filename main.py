from fastapi import FastAPI, Response
import time
import random
import psutil

app = FastAPI(title="Monitoring Demo App")

@app.get("/")
def home():
    return {"status": "healthy"}

@app.get("/metrics")
def metrics():
    """Return metrics in proper Prometheus text format"""
    cpu = psutil.cpu_percent(interval=0.1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    metrics_text = f"""# HELP cpu_usage_percent Current CPU usage percentage
# TYPE cpu_usage_percent gauge
cpu_usage_percent {cpu}

# HELP memory_usage_percent Current memory usage percentage
# TYPE memory_usage_percent gauge
memory_usage_percent {memory}

# HELP disk_usage_percent Current disk usage percentage
# TYPE disk_usage_percent gauge
disk_usage_percent {disk}

# HELP active_requests Number of active requests
# TYPE active_requests gauge
active_requests {random.randint(10, 200)}

# HELP error_rate Error rate in percentage
# TYPE error_rate gauge
error_rate {round(random.uniform(0.1, 5), 2)}
"""
    return Response(content=metrics_text, media_type="text/plain")
