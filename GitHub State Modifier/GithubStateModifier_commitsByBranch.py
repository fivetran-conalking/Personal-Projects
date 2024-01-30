import json
from datetime import datetime

# Specify the file path where you saved the state
file_path = '/Users/jake.dalton/Downloads/gitubState.json'

# Specify the new date you want to set for all branches within commitsByBranch
new_date = '2023-01-01T00:00:00Z'

# Boolean to control whether the cutoff_date feature is active
use_cutoff_date = True

# Specify the cut-off date. Dates on or before this will be updated (if use_cutoff_date is True)
cutoff_date = '2023-01-01T00:00:00Z'
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# NO EDITS NEEDED BELOW THIS POINT

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
def parse_date(date_str):
    for fmt in ('%Y-%m-%dT%H:%M:%S.%fZ', '%Y-%m-%dT%H:%M:%SZ'):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            pass
    raise ValueError('no valid date format found')
def is_date_before_or_equal(date_str, cutoff_date_str):
    date = parse_date(date_str)
    cutoff = parse_date(cutoff_date_str)
    return date <= cutoff
with open(file_path, 'r') as file:
    data = json.load(file)
for repo_id, repo_data in data['repos'].items():
    if 'commitsByBranch' in repo_data:  
        for branch, date in repo_data['commitsByBranch'].items():
            if not use_cutoff_date or is_date_before_or_equal(date, cutoff_date):
                repo_data['commitsByBranch'][branch] = new_date
with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)
