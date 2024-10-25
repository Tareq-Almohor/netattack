import click
from scripts.valid_ip import check_valid_ip
from scripts.attacks_tab import attacks_tab

@click.command()
@click.option('--dstip',type=str)
@click.option('--srcip',type=str)
@click.option('--dfltgtw',type=str)

def main(dstip,srcip,dfltgtw):
    click.secho('------------------------------------',fg='yellow')
    click.secho('|    ______ _____  ____  ______    |',fg='yellow')
    click.secho('|      /   /      /        /       |',fg='yellow')
    click.secho('|     /   /____  /____    /        |',fg='yellow')
    click.secho('|    /   /_____  ____/   /         |',fg='yellow')
    click.secho('------------------------------------',fg='yellow')

    click.secho('[1] Show All IPs  [2] Change Destination IP  [3] Change Source IP  [4] Change Default Gateway  [5] Attack  [6] Exit',fg='bright_yellow')
    choice = input('> Please pick a choice: ')
    while(choice != '6'):
        if choice == '1':
            click.echo(f'The Source IP is {srcip}, the Destination IP is {dstip}, and the Default Gateway is {dfltgtw}')
            choice = input('> Please pick a choice: ')
        elif choice == '2':
            dstip = input('> Please enter the Destination IP: ')
            while(not check_valid_ip(dstip)):
                dstip = input('The IP you have entered is invalid. Please enter a valid IP: ')
            click.echo(f'Valid IP! The Destination IP is {dstip}')
            choice = input('> Please pick a choice: ')
        elif choice == '3':
            srcip = input('> Please enter the Source IP: ')
            while(not check_valid_ip(srcip)):
                srcip = input('The IP you have entered is invalid. Please enter a valid IP: ')
            click.echo(f'Valid IP! The Source IP is {srcip}')
            choice = input('> Please pick a choice: ')
        elif choice == '4':
            dfltgtw = input('> Please enter the Default Gateway: ')
            while(not check_valid_ip(dfltgtw)):
                dfltgtw = input('The IP you have entered is invalid. Please enter a valid IP: ')
            click.echo(f'Valid IP! The Default Gateway is {dfltgtw}')
            choice = input('> Please pick a choice: ')
        elif choice == '5':
            if dstip == None and srcip == None and dfltgtw == None:
                click.echo('You did not assign the Destination IP,Source IP, and Default Gateway.')
                choice = input('> Please pick a choice: ')
            elif dstip == None:
                click.echo('You did not assign the Destination IP.')
                choice = input('> Please pick a choice: ')
            elif srcip == None:
                click.echo('You did not assign the Source IP.')
                choice = input('> Please pick a choice: ')
            elif dfltgtw == None:
                click.echo('You did not assign the Default Gateway.')
                choice = input('> Please pick a choice: ')
            #elif not check_valid_ip(dstip) and not check_valid_ip(srcip):
            #    click.echo('The Destination and Source IPs you wrote is invalid. Please change the IP.')
            #    choice = input('> Please pick a choice: ')
            #elif not check_valid_ip(dstip):
            #    click.echo('The Destination IP you wrote is invalid. Please change the IP.')
            #    choice = input('> Please pick a choice: ')
            #elif not check_valid_ip(srcip):
            #    click.echo('The Source IP you wrote is invalid. Please change the IP.')
            #    choice = input('> Please pick a choice: ') 
            else:
                attacks_tab(srcip,dstip,dfltgtw)
                break
        else:
            click.echo('Invalid input.')
            choice = input('Please pick a choice: ')
    else:
        click.echo('Exiting TEST')

if __name__ == '__main__':
    main()
