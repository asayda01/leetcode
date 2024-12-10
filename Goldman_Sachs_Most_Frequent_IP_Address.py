"""

Given a list of logs with IP addresses in the following format.
lines = ["10.0.0.1 - GET 2020-08-24", "10.0.0.1 - GET 2020-08-24", "10.0.0.2 - GET 2020-08-20"]

Return the most frequent IP address from the logs. The retuned IP address value must be in a string format.
 If multiple IP addresses have the count equal to max count,
  then return the address as a comma-separated string with IP addresses in sorted order.

"""


def frequentIP(address):

    maxCount = 0
    table = {}
    for addr in address:
        addr = addr.split()[0]
        table[addr] = table.get(addr, 0) + 1
        maxCount = max(maxCount, table[addr])

    maxIp = [ip for ip, count in table.items() if count == maxCount]

    if len(maxIp) > 1:
        return ','.join(sorted(maxIp))
    else:
        return maxIp[0]


lines = ["10.0.0.1 - GET 2020-08-24", "10.0.0.1 - GET 2020-08-24", "10.0.0.2 - GET 2020-08-20"]

print(frequentIP(lines))
