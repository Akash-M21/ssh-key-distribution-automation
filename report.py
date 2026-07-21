success = []
failed = []


def add_success(host):
    success.append(host)


def add_failure(host, reason):
    failed.append(
        {
            "host": host,
            "reason": reason
        }
    )


def print_report():

    total = len(success) + len(failed)

    print("\n")
    print("=" * 60)
    print("SSH KEY DISTRIBUTION REPORT")
    print("=" * 60)

    print(f"Total Servers : {total}")
    print(f"Successful    : {len(success)}")
    print(f"Failed        : {len(failed)}")

    print("\nSuccessful Hosts")
    print("-" * 60)

    if success:

        for host in success:
            print(f"✔ {host}")

    else:

        print("None")

    print("\nFailed Hosts")
    print("-" * 60)

    if failed:

        for item in failed:
            print(f"✖ {item['host']} ({item['reason']})")

    else:

        print("None")

    print("=" * 60)
