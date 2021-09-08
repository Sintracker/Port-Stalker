#Ascii Text Library
import pyfiglet
import termcolor
from termcolor import cprint, colored
from pyfiglet import figlet_format,Figlet

print('''\
     ...  ..   ... .   .. . . .  ..      .                    
             .     .       ..        ...  ....    ,,. . .                       
           .          .., ..  .      .      .             ,       .             
        ..    .,,/  ..                      ,..... *,... .,****((//(*.. ...     
      .,, . ..,.,* ..              ,        .(#/##.,,/,,*,/%(/(*(/(,,,   ..     
  ..  ..,....,., .             .,        .*(/&#%#%&.(/##&%##(*(,. *  . ., .     
. . . ..,,. ,,,.,..,.  . . ,,,           .//.%&%%/*%(%&%&&&&(%/,//(.,.,.,       
 .. . ,* *.,/,,*..,,  .  .,,%(...      . *&#%&&&&&&&&&&&&&&&%%/(%(/*/*,. ..     
      .., .,,**,,.(,     ,.#&&(,*.      .,#&&&@&&&&%&&&&%&&&&%%%##*,/.,         
  . .    ...*,.  .    .#%&@&&&%@&.       .%%@%&%&&#&@&&&&&&&&&%#%#/,. ,,        
. ..,..,  .*.. ..(,.%&&&&&&&@&@@@@&.  ...*@&@&&&%@@@&@@&&&&&%&%&%%(# .   ..     
       .,,./*#* .,,,&&&&&&&@&@@@&&@/.  ..#&@&@&@&&&@&@@@@&&&@&&%%(%/./  ..,     
   .. .,.. ,,(*(*(/%&&@&&&&@@&&&@@&.,, ,..@&&&@@@@&@&@@@@&&&%%%%##/*..          
...,,  *,/**//.(.  .&&&&@&&&@@@&@#,.......%@&@&&@&&@@&&&&%%##(/*..,.            
          ..,  ...     *.*/..,  .      ,..(%&@@@@&&(,/,%#&@#%%#&(,,.            
   ....                .     ... ... .,*..,#@@@@@&@(&,...  . ,##**..            
..,,.. ,,/ .*.. . .                . ., .. .@&@&@@@%&&(/(%##%&&%%(/(*,.,..*. .  
  ..    ...,,.**,..     ,  ,     ...  .(...,&@@@@&@#%&%&&(&%&&%##(#(*/#**. .    
    .  . .*(/*&%#%*.. ,..         ,  ,/..   ,&@@&&%%&&%@&@&&%%%(/* . ...        
   ....,. *(,*#*(*#.*. * . . . *            .&&@&@&&&%%&&&&&&#((,,,.,. ,,*.   ..
                  #%.(.., ..,..... ,       ..,%&@&@&&&&&&&&%&(%,                
                 ,#%,.%,..     *...,/(&&&%&&&@&&@&&&%%&&#&@#*#/./*/ **.         
                 .  ./. * ,* #  .  ., .* .&&%#%&&%%&%&&&&&&%%%/  #*.***, ,.  .  
          , ..*.(**/%###***          . ,,#.,/%/%%&&%&#%%&&%%&##%/(**,  ,...  .  
       ,..  ,.* ., #*#* (.,*.#/%//*.*   *#%&&%%&&&%%%&%%%&&%#(,..  .,,  ...     
             ..,,,.*,..(/,*(,#(%/%%%%%&%%&%%&&%#%%&&%&%%#%#(/*.* ,,.            
                . ...*. (#.*(/   ,..(,#(/,,,(#/((#%###(#(//,,,,..  ....         
           .,. .   , * . ..***,*.. ...,,*(///((#((##((/*(/.  . .. ..            
                    ,  .               . .. ,.*,.**(,/,*  ..                    
      .  . . , . .     ..,.   ...,/,. ...**.*//(((/(/(*(*,,,,.,..... . .        
                                            ...... .. .  ''')

#ascii with formatted & coloured
cprint(figlet_format('Port Stalker', font='gothic'),'red', attrs=['bold'])

import nmap

scanner = nmap.PortScanner()

print("Port Stalker, simple nmap automation tool")
print("<------------------------------------------->")

ip_addr = input("Enter target IP address to scan: ")
print("The targetted IP is: ", ip_addr)
type(ip_addr)

resp = input (""" \nEnter the type of scan you'd like to run 
              1)SYN ACK Scan
              2)UDP Scan
              3)Comprehensive Scan \n""")
print("Your selected scan type is: ",resp)

if resp == '1':
   print("Nmap Version: ", scanner.nmap_version)
   scanner.scan(ip_Addr, '1-1024', '-v -sS')
   print(scanner.scaninfo())
   print("IP Status: ", scanner[ip_addr].state())
   print(scanner[ip_addr].all_protocols())
   print("Open Ports: ",scanner[ip_addr]['tcp'].keys())
elif resp == '2':
   print("Nmap Version: ", scanner.nmap_version)
   scanner.scan(ip_Addr, '1-1024', '-v -sU')
   print(scanner.scaninfo())
   print("IP Status: ", scanner[ip_addr].state())
   print(scanner[ip_addr].all_protocols())
   print("Open Ports: ",scanner[ip_addr]['udp'].keys())
elif resp == '3':
   print("Nmap Version: ", scanner.nmap_version)
   scanner.scan(ip_Addr, '1-1024', '-v -sS -sV -sC -A -O')
   print(scanner.scaninfo())
   print("IP Status: ", scanner[ip_addr].state())
   print(scanner[ip_addr].all_protocols())
   print("Open Ports: ",scanner[ip_addr]['tcp'].keys())
elif resp >= '4':
     print("Enter a valid option")



