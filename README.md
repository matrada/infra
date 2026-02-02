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
uv run cdk synth     # generate cloudformation
uv run cdk diff      # preview changes
uv run cdk deploy    # ship it
uv run cdk destroy   # tear down
```

### egyéb notes
- cdk.context.json gitignored 