# Regression test 1: vulnerable base image

## Change
Base image changed from `python:3.12-slim` to `python:3.8-slim-buster` on branch `test/vulnerable-base`, submitted as a pull request.

## Expected
The image security gate blocks the change.

## Result
- `image-security` failed at the Trivy step (CRITICAL severity, unfixed findings excluded).
- `test`, `gitleaks` and `checkov` passed, so only the supply-chain check caught it.
- Trivy also warned that Debian 10 is end-of-life, so detection may be incomplete.

## Evidence
- Screenshots: (add)
- Trivy report: (add file or excerpt)
- Example findings: (CVE IDs and packages)

## Conclusion
A vulnerable or unsupported base image cannot pass CI. With branch protection requiring this check, it cannot be merged.