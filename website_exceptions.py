with open('websites.txt', 'r') as f:
    sites = f.read().splitlines()

nl = '\n'

for site in sites:
    with open('websites.txt', 'a') as f:
        f.write(f'{nl}{site}/*{nl}*.{site}{nl}*.{site}/*')