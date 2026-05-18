[![DevSecOps Automated Security Scan](https://github.com/annasalakram/automated-devsecops-pipeline/actions/workflows/security-scan.yml/badge.svg)](https://github.com/annasalakram/automated-devsecops-pipeline/actions/workflows/security-scan.yml)

# Enterprise Automated DevSecOps Pipeline
> Automated DevSecOps pipeline using GitHub Actions, Bandit (SAST), and Gitleaks to detect hardcoded secrets and code vulnerabilities.

## 🚀 Overview
This project demonstrates the implementation of automated security testing (**Shift-Left Security**) integrating a robust GitHub Actions CI/CD pipeline. Every code change is dynamically scanned in real-time to proactively mitigate security risks and enforce compliance metrics before deployment into production environments.

## 🛠️ Integrated Security Tools
* **Gitleaks:** Executes comprehensive commit history auditing to detect and prevent the leakage of sensitive high-entropy credentials, including API Keys, access tokens, or SSH private keys.
* **Bandit:** A specialized Static Application Security Testing (SAST) framework for Python, engineered to scan abstract syntax trees (AST) and intercept structural programming vulnerabilities, such as SQL Injection and insecure inputs.


