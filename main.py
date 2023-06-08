import socket
from socket import gethostbyname, gethostbyaddr, setdefaulttimeout


def scan(tgtHost, tgtPort):
    try:
        connskt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connskt.connect((tgtHost, tgtPort))
        print('[+] %d/tcp open' % tgtPort)
        connskt.close()
    except socket.error:
        print('[-] %d/tcp closed' % tgtPort)


def portScan(tgtHost, tgtPorts):
    try:
        tgtIp = gethostbyname(tgtHost)
    except socket.gaierror:
        print('[-] Cannot resolve %s' % tgtHost)
        return

    try:
        tgtName = gethostbyaddr(tgtIp)
        print('\n[+] Scan result: %s' % tgtName[0])
    except socket.herror:
        print('\n[+] Scan result: %s' % tgtIp)

    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scanning port: %d' % tgtPort)
        scan(tgtHost, int(tgtPort))


if __name__ == '__main__':
    portScan('google.com', [80, 22])
