<p align="center">
  <img src="https://img.shields.io/badge/VulnScope-v1.0.0-6366f1?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMiAxNWwtNS01IDEuNDEtMS40MUwxMCAxNC4xN2w3LjU5LTcuNTlMMTkgOGwtOSA5eiIvPjwvc3ZnPg==&labelColor=0a0e17" alt="VulnScope v1.0.0"/>
</p>

<h1 align="center">
  <br>
  🛡️ VulnScope
  <br>
</h1>

<h4 align="center">A production-quality network vulnerability scanner for authorized security assessments.</h4>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/python-3.12+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.12+"></a>
  <a href="#"><img src="https://img.shields.io/badge/license-MIT-00C853?style=flat-square" alt="License: MIT"></a>
  <a href="#"><img src="https://img.shields.io/badge/CI-passing-00e676?style=flat-square&logo=github-actions&logoColor=white" alt="CI Passing"></a>
  <a href="#"><img src="https://img.shields.io/badge/tests-101%20passed-00e676?style=flat-square&logo=pytest&logoColor=white" alt="Tests: 101 passed"></a>
  <a href="#"><img src="https://img.shields.io/badge/code%20style-PEP8-6366f1?style=flat-square" alt="Code style: PEP8"></a>
  <a href="#"><img src="https://img.shields.io/badge/reports-HTML%20%7C%20JSON%20%7C%20CSV-ff9100?style=flat-square" alt="Reports: HTML | JSON | CSV"></a>
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-reports--output">Reports</a> •
  <a href="#-project-structure">Structure</a> •
  <a href="#-contributing">Contributing</a> •
  <a href="#-license">License</a>
</p>

---

<br>

> [!CAUTION]
> **AUTHORIZED USE ONLY** — VulnScope is designed exclusively for security assessments on networks you own or have explicit written permission to test. Unauthorized scanning is illegal and may violate the Computer Fraud and Abuse Act (CFAA), the Computer Misuse Act, or equivalent laws in your jurisdiction. **Always obtain proper authorization before scanning.**

<br>

## 📋 Overview

**VulnScope** is a modular, extensible Python-based network security scanner that performs safe asset discovery, port scanning, service identification, and automated report generation. It is built with production-quality standards: clean OOP architecture, comprehensive error handling, rich terminal output, and a stunning dark-themed HTML dashboard.

VulnScope does **not** include any offensive capabilities — no exploitation, no brute-forcing, no credential attacks, no malware, and no privilege escalation. It focuses solely on **reconnaissance and visibility**.

```
 ██╗   ██╗██╗   ██╗██╗     ███╗   ██╗███████╗ ██████╗ ██████╗ ██████╗ ███████╗
 ██║   ██║██║   ██║██║     ████╗  ██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
 ██║   ██║██║   ██║██║     ██╔██╗ ██║███████╗██║     ██║   ██║██████╔╝█████╗
 ╚██╗ ██╔╝██║   ██║██║     ██║╚██╗██║╚════██║██║     ██║   ██║██╔═══╝ ██╔══╝
  ╚████╔╝ ╚██████╔╝███████╗██║ ╚████║███████║╚██████╗╚██████╔╝██║     ███████╗
   ╚═══╝   ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═════╝╚═╝     ╚══════╝
```

<br>

## ✨ Features

### 🔍 Scanning & Discovery
| Feature | Description |
|---------|-------------|
| **Host Discovery** | ICMP ping + TCP probe fallback (ports 80, 443, 22, 445) with configurable timeouts |
| **CIDR & Range Support** | Scan `192.168.1.0/24`, `10.0.0.1-10.0.0.50`, single IPs, or comma-separated lists |
| **Multi-Threaded Scanning** | Configurable thread pool (default: 100) for high-speed TCP connect scanning |
| **Port Flexibility** | Preset lists (`top100`, `top1000`), custom ranges (`1-1024`), or explicit lists (`22,80,443`) |
| **Banner Grabbing** | Safe socket reads with protocol-specific probes (HTTP HEAD, SMTP EHLO, FTP greeting, SSH version) |
| **Service Detection** | Regex-based fingerprinting of 30+ services with version extraction |
| **Severity Ratings** | Automated risk classification — CRITICAL, HIGH, MEDIUM, LOW, INFO |

