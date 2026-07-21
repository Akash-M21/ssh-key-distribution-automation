---

```markdown
# 🔐 SSH Key Distribution Automation

![Python Version](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat&logo=python&logoColor=white)
![Ansible](https://img.shields.io/badge/Ansible-Ready-EE0000?style=flat&logo=ansible&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Supported-FCC624?style=flat&logo=linux&logoColor=black)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Automate passwordless SSH authentication across multiple Linux servers using Python, preparing multi-node infrastructure for seamless Ansible orchestration.

---

## 📌 Overview

Managing SSH access manually across expanding server environments is repetitive, error-prone, and unsustainable at scale. 

This project provides a modular, lightweight Python automation framework that verifies host connectivity, deploys public SSH keys, handles edge-case execution failures gracefully, and generates actionable summary reports. It eliminates manual key management and acts as a foundation for Ansible node onboarding.

### ✨ Key Features
- **Network Pre-checks:** Automated ICMP/port reachability checks before attempting key copy operations.
- **Secure Handling:** Interactively captures server credentials without storing plaintext passwords using `getpass`.
- **Batch Processing:** Reads target server metadata directly from structured inventory source files (`servers.csv`).
- **Resilient Execution:** Catches execution errors per-host without halting the pipeline.
- **Reporting System:** Terminal-formatted summary breakdown of successful vs. failed operations with failure reasons.
- **Ansible Readiness:** Prepares raw Linux hosts for passwordless Ansible playbook deployments.

---

## 🖼️ Architecture & Workflow

```text
               ┌───────────────────────┐
               │  User Inputs & CSV    │
               └──────────┬────────────┘
                          │
                          ▼
               ┌───────────────────────┐
               │ Verify Reachability   │
               └──────────┬────────────┘
                          │
                   Is Host Reachable?
                 ┌────────┴────────┐
                YES               NO
                 │                 │
                 ▼                 ▼
     ┌──────────────────────┐  ┌──────────────────────┐
     │  Deploy SSH Public   │  │  Log Failure Reason  │
     │  Key via Paramiko    │  └──────────────────────┘
     └──────────┬───────────┘
                │
                └─────────┬────────┘
                          │
                          ▼
               ┌───────────────────────┐
               │ Print Summary Report  │
               └──────────┬────────────┘
                          │
                          ▼
             [ Ready for Ansible Control ]

```

---

## 📂 Repository Structure

```text
ssh-key-distribution-automation/
│
├── main.py                 # Core application entry point
├── config.py               # Application configuration & default paths
├── ping.py                 # Network reachability verification module
├── ssh_copy.py             # SSH key distribution logic
├── report.py               # Summary report generator module
├── servers.csv             # Target inventory configuration
├── requirements.txt        # Python dependency manifest
├── LICENSE                 # MIT License file
└── README.md               # Documentation

```

---

## 🛠️ Tech Stack & Requirements

* **Language:** Python 3.8+
* **Core Libraries:** `paramiko`, `getpass`, `csv`
* **Target OS:** Linux (Ubuntu/Debian, RHEL/CentOS/Rocky), macOS
* **Prerequisites:** OpenSSH Client, existing SSH keypair (`id_rsa` / `id_rsa.pub`)

---

## ⚙️ Quick Start

### 1. Clone & Set Up Environment

```bash
# Clone repository
git clone [https://github.com/](https://github.com/)<your-username>/ssh-key-distribution-automation.git
cd ssh-key-distribution-automation

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

```

### 2. Configure SSH Keys & Inventory

If you do not have an existing SSH key pair, generate one:

```bash
ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N ""

```

Update `servers.csv` with your target server details:

```csv
hostname,ip
server-web-01,192.168.1.10
server-db-01,192.168.1.20
server-app-01,192.168.1.30

```

---

## 🚀 Execution

Run the script and provide the initial remote host credentials when prompted:

```bash
python main.py

```

### 📊 Sample Output

```text
==================================================
           SSH KEY DISTRIBUTION REPORT            
==================================================

SUCCESSFUL DEPLOYMENTS
--------------------------------------------------
[✓] server-web-01 (192.168.1.10) - Key installed successfully
[✓] server-db-01  (192.168.1.20) - Key installed successfully

FAILED DEPLOYMENTS
--------------------------------------------------
[✗] server-app-01 (192.168.1.30) - Host Unreachable (Ping Timeout)

--------------------------------------------------
EXECUTION SUMMARY
--------------------------------------------------
Total Hosts Processed : 3
Successful           : 2
Failed               : 1
==================================================

```

---

## 💡 Practical Use Cases

* **Cloud VM Onboarding:** Mass-configuring fresh EC2, Compute Engine, or Azure instances after deployment.
* **Ansible Bootstrap:** Setting up passwordless access on targeted nodes before running initial playbooks.
* **DevOps Lab Environment:** Quickly provisioning access controls across heterogeneous Linux lab instances.

---

## 📈 Future Enhancements

* [ ] Add parallel host processing via Python `concurrent.futures`.
* [ ] Support YAML/Dynamic Inventory sources.
* [ ] Add structured log output to disk (`/logs/execution.log`).
* [ ] Generate standard Ansible inventory files (`hosts.ini`) post-successful execution.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 👨‍💻 Author

**Akash M**

*DevOps & Infrastructure Automation*

[GitHub Profile](https://www.google.com/search?q=https://github.com/%3Cyour-username%3E) | [LinkedIn Profile](https://www.google.com/search?q=https://linkedin.com/in/%3Cyour-profile%3E)

```

```
