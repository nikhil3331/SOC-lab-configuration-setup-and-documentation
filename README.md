NOTE: This repository serves exclusively as the technical documentation for my "SOC Lab" environment and configuration. For the full project overview, live demonstrations, and detailed case studies, please contact me for the link to my Portfolio.

Project Overview:

This project is a fully-functional SOC simulation environment built to showcase real-world, hands-on cybersecurity skills focusing on Detection, log analysis & correlation, incident response, logs pipeline & infrastructure rather than attack execution.


The environment consists of a Windows Server VM and a Docker-based application stack hosted on a Kali VM, with all telemetry centrally collected and managed through Splunk Enterprise which is also hosted in Kali VM. This project emphasizes how logs are generated, forwarded, indexed, and validated across heterogeneous systems.

Core areas covered include:-

1. Splunk Enterprise deployment and administration

2. Windows server endpoint logging using Splunk Universal Forwarder and Sysmon

3. Docker container stack log forwarding via HTTP Event Collector (HEC)

4. Reverse proxy access logging and DVWA web application telemetry

5. Log analysis and detection search queries in splunk

This repository is flexible, one can scale up with more containers according to their own requirements,this serves as a technical reference for building a SOC-ready lab environment, closely mirroring how real security monitoring platforms are deployed and maintained.

Goal:
The goal was to create an environment where realistic attacks can be executed and custom detections can be developed.


🔐 Security Disclaimer

- This repository is created strictly for educational, research, and defensive security practice purposes.


⚠️ Intended Use

This project simulates vulnerable services, attack traffic, and log generation to support:

- SOC analyst training

- SIEM detection engineering

- Incident investigation workflows

- Blue-team skill development

- All attacks, beacons, and log simulations are performed inside an isolated lab environment using virtual machines and containers.


🚫 Prohibited Use

The techniques, configurations, and scripts in this repository must not be used against:

- Production systems

- Networks you do not own

- Systems without explicit written authorization

- Any misuse of the content is solely the responsibility of the user.


🔑 Secrets & Credentials

- No real credentials, tokens, or secrets are stored in this repository.

- All sensitive values (e.g., Splunk HEC tokens, URLs, credentials) are injected at runtime via:

Environment variables

- Local .env files (explicitly excluded from version control)

- Placeholder values shown in configuration files are non-functional examples only.


🌐 Network Isolation

The lab is designed to run on:

- Private Docker bridge networks

- Local virtual machines

It should never be exposed directly to the public internet.

If internet access is enabled, it is limited to package downloads and controlled testing only.


🧪 Vulnerable Components

This project intentionally deploys insecure and vulnerable applications (e.g., DVWA) to:

- Generate realistic security telemetry

- Validate detection and alerting logic

These components are unsafe by design and must be treated as disposable lab assets.


📚 Responsibility Notice

By using this repository, you acknowledge that:

- You understand the risks of running vulnerable software

- You will operate the lab in a controlled and authorized environment

- You accept full responsibility for any actions performed using this material

