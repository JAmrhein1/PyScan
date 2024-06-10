# PyScan

PyScan is a powerful and versatile network scanning tool designed for educational purposes. This tool supports both IPv4 and IPv6 scanning, allowing you to identify open ports and service banners on target systems. With PyScan, you can efficiently scan a range of ports, filter results to show only open ports, and even exclude specific ports from your scan.

## Features

- **IPv4 and IPv6 Support**: Scan both IPv4 and IPv6 addresses seamlessly.
- **Service Detection**: Identify services running on open ports using a predefined port-to-service mapping.
- **Banner Grabbing**: Retrieve service banners from open ports to gather more information about the running services.
- **Custom Port Ranges**: Specify custom start and end ports for your scans.
- **Ignored Ports**: Exclude specific ports from scanning to focus on relevant ports.
- **User-friendly Interface**: Intuitive command-line interface with clear warnings and prompts.

## Usage

1. **Install Dependencies**:
   Ensure you have the required dependencies installed:
   ```bash
   pip install termcolor
2. **Run PyScan**:
   Execute the script and follow the prompts:
   ```bash
   python pyscan.py
3. **Input Target**:
Enter the target IP address (IPv4 or IPv6) or domain.

4. **Ping Target**:
The tool will ping the target to check for reachability.

5. **Specify Port Range**:
Enter the start and end ports for scanning.

6. **Ignored Ports**:
Optionally, enter ports to ignore (comma-separated).

7. **Show Only Open Ports**:
Choose whether to display only open ports or all scanned ports.

8. **Scan Again**:
After the scan, you have the option to scan another network.

## Example
![image](https://github.com/JAmrhein1/PyScan/assets/167656090/ac121f31-b7fa-4e84-9d6b-8cae6671eb17)

## Disclaimer
**Warning** This network scanning tool is intended for educational purposes only. Unauthorized scanning of networks or systems is illegal and may result in severe legal consequences. Ensure that you have explicit permission from the network owner before using this tool. Use at your own risk. The developer is not responsible for any damage caused by this tool.

## License
MIT License

## Contributing
Feel free to contribute, I am a 3rd year computer science student who is trying to get more projects on my resume. This code might not be the most clean or well formated but it works for me and it was a fun project to do regardless.

## Contact
For any suggestions, please open an issue on this repository

## Notes
Yes, I do understand that python isn't known to be a fast language is is quite slow in comparison to other languages but, python is the language I'm most comfortable in.
   
