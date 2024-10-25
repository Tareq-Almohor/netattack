import click
from scripts.attacks.syn_flood import syn_flood
from Test_CLI.scripts.attacks.arp_spoofing import arp_spoofing
from scripts.attacks.ip_spoofing import ip_spoofing

def attacks_tab(srcip:str,dstip:str,dfltgtw:str):
    click.secho('[1] SYN Flood  [2] ARP Spoofing  [3] IP Spoofing  [4] DNS Spoofing',fg='bright_yellow')
    attack_choosen = input('> Please enter the attack you want to launch (Number): ')
    while(True):
        if attack_choosen == '1':
            click.secho(f'Launching SYN Flood attack on {dstip}')
            syn_flood(srcip,dstip)
            break
        elif attack_choosen == '2':
            click.secho(f'Launching ARP Spoofing attack on {dstip}')
            arp_spoofing(dstip,dfltgtw)
            break
        elif attack_choosen == '3':
            click.secho(f'Launching IP Spoofing attack on {dstip}')
            ip_spoofing(dstip)
            break
        elif attack_choosen == '4':
            click.secho(f'Launching DNS Spoofing attack on {dstip}')
            
            break
        else:
            click.secho('Invalid input.')
            attack_choosen = input('> Please enter the attack you want to launch (Number): ')
