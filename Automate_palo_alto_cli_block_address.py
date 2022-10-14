#This file converts ipaddress iocs into fortigate command line
#If you want to generate to panorama managed palo alto fws, enable 1 bellow

panorama_mode = 0
#You can change the names bellow to your desired files
with open('ipaddress-iocs.txt', 'r') as f, open('ipaddress-iocs-palo-alto-fws.txt', 'w') as fo:
    string_names = []
    print("Reading the file...")
    fo.write("configure\n")
    for line in f:

        # name = "edit \"BLOCK-" + line.strip() + "\"\n"
        object_name = "BLOCK_" + line.strip()
        string_names.append(object_name.strip())
        #if you work for a MSSP, change the line bellow for your ticket number
        description = "set comment \"Ticket#\" \n"
        if panorama_mode == 0:
            address = "set address " + object_name + " ip-netmask " + line.strip() + "/32 \n"
        if panorama_mode == 1:
            address = "set shared address " + object_name + " ip-netmask " + line.strip() + "/32 \n"
        # fortigate_address =  "edit " + name + comment + address + "next \n"
        fo.write(address)
    chunck_grp = "".join(str(name + " ") for name in string_names)
    if panorama_mode == 0: fo.write("set address-group GRP_YYYYYYYYY" + " static [ " + chunck_grp + " ]")
    if panorama_mode == 1: fo.write("set shared address-group GRP_YYYYYYYYY" + " static [ " + chunck_grp + " ]")
    print("Finished with success! The file will be in the same input folder")

