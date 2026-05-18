[![DevSecOps Automated Security Scan](https://github.com/annasalakram/automated-devsecops-pipeline/actions/workflows/security-scan.yml/badge.svg)](https://github.com/annasalakram/automated-devsecops-pipeline/actions/workflows/security-scan.yml)

# Enterprise Automated DevSecOps Pipeline
> Automated DevSecOps pipeline using GitHub Actions, Bandit (SAST), and Gitleaks to detect hardcoded secrets and code vulnerabilities.

## 🚀 Overview
This project demonstrates the implementation of automated security testing (**Shift-Left Security**) integrating a robust GitHub Actions CI/CD pipeline. Every code change is dynamically scanned in real-time to proactively mitigate security risks and enforce compliance metrics before deployment into production environments.

## 🛠️ Integrated Security Tools
* **Gitleaks:** Executes comprehensive commit history auditing to detect and prevent the leakage of sensitive high-entropy credentials, including API Keys, access tokens, or SSH private keys.
* **Bandit:** A specialized Static Application Security Testing (SAST) framework for Python, engineered to scan abstract syntax trees (AST) and intercept structural programming vulnerabilities, such as SQL Injection and insecure inputs.

## 📊 Security Audit Metrics (Pre-Remediation Log)

During the initial pipeline simulation, the automated Bandit engine successfully intercepted and flagged the following vulnerabilities in the legacy code (`app.py`):

| Test ID | Severity | Confidence | Vulnerability Type | Target Line | CWE Reference | Status |
| :---: | :---: | :---: | :--- | :---: | :---: | :---: |
| **B105** | 🟡 LOW | MEDIUM | Possible hardcoded password / credential string | Line 7 | [CWE-798](https://cwe.mitre.org/data/definitions/798.html) | 🛡️ Fixed |
| **B608** | 🟠 MEDIUM | LOW | Hardcoded SQL expressions (SQL Injection vector) | Line 24 | [CWE-89](https://cwe.mitre.org/data/definitions/89.html) | 🛡️ Fixed |

## 🔍 Vulnerability Brief & Remediation Engineering
1. **B105 (Hardcoded Password):** Bandit detected an exposed plaintext infrastructure key (`AWS_SECRET_KEY`). 
   * *Remediation applied:* Extracted the sensitive data out of the source code and refactored the script to leverage secure environment variables via `os.getenv()`.
2. **B608 (Insecure SQL String Construction):** Bandit identified risky string formatting inside an execute query wrapper, exposing the database to input manipulation.
   * *Remediation applied:* Implemented robust query parameterization (`?` placeholders) to properly neutralize user input, shifting the codebase to a fully hardened state.

> 💡 **Professional Outcome:** Following these remediation commits, the automated pipeline executed a clean scan, successfully transitioning this enterprise repository to a global **PASSING** status.

## 📂 How to Access the Live Dashboard

> 💡 **Note for Security Professionals:**
> Since this is an open-source project, the interactive security metrics are fully visible to the public. To inspect the live vulnerability tracking system, please follow these steps:
>
> 1. Navigate to the top navigation bar of this repository.
> 2. Click on the **[🛡️ Security]** tab.
> 3. Under the *Vulnerability alerts* section in the left sidebar, select **[Code scanning]**.

## 🔄 Pipeline Architecture & Security Workflow
Here is how the automated DevSecOps pipeline orchestrates security checks on every code change:

```mermaid
graph TD
    A["Developer Action: Push / PR"] --> B("GitHub Actions Runner")
    
    subgraph CI_Pipeline ["CI Pipeline: Security Auditing"]
        B --> C["Step 1: Checkout Code"]
        C --> D["Step 2: Gitleaks Secret Scanner"]
        D --> E["Step 3: Setup Python Environment"]
        F["Step 4: Bandit SAST Scan"]
        E --> F
    end

    subgraph Feedback_Loop ["Vulnerability Feedback Loop"]
        F --> G["bandit_report.txt"]
        F --> H["bandit_results.sarif"]
    end

    G --> I["GitHub Artifacts Storage"]
    H --> J["GitHub Advanced Security Tab"]
    
    J --> K{"Code Scanning Alerts"}
    K --> L["Automatically Closed as Fixed"]
