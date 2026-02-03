# infra

personal aws infra cdk stack ramblings

## notes

### prerequisites
- aws cli
- node.js
- uv

### nodejs/npm
```bash
npm install -g aws-cdk
cdk --version
```

### init cdk repo
```bash
cdk init --language python
```

### switch to uv:
```bash
rm requirements*.txt source.bat
# create pyproject.toml with aws-cdk-lib, constructs
uv sync
```

### key files
- app.py — entry point, instantiates stacks
- infra/*.py — stack definitions
- cdk.json — tells cdk how to run app

### stacks
- BatchExtract

### parancsok
```bash
uv run cdk bootstrap
uv run cdk synth
uv run cdk diff
uv run cdk deploy
uv run cdk destroy
```

### egyéb notes
- cdk.context.json gitignored 