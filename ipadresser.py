import ipaddress

ip = input("Indtast en IPv4-adresse: ")

try:
    adresse = ipaddress.ip_address(ip)

    if adresse.version == 4:
        print("Det er en gyldig IPv4-adresse!")
    else:
        print("Det er en IPv6-adresse. Vi skal bruge IPv4.")

except ValueError:
    print("Det er ikke en gyldig IP-adresse.")