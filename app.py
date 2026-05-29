from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head><title>Meet Hingu | DevOps Pipeline</title>
    <style>
        body { font-family: Arial, sans-serif; background: #0f1117; color: #fff; 
               display: flex; align-items: center; justify-content: center; 
               height: 100vh; margin: 0; }
        .card { text-align: center; padding: 40px; border: 1px solid #1A56DB;
                border-radius: 12px; max-width: 500px; }
        h1 { color: #1A56DB; }
        .badge { background: #1A56DB; padding: 6px 14px; border-radius: 20px; 
                 font-size: 13px; display: inline-block; margin: 4px; }
        .green { color: #22c55e; font-weight: bold; }
    </style>
    </head>
    <body>
    <div class="card">
        <h1>🚀 Meet Hingu</h1>
        <p>DevOps Engineer | GCP | Kubernetes | CI/CD</p>
        <p class="green">✅ Running on GKE — Auto-deployed via CI/CD</p>
        <br>
        <span class="badge">Docker</span>
        <span class="badge">Kubernetes</span>
        <span class="badge">GCP</span>
        <span class="badge">GitHub Actions</span>
        <br><br>
        <p style="color:#888;font-size:13px">Every push to main auto-deploys this app 🔄</p>
    </div>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "version": os.getenv("APP_VERSION", "v1")}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
