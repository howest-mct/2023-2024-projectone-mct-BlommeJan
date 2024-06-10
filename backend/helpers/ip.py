from subprocess import getoutput

class IPAddress:
    def __call__(self):
        ips = getoutput("hostname --all-ip-addresses").split()
        # Filter out the IP you want based on a criterion, here assuming the second IP or a specific subnet
        return ips[1] if len(ips) > 1 else ips[0] if ips else 'No IP found'
    
if __name__ == '__main__':
    ip = IPAddress() # Creating an instance of IPAddress
    print(ip()) # Now calling the instance to get the IPs and printing them