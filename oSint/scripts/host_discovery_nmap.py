import nmap


def run_host_discovery(ip:str):
    nm = nmap.PortScanner()
    maschine = nm.scan(ip, arguments='-sV -O')

    hosts = [] 

    for host in nm.all_hosts():
        protocols = []
        ports = []
        dict_host = {}
        dict_host['ip'] = host
        dict_host['state'] = nm[host].state()
        dict_host['os'] = maschine['scan'][host]['osmatch'][0]['name']
        dict_host['accuracy'] = maschine['scan'][host]['osmatch'][0]['accuracy']
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
        print(f"OS: {maschine['scan'][host]['osmatch'][0]['name']} ")
        print(f"accuracy: {maschine['scan'][host]['osmatch'][0]['accuracy']}%")
        for proto in nm[host].all_protocols():
            protocols.append(proto)
            print('----------')
            print('Protocol : %s' % proto)

            lport = nm[host][proto].keys()

            for port in lport:
                print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
                ports.append([port, nm[host][proto][port]['state'] ])
        dict_host['protocols'] = protocols
        dict_host['port'] = ports
        hosts.append(dict_host)
    return hosts

run_host_discovery("192.168.178.87")