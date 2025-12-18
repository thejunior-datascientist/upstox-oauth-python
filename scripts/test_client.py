from client.upstox_client import UpstoxClient

client = UpstoxClient()

print("\nPROFILE:\n")
print(client.get_profile())
