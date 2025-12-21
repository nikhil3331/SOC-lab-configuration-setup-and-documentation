Project Overview:

This project is a fully-functional SOC simulation environment built to showcase real-world, hands-on cybersecurity skills focusing on Detection, log analysis & correlation, incident response, logs pipeline & infrastructure rather than attack execution 

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
