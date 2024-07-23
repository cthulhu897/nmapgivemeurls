import sys
import xml.etree.ElementTree as ET

def parse_nmap_file(file_path):
    """
    Parse an Nmap XML file and return the root of the XML tree.
    
    Args:
        file_path (str): Path to the Nmap XML file.
    
    Returns:
        xml.etree.ElementTree.Element: Root of the parsed XML tree.
    """
    try:
        tree = ET.parse(file_path)
        return tree.getroot()
    except ET.ParseError as e:
        sys.stderr.write(f"Error parsing the file: {e}\n")
        sys.exit(1)
    except FileNotFoundError:
        sys.stderr.write(f"File not found: {file_path}\n")
        sys.exit(1)

def extract_http_services(nmap_root):
    """
    Extract services with 'http' in their name from the Nmap XML root.
    
    Args:
        nmap_root (xml.etree.ElementTree.Element): Root of the Nmap XML tree.
    
    Returns:
        list: List of tuples containing host, port, protocol, and service name.
    """
    services = []
    for host in nmap_root.findall(".//host"):
        ip_address = host.find("address").get("addr")
        for port in host.findall(".//port"):
            port_id = int(port.get("portid"))
            protocol = port.get("protocol")
            service = port.find("service")
            if service is not None:
                svc_name = service.get("name", "").lower()
                if "http" in svc_name:
                    services.append((ip_address, port_id, protocol, svc_name))
    return services

def infer_protocol_and_print_urls(services):
    """
    Infer the protocol based on the port and print the corresponding URLs.
    
    Args:
        services (list): List of tuples containing host, port, protocol, and service name.
    """
    for service in services:
        host, port, protocol, svc_name = service
        if port == 443:
            print(f"https://{host}")
        elif port == 80:
            print(f"http://{host}")
        else:
            print(f"http://{host}:{port}")
            print(f"https://{host}:{port}")

def main():
    """
    Main function to parse an Nmap file, extract HTTP/HTTPS services, and print URLs.
    """
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: python script.py <file_path>\n")
        sys.exit(1)

    file_path = sys.argv[1]
    nmap_root = parse_nmap_file(file_path)
    http_services = extract_http_services(nmap_root)
    infer_protocol_and_print_urls(http_services)

if __name__ == "__main__":
    main()
