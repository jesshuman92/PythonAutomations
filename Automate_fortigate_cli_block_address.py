import ipaddress
##Convert ipaddress and fqdns into fortigate cli commands - txt
##Change the variables bellow to your input, output file and ticket name if you work with a ITSM tool.
input_file_name = 'input-ioc-xxxxx.txt'
output_file_name = 'output-fortigate-xxxxxx.txt'
ticket_name = 'Ticket#'
group_name = "GRP_xxxxx"
create_newgroup = 1 # 1 in case you will create a new group or 0, in case you will append only.

with open(input_file_name, 'r') as f, open(output_file_name, 'w') as fo:
    string_names = []
    print("Reading the file...")
    fo.write("config firewall address\n")
    for line in f:

        # name = "edit \"BLOCK-" + line.strip() + "\"\n"

        name = "\"BLOCK_" + line.strip() + "\"\n"
        string_names.append(name.strip())
        comment = "set comment \"{}\"\n".format(ticket_name)
        try:
            ipaddress.ip_address(line.strip())
            address = "set subnet " + line.strip()  + " 255.255.255.255 \n"
        except ValueError:
            address = "set type fqdn \nset fqdn \"{}\"\n".format(line.strip())
        fortigate_address =  "edit " + name + comment + address + "next \n"
        fo.write(fortigate_address)
    fo.write("end\n")
    fo.write("config firewall addrgrp\n")
    if create_newgroup == 1: fo.write("edit {}\n".format(group_name) + "set member ")
    elif create_newgroup == 0: fo.write("edit {}\n".format(group_name) + "append member ")
    chunck_grp = "".join( str(n + " ") for n in string_names)
    fo.write(chunck_grp)
    fo.write("\nnext\n")
    fo.write("end\n")
    print("Completed! Get your file from the same input folder!")


