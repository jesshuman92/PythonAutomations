#!/usr/bin/python3
# pip3 install hashlib virustotal-api
import json
import pprint
import sys
import hashlib
from os import path
from random import sample
from datetime import datetime
from virus_total_apis import PublicApi as VirusTotalPublicApi

import requests


with open('input-hashes.txt', 'r') as f, open('output.txt', 'w') as fo:
    print("Running... Wait.")

    #READ INPUT AND ACCESS VT API
    for line in f:
        id_hash = line.strip()
        url = "https://www.virustotal.com/api/v3/files/" + id_hash
        headers = {
            "Accept": "application/json",

            #INPUT YOUR API KEY BELLOW
            "x-apikey": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        }
        response = requests.get(url, headers=headers)
        response_dict = response.json()

        #IF NEEDED UNCOMMENT AND GET FULL RESPONSE BELLOW
        #print(response.text)

# BLOCK BELOW TEST MALICIOUNESS
# UNCOMMENT IF NEEDED
#         for key in response_dict.keys():
#
#             if key == "error":
#                 fo.write("Hash: " + id_hash + "\n")
#                 fo.write("Result: Unknown!" + "\n")
#             elif key == "data":
#                 fo.write("Hash: " + id_hash + "\n")
#                 malicious_score = response_dict['data']['attributes']['last_analysis_stats']['malicious']
#                 if malicious_score >= 1:
#                     resultado = "Resul: Malicious! VT score:" + str(malicious_score) + "/68" + "\n"
#                     fo.write(resultado)
#                 else:
#                     fo.write("Resul: Clean hash!" + "\n")

#BLOCK BELOW - GET THE HASHS IN MULTIPLE FORMATS
#UNCOMMENT IF NEEDED
        for key in response_dict.keys():
            if key == "error":
                fo.write("Result: Unknown!" + "\n")
                print("Result: Unknown!")
            elif key == "data":

                #UNCOMMENT WHAT YOU GOING TO USE
                #fo.write(response_dict['data']['attributes']['sha1'] + "\n")
                #fo.write(response_dict['data']['attributes']['sha256'] + "\n")
                fo.write(response_dict['data']['attributes']['md5']+ "\n")

                # ONLY PRINT
                #print("sha256: " + response_dict['data']['attributes']['sha256'])
                #print("sha1: " + response_dict['data']['attributes']['sha1'])
                print("md5: " + response_dict['data']['attributes']['md5'])



    print("Completed with sucess, find your file in the same folder of the input!")






