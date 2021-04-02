import random
import json

fake_ip_address = f"{random.randrange(1, 99)}.{random.randrange(1, 999)}.{random.randrange(1, 999)}.{random.randrange(1, 999)}"

with open('json/ip_address.json', 'r') as f:
    ip = json.load(f)
ip["ip_address"] = fake_ip_address
with open('json/ip_address.json', 'w') as f:
    json.dump(ip, f, indent=4)
    print(fake_ip_address)
