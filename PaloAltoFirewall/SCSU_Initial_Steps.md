1.	Grab config file from transfer.sh

2.	Paste config file into Putty session

>a.	First type set cli scripting-mode on

>b.	Configure

>c.	Paste

>d.	Fix

3.	Change admin password from command line

>a.	Configure

>b.	Set mgt-config users admin password

>d.	Commit

4.	Change secondary DNS server to 8.8.8.8

>a.	commit

5.	Download and Install Dynamic Updates

6.	Add rule above that rule to allow web browsing to 184.168.221.40

>a.	commit

7.	Check for software updates – download the base 6.0.1 (Do not install) and then the latest. (Install this one)

8.	Setup syslog forwarding to 172.20.241.3

>a.	Create forwarding profile from Device Tab

>b.	From Objects tab – Log Forwarding

>c.	Only forward high and critical logs to forwarding profile

>d.	commit

9.	Setup NTP server 

>a.	Device Tab

>b.	206.71.252.18

>c.	74.120.81.219

>d.	Commit



