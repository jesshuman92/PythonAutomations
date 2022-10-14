
<!-- ABOUT THIS PROJECT -->
## PythonAutomations

This project started with a need for automating simple daily tasks, such as verifying hashes or scripting into some firewall commands, getting reports...
I am now slowly making it public so it may help others.

Script "Get_hash_maliciousness_virus_total.py":
* Get Hashes in formats sha256, sha1, md5 for purposes of inputting in different console ex: Trendmicro/Palo alto Cortex, from Virus Total
* Get maliciouness score from VT when you have too many hashes to test mannualy 

Script "Automate_palo_alto_cli_block_address.py"
* Get ip address and turn them into palo alto fws/panorama managed cli groups (commandline) for easy dealing with huge blocks of ip to block.

Script "Automate_fortigate_cli_block_address.py" 
* Get ip address and fqdn and turn them into fortigate cli groups (commandline).

