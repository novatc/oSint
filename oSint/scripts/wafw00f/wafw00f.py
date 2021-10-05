from modules.wafw00f.art import randomArt
from modules.wafw00f.main_waf00f import WAFW00F, buildResultRecord


def run_wafw00f(url):
    results = []
    art = randomArt()
    results.append(art)
    print(randomArt())
    attacker = WAFW00F(url)
    waf = attacker.identwaf(findall=True)
    print('Identified WAF: %s' % waf)
    if len(waf) > 0:
        for i in waf:
            results.append(buildResultRecord(url, i))
        print('[+] The site is behind %s%s%s WAF.')
    if len(waf) == 0:
        print('[+] Generic Detection results:')
        if attacker.genericdetect():
            print('Generic Detection: %s' % attacker.knowledge['generic']['reason'])
            print('[*] The site %s seems to be behind a WAF or some sort of security solution' % url)
            print('[~] Reason: %s' % attacker.knowledge['generic']['reason'])
            results.append(buildResultRecord(url, 'generic'))
        else:
            print('[-] No WAF detected by the generic detection')
            results.append(buildResultRecord(url, None))
    print('[~] Number of requests: %s' % attacker.requestnumber)
    return results
