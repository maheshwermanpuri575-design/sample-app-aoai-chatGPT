import openai
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Initialize Azure Key Vault client
credential = DefaultAzureCredential()
key_vault_name = input("Enter your Key Vault name: ")  # Dynamically input Key Vault name
client = SecretClient(vault_url=f"https://{key_vault_name}.vault.azure.net/", credential=credential)

# Initialize Azure OpenAI client
openai.api_type = "azure"
openai.api_base = "https://azaideoai.openai.azure.com/"  # Replace with your OpenAI resource name
openai.api_version = "2024-12-01-preview"  # Verify this with current API version in Azure
openai.api_key = "DKswmcYMX1DHDCaHKUPHIdDQIaflSKRnPM0RbRlh3SaP9w0VhTYmJQQJ99BHACHYHv6XJ3w3AAABACOG1SeR"  # Replace with your OpenAI API Key

# Function to get secret from Key Vault
def get_secret(secret_name):
    try:
        secret = client.get_secret(secret_name)
        return secret.value
    except Exception as e:
        return f"Error retrieving secret: {e}"

# Function to query Azure OpenAI
def query_openai(prompt):
    try:
        response = openai.ChatCompletion.create(
            engine="gpt-4o-mini",  # Replace with your Azure OpenAI model name
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error querying OpenAI: {e}"

# Main program loop to process user input
def main():
    while True:
        user_input = input("Enter your request (type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        
        if "secret" in user_input.lower():
            secret_name = input("Enter the secret name you want to retrieve: ")  # Dynamically input secret name
            secret_value = get_secret(secret_name)
            print(f"Secret Value: {secret_value}")
        
        elif "VM" in user_input:
            # Replace with logic for retrieving VM specifications
            vm_name = input("Enter the VM name you want to retrieve specifications for: ")  # Dynamically input VM name
            print(f"VM Specifications for {vm_name} (to be implemented)...")
        
        else:
            response = query_openai(user_input)
            print(f"AI Response: {response}")

if __name__ == "__main__":
    main()
