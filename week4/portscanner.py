devices = [("192.168.1.10", [22, 80, 443]), ("192.168.1.11", [21, 22, 80]), ("192.168.1.12", [23, 80, 3389])]
risky_ports = [21, 23, 3389]

risk_counter = 0
print('Scanning network devices...')
for dev in devices:
    openports = dev[1]
    for port in openports:
        if port in risky_ports:
            risk_counter += 1
            print(f"{dev[0]} has risky port {port} open")

print(f"Scan complete: {risk_counter} security risks found")
