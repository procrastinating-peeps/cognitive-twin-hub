# Turbine Digital Twin & Real-Time Telemetry Dashboard

A lightweight, offline-first IoT Digital Twin dashboard that simulates real-time industrial turbine telemetry. It handles smooth 60 FPS rendering and data visualization using zero-dependency browser APIs, complete with an automated anomaly detection system.

## 💡 Why I Built This

Most modern dashboards rely heavily on massive, resource-guzzling 3D frameworks and external CDNs that completely fall apart if the network drops or if they are run on low-spec field hardware. 

I built this project to prove you can create a highly responsive, visually rich mission control room using pure, native web technologies. By moving complex mathematical geometry calculations directly onto the browser's native hardware-accelerated loops, this dashboard maintains a flawless 60 FPS refresh cycle on a tiny memory footprint (<12MB)—even entirely offline.

## 🛠️ Technical Highlights & Features

* **Custom Isometric Canvas Engine:** Built a lightweight rendering pipeline using the HTML5 Canvas API. It translates structural vectors into an isometric space with smooth shading and friction glow effects, running smoothly on the physical GPU without heavy 3D engine overhead.
* **Zero-Dependency SVG Charting:** Instead of pulling in massive chart charting libraries, the real-time timeline graph maps data directly into dynamic SVG paths, eliminating main-thread layout thrashing.
* **Real-Time Anomaly Detection & HUD Alarms:** A background execution clock evaluates data points every 800ms. If the turbine speeds surge into unsafe limits (>1535 RPM), the entire UI enters a flashing warning state and dynamically injects emergency logs.
* **Interactive Shading Controls:** Includes a hardware diagnostic deck to toggle the turbine on the fly between solid physical rendering and an X-Ray wireframe mode for structural troubleshooting.
* **Instant Snapshot Data Exporter:** Features a serialization layer that caches rolling runtime telemetry points, letting users download data streams into a structured `.csv` file instantly.

## 📐 The Architecture

* **Frontend:** Vanilla HTML5, Canvas API (2D/Isometric context), Native SVG Path Matrices, Tailwind CSS.
* **Backend Pipeline:** Python (FastAPI), Docker virtualization, webhook dispatch simulators.

## 🚀 Running it Locally

### 1. Clone the repository
```bash
git clone [https://github.com/procrastinating-peeps/cognitive-twin-hub.git](https://github.com/procrastinating-peeps/cognitive-twin-hub.git)
cd cognitive-twin-hub
