import streamlit as st

st.set_page_config(page_title="Website Investigation Tool")

st.title("Website Investigation Tool")

# Create an input bar for entering the website domain
domain = st.text_input("Enter the website domain (e.g., example.com):", "example.com")

# Dictionary of service URLs
services = {
    "Whois Lookup": "https://www.who.is/whois/{}",
    "Whoxy": "https://whoxy.com/{}",
    # Add other services here...
}

# Button to trigger the investigation
if st.button("Investigate"):
    # JavaScript snippet for opening URLs
    js = "<script>"
    
    # Iterate through each service URL
    for service_name, service_url_template in services.items():
        # Create a link to open the external website
        service_url = service_url_template.format(domain)
        js += f"window.open('{service_url}', '_blank');"

    js += "</script>"

    # Embed JavaScript in the page
    st.markdown(js, unsafe_allow_html=True)
