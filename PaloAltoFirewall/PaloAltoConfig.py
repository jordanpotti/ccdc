#!/usr/bin/env python

#Run this with your team number and then Putty into the Palo Alto. Enter "set cli scripting-mode on" and then "cofigure"
#Then copy and past the output of the script. The first command increases the winow buffer size and the second command enters configure mode.

import sys


if len(sys.argv) != 2:
    print "Usage: fw_conf.py <team #>"
    sys.exit(0)

team_num = sys.argv[1]

with open("""PAConfig"""+team_num+""".txt""", "w") as command_file:
	commands="""set deviceconfig system permitted-ip 172.20.241.0/24
set deviceconfig system service disable-telnet yes
set deviceconfig system login-banner AuthorizedAccessOnlythorizedAccessOnly
set network profiles zone-protection-profile Default discard-overlapping-tcp-segment-mismatch yes discard-unknown-option yes tcp-reject-non-syn yes flood tcp-syn enable yes syn-cookies maximal-rate 500
set network profiles zone-protection-profile Default flood icmp enable yes
set network profiles zone-protection-profile Default flood udp enable yes
set network profiles zone-protection-profile Default flood other-ip enable yes
set network profiles zone-protection-profile Default flood icmpv6 enable yes
set network profiles interface-management-profile none
set network interface ethernet ethernet1/3 layer3 interface-management-profile none
set network interface ethernet ethernet1/2 layer3 interface-management-profile none
delete rulebase security rules Any-Any
delete rulebase security rules LAN2DMZ
delete rulebase security rules DMZ2LAN
delete rulebase security rules any2any
set address Private1 ip-range 10.0.0.0-10.255.255.255
set address Private2 ip-range 172.16.0.0-172.16.255.255
set address Private3 ip-range 192.168.0.0-192.168.255.255
set rulebase security rules GoogleDNS action allow from any to any source any destination 8.8.8.8
set rulebase security rules GoogleDNS application dns service application-default
set rulebase security rules DNSoutBlock action allow from LAN to EXTERNAL source any destination any profile-setting profiles spyware strict virus default vulnerability strict
set rulebase security rules DNSoutBlock action allow from DMZ to EXTERNAL source any destination any
set rulebase security rules DNSoutBlock application DNS service application-default
set rulebase security rules NTPandSYSLOGandDNS action allow from LAN to DMZ source any destination any profile-setting profiles spyware strict virus default vulnerability strict
set rulebase security rules NTPandSYSLOGandDNS action allow from DMZ to LAN source any destination
set rulebase security rules NTPandSYSLOGandDNS application ntp service application-default
set rulebase security rules NTPandSYSLOGandDNS application syslog service application-default
set rulebase security rules NTPandSYSLOGandDNS application dns service application-default
set rulebase security rules NTPandSYSLOGandDNS application ssl service application-default
set rulebase security rules NTPandSYSLOGandDNS application web-browsing service application-default
set rulebase security rules CentOStoUbuntuDB action allow from any to any source 172.20.240.11 destination 172.25."""+team_num+""".23 profile-setting profiles spyware strict virus default vulnerability strict
set rulebase security rules CentOStoUbuntuDB from any source 172.25."""+team_num+""".11
set rulebase security rules CentOStoUbuntuDB application any service any
set rulebase security rules PrivateIPOutNoNo action deny from LAN to External source any destination Private1
set rulebase security rules PrivateIPOutNoNo action deny from LAN to External source any destination Private2
set rulebase security rules PrivateIPOutNoNo action deny from DMZ to External source any destination Private3
set rulebase security rules PrivateIPOutNoNo application any service any
set rulebase security rules PaloAltoOut action allow from LAN to External source 172.20.241.100 destination any
set rulebase security rules PaloAltoOut action allow from LAN to DMZ source 172.20.241.100 destination any
set rulebase security rules PaloAltoOut application paloalto-updates service any
set rulebase security rules PaloAltoOut application dns service any
set rulebase security rules PaloAltoOut application ntp service any
set rulebase security rules Win7External action allow from External to External source 172.31."""+team_num+""".3 destination any
set rulebase security rules Win7External application any service any
set rulebase security rules CentOSin action allow from External to DMZ source any destination 172.25."""+team_num+""".11 profile-setting profiles spyware strict virus default vulnerability strict
set rulebase security rules CentOSin application ssl service application-default
set rulebase security rules CentOSin application web-browsing service application-default
set rulebase security rules 2008DNStoUbuntuDNS action allow from LAN to DMZ source 172.20.241.27 destination 172.20.240.23 profile-setting profiles spyware strict virus default vulnerability strict
set rulebase security rules 2008DNStoUbuntuDNS application dns service application-default
set rulebase security rules DEBIANtoUBUNTU action allow from LAN to DMZ source 172.20.241.39 destination 172.20.240.23 profile-setting profiles spyware strict virus default vulnerability strict
set rulebase security rules DEBIANtoUBUNTU application mysql service application-default
set rulebase security rules DEBIANtoUBUNTU to External destination 172.25."""+team_num+""".23
set rulebase security rules DEBIANtoUBUNTU to DMZ
set rulebase security rules UbuntuDNSto2008DNS action allow from DMZ to LAN source 172.20.240.23 destination 172.20.241.27 profile-setting profiles spyware strict virus default vulnerability strict
set rulebase security rules UbuntuDNSto2008DNS application dns service application-default
set rulebase security rules UbuntuDNSto2008DNS application ntp service application-default
set rulebase security rules UbuntuDNSto2008DNS application active-directory service application-default
set rulebase security rules UbuntuDNSto2008DNS application ldap service application-default
set rulebase security rules UbuntuDNSto2008DNS application ms-ds-smb service application-default
set rulebase security rules UbuntuDNSto2008DNS application msrpc service application-default
set rulebase security rules UbuntuDNSto2008DNS application ms-ds-smb service application-default
set rulebase security rules UbuntuDNSto2008DNS application netbios-ss service application-default
set rulebase security rules UbuntuDNSto2008DNS application netbios-dg service application-default
set rulebase security rules CentOSDNSto2008DNS action allow from DMZ to LAN source 172.20.240.11 destination 172.20.241.27 profile-setting profiles spyware strict virus default vulnerability strict
set rulebase security rules CentOSDNSto2008DNS application dns service application-default
set rulebase security rules CentOSDNSto2008DNS application ntp service application-default
set rulebase security rules CentOSDNSto2008DNS application active-directory service application-default
set rulebase security rules CentOSDNSto2008DNS application ldap service application-default
set rulebase security rules CentOSDNSto2008DNS application ms-ds-smb service application-default
set rulebase security rules CentOSDNSto2008DNS application msrpc service application-default
set rulebase security rules CentOSDNSto2008DNS application netbios-ss service application-default
set rulebase security rules CentOSDNSto2008DNS application netbios-dg service application-default
set rulebase security rules UbuntuDNSin action allow from External to DMZ source any destination 172.25."""+team_num+""".23 profile-setting profiles spyware strict virus default vulnerability strict
set rulebase security rules UbuntuDNSin application dns service application-default
set rulebase security rules DEBIANin action allow from External to LAN source any destination 172.25."""+team_num+""".39 profile-setting profiles spyware strict virus default vulnerability strict
set rulebase security rules DEBIANin application web-browsing service application-default
set rulebase security rules DEBIANin application smtp service application-default
set rulebase security rules DEBIANin application pop3 service application-default
set rulebase security rules DEBIANin application ssl service application-default
set rulebase security rules DEBIANin application imap service application-default
set rulebase security rules 2008DNSin action allow from External to LAN source any destination 172.25."""+team_num+""".27 profile-setting profiles spyware strict virus default vulnerability strict
set rulebase security rules 2008DNSin application dns service application-default
set rulebase security rules DMZout-CentOS action allow from DMZ to External source 172.20.240.11 destination any profile-setting profiles spyware strict virus default vulnerability strict
set rulebase security rules DMZout-CentOS application ssl service application-default
set rulebase security rules DMZout-CentOS application ftp service application-default
set rulebase security rules DMZout-CentOS application yum service application-default
set rulebase security rules DMZout-CentOS application github service application-default
set rulebase security rules DMZout-CentOS application git-base service application-default
set rulebase security rules DMZout-CentOS application ssh service application-default
set rulebase security rules DMZout-CentOS application web-browsing service application-default
set rulebase security rules DMZout-Ubuntu action allow from DMZ to External source 172.20.240.23 destination any profile-setting profiles spyware strict virus default vulnerability strict
set rulebase security rules DMZout-Ubuntu application dns service application-default
set rulebase security rules DMZout-Ubuntu application web-browsing service application-default
set rulebase security rules DMZout-Ubuntu application ssl service application-default
set rulebase security rules DMZout-Ubuntu application apt-get service application-default
set rulebase security rules SERVERout-2012WAout action allow from LAN to External source 172.20.241.3 destination any profile-setting profiles spyware strict virus default vulnerability strict
set rulebase security rules SERVERout-2012WAout application web-browsing service application-default
set rulebase security rules SERVERout-2012WAout application ssl service application-default
set rulebase security rules SERVERout-2012WAout application git-base service application-default
set rulebase security rules SERVERout-2012WAout application ms-update service application-default
set rulebase security rules SERVERout-2012WAout application github service application-default
set rulebase security rules SERVERout-2008AD action allow from LAN to External source 172.20.241.27 destination any profile-setting profiles spyware strict virus default vulnerability strict
set rulebase security rules SERVERout-2008AD application ssl service application-default
set rulebase security rules SERVERout-2008AD application ms-update service application-default
set rulebase security rules SERVERout-2008AD application dns service application-default
set rulebase security rules SERVERout-2008AD application web-browsing service application-default
set rulebase security rules SERVERout-Debian action allow from LAN to External source 172.20.241.39 destination any profile-setting profiles spyware strict virus default vulnerability strict
set rulebase security rules SERVERout-Debian application pop3 service application-default
set rulebase security rules SERVERout-Debian application imap service application-default
set rulebase security rules SERVERout-Debian application dns service application-default
set rulebase security rules SERVERout-Debian application ocsp service application-default
set rulebase security rules SERVERout-Debian application smtp service application-default
set rulebase security rules SERVERout-Debian application ssh service application-default
set rulebase security rules SERVERout-Debian application github service application-default
set rulebase security rules SERVERout-Debian application git-base service application-default
set rulebase security rules SERVERout-Debian application ssl service application-default
set rulebase security rules SERVERout-Debian application subversion service application-default
set rulebase security rules SERVERout-Debian application sourceforge service application-default
set rulebase security rules SERVERout-Debian application apt-get service application-default
set rulebase security rules SERVERout-Debian application web-browsing service application-default
set rulebase security rules INTERZONELAN action allow from LAN to LAN source any destination any
set rulebase security rules INTERZONELAN application any service any
set rulebase security rules INTERZONEDMZ action allow from DMZ to DMZ source any destination any
set rulebase security rules INTERZONEDMZ application any service any
set rulebase security rules DENYALLEXTERNAL action deny from External to any source any destination any
set rulebase security rules DENYALLEXTERNAL application any service any
set rulebase security rules DENYALL action deny from any to any source any destination any
set rulebase security rules DENYALL application any service any
commit
	"""

	command_file.write(commands)
	print "File is written to PAConfig_TEAMNUM.txt"
  print "Putty into the Palo Alto. Enter 'set cli scripting-mode on' and then 'configure'"
  print "Then copy and past the output of the script."
