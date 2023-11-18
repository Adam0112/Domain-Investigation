import webbrowser
import time
import random
import streamlit as st

st.set_page_config(page_title="Website Investigation Tool")

st.title("Website Investigation Tool")

# Create an input bar for entering the website domain
domain = st.text_input("Enter the website domain (e.g., example.com):", "example.com")

# Define a function to open a website in a web browser
def open_website_in_browser(domain, service_url):
    url = service_url.format(domain)
    webbrowser.open(url)

# Dictionary of service URLs
services = {
    "Whois Lookup": "https://www.who.is/whois/{}",
    "Whoxy": "https://whoxy.com/{}",
    "Threat Intelligence": "https://threatintelligenceplatform.com/{}",
    "Certificate Search": "https://crt.sh/?q={}",
    "Domain History": "https://securitytrails.com/domain/{}",
    "Malware Scanning": "https://www.virustotal.com/gui/domain/{}",
    "urlscan.io": "https://urlscan.io/result/{}",
    "builtwith.com": "https://builtwith.com/relationships/{}",
    "dnslytics.com": "https://dnslytics.com/domain/{}",
    "spyonweb.com": "https://spyonweb.com/{}",
    "archive.org": "https://web.archive.org/web/*/{}",
    "archive.eu": "https://archive.eu/{}",
    "CrowdTangle": "https://apps.crowdtangle.com/search?q={}&platform=facebook&sortBy=score&sortOrder=desc",
    "host.io": "https://host.io/{}"
}

# Button to trigger the investigation
if st.button("Investigate"):
    # Iterate through each service URL
    for service_name, service_url in services.items():
        open_website_in_browser(domain, service_url)

        # Generate a random sleep time
        sleep_time = random.uniform(1, 5)
        time.sleep(sleep_time)
