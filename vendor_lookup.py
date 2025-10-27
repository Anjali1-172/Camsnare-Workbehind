import requests

def get_vendor(mac):
    try:
        response = requests.get(f"https://api.macvendors.com/{mac}")
        return response.text
    except:
        return "Unknown Vendor"