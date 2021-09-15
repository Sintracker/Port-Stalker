#! /usr/bin/python3


#Ascii Text Library
import termcolor
from termcolor import cprint, colored
import pyfiglet
from pyfiglet import figlet_format,Figlet

print('''\
                                                                                     
                                   *@@     @@,                                  
                                 @@@@@     @@@@@                                
                               @@@@@@@@@@@@@@@@@@@                              
                             @@@@@@@@@@@@@@@@@@@@@@@                            
                           @@@@@@@@@@@     @@@@@@@@@@@                          
                         @@@@@@@@@@#         #@@@@@@@@@@                        
                       @@@@@@@@@@    /@   @/    @@@@@@@@@@                      
                     @@@@@@@@@@    @@@@   @@@@    @@@@@@@@@@                    
                   @@@@@@@@@,    @@@@@     @@@@@    .@@@@@@@@@                  
                 @@@@@@@@@    &@@@@@   @ @   @@@@@&    @@@@@@@@@                
               @@@@@@@@@    @@@@@@  #@@@ @@@#  @@@@@@    @@@@@@@@@              
             @@@@@@@@@    @@@@@@  @@@,     *@@@  @@@@@@    @@@@@@@@@            
           @@@@@@@@@    @@@@@@  @@@           @@@  @@@@@@    @@@@@@@@@          
         @@@@@@@@@    @@@@@@  @@@     @@@@@     @@@  @@@@@@    @@@@@@@@@        
          @@@@@@ @@@    @@@@@  @@@    @@@@@    @@@  @@@@@    @@@ @@@@@@         
           (@@@@@, @@@     @@@@   @@         @@   @@@@     @@@.,@@@@@#          
             @@@@@@ @@@@      @@@   @       @.  @@@      @@@@ @@@@@@            
              .@@@@@  @@@@      @@   @     @   @@      @@@@  @@@@@,             
                @@@@   @@@       #@           @#       @@@   @@@@               
                @@@@   @@@         &         &         @@@   @@@@               
               #@@@#    @@                             @@    #@@@#              
               @@@@        @    @@(           #@@    @        @@@@              
               @@@@             .@@@@       @@@@.             @@@@              
               *@@@@             @@@@       @@@@             @@@@*              
                @@@@             @@@@       @@@@             @@@@               
                 @@@#             @@@       @@@             #@@@                
                  @@@             @@@       @@@             @@@                 
                   @@             @@@       @@@             @@                  
                    @@             @@       @@             @@                   
                     @             @@       @@             @                    
                      @             @       @             @                     
                                    @       @       ''')
print("<------------------------------------------------------------------------------------------------>")
#ascii with formatted & coloured
cprint(figlet_format('Port Stalker', font='gothic'),'red', attrs=['bold'])

import nmap

scanner = nmap.PortScanner()

print("[INFO]")
print("[ || ]   Port Stalker, simple nmap automation tool]")
print("[ || ]")
print("[ || ]")
print("[DISCLAIMER] We do not promote the use of this tool for illegal purposes, ethical use only.")
print("<------------------------------------------------------------------------------------------------>")

ip_addr = input("Enter target IP address to scan: ")
print("[+] The targetted IP is: ", ip_addr)
type(ip_addr)
open_ports = "-p"
count = 0

resp = input (""" \nEnter the type of scan you'd like to run 
              1)SYN ACK Scan
              2)UDP Scan
              3)Comprehensive Scan
              4)Service versions and OS scan
              5)Show Usage \n""")
print("Your selected scan type is: ",resp)

if resp == '1':
   print("Nmap Version: ", scanner.nmap_version)
   print("Performing -v -sS on "+ip_addr+"...")
   scanner.scan(hosts=ip_addr, arguments= "-v -sS")
   print(scanner.scaninfo())
   print("\nHost : %s" % ip_addr)
   print("State : %s" % scanner[ip_addr].state())
   for proto in scanner[ip_addr].all_protocols():
       print("Protocol : %s" % proto)
       print()
       lport = scanner[ip_addr][proto].keys()
       sorted(lport)
       for port in lport:
           print("Port : %s\tState : %s" % (port, scanner[ip_addr][proto][port]["state"]))
           if count == 0:
              open_ports = open_ports+" "+str(port)
              count = 1
           else:
                open_ports = open_ports+","+str(port)
   print("\nOpen Ports : -v -sS "+open_ports+" "+ip_addr)
elif resp == '2':
   print("Nmap Version: ", scanner.nmap_version)
   print("Performing -v -sU on "+ip_addr+"...")
   scanner.scan(hosts=ip_addr, arguments= "-v -sU")
   print(scanner.scaninfo())
   print("\nHost : %s" % ip_addr)
   print("State : %s" % scanner[ip_addr].state())
   for proto in scanner[ip_addr].all_protocols():
       print("Protocol : %s" % proto)
       print()
       lport = scanner[ip_addr][proto].keys()
       sorted(lport)
       for port in lport:
           print("Port : %s\tState : %s" % (port, scanner[ip_addr][proto][port]["state"]))
           if count == 0:
              open_ports = open_ports+" "+str(port)
              count = 1
           else:
                open_ports = open_ports+","+str(port)            
   print("\nOpen Ports : -v -sU "+open_ports+" "+ip_addr)
elif resp == '3':
   print("Nmap Version: ", scanner.nmap_version)
   print("Performing comprehensive scan on "+ip_addr+"...")
   scanner.scan(hosts=ip_addr, arguments= "-sS -sV -sC -A -O")
   print(scanner.scaninfo())
   print("\nHost : %s" % ip_addr)
   print("State : %s" % scanner[ip_addr].state())
   for proto in scanner[ip_addr].all_protocols():
       print("Protocol : %s" % proto)
       print()
       lport = scanner[ip_addr][proto].keys()
       sorted(lport)
       for port in lport:
           print("Port : %s\tState : %s" % (port, scanner[ip_addr][proto][port]["state"]))
           if count == 0:
              open_ports = open_ports+" "+str(port)
              count = 1
           else:
                open_ports = open_ports+","+str(port)
   print("For nmap use copy :")             
   print("\nOpen Ports : -sS -sV -sC -A -O "+open_ports+" "+ip_addr)
elif resp == '4':
   print("Nmap Version: ", scanner.nmap_version)
   print("Performing service versions and OS scan on "+ip_addr+"...")
   scanner.scan(hosts=ip_addr, arguments= "-v -sV -O")
   print(scanner.scaninfo())
   print("\nHost : %s" % ip_addr)
   print("State : %s" % scanner[ip_addr].state())
   for proto in scanner[ip_addr].all_protocols():
       print("Protocol : %s" % proto)
       print()
       lport = scanner[ip_addr][proto].keys()
       sorted(lport)
       for port in lport:
           print("Port : %s\tState : %s" % (port, scanner[ip_addr][proto][port]["state"]))
           if count == 0:
              open_ports = open_ports+" "+str(port)
              count = 1
           else:
                open_ports = open_ports+","+str(port)
   print("For nmap use copy :")             
   print("\nOpen Ports : -v -sV -O "+open_ports+" "+ip_addr)
   

elif resp == '5':
   print("""\nThis utility is to be used with Nmap.\n
   [!] The purpose of this utility is to show the open ports of an ip address 
   (TCP/UDP) and giving a response on which ports are open with the respective arguments
   to perform a deeper scan later on Nmap with said arguments, while also showing the respective commands 
   for a faster scan. \n""") 
elif resp >= '6' or resp <= '0':
     print("Enter a valid option")