### 📊 Reporting
| Feature | Description |
|---------|-------------|
| **HTML Dashboard** | Stunning dark-themed glassmorphism report with Chart.js visualizations |
| **Interactive Tables** | Column sorting, severity filtering, full-text search, CSV export from browser |
| **JSON Export** | Machine-readable structured output with full metadata |
| **CSV Export** | Flat tabular format for spreadsheet analysis |
| **Single-File HTML** | CSS & JS inlined for zero-dependency portability |

### ⚙️ Developer Experience
| Feature | Description |
|---------|-------------|
| **Interactive Web GUI** | Stunning Flask-powered web dashboard with real-time scan progress |
| **Rich Terminal UI** | Color-coded output, progress bars, ASCII art banner via Rich |
| **YAML Configuration** | Persistent settings with CLI override support |
| **Modular Architecture** | Clean OOP design with abstract reporters and separated concerns |
| **101 Unit Tests** | Comprehensive pytest suite with mocked network operations |
| **GitHub Actions CI** | Automated linting (flake8) and testing on every push/PR |
| **PEP 8 Compliant** | Type hints, docstrings, and consistent code style throughout |

### 🛡️ Severity Classification

| Severity | Services | Color |
|----------|----------|-------|
| 🔴 **HIGH** | Telnet, FTP, SMB, NetBIOS | `#ff5252` |
| 🟠 **MEDIUM** | RDP, MySQL, PostgreSQL, MSSQL, SNMP, VNC | `#ff9100` |
| 🟡 **LOW** | SSH, SMTP, IMAP, POP3 | `#ffea00` |
| 🔵 **INFO** | HTTP, HTTPS, DNS | `#00e5ff` |

<br>

## 🏗 Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                          CLI  (cli.py)                              │
│             argparse  ·  Rich console  ·  orchestration             │
└──────────┬──────────────────┬──────────────────┬────────────────────┘
           │                  │                  │
           ▼                  ▼                  ▼
┌────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ Config Loader  │  │ Network Parser  │  │   Rich Logger   │
│  (config.py)   │  │ (network.py)    │  │  (logger.py)    │
│                │  │                 │  │                 │
│ YAML → dataclass│  │ CIDR / ranges / │  │ Console + file  │
│ + CLI merge    │  │ port specs      │  │ dual output     │
└────────────────┘  └────────┬────────┘  └─────────────────┘
                             │
                    ┌────────▼────────┐
                    │ Host Discovery  │
                    │ (discovery.py)  │
                    │                 │
                    │ ICMP ping       │
                    │ TCP probe       │
                    │ ThreadPool      │
                    └────────┬────────┘
                             │  alive hosts
                    ┌────────▼────────┐
                    │  Port Scanner   │
                    │  (scanner.py)   │
                    │                 │
                    │ TCP connect     │
                    │ Multi-threaded  │
                    │ Progress bars   │
                    └────────┬────────┘
                             │  open ports
                    ┌────────▼────────┐
                    │Service Detector │
                    │(service_det.py) │
                    │                 │
                    │ Banner grabbing │
                    │ Protocol probes │
                    │ Severity rating │
                    └────────┬────────┘
                             │  enriched results
           ┌─────────────────┼─────────────────┐
           ▼                 ▼                  ▼
┌────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ HTML Reporter  │  │ JSON Reporter   │  │ CSV Reporter    │
│                │  │                 │  │                 │
│ Jinja2 + CSS   │  │ Pretty-print    │  │ Flat rows       │
│ + Chart.js     │  │ + metadata      │  │ IP/Port/Service │
│ Dark dashboard │  │                 │  │                 │
└────────────────┘  └─────────────────┘  └─────────────────┘
```

### Data Flow

```
User Input → parse_targets() → HostDiscovery.discover()
                                        │
                                  alive IPs
                                        │
                                PortScanner.scan_hosts()
                                        │
                                  HostResult[]
                                        │
                            ServiceDetector.detect_services()
                                        │
                              enriched HostResult[]
                                        │
                                   ScanResult
                                        │
                          ┌─────────────┼─────────────┐
                          ▼             ▼             ▼
                     HTML report   JSON report   CSV report
