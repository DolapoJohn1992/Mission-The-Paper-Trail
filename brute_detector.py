failed_count = 0
attacker_ips = []

with open("auth_audit.log", "r") as log_file, open("brute_report.txt", "w") as report_file:
    for line in log_file:
        if "Failed password" in line:
            report_file.write(line)
            failed_count += 1
            words = line.split()
            attacker_ips.append(words[-1])

# --- NEW ANALYSIS SECTION ---
unique_ips = set(attacker_ips)

print("-" * 30)
print(f"TOTAL ATTEMPTS: {failed_count}")

# Check each unique IP to see how many times it attacked
for ip in unique_ips:
    attempts = attacker_ips.count(ip)
    print(f"IP {ip} attempted {attempts} times.")
    
    # THRESHOLD ALERT: If an IP tried more than 2 times, flag it!
    if attempts > 2:
        print(f"!!! CRITICAL ALERT: Potential Brute Force from {ip} !!!")

print("-" * 30)