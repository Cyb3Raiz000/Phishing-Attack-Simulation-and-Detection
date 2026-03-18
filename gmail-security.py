import imaplib
import email
import re
import quopri
from urllib.parse import urlparse, parse_qs

# --- 1. THE ADVANCED LOGIC ENGINE ---
def analyze_email(raw_text):
    msg = email.message_from_string(raw_text)
    score = 0
    findings = []
    
    display_from = str(msg.get('From', ''))
    return_path = str(msg.get('Return-Path', ''))
    auth_results = str(msg.get('Authentication-Results', ''))

    # ACTION: Check SPF/DKIM (Standard Security Protocols)
    if "spf=fail" in auth_results.lower():
        score += 40
        findings.append("SPF Failure: Sender identity cannot be verified")
    
    # Check for Display Name Spoofing
    if "google" in display_from.lower() and "@google.com" not in return_path.lower():
        score += 50
        findings.append("Spoofing: Name says 'Google' but email source is different")

    # Bytes-safe Body Extraction
    body_bytes = b""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() in ["text/html", "text/plain"]:
                payload = part.get_payload(decode=True)
                if payload: body_bytes += payload
    else:
        payload = msg.get_payload(decode=True)
        if payload: body_bytes = payload

    try:
        body_text = quopri.decodestring(body_bytes).decode('utf-8', errors='ignore')
    except:
        body_text = body_bytes.decode('utf-8', errors='ignore')

    # URL Analysis & Defanging
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', body_text)
    defanged_urls = [u.replace("http", "hxxp").replace(".", "[.]") for u in urls] # Security Best Practice

    for url in urls:
        if 'rid=' in url.lower():
            score += 50
            findings.append("Gophish Signature: Likely a simulated attack")
        if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url):
            score += 30
            findings.append("Suspicious: Link points to raw IP address")

    return min(score, 100), display_from, findings, defanged_urls

# --- 2. THE SECURITY ACTION CONTROLLER ---
def run_security_scan():
    # CONFIGURATION (Use your App Password)
    GMAIL_USER = "company-email@gmail.com"
    GMAIL_PASS = "company-email-app-password"

    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(GMAIL_USER, GMAIL_PASS)
        mail.select("inbox")
        
        status, messages = mail.search(None, 'UNSEEN')
        email_ids = messages[0].split()
        
        # Taking the last 20 for this security batch
        test_ids = email_ids[-50:]
        print(f"\n[!] CYB3RAIZ000: Monitoring {len(test_ids)} fresh entries...")

        for e_id in test_ids:
            _, data = mail.fetch(e_id, "(RFC822)")
            raw_email = data[0][1].decode('utf-8', errors='ignore')
            
            score, sender, reasons, links = analyze_email(raw_email)

            if score >= 70:
                print(f"\n🚨 [CRITICAL ACTION] Phish from: {sender}")
                print(f"   REASON: {', '.join(reasons)}")
                
                # ACTION 1: Permanent Quarantine (Move to Trash)
                mail.store(e_id, '+X-GM-LABELS', '\\Trash')
                
                # ACTION 2: Label as Spam for Gmail's internal filters
                mail.store(e_id, '+X-GM-LABELS', '\\Spam')
                
                # ACTION 3: Log Malicious URLs for Blacklisting
                with open("blacklist_urls.txt", "a") as f:
                    for l in links: f.write(f"{l}\n")
                print("   [+] URLs defanged and added to Blacklist Log.")

            elif score >= 30:
                print(f"⚠️  [SUSPICIOUS] {sender} | Score: {score}")

        mail.logout()
        print("\n--- ✅ Security Action Cycle Complete ---")

    except Exception as e:
        print(f"Security Engine Error: {e}")

if __name__ == "__main__":
    run_security_scan()
