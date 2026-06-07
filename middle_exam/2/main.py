import socket;

ip = '220.69.189.125';
port = 443;

domain = socket.getfqdn(ip);
protocol = socket.getservbyport(port);

print(domain);
print(protocol);
print(f"{protocol}://{domain}");
print(socket.inet_aton(ip));
