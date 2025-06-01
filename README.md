## 🔐 Wi-Fi Credential Extractor (Educational Use Only)

> **DISCLAIMER:**
> This tool is intended for **educational and authorized penetration testing** purposes **only**.
> **Do not run this on machines or networks you do not own or have explicit permission to test.**
> Misuse may violate laws and regulations and is solely the responsibility of the user.

### 📖 Description

This Python script extracts saved Wi-Fi SSIDs and passwords from a Windows system using the built-in `netsh` utility. It demonstrates how attackers with local access could exfiltrate sensitive credentials, helping defenders understand risks and improve endpoint security.

Collected data is sent to a specified webhook endpoint for testing secure communication and incident response scenarios.

### 🛠 Features

* Lists all saved Wi-Fi profiles
* Retrieves saved passwords (if present)
* Sends credentials to a remote webhook
* Useful in red team simulations or security awareness demos

---

### ⚙️ How It Works

The script:

1. Uses `subprocess` to invoke Windows `netsh` commands.
2. Extracts all saved Wi-Fi profiles.
3. Retrieves passwords in cleartext (if available).
4. Sends the results to a user-defined webhook using `requests`.

---

### 💡 Example Use Cases

* **Red Team Simulations**: Show the risk of credential theft from compromised endpoints.
* **Security Awareness**: Educate users about storing sensitive credentials on shared or insecure systems.
* **Blue Team Training**: Demonstrate what types of exfiltration to monitor for.

---

### 🚫 Warning

* **Do not use this tool on systems you do not have authorization to test.**
* **Do not upload this to public GitHub repositories unless clearly marked for ethical/educational use.**
* **This project should never be used for unauthorized access or malicious activity.**

---

### 📦 Converting to EXE

You can convert the script to a standalone `.exe` file using [auto-py-to-exe](https://github.com/brentvollebregt/auto-py-to-exe):

```bash
pip install auto-py-to-exe
auto-py-to-exe
```

Use "One file" and "Window based" options to create a compact executable.

---

### 🔐 How to Protect Yourself

* Avoid storing Wi-Fi credentials on shared systems.
* Use local firewall rules and EDR tools to block unexpected outbound requests.
* Monitor for suspicious `netsh` usage via event logs and alerts.
