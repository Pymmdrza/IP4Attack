import time
from ipaddress import IPv4Network
from colorama import Fore, Style
from rich import print
from rich.console import Console

console = Console()

z = 0
fu = 0
mmdrza = str(f'''


       ╔═══════════════════════════════════════════════════════════════════════╗  
       ║      [deep_sky_blue1]╔═╗╦═╗╔═╗╔═╗╦═╗╔═╗╔╦╗╔╦╗╔═╗╦═╗[/][orange3]  ╔╦╗╔╦╗╔╦╗╦═╗╔═╗╔═╗ ╔═╗╔═╗╔╦╗[/]     ║
       ║      [turquoise2    ]╠═╝╠╦╝║ ║║ ╦╠╦╝╠═╣║║║║║║║╣ ╠╦╝[/][yellow1]  ║║║║║║ ║║╠╦╝╔═╝╠═╣ ║  ║ ║║║║[/]     ║
       ║      [deep_sky_blue1]╩  ╩╚═╚═╝╚═╝╩╚═╩ ╩╩ ╩╩ ╩╚═╝╩╚═[/][orange3]  ╩ ╩╩ ╩═╩╝╩╚═╚═╝╩ ╩o╚═╝╚═╝╩ ╩[/]     ║
       ╠═══════════════════════════════════════════════════════════════════════║
       ║  [red        ]     ╔═╗╦╔╦╗╦═╗  [/][grey66]╔═╗╔═╗╦═╗  ╔╗ ╔═╗╔╦╗╔═╗╦ ╦  ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═[/]      ║
       ║  [bright_red ]     ║  ║ ║║╠╦╝  [/][grey93]╠╣ ║ ║╠╦╝  ╠╩╗╠═╣ ║ ║  ╠═╣  ╠═╣ ║  ║ ╠═╣║  ╠╩╗[/]      ║
       ║  [red        ]     ╚═╝╩═╩╝╩╚═  [/][grey66]╚  ╚═╝╩╚═  ╚═╝╩ ╩ ╩ ╚═╝╩ ╩  ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩[/]      ║
       ║  [gold1      ]    CIDR TO IP RANGE LIST [/][white]: Programmer Mmdrza.Com  :[grey66]t.me/PyMmdrza[/]    ║
       ╚═══════════════════════════════════════════════════════════════════════╝''')

cidr = str(input('INSERT CIDR => '))
filex = str(input('INSERT OUTPUT FILE NAME => [With .txt] : '))
print(mmdrza)

for addr in IPv4Network(f'{cidr}'):
    z += 1
    with open(filex, 'a') as fx:
        fx.write(str(addr) + '\n')
        fx.close()
        console.print(f"""
                        {mmdrza}\r                        
       [dark_green   ]000  [/][white] 
       [green        ]001  [/][white] Generated[/]    :[yellow] {z}\r [/]   
       [green4       ]011  [/][white] OUTPUT FILE[/]  :[cyan] {filex} [/]   
       [green3       ]111  [/][white] CIDR         [/]:[orange1] {cidr}\r   
       [green1       ]110  [/][white] IP           [/]:[white] {addr}\r  [/]                                      
       [spring_green1]10  [/][white]                                       
                        
     
                  """)

        time.sleep(0.1)
        console.clear()
