BASE_URL = "cisco.com"

def get_url(base_url, module, container, resource=None):
    # Returns the RESTCONF URL
    url = f'{BASE_URL}/{module}:{container}/{resource}'
    return url

print(get_url(BASE_URL, "devnet", "c1", "bgp"))

    