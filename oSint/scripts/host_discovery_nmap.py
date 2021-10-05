import nmap


def run_host_discovery(ip: str):
    nm = nmap.PortScanner()
    machine = nm.scan(ip, arguments='-sV -O')

    hosts = []

    for host in nm.all_hosts():
        protocols = []
        ports = []
        dict_host = {}
        dict_host['ip'] = host
        dict_host['state'] = nm[host].state()
        dict_host['os'] = machine['scan'][host]['osmatch'][0]['name']
        dict_host['accuracy'] = machine['scan'][host]['osmatch'][0]['accuracy']

        for proto in nm[host].all_protocols():
            protocols.append(proto)

            lport = nm[host][proto].keys()

            for port in lport:
                ports.append([port, nm[host][proto][port]['state']])
        dict_host['protocols'] = protocols
        dict_host['port'] = ports
        hosts.append(dict_host)
    return hosts

# x = run_host_discovery("195.60.121.167")
# print(x)