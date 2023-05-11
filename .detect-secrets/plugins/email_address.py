import re
from detect_secrets.plugins.base import RegexBasedDetector

class EmailAddressDetector(RegexBasedDetector):
    """Scans for email addresses."""
    secret_type = 'Email Address'
    skip_list = [
        'git@',
        # Add more paths to skip as needed
    ]
    
    skip_pattern = '|'.join(f'({re.escape(email)})' for email in skip_list)

    denylist = [
        re.compile(rf'\b[A-Za-z0-9._%+-]+@(?!{skip_pattern})[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
    ]
