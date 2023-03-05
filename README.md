# Ease Subdomain Finder

A subdomain enumerator is a tool or script that is used to discover subdomains associated with a given domain. Subdomains are commonly used by organizations to separate different parts of their website, such as subdomains for blogs, forums, or e-commerce sections.

A subdomain enumerator works by generating a list of possible subdomains based on a provided domain name, and then checking each one to see if it resolves to an IP address. This process is typically performed by sending DNS queries to the domain name server (DNS) and checking the responses.


## Installation

```bash
pip3 install requests
pipe install argparse
```

## Usage

```python
#Clone git repository
git clone https://github.com/Benson306/Ease-Subdomain-Finder

# Go into Directory
cd Ease-Subdomain-Finder

# Run the subdomain enumerator
python3 ease.py -u <TARGET URL> -w <WORDLIST>

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)