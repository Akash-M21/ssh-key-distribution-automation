from ssh import create_ssh_client

import paramiko


def copy_ssh_key(ip, username, password, public_key):
    """
    Copy SSH public key to remote server.

    Returns:
        (bool, str)
    """

    ssh = None

    try:

        ssh = create_ssh_client(
            ip,
            username,
            password
        )

        command = f"""
mkdir -p ~/.ssh &&
chmod 700 ~/.ssh &&
touch ~/.ssh/authorized_keys &&
grep -qxF "{public_key}" ~/.ssh/authorized_keys || echo "{public_key}" >> ~/.ssh/authorized_keys &&
chmod 600 ~/.ssh/authorized_keys
"""

        stdin, stdout, stderr = ssh.exec_command(command)

        exit_status = stdout.channel.recv_exit_status()

        if exit_status == 0:
            return True, "Success"

        return False, stderr.read().decode().strip()

    except paramiko.AuthenticationException:
        return False, "Authentication Failed"

    except paramiko.SSHException:
        return False, "SSH Connection Failed"

    except Exception as e:
        return False, str(e)

    finally:

        if ssh:
            ssh.close()
