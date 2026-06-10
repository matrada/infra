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
- CpuTasks — platform: Fargate compute environment + job queue `cpu-tasks`
- GpuTasks — planned: EC2 GPU compute environment + queue `gpu-tasks` (Fargate can't attach GPUs)

workload stacks (bucket, ECR repo, roles, job definition) come later — job definitions are queue-independent, the queue is picked at submit time

### parancsok
```bash
uv run cdk bootstrap
uv run cdk synth
uv run cdk diff
uv run cdk deploy
uv run cdk destroy
uv run pytest
```

### egyéb notes
- cdk.context.json is gitignored — it caches VPC/subnet lookups but contains the account ID and network topology, so it's kept out of this public repo. Re-run `cdk synth` to regenerate it locally.