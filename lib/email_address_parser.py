import re

class EmailAddressParser:
    def __init__(self, email_string):

        self.email_string = email_string
    
    def parse(self):
        emails = re.split(r'[,\s]+', self.email_string)
        
       
        emails = [email.strip() for email in emails if email.strip()]
        
        
        valid_emails = [email for email in emails if '@' in email]
        
        unique_emails = list(set(valid_emails))
       
        unique_emails.sort()
        
        return unique_emails


# Test cases
if __name__ == "__main__":
    # Test with comma-separated emails
    email_addresses = "john@doe.com, person@somewhere.org"
    parser = EmailAddressParser(email_addresses)
    print(parser.parse())

    
    # Test with space-separated emails
    parser2 = EmailAddressParser("john@doe.com person@somewhere.org")
    print(parser2.parse())

    
