import re


def validate_email_address(email_address: str) -> bool:
    """This function takes in email address and validates that email
    address based on the presence of "@", no space in the address and
    vaalid email providers such as yahoo, gmail and outlook.

    Args:
        email_address (str): email address to be validates

    Returns:
        bool: True if email address is valid else False
    """
    valid_providers = ['yahoo', 'gmail', 'outlook']
    email_format = r'^[a-zA-Z0-9._%+-]+@[a-ZA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_address, email_format):
        return False

    domain = email_address.split("@")[1].lower()

    if 'yopmail' in domain:
        return False
    
    if any(provider in domain for provider in valid_providers):
        return True
    
    return False
    
    

    