import time
import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/v1/telemetry")
def get_cognitive_telemetry():
    """Generates robust, crash-proof physics telemetry telemetry streams."""
    try:
        base_rpm = 1500.0
        rpm = base_rpm + random.uniform(-40.0, 40.0)
        
        # 5% chance to trigger an anomaly state phase
        inject_anomaly = random.random() < 0.05
        
        if inject_anomaly:
            vibration = 4.5 + random.uniform(1.0, 3.0)
            health_index = random.uniform(40.0, 65.0)
            status = "CRITICAL_ANOMALY"
        else:
            vibration = 1.2 + random.uniform(-0.2, 0.3)
            health_index = random.uniform(96.5, 99.9)
            status = "NOMINAL"

        return {
            "timestamp": float(time.time()),
            "rpm": float(round(rpm, 2)),
            "vibration": float(round(vibration, 3)),
            "health_index": float(round(health_index, 1)),
            "status": str(status),
            "prediction": "BEARING_FAILURE_RISK" if inject_anomaly else "HEALTHY"
        }
    except Exception as e:
        # Fallback safe payload structure so the service NEVER crashes the container thread
        return {
            "timestamp": float(time.time()),
            "rpm": 1500.0,
            "vibration": 1.2,
            "health_index": 98.0,
            "status": "NOMINAL",
            "prediction": "HEALTHY"
        }