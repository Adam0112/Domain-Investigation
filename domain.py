import streamlit as st

# Set the configuration for the page
st.set_page_config(page_title="Website Investigation Tool")

# Title of your app
st.title("Website Investigation Tool")

# Input field for the user to enter the domain
domain = st.text_input("Enter the website domain (e.g., example.com):", "example.com")

# Dictionary containing the services and their respective URL templates
services = {
    "Whois Lookup": "https://www.who.is/whois/{}",
    "Whoxy": "https://whoxy.com/{}",
    # You can add more services here
}

# Action button for the user to trigger the investigation process
if st.button("Investigate"):
    # Iterate through each service and generate clickable links
    for service_name, service_url_template in services.items():
        # Format the service URL with the user-entered domain
        service_url = service_url_template.format(domain)
        # Display each link as a clickable hyperlink with target="_blank"
        st.markdown(f'<a href="{service_url}" target="_blank">{service_name}</a>', unsafe_allow_html=True)
