import subprocess

from config import PING_COUNT


def ping(ip):
    """
    Check whether a host is reachable.

    Args:
        ip (str): IP address of the server.

    Returns:
        bool: True if reachable, False otherwise.
    """

    result = subprocess.run(
        ["ping", "-c", str(PING_COUNT), ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return result.returncode == 0
