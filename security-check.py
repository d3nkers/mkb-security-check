"""
MKB security ccheck tool

Eenvoudige beveiligingscheck voor websites, speciaal gericht op MKB'ers.

Copyright (c) 2025 d3nkers solutions - https://d3nkers-solutions.nl
"""

import argparse
import requests
import json
import os
import re
import logging
from urllib.parse import urlparse

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def has_https(url):
    parsed_url = urlparse(url)
    if parsed_url.scheme != "https":
        return False, "Geen HTTPS! Dit kan een risico zijn."
    return True, "HTTPS is actief."

def get_headers(url):
    try:
        response = requests.get(url, timeout=5)
        return response.headers
    except requests.exceptions.Timeout:
        logging.warning("Timeout bij het ophalen van headers voor %s", url)
        return None
    except requests.exceptions.RequestException as e:
        logging.error("Fout bij ophalen headers: %s", e)
        return None

def missing_headers(headers):
    needed = ["X-Frame-Options", "Content-Security-Policy", "Strict-Transport-Security", "Referrer-Policy", "Permissions-Policy"]
    return ", ".join([h for h in needed if h not in headers]) if headers else "Kan headers niet ophalen."

def find_waf(url):
    try:
        response = requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
        known_waf = ["Server", "X-Sucuri-ID", "CF-RAY", "X-CDN", "X-Powered-By"]
        waf_detected = [f"{h}: {response.headers[h]}" for h in known_waf if h in response.headers]
        if response.status_code == 403:
            waf_detected.append("Mogelijk een WAF, kreeg HTTP 403.")
        return ", ".join(waf_detected) if waf_detected else "Geen WAF gevonden."
    except requests.exceptions.RequestException:
        return "Probleem bij ophalen van pagina."

def check_cms(url):
    try:
        response = requests.get(url, timeout=5)
        cms_signals = {
            "WordPress": ["wp-content", "wp-includes"],
            "Joomla": ["Joomla"],
            "Drupal": ["drupal.js"],
            "Magento": ["Mage.Cookies"]
        }
        for cms, markers in cms_signals.items():
            if any(marker in response.text for marker in markers):
                return cms
        return "Geen CMS gedetecteerd."
    except requests.exceptions.RequestException:
        return "CMS niet bepaald."

def dir_listing(url):
    try:
        response = requests.get(url + "/", timeout=5)
        return "⚠️ Directory Listing AAN!" if "Index of /" in response.text else "Geen directory listing."
    except requests.exceptions.RequestException:
        return "Geen respons."

def save_results(results, fmt, filename):
    try:
        if fmt == "json":
            with open(filename, "w") as f:
                json.dump(results, f, indent=4)
        elif fmt == "html":
            with open(filename, "w") as f:
                f.write("""
                <html>
                <head><title>Security Rapport</title>
                <style>body { font-family: Arial; }</style>
                </head>
                <body><h1>Security Rapport</h1><table>
                <tr><th>Check</th><th>Resultaat</th></tr>
                """)
                for key, value in results.items():
                    f.write(f"<tr><td>{key}</td><td>{value}</td></tr>")
                f.write("</table></body></html>")
        if os.path.exists(filename):
            logging.info("✅ Rapport opgeslagen als: %s", filename)
        else:
            logging.warning("❌ Opslaan mislukt!")
    except IOError:
        logging.error("Kan bestand niet schrijven: %s", filename)

def main():
    parser = argparse.ArgumentParser(description="Security check voor websites.")
    parser.add_argument("url", help="Website om te scannen.")
    parser.add_argument("--output", help="Opslaan als JSON of HTML", choices=["json", "html"], default=None)
    args = parser.parse_args()

    url = args.url if args.url.startswith("http") else "https://" + args.url
    domain = urlparse(url).netloc.replace(".", "_")
    logging.info("Scanning: %s", url)
    
    results = {
        "HTTPS": has_https(url)[1],
        "Missende Headers": missing_headers(get_headers(url)),
        "WAF Detectie": find_waf(url),
        "CMS Detectie": check_cms(url),
        "Directory Listing": dir_listing(url)
    }
    
    for key, value in results.items():
        print(f"{key}: {value}")
    
    if args.output:
        filename = f"security_report_{domain}.{args.output}"
        save_results(results, args.output, filename)

if __name__ == "__main__":
    main()

