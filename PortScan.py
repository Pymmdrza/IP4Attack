import socket
from rich import print

hosts: str = input('INSERT FILE IPLIST [Just names] : ')
ports = int(input('INSERT PORT NUMBER  : '))
timeout_seconds = 0.5
z = 0
fu = 0
with open(str(hosts + '.txt'), 'r') as filehosts:
    for host in filehosts:
        z += 1
        host = host.rstrip("\n")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout_seconds)
        result = sock.connect_ex((host, int(ports)))
        if result == 0:
            fu += 1
            # print("[green]Host: {}, [/][yellow]Port: {}, [/][cyan]Status:[/][green] True[/]".format(host, ports))
            print(f"""[green]Successful Connect[/][gold1] : [/][white]{host}[/][red1]:[/][blue]{ports}[/][gold1] ---- [/][with][[/][b green]TRUE[/][white]][/]""")
            with open(hosts + "_output_scan.txt", "a") as fc:
                fc.write('\n' + str(host) + ':' + str(ports))
                fc.close()
        else:
            #    print("[gold1]Scan:{} [/][white] Found: {} [/][red]Host: {}, Port: {}, Status[/]:[white on red] False [/]".format(z, fu, host, ports))
            print(f"""[gold1]{z}[/]  [red][[/][white]Total Found:{fu}[/][red]][white on red][FALSE][/][red1] Scan IP PORT[/][yellow]:[/][yellow1]{ports} [red1]in This IP:[/][yellow1]{host}[/]""")
            sock.close()
