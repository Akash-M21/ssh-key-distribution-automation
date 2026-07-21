import paramiko

from config import (
    SSH_PORT,
    SSH_TIMEOUT
)


def create_ssh_client(ip, username, password):
    """
    Create and return an authenticated SSH client.

    Args:
        ip (str): Server IP address
        username (str): SSH username
        password (str): SSH password

    Returns:
        paramiko.SSHClient
    """

    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(
        paramiko.AutoAddPolicy()
    )

    ssh.connect(
        hostname=ip,
        port=SSH_PORT,
        username=username,
        password=password,
        timeout=SSH_TIMEOUT
    )

    return ssh
