from ufc import get_sherdog_link, parse_sherdog_fighter

sherdog_link = get_sherdog_link('Ilia Topuria')
print("Sherdog URL:", sherdog_link)


fighter_data = parse_sherdog_fighter(sherdog_link)
print(fighter_data)
