[Chicago CyberSecurity](https://www.meetup.com/chicagosecurity) is an organization dedicated to promoting the education of security in the Chicago community.

![Chicago CyberSecurity](https://img1.wsimg.com/isteam/ip/3eb9c502-58c2-4efc-a007-6e37f653acd0/29e675f7-8a51-463c-8b06-8d914c9d6b52.png)

================================================================================

*This a sample demo to demonstrate how we can automate the collection of threat intelligence and lauch an automated attack based on the collected intel.*
================================================================================

* Prerequisites for making this demo work:

  * [Python3](https://www.python.org/downloads)
  * [MISP VM](https://www.misp-project.org/download)
  * [MISP API](https://github.com/MISP/PyMISP)
  * [Metasploit Python3 Library](https://github.com/iCarossio/PyMetasploit_Python3)
  * Vulnerable Tomcat Server (I used an Ubuntu VM)

================================================================================

* Preparations
  * You must obtain the [vFeed database](vfeed.io) from their website
  * Update the environment variables to reflect yours:
    * misp_key = yourmisp_apikey
    * misp_api_endpoint = yourmisp_endpoint
    * remote_ip = the_victim_ip (vulnerable Tomcat server)
    * metasploit_login = yourmsf_password

================================================================================

* How to Run
python3 mydemo.py
