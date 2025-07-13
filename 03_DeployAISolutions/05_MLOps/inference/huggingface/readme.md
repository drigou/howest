# Deploy and upload to huggingface

````bash
# install huggingface cli
pip install huggingface-cli

# login 
huggingface-cli login --token <auth_token>

# Create repo
huggingface-cli repo create drgou/howest-deployathome --type model

```