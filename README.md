# video-mp3-services

## Local Installation

**Requirements**:

- Docker: [https://www.docker.com/get-started/](https://www.docker.com/get-started/)
- Kubernetes CLI: [https://kubernetes.io/docs/tasks/tools/](https://kubernetes.io/docs/tasks/tools/)
- Minikube (For local installation): [https://minikube.sigs.k8s.io/docs/start/](https://minikube.sigs.k8s.io/docs/start/)
- k9s (For cluster management): [https://github.com/derailed/k9s](https://github.com/derailed/k9s)

**Setup Ingress For Gateway:**

- Enable Ingress in Kubernetes for Gateway:

```bash
minikube addons list
minikube addons enable ingress
```

- Activate Ingress in Kubernetes:

```bash
minikube tunnel
```
