import socket

def scan_ports(target):

    ports_to_scan = [21,22,23,25,53,80,110,143,443,445,3389]
    results = []

    for port in ports_to_scan:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        try:
            result = s.connect_ex((target, port))
            if result == 0:
                results.append({"port": port, "state": "open"})
        except:
            pass

        s.close()

    return results