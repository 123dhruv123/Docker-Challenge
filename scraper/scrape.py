import psutil
import time
import os

# Ensure the shared directory exists
os.makedirs('/shared', exist_ok=True)

while True:
    # Gather OS Metrics
    cpu_usage = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    
    mem_used_gb = round(mem.used / (1024**3), 2)
    mem_total_gb = round(mem.total / (1024**3), 2)
    
    # Generate HTML
    html_content = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>System Metrics</title>
            <style>
                body {{ font-family: Arial, sans-serif; padding: 40px; background-color: #f4f4f9; }}
                .card {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); max-width: 400px; }}
                h2 {{ color: #333; margin-top: 0; }}
                .metric {{ font-size: 1.2em; margin: 10px 0; }}
                .footer {{ margin-top: 20px; font-size: 0.8em; color: #777; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h2>Live OS Metrics</h2>
                <div class="metric">🖥️ <strong>CPU Usage:</strong> {cpu_usage}%</div>
                <div class="metric">🧠 <strong>Memory Usage:</strong> {mem.percent}%</div>
                <div style="font-size: 0.9em; color: #555;">({mem_used_gb} GB used of {mem_total_gb} GB)</div>
                <div class="footer">Last updated: {time.ctime()}</div>
            </div>
        </body>
    </html>
    """
    
    # Write to the shared volume
    with open('/shared/index.html', 'w') as f:
        f.write(html_content)
        
    # Wait 4 seconds (psutil.cpu_percent takes 1 second, so loop is 5s)
    time.sleep(4)
