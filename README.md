# 🚀 Production CI/CD Pipeline on GCP

**Built by Meet Hingu** | DevOps Engineer | GCP | Kubernetes | Terraform

---

## 🏗️ Pipeline Architecture

```
GitHub Push (main)
      ↓
GitHub Actions (CI)
  → Build Docker image
  → Security scan (Trivy)
  → Run tests
      ↓
GCP Artifact Registry
  → Versioned image stored
      ↓
GKE — Google Kubernetes Engine (CD)
  → Rolling update deployment
  → HPA auto-scaling (2–10 replicas)
  → Health checks via liveness/readiness probes
      ↓
Live App — External LoadBalancer IP
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Source Control | GitHub |
| CI/CD | GitHub Actions |
| Containerization | Docker |
| Security Scanning | Trivy |
| Image Registry | GCP Artifact Registry |
| Orchestration | Kubernetes (GKE) |
| Auto-scaling | HPA (CPU-based) |
| Cloud | Google Cloud Platform |

---

## 📁 Project Structure

```
devops-cicd-pipeline/
├── app.py                        # Flask application
├── Dockerfile                    # Container definition
├── requirements.txt
├── k8s/
│   ├── deployment.yaml           # K8s Deployment (2 replicas, rolling update)
│   ├── service.yaml              # LoadBalancer Service
│   └── hpa.yaml                  # HPA (scale 2–10 on 70% CPU)
└── .github/
    └── workflows/
        └── cicd.yml              # Full CI/CD pipeline
```

---

## ⚡ Key Features

- ✅ **Automated CI/CD** — every push to main triggers full pipeline
- ✅ **Security scanning** — Trivy blocks critical vulnerabilities before deploy
- ✅ **Zero-downtime deployments** — rolling update strategy
- ✅ **Auto-scaling** — HPA scales pods from 2 to 10 based on CPU
- ✅ **Health checks** — liveness & readiness probes on every pod
- ✅ **Image versioning** — every image tagged with git commit SHA

---

## 🔧 Setup

### Prerequisites
- GCP Account with billing enabled
- `gcloud` CLI installed
- `kubectl` installed
- Docker installed

### Deploy in 4 steps

```bash
# 1. Create GKE cluster
gcloud container clusters create devops-cluster \
  --zone=asia-south1-a --num-nodes=2 --machine-type=e2-medium

# 2. Create Artifact Registry
gcloud artifacts repositories create devops-repo \
  --repository-format=docker --location=asia-south1

# 3. Build & push image manually (first time)
docker build -t asia-south1-docker.pkg.dev/PROJECT_ID/devops-repo/devops-app:v1 .
docker push asia-south1-docker.pkg.dev/PROJECT_ID/devops-repo/devops-app:v1

# 4. Deploy to GKE
kubectl apply -f k8s/
kubectl get service devops-app-service  # Get external IP
```

### Add GitHub Secret
1. GCP → IAM → Service Accounts → Create (`github-actions-sa`)
2. Roles: `Kubernetes Engine Developer` + `Artifact Registry Writer`
3. Download JSON key
4. GitHub repo → Settings → Secrets → `GCP_SA_KEY` → paste JSON

---

*This pipeline runs the same architecture I use at scale for live-streaming infrastructure at Reliance Jio, serving millions of concurrent users.*

---
⭐ Star this repo if it helped you!
