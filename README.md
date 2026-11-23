# KubeShield X

A Kubernetes security and compliance operations platform: prevention, detection and evidence in one local-first project.

## Status
- [x] Phase 1: Kind cluster, namespaces, quotas, RBAC, hardened sample app
- [ ] Phase 2: Helm and GitOps
- [ ] Phase 3: DevSecOps pipeline
- [ ] Phase 4: Kubernetes security (Falco, Kyverno)
- [ ] Phase 5: Observability
- [ ] Phase 6-8: Security operations, attack simulations, EKS

## Architecture (Phase 1)

```
localhost:8080 -> NodePort 30080 -> Service -> security-api pods (x2)
                                              (non-root, read-only FS,
                                               caps dropped, limits set)
Kind cluster: 1 control-plane + 2 workers
Namespaces: app | security | monitoring
```

## Quick start
```bash
kind create cluster --config kubernetes/kind-config.yaml
docker build -t kubeshield/security-api:0.1.0 app/security-api/
kind load docker-image kubeshield/security-api:0.1.0 --name kubeshield
kubectl apply -f kubernetes/namespaces/
kubectl apply -f kubernetes/rbac/
kubectl apply -f kubernetes/app/
curl localhost:8080/health
```