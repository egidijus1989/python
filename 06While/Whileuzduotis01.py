kaina = float(input('Iveskite kavos kaina...'))
likutis = kaina

while kaina > 0:
    moneta = float(input('idekite...'))
    likutis = kaina - moneta
    print(f'liko sumoketi {likutis}')