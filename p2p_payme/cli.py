#!/usr/bin/env python3

import argparse
from p2p_payme.auth.api import Authenticator


def main():
    authenticator = Authenticator()

    parser = argparse.ArgumentParser(description="p2p_payme - Authentication CLI")
    parser.add_argument("-u", "--phone_number", help="Phone Number")
    parser.add_argument("-p", "--password", help="Password")

    args = parser.parse_args()

    if not args.phone_number:
        args.phone_number = input("Phone Number: ")
    if not args.password:
        args.password = input("Password: ")
    
    authenticator.set_credentials(args.phone_number, args.password)
    # Prompt the user for verification code interactively
    verification_code = input("Verification Code: ")

    deviceId = authenticator.activate(verification_code=verification_code)
    
    print(f"Device Id: {deviceId}")



if __name__ == "__main__":
    main()
