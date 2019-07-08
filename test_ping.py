from ping3 import ping, verbose_ping

regionIP = {
    "NA": "104.160.131.3",
    "EUW": "104.160.141.3",
    "EUNE": "104.160.142.3",
    "OCE": "104.160.156.1",
    "LAN": "104.160.136.3",
}

while True:
    choice = input ("Which server would you like?:\n1. NA\n2. EUW\n3. EUNE\n4. OCE\n5. LAN\n\n")
    if choice in ['1','2','3','4','5']:
        break
# process the input
if choice == '1': 
     verbose_ping(regionIP.get("NA"), timeout=10, count=16)
elif choice == '2': 
    verbose_ping(regionIP.get("EUW"), timeout=10, count=16)
elif choice == '3': 
    verbose_ping(regionIP.get("EUNE"), timeout=10, count=16)
elif choice == '4': 
    verbose_ping(regionIP.get("OCE"), timeout=10, count=16)
elif choice == '5': 
    verbose_ping(regionIP.get("LAN"), timeout=10, count=16)