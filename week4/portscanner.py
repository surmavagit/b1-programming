devices = [("192.168.1.10", [22, 80, 443]), ("192.168.1.11", [21, 22, 80]), ("192.168.1.12", [23, 80, 3389])]
risky_ports = [21, 23, 3389]

vulnerabilities = []

print('Scanning network devices...')
for dev in devices:
    openports = dev[1]
    for port in openports:
        if port in risky_ports:
            vulnerabilities.append((dev[0], port))

for issue in vulnerabilities:
    print(f"{issue[0]} has risky port {issue[1]} open")
print(f"Scan complete: {len(vulnerabilities)} security risks found")
