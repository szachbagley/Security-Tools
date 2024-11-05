# Autoscan

This script simplifies the process of running Nmap scans on multiple targets with various options. 

## Features

Multiple Targets Support: Scan multiple IP addresses, ranges, or hostnames simultaneously.

Customizable Scans: Choose from different scan types or specify custom Nmap options.

Port Specification: Define specific ports or port ranges to scan.

OS Detection: Enable OS detection during scans.
Output Formats: Select different output formats for your scan results.

Logging: Keeps a log of all scan activities and errors.

Concurrent Scanning: Utilizes multithreading to perform scans faster.

## Prerequisites

Python 3.x

Nmap Installed: Make sure Nmap is installed and accessible in your system's PATH.

## Installation

Clone the Repository:

```
git clone https://github.com/yourusername/nmap-scanner-tool.git
```

Navigate to the Directory:

```
cd nmap-scanner-tool
```

## Usage

```
python nmap_scanner.py [options] target1 target2 ...
```

### Positional Arguments

```targets```: One or more target IP addresses, ranges, or hostnames.

### Optional Arguments

```--save```: Save the output to a text file.

```--scan-type```: Type of scan to perform (vulnerability, tcp_syn, aggressive, ping). Default is vulnerability.

```--ports```: Specify ports to scan (e.g., "1-1000", "80,443").

```--os-detection```: Enable OS detection.

```--additional-options```: Additional Nmap command-line options enclosed in quotes.

```--output-format```: Output format:

- ```N```: Normal

- ```X```: XML

- ```G```: Grepable

- ```S```: Script kiddie

- ```A```: All

## Examples
Basic Vulnerability Scan

```
python nmap_scanner.py 192.168.1.1
```

TCP SYN Scan on Multiple Targets

```
python nmap_scanner.py 192.168.1.1 192.168.1.2 --scan-type tcp_syn
```

Aggressive Scan with OS Detection

```
python nmap_scanner.py example.com --scan-type aggressive --os-detection
```

Specify Ports and Save Output

```
python nmap_scanner.py 192.168.1.0/24 --ports 1-1000 --save
```

Using Additional Nmap Options

```
python nmap_scanner.py target.com --additional-options "-Pn --traceroute"
```

## Logs

All scan activities and errors are logged in nmap_scanner.log.