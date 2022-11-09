#!/usr/bin/env python

##########################################
# Ping Test                              #
# Test for On or Offline host using ping #
# Written by Diego Viane                 #
# https://github.com/diegoviane2/        #
##########################################

from pythonping import ping

def host_test(ip_addr):
    data = ping(target=ip_addr, count=5, timeout=2)
    
    return {
        'host': ip_addr,
        'avg_latency': data.rtt_avg_ms,
        'min_latency': data.rtt_min_ms,
        'max_latency': data.rtt_max_ms,
        'packet_loss': data.packet_loss
    }
    
hosts = [
    '192.168.0.1',
    '192.168.0.2'
]

print('[ begin test ... ]')

for host in hosts:
    print(host_test(host))

print('[ END ]')


# ToDo:
# Get address list from a external text file.
# CSV format.

# Show a warning message if any ocurrency of Packet Loss.

# Generate a Log file with timestamps. Can be only launch time.