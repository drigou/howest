# Kubernetes deployment of model animal-cnn

Some CLI which can come in handy (using a k3d cluster)

```bash
# List all the clusters on k3d
k3d cluster list 

# Start a cluster
k3d cluster start <cluster_name>

# Stop a cluster
k3d cluster stop <cluster_name>
```

Some kubectl CLI which can be usefull

```bash
# Get a namespace
kubectl get namespaces
kubectl get ns

# Create a namespace
kubectl create namespace <namespace-name>

# Check which namespace is the current namespace
kubectl config view --minify | findstr namespace
kubectl config view --minify | grep namespace

# Set a default namespace
kubectl config set-context --current --namespace <my-namespace>

# Create service / deployment
kubectl apply -f ./inference/kubernetes/deployment.yaml

# Check for deployments / service
kubectl get deployments
kubectl get services

# Port forward service 
kubectl port-forward services/svc-vue-docker 8080:80 

# Other commands 
kubectl get nodes 
kubectl describe node <node-name> 
kubectl get nodes --show-labels=true
```