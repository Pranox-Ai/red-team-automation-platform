import nmap

def scan_ports(target):

    results = []

    try:
        scanner = nmap.PortScanner()
        scanner.scan(target, '1-1024')

        for host in scanner.all_hosts():
            for proto in scanner[host].all_protocols():

                ports = scanner[host][proto].keys()

                for port in ports:
                    results.append({
                        "port": port,
                        "state": scanner[host][proto][port]['state']
                    })

    except:
        results.append({
            "port": "Nmap not supported on this server",
            "state": "Unavailable"
        })

    return results