```

### Core Data Models

```
ScanResult
├── target: str                    # "192.168.1.0/24"
├── hosts: list[HostResult]
│   ├── ip: str                    # "192.168.1.5"
│   ├── hostname: str | None       # "web-server.local"
│   ├── is_alive: bool
│   └── ports: list[PortResult]
│       ├── port: int              # 443
│       ├── state: str             # "open"
│       ├── service: str           # "https"
│       ├── banner: str            # "Server: nginx/1.24"
│       ├── version: str           # "nginx 1.24"
│       └── severity: Severity     # Severity.INFO
├── scan_start / scan_end: datetime
└── config: dict
```

<br>

## 📦 Installation

### Prerequisites

- **Python 3.12** or higher
- **pip** package manager
- **Git** (to clone the repository)

### Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/vulnscope.git
cd vulnscope

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt

# Verify installation
python -m vulnscope --version
```

### Install as a Package

```bash
pip install -e .

# Now available globally
vulnscope --version
```

### Requirements

| Package | Version | Purpose |
|---------|---------|---------|
| [rich](https://github.com/Textualize/rich) | ≥ 13.7.0 | Colorful terminal output, progress bars, tables |
| [Jinja2](https://jinja.palletsprojects.com/) | ≥ 3.1.3 | HTML report templating |
| [PyYAML](https://pyyaml.org/) | ≥ 6.0.1 | Configuration file parsing |
| [pytest](https://pytest.org/) | ≥ 8.0.0 | Unit testing framework |
| [pytest-cov](https://github.com/pytest-dev/pytest-cov) | ≥ 4.1.0 | Test coverage reporting |
| [flake8](https://flake8.pycqa.org/) | ≥ 7.0.0 | Code style linting |

<br>

## 🚀 Usage

### Interactive Web GUI

VulnScope now includes a stunning, built-in Web GUI that allows you to configure targets, run scans in the background, and view results in real-time on a dark-themed glassmorphism dashboard.

```bash
# Launch the Web GUI server
python -m vulnscope --gui
```

Once the server starts, open your browser and navigate to **http://127.0.0.1:5000**.
From the sidebar, enter your Target (e.g. `127.0.0.1`), Ports (e.g. `top100`), and hit **Launch Scan**.

### Basic Scan (CLI)

```bash
# Scan a subnet with default settings (top 100 ports, 100 threads)
python -m vulnscope 192.168.1.0/24
```

### Advanced Examples

```bash
# Launch the Interactive Web GUI
python -m vulnscope --gui

# Scan an IP range with custom ports
python -m vulnscope 192.168.1.10-192.168.1.50 -p 22,80,443,3306,8080

# Full port range scan with increased threads
python -m vulnscope 10.0.0.0/24 -p 1-65535 -t 500

# Scan a single host, output only JSON, custom timeout
python -m vulnscope 192.168.1.5 -p top100 -f json --timeout 5

# Skip host discovery (assume all hosts alive)
python -m vulnscope 172.16.0.0/24 --no-discovery -p 1-1024

# Use a custom config file with verbose output
python -m vulnscope 10.10.10.0/24 -c my_config.yaml -v -o reports/

# Generate only HTML and CSV reports
python -m vulnscope 192.168.1.0/24 -f html,csv -o /path/to/reports
```

### Command-Line Options

| Option | Short | Default | Description |
|--------|-------|---------|-------------|
| `--gui`  | — | `False` | Launch the interactive Web GUI dashboard |
| `target` | — | *(required unless --gui)* | Target specification: CIDR, IP range, or single IP |
| `--ports` | `-p` | `top100` | Port specification: `top100`, `top1000`, range, or list |
| `--threads` | `-t` | `100` | Number of concurrent scanning threads |
| `--timeout` | — | `2.0` | TCP connection timeout in seconds |
| `--output-dir` | `-o` | `output` | Directory for report files |
| `--format` | `-f` | `html,json,csv` | Comma-separated output formats |
| `--config` | `-c` | `None` | Path to YAML configuration file |
| `--no-discovery` | — | `False` | Skip host discovery, scan all targets |
| `--verbose` | `-v` | `0` | Increase verbosity (repeat for more: `-vv`) |
| `--version` | — | — | Show version and exit |

### Configuration File

Create a `config.yaml` to persist your preferred settings:

```yaml
# VulnScope Configuration
scan:
  ports: "top100"
  threads: 100
  timeout: 2.0
  banner_timeout: 3.0
  max_retries: 1

discovery:
  enabled: true
  timeout: 1.0

output:
  dir: "output"
  formats:
    - html
    - json
    - csv

logging:
  level: "INFO"
```

> **Note:** CLI arguments always override configuration file values.

<br>

## 📊 Reports & Output

VulnScope generates reports in three formats, all saved to the output directory with timestamped filenames.

### 🌐 HTML Dashboard

The HTML report is a self-contained, interactive dashboard with a dark glassmorphism theme:

<table>
<tr>
<td width="50%">

**Header & Summary Cards**
- Scan metadata (target, duration, version)
- Color-coded severity count cards
- Total hosts, alive hosts, open ports at a glance

</td>
<td width="50%">

**Interactive Charts**
- Severity distribution doughnut chart
- Top ports horizontal bar chart
- Powered by Chart.js

</td>
</tr>
<tr>
<td width="50%">

**Findings Table**
- Sortable columns (IP, port, service, severity)
- Full-text search across all fields
- Severity filter toggle buttons

</td>
<td width="50%">

**Export & Accessibility**
- Export visible rows as CSV from browser
- Responsive layout (mobile → desktop)
- Semantic HTML with ARIA labels

</td>
</tr>
</table>

> 📸 *Open the generated HTML file in any modern browser to see the full interactive dashboard. No server required — it's a single self-contained file.*

#### Dashboard Color Palette

| Element | Color | Hex |
|---------|-------|-----|
| Background | Deep Navy | `#0a0e17` |
| Surface | Dark Blue | `#131a2b` |
| Cards | Midnight | `#1a2340` |
| Accent | Indigo | `#6366f1` |
| Critical Badge | Red | `#ff1744` |
| High Badge | Red-Orange | `#ff5252` |
| Medium Badge | Orange | `#ff9100` |
| Low Badge | Yellow | `#ffea00` |
| Info Badge | Cyan | `#00e5ff` |

---

### 📄 JSON Output

Structured, machine-readable output with full scan metadata:

```json
{
  "target": "192.168.1.0/24",
  "scanner_version": "1.0.0",
  "scan_start": "2026-06-27T12:00:00",
  "scan_end": "2026-06-27T12:02:34",
  "scan_duration_seconds": 154.0,
  "config": {
    "ports": "top100",
    "threads": 100,
    "timeout": 2.0
  },
  "hosts": [
    {
      "ip": "192.168.1.1",
      "hostname": "gateway.local",
      "is_alive": true,
      "ports": [
        {
          "port": 22,
          "state": "open",
          "protocol": "tcp",
          "service": "ssh",
          "version": "OpenSSH 8.9p1",
          "banner": "SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.6",
          "severity": "low"
        },
        {
          "port": 80,
          "state": "open",
          "protocol": "tcp",
          "service": "http",
          "version": "nginx 1.24.0",
          "banner": "HTTP/1.1 200 OK\r\nServer: nginx/1.24.0",
          "severity": "info"
        }
      ]
    }
  ],
  "summary": {
    "total_hosts_scanned": 254,
    "alive_hosts": 5,
    "total_open_ports": 14,
    "severity_counts": {
      "critical": 0,
      "high": 3,
      "medium": 4,
      "low": 5,
      "info": 2
    }
  }
}
```

---

### 📋 CSV Output

Flat tabular format ideal for spreadsheet analysis and data pipelines:

```
IP,Hostname,Port,Protocol,State,Service,Version,Banner,Severity
192.168.1.1,gateway.local,22,tcp,open,ssh,OpenSSH 8.9p1,"SSH-2.0-OpenSSH_8.9p1",low
192.168.1.1,gateway.local,80,tcp,open,http,nginx 1.24.0,"HTTP/1.1 200 OK",info
192.168.1.1,gateway.local,443,tcp,open,https,nginx 1.24.0,"",info
192.168.1.5,web-server.local,3306,tcp,open,mysql,MySQL 8.0.36,"",medium
192.168.1.10,file-server.local,445,tcp,open,smb,SMB 3.1.1,"",high
192.168.1.20,legacy-host.local,23,tcp,open,telnet,,"login:",high
```

<br>

## 📁 Project Structure

```
VulnScope/
│
├── 📂 vulnscope/                  # Main application package
│   ├── __init__.py                # Package metadata & version
│   ├── __main__.py                # Entry point: python -m vulnscope
│   ├── cli.py                     # Argparse CLI + Rich orchestration
│   ├── config.py                  # YAML config loader + ScanConfig dataclass
│   │
│   ├── 📂 core/                   # Core scanning engine
│   │   ├── __init__.py
│   │   ├── models.py              # Severity, PortResult, HostResult, ScanResult
│   │   ├── discovery.py           # ICMP ping + TCP probe host discovery
│   │   ├── scanner.py             # Multi-threaded TCP connect port scanner
│   │   └── service_detector.py    # Banner grabbing + service fingerprinting
│   │
│   ├── 📂 reporting/              # Report generation engine
│   │   ├── __init__.py
│   │   ├── base.py                # Abstract BaseReporter class
│   │   ├── html_report.py         # Jinja2 HTML dashboard generator
│   │   ├── json_report.py         # Structured JSON exporter
│   │   ├── csv_report.py          # Flat CSV exporter
│   │   └── 📂 templates/          # Report assets (separated concerns)
│   │       ├── dashboard.html     # Jinja2 template
│   │       ├── 📂 css/
│   │       │   └── style.css      # Dark glassmorphism design system
│   │       └── 📂 js/
│   │           └── dashboard.js   # Chart.js + search/filter/sort
│   │
│   └── 📂 utils/                  # Shared utilities
│       ├── __init__.py
│       ├── logger.py              # Rich console + file logging
│       └── network.py             # CIDR/range/port parsing
│
├── 📂 tests/                      # Test suite (101 tests)
│   ├── __init__.py
│   ├── test_models.py             # 25 tests — data model validation
│   ├── test_network.py            # 20 tests — network parsing
│   ├── test_discovery.py          # 11 tests — host discovery
│   ├── test_scanner.py            #  9 tests — port scanning
│   ├── test_service_detector.py   # 20 tests — service identification
│   └── test_reporting.py          # 11 tests — report generation
│
├── 📂 config/
│   └── default_config.yaml        # Default configuration template
│
├── 📂 output/
│   └── 📂 sample/
│       └── sample_scan_results.json  # Example scan output
│
├── 📂 .github/workflows/
│   └── ci.yml                     # GitHub Actions: lint + test
│
├── requirements.txt               # Python dependencies
├── setup.py                       # Package installation config
├── LICENSE                        # MIT License
├── .gitignore                     # Git ignore rules
└── README.md                      # ← You are here
```

<br>

## 🔧 Technologies Used

<table>
<tr>
<td align="center" width="120">
  <strong>Python 3.12+</strong><br/>
  <sub>Core Language</sub>
</td>
<td align="center" width="120">
  <strong>Rich</strong><br/>
  <sub>Terminal UI</sub>
</td>
<td align="center" width="120">
  <strong>Jinja2</strong><br/>
  <sub>HTML Templating</sub>
</td>
<td align="center" width="120">
  <strong>PyYAML</strong><br/>
  <sub>Configuration</sub>
</td>
<td align="center" width="120">
  <strong>Chart.js</strong><br/>
  <sub>Data Visualization</sub>
</td>
<td align="center" width="120">
  <strong>pytest</strong><br/>
  <sub>Testing</sub>
</td>
</tr>
</table>

| Category | Technologies |
|----------|-------------|
| **Language** | Python 3.12+ with type hints, dataclasses, enums |
| **Networking** | `socket`, `subprocess`, `ipaddress` (stdlib) |
| **Concurrency** | `concurrent.futures.ThreadPoolExecutor` |
| **Terminal UI** | Rich (console, progress bars, panels, tables) |
| **Templating** | Jinja2 with autoescape |
| **Configuration** | PyYAML |
| **Visualization** | Chart.js 4.4 (CDN) |
| **Testing** | pytest, pytest-cov, unittest.mock |
| **Linting** | flake8 |
| **CI/CD** | GitHub Actions |

<br>

## 🛡️ Security & Legal Disclaimer

> [!WARNING]
> **This tool is provided for educational and authorized security testing purposes only.**

### You MUST:
- ✅ Own the target network, **or**
- ✅ Have explicit, written authorization from the network owner
- ✅ Comply with all applicable local, state, national, and international laws
- ✅ Follow your organization's security assessment policies

### This tool does NOT:
- ❌ Exploit vulnerabilities
- ❌ Perform brute-force or password attacks
- ❌ Deploy malware or backdoors
- ❌ Attempt privilege escalation
- ❌ Establish persistence mechanisms
- ❌ Exfiltrate any data

### Scope of Functionality

VulnScope is strictly a **passive reconnaissance** tool that performs:
1. **ICMP/TCP host discovery** — determines if hosts are online
2. **TCP connect scanning** — identifies open ports via standard socket connections
3. **Banner grabbing** — reads publicly available service banners
4. **Service identification** — maps ports to known services
5. **Report generation** — documents findings in structured formats

**The authors assume no liability for misuse of this software.** Unauthorized network scanning may constitute a criminal offense under laws such as the CFAA (United States), Computer Misuse Act (United Kingdom), StGB §202a-c (Germany), and similar legislation worldwide.

<br>

## 🗺️ Future Roadmap

| Phase | Feature | Status |
|-------|---------|--------|
| **v1.1** | UDP port scanning support | 🔲 Planned |
| **v1.1** | IPv6 network support | 🔲 Planned |
| **v1.1** | PDF report generation | 🔲 Planned |
| **v1.2** | OS fingerprinting via TCP/IP stack analysis | 🔲 Planned |
| **v1.2** | Vulnerability database integration (CVE mapping) | 🔲 Planned |
| **v1.2** | Plugin architecture for custom scanners | 🔲 Planned |
| **v1.3** | Async I/O scanning engine (asyncio) | 🔲 Planned |
| **v1.3** | Real-time web dashboard with WebSockets | 🔲 Planned |
| **v1.3** | REST API for programmatic access | 🔲 Planned |
| **v2.0** | Scan scheduling & diff reports | 🔲 Planned |
| **v2.0** | Multi-user scan management | 🔲 Planned |
| **v2.0** | Integration with SIEM platforms | 🔲 Planned |

<br>

## 🤝 Contributing

Contributions are welcome! VulnScope is designed to be easy to extend.

### Getting Started

```bash
# Fork and clone the repository
git clone https://github.com/yourusername/vulnscope.git
cd vulnscope

# Set up development environment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run tests to verify your setup
python -m pytest tests/ -v

# Run linter
python -m flake8 vulnscope/ --max-line-length=120
```

### Development Workflow

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Write** tests for your changes
4. **Implement** your changes following the existing code style
5. **Run** the full test suite: `python -m pytest tests/ -v`
6. **Lint** your code: `python -m flake8 vulnscope/ --max-line-length=120`
7. **Commit** with a descriptive message: `git commit -m "feat: add UDP scanning support"`
8. **Push** and open a Pull Request

### Code Style Guidelines

- Follow **PEP 8** with a max line length of **120 characters**
- Use **type hints** for all function signatures
- Write **docstrings** for all public classes and methods
- Add **unit tests** for new functionality
- Use **`get_logger(__name__)`** for module-level logging
- Extend **`BaseReporter`** to add new export formats

### Adding a New Reporter

```python
# vulnscope/reporting/my_reporter.py

from vulnscope.reporting.base import BaseReporter
from vulnscope.core.models import ScanResult


class MyReporter(BaseReporter):
    """My custom report format."""

    def generate(self, scan_result: ScanResult) -> str:
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        filepath = self._make_filename("vulnscope_report", "ext", timestamp)
        # ... write your report ...
        return filepath
```

### Commit Convention

| Prefix | Description |
|--------|-------------|
| `feat:` | New feature |
| `fix:` | Bug fix |
| `docs:` | Documentation update |
| `test:` | Test addition or modification |
| `refactor:` | Code refactoring |
| `style:` | Code style / formatting |
| `ci:` | CI/CD changes |

<br>

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

```
MIT License — Copyright (c) 2024-2026 VulnScope Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files, to deal in the Software
without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software, subject to the following conditions: ...
```

<br>

---

<p align="center">
  <sub>Built with 🐍 Python • 💎 Rich • 📊 Chart.js</sub>
  <br>
  <sub>Made for authorized security assessments — scan responsibly.</sub>
</p>
