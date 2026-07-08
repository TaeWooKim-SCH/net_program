# SSH: 원격 시스템의 CPU 및 메모리 정보 조회하기

import getpass
import paramiko

PORT = 22

cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)

user = input('Username: ')
pwd = getpass.getpass('Password: ')

cli.connect('114.71.220.5', port=22, username=user, password=pwd)

stdin, stdout, stderr = cli.exec_command('cat /proc/cpuinfo')
print(stdout.read().decode())

stdin, stdout, stderr = cli.exec_command('cat /proc/meminfo')
print(stdout.read().decode())

cli.close()