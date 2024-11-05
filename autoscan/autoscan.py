import subprocess
import argparse
from datetime import datetime
import threading
import logging
import shutil
import sys

# Configure logging
logging.basicConfig(filename='nmap_scanner.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def is_nmap_installed():
    if shutil.which('nmap') is None:
        print("Error: Nmap is not installed. Please install Nmap to use this tool.")
        sys.exit(1)


def run_nmap_scan(target, scan_type, options):
    try:
        print(f"Running Nmap {scan_type} scan on {target}")

        nmap_commands = ['nmap'] + options + [target]

        results = subprocess.run(nmap_commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if results.returncode == 0:
            print(f"Scan on {target} completed successfully!\n")
            logging.info(f"Scan on {target} completed successfully.")
            return results.stdout
        else:
            print(f"Error scanning {target}: {results.stderr}")
            logging.error(f"Error scanning {target}: {results.stderr}")
            return None

    except Exception as e:
        print(f"Exception occurred while scanning {target}: {str(e)}")
        logging.error(f"Exception occurred while scanning {target}: {str(e)}")
        return None


def save_report(target, report, scan_type):
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"nmap_{scan_type}_scan_{target}_{current_time}.txt"
    with open(filename, 'w') as file:
        file.write(report)
    print(f"Report saved as {filename}")


def scan_target(target, args):
    scan_options = []
    scan_type = args.scan_type

    if scan_type == 'vulnerability':
        scan_options.extend(['-sV', '--script', 'vuln'])
    elif scan_type == 'tcp_syn':
        scan_options.append('-sS')
    elif scan_type == 'aggressive':
        scan_options.append('-A')
    elif scan_type == 'ping':
        scan_options.append('-sn')

    if args.ports:
        scan_options.extend(['-p', args.ports])

    if args.os_detection:
        scan_options.append('-O')

    if args.additional_options:
        scan_options.extend(args.additional_options.split())

    if args.output_format:
        scan_options.extend(['-o' + args.output_format, f"{scan_type}_scan_{target}"])

    scan_result = run_nmap_scan(target, scan_type, scan_options)

    if scan_result and args.save:
        save_report(target, scan_result, scan_type)


def main():
    is_nmap_installed()

    parser = argparse.ArgumentParser(description='Automated Nmap Scanner')

    parser.add_argument('targets', nargs='+', help='Target IP addresses, ranges, or hostnames')
    parser.add_argument('--save', action='store_true', help='Save the output to a text file')
    parser.add_argument('--scan-type', choices=['vulnerability', 'tcp_syn', 'aggressive', 'ping'],
                        default='vulnerability', help='Type of scan to perform')
    parser.add_argument('--ports', help='Specify ports to scan (e.g., "1-1000", "80,443")')
    parser.add_argument('--os-detection', action='store_true', help='Enable OS detection')
    parser.add_argument('--additional-options', help='Additional Nmap command-line options')
    parser.add_argument('--output-format', choices=['N', 'X', 'G', 'S', 'A'],
                        help='Output format: N (normal), X (XML), G (grepable), S (script kiddie), A (all)')

    args = parser.parse_args()

    threads = []

    for target in args.targets:
        thread = threading.Thread(target=scan_target, args=(target, args))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
