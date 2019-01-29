**Chicago CyberSecurity group is an organization dedicated to promoting the education of security in the Chicago community. More information about the organization can be found here: https://www.meetup.com/chicagosecurity/**

=================

#This a sample demo to demonstrate how we can automate the collection of threat intelligence and lauch an automated attack based on the collected intel.

=================

### Prerequisites for making this demo work
# You need to use Python3 for this to work
* 1. MISP VM: https://www.misp-project.org/download/
* 2. MISP API (pymisp): https://github.com/MISP/PyMISP
* 3. Metasploit Python Library: https://github.com/allfro/pymetasploit
* Use this one for python3: https://github.com/iCarossio/PyMetasploit_Python3
* 4. Vulnerable Tomcat Server (I used an Ubuntu VM)

=================

### Preparations
#You must obtain the vFeed database from their website at vfeed.io
Update the environment variables to reflect yours:
misp_key = yourmisp_apikey
misp_api_endpoint = yourmisp_endpoint
remote_ip = the_victim_ip (vulnerable Tomcat server)
metasploit_login = yourmsf_password

=================

### How to Run
python3 mydemo.py