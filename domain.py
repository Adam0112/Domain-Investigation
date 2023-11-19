import streamlit as st
from streamlit.components.v1 import html

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
        # Display each link as a clickable hyperlink
        st.markdown(f"[{service_name}]({service_url})", unsafe_allow_html=True)

# Function to open a link in a new tab
def open_page(url):
    open_script = f"""
        <script type="text/javascript">
            window.open('{url}', '_blank').focus();
        </script>
    """
    html(open_script)

# Button to open a specific link (you can add this button as needed)
if st.button('Open link', on_click=open_page, args=('https://streamlit.io',)):
    pass  # You can perform additional actions if needed when the button is clicked
