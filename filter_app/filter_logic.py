import re
from .models import ProhibitedPattern

def scan_job_description(content):
    patterns = ProhibitedPattern.objects.values_list('pattern', flat=True)
    for pattern in patterns:
        if re.search(pattern, content, re.IGNORECASE):
            return True
    return False
