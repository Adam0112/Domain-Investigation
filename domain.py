import streamlit as st
from streamlit.components.v1 import html

# Function to generate JavaScript for opening a new tab
def open_page(url):
    open_script = f"""
        <script type="text/javascript">
            window.open("{url}", "_blank").focus();
        </script>
    """
    html(open_script)

# Inserting the domain you want to investigate
domain = st.text_input("Enter the domain you want to investigate:", "example.com")

# Creating a dictionary of service URLs
services = {
    "Whois Lookup": "https://www.who.is/whois/{}",
    # ... (add other services here)
}

# Display buttons for each service
for service_name, service_url in services.items():
    formatted_url = service_url.format(domain)
    if st.button(f'Open {service_name}'):
        open_page(formatted_url)
