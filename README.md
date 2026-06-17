<h1 align="center">
  <img
    src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=32&pause=1000&color=ffffff&center=true&vCenter=true&width=750&lines=Pulse+-+Your+System's+Heartbeat"
    alt="Pulse - Your System's Heartbeat"
  />
</h1>

<p align="center"><i>Real-time system monitoring from your terminal.</i></p>

---

Pulse is a **terminal-based system monitoring dashboard built in Python**, designed to provide real-time insights into system performance through an interactive and visually organized interface.

The project focuses on **Python package management, operating system APIs, system resource monitoring, modular software architecture, terminal user interfaces, dataclasses, and real-time dashboard development**, while leveraging powerful third-party libraries to create a practical monitoring utility.

> Note: Pulse is a learning-focused systems programming project that continuously monitors key system metrics and presents them through a live-updating dashboard directly within the terminal.

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python_3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.x"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Category-System_Monitoring-22c55e?style=for-the-badge" alt="System Monitoring"/>
  <img src="https://img.shields.io/badge/Type-Terminal_Dashboard-f97316?style=for-the-badge" alt="Terminal Dashboard"/>
  <img src="https://img.shields.io/badge/Domain-System_Utilities-6366f1?style=for-the-badge" alt="System Utilities"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Live_Refresh-Supported-2563eb?style=for-the-badge" alt="Live Refresh"/>
  <img src="https://img.shields.io/badge/Monitoring-Real_Time-7c3aed?style=for-the-badge" alt="Real Time Monitoring"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-success?style=for-the-badge" alt="License"/>
</p>

## Features

1. ### CPU Monitoring

   * Displays current CPU utilization
   * Updates continuously in real time
   * Clean and readable terminal presentation
   * Built using operating system performance APIs

2. ### Memory Monitoring

   * Displays total memory capacity
   * Shows used and available memory
   * Reports memory utilization percentage
   * Live-updating statistics

3. ### Disk Monitoring

   * Displays total disk capacity
   * Tracks used and free storage
   * Reports disk usage percentage
   * Real-time storage information

4. ### Process Monitoring

   * Displays top running processes
   * Shows process IDs (PID)
   * Displays CPU consumption per process
   * Automatically updates process information

5. ### Network Monitoring

   * Tracks bytes sent and received
   * Displays overall network activity
   * Updates continuously alongside system metrics
   * Integrated into the dashboard interface

6. ### Live Dashboard Interface

   * Built using Rich layouts and panels
   * Real-time dashboard refresh
   * Structured terminal-based UI
   * Supports continuous monitoring sessions

## Project Architecture

<p align="center">
  <img src="assets/dir-structure.png" alt="Project Structure" width="300">
</p>

## Tech Stack

<div align="center">

| Component         | Technology   |
| ----------------- | ------------ |
| Language          | Python 3     |
| System Monitoring | psutil       |
| Terminal UI       | rich         |
| Data Models       | dataclasses  |
| Version Control   | Git + GitHub |

</div>

## Build & Run Instructions

### Requirements

* Python 3.10 or higher
* Git (for cloning the repository)

### Clone the Repository

```bash
git clone https://github.com/abhi-saurav-saroya/pulse.git
cd pulse
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python main.py
```

or

```bash
python3 main.py
```

### Usage

1. Launch Pulse.
2. The dashboard will start automatically.
3. Monitor CPU, Memory, Disk, Network, and Process activity.
4. Watch metrics update in real time.
5. Press **Ctrl + C** to exit the dashboard.

<p align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
</p>

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer" alt="Footer"/>

<i>Built to learn, designed to monitor, engineered one heartbeat at a time. 💓</i>

<i>Pulse — Your System's Heartbeat.</i>

<p align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
</p>

**© 2026 Open Source Project | Pulse - Your System's Heartbeat | MIT License**

</div>
