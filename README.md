# video-mp3-services

## Local Installation

**Requirements**:

- Docker: [https://www.docker.com/get-started/](https://www.docker.com/get-started/)
- Kubernetes CLI: [https://kubernetes.io/docs/tasks/tools/](https://kubernetes.io/docs/tasks/tools/)
- Minikube (For local installation): [https://minikube.sigs.k8s.io/docs/start/](https://minikube.sigs.k8s.io/docs/start/)
- k9s (For cluster management): [https://github.com/derailed/k9s](https://github.com/derailed/k9s)

**Internal Host Setup:**

- Go to the hosts folder:

```bash
sudo nvim /etc/hosts
```

- Add this to the hosts file:

```
127.0.0.1 kubernetes.docker.internal
127.0.0.1 mp3converter.com
127.0.0.1 rabbitmq-manager.com
```

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
