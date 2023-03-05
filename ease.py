import argparse
import requests

def enum_subdomains(url, wordlist):
    with open(wordlist, 'r') as file:
        subdomains = file.read().splitlines()

    for subdomain in subdomains:
        test_url = f'http://{subdomain}.{url}'

        try:
            requests.get(test_url)
            print(f'[+] Found subdomain: {test_url}')
        except requests.exceptions.RequestException:
            pass

if __name__ == '__main__':
    # Define the banner
    banner = """
             ___    ___    _______   _______   ________  _________   
            |"  |  |"  |  /"      \ /"      \ |"        \/"        |  
            ||  |  ||  | (:        (:        ||     __/  \         \ 
            |:  |  |:  |  \___/   \ \___/   /  )__/  \\  /        /  
            |.  |  |.  |   /  ___  \\//  ___/      /   /|:   __   \  
            /\  |\ /\  |\ //  \__/\ /  \__/\     |   // |  /" \   :) 
            (__\|_)(__\|_)(__________)(________)  \__/(__|__/\  __/  
                                                          ( (__)     
            Ease Subdomain Founder                                  
            Created By: Benson Ndiwa (BenBugs)                    
            """
    print(banner)
    parser = argparse.ArgumentParser(description='Enumerate subdomains of a website')
    parser.add_argument('-u', '--url', type=str, help='The base URL to scan for subdomains', required=True)
    parser.add_argument('-w', '--wordlist', type=str, help='The wordlist to use for subdomain enumeration', required=True)
    args = parser.parse_args()

    enum_subdomains(args.url, args.wordlist)
