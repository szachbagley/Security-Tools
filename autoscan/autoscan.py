# test comment for github
# import necessary packages for processing, parsing, and date
import subprocess
import argparse
from datetime import datetime

# run scan
def run_nmap_vuln_scan(target_ip):
    try:
        
        # print text showing can is running on target
        print(f"Running Nmap Vulnerability scan on {target_ip}")
        
        # get commands to run nmap, get version numbers, and find vulnerabilies by using scripts
        nmap_commands = ['nmap', '-sV', '--script', 'vuln', target_ip]
        
        # get results from scan, including output and error messages
        results = subprocess.run(nmap_commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text = True)
        
        # return results if successful
        if results.returncode == 0:
            print("Sucessful Scan!\n")
            return results.stdout
        
        # error message if unsuccessful
        else:
            print(f"Error: {results.stderr}")
            return None
        
    # create exception if scan cannot start
    except Exception as e:
        print(f"Error: {str(e)}")
        return None
    
# save report
def save_report(target_ip, report):
    
    # get current date and time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # create a report header with date and time
    report_header = f"Nmap Vulnerability Scan Report\nTarget: {target_ip}\nDate: {current_time}\n\n"
    
    # save the scan result to a text file
    filename = f"nmap_vuln_scan_{target_ip}.txt"
    with open(filename, 'w') as file:
        file.write(report_header + report)
    
    print(f"Report saved as {filename}")
   
# main process to run functions    
def main():
    
    # set up argument parsing for the script
    parser = argparse.ArgumentParser(description='Automated Nmap Vulnerability Scanner')
    
    # add target
    parser.add_argument('target_ip', help='Target IP address or range')
    
    # save file
    parser.add_argument('--save', action='store_true', help='Save the output to a text file')

    args = parser.parse_args()

    # run the nmap scan
    scan_result = run_nmap_vuln_scan(args.target_ip)

    if scan_result:
        print("\nScan Results:\n")
        print(scan_result)

        # save the report if prompted
        if args.save:
            save_report(args.target_ip, scan_result)

if __name__ == "__main__":
    main()    