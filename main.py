import csv
import os
import sys

from getpass import getpass

from config import (
    PUBLIC_KEY_PATH,
    INVENTORY_FILE
)

from ping import ping
from ssh_copy import copy_ssh_key
from report import (
    add_success,
    add_failure,
    print_report
)


def main():

    print("=" * 55)
    print(" SSH KEY DISTRIBUTION AUTOMATION ")
    print("=" * 55)

    # Username

    username = input("Username : ")

    # Password

    password = getpass("Password : ")

    # Check Public Key

    if not os.path.exists(PUBLIC_KEY_PATH):
        print(f"\nPublic key not found: {PUBLIC_KEY_PATH}")
        sys.exit(1)

    # Read Public Key

    with open(PUBLIC_KEY_PATH) as file:
        public_key = file.read().strip()

    # Read Inventory

    with open(INVENTORY_FILE) as file:

        reader = csv.DictReader(file)

        servers = list(reader)

    total = len(servers)

    print(f"\nFound {total} server(s).\n")

    # Process Servers

    for count, server in enumerate(servers, start=1):

        hostname = server.get("hostname")
        ip = server.get("ip")

        if not hostname or not ip:
            continue

        print("-" * 55)
        print(f"[{count}/{total}] {hostname}")
        print(f"IP Address : {ip}")

        # Ping Test

        if not ping(ip):

            print("Status     : Host Unreachable")

            add_failure(
                hostname,
                "Host Unreachable"
            )

            continue

        print("Status     : Host Reachable")

        # Copy SSH Key

        status, message = copy_ssh_key(
            ip,
            username,
            password,
            public_key
        )

        if status:

            print("SSH Key    : Installed")

            add_success(hostname)

        else:

            print(f"SSH Key    : Failed ({message})")

            add_failure(
                hostname,
                message
            )

    print_report()


if __name__ == "__main__":
    main()
