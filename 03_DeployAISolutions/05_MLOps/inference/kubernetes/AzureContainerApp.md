# Deploy on an azure container app

```bash
# Create azure container registry
az acr create --name myappacrdg --sku Basic --location westeurope

# Tag docker image
docker tag drgou/animal-cnn:v1.0.0 myappacrdg.azurecr.io/animal-cnn:1.0.0

# Push to azure container registry
docker push myappacrdg.azurecr.io/animal-cnn:1.0.0

# Create container app environment
az containerapp env create --name myapp-env-dg --location westeurope

# Deploy container app 
az containerapp create --name animal-cnn \
    --environment myapp-env-dg \
    --image myappacrdg.azurecr.io/animal-cnn:1.0.0 \ 
    --registry-server myappacrdg.azurecr.io \
    --target-port 8000 \
    --ingress external \
    --registry-username <username> \
    --registry-password <password>

# Get username and password
az acr credential show myappacrdg 

# Some other code which is helpfull 
az config get 
```