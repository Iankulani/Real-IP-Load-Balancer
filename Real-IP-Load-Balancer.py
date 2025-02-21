# -*- coding: utf-8 -*-
"""
Created on Fri Feb  21 03:345:47 2025

@author: IAN CARTER KULANI

"""

from colorama import Fore
import pyfiglet
import os
font=pyfiglet.figlet_format("IP LOAD BALANCER")
print(Fore.GREEN+font)

import requests

def get_real_ip(ip_address):
    # Define headers that may contain the real IP behind the load balancer
    real_ip_headers = [
        "X-Forwarded-For", 
        "X-Real-IP", 
        "X-Forwarded-Host", 
        "X-Cluster-Client-IP", 
        "X-Forwarded-Proto"
    ]
    
    try:
        # Send a request to the IP address
        response = requests.get(f'http://{ip_address}')
        
        # Check if the real IP headers are in the response headers
        for header in real_ip_headers:
            if header in response.headers:
                real_ip = response.headers.get(header)
                print(f"Real IP detected! Header: {header} = {real_ip}")
                return real_ip
        
        # If no real IP header is found, display a message
        print("No real IP headers found.")
        return None

    except requests.RequestException as e:
        print(f"Error contacting IP: {e}")
        return None

def main():
    # Prompt the user to enter the public IP address
    ip_address = input("Enter the IP address to check the Real IP behind the Load Balancer:")
    
    # Get the real IP behind the load balancer
    real_ip = get_real_ip(ip_address)
    
    if real_ip:
        print(f"The real IP behind the load balancer for {ip_address} is: {real_ip}")
    else:
        print(f"Could not detect the real IP behind the load balancer for {ip_address}.")

if __name__ == "__main__":
    main()
