import json
from datetime import datetime

# Specify the file path where you saved the state
file_path = '/Users/jake.dalton/Downloads/gitubState.json'

# Boolean to control whether the cutoff_date feature is active for each category
use_cutoff_date_issueComments = True
use_cutoff_date_issueEvents = True
use_cutoff_date_issues = True
use_cutoff_date_projects = True
use_cutoff_date_securityAlerts = True
use_cutoff_date_workflowRuns = True

# Specify the cutoff date for each category
cutoff_date_issueComments = '2023-01-01T00:00:00Z'
cutoff_date_issueEvents = '2023-01-01T00:00:00Z'
cutoff_date_issues = '2023-01-01T00:00:00Z'
cutoff_date_projects = '2023-01-01T00:00:00Z'
cutoff_date_securityAlerts = '2023-01-01T00:00:00Z'
cutoff_date_workflowRuns = '2023-01-01T00:00:00Z'

# Specify which target endpoints you intend to modify by setting to True
edit_issueComments = True
edit_issueEvents = True
edit_issues = True
edit_projects = True
edit_securityAlerts = True
edit_workflowRuns = True

# Specify the target dates for general sections
target_date_general_issueComments = '2023-01-01T00:00:00Z'
target_date_general_issueEvents = '2023-01-01T00:00:00Z'
target_date_general_issues = '2023-01-01T00:00:00Z'
target_date_general_projects = '2023-01-01T00:00:00Z'
target_date_general_securityAlerts = '2023-01-01T00:00:00Z'
target_date_general_workflowRuns = '2023-01-01T00:00:00Z'

# Specify the target repo IDs and their respective dates IF you have target IDs
target_ids_issueComments = []
target_date_issueComments_targetIDs = '2023-01-01T00:00:00Z'

target_ids_issueEvents = []
target_date_issueEvents_targetIDs = '2023-01-01T00:00:00Z'

target_ids_issues = []
target_date_issues_targetIDs = '2023-01-01T00:00:00Z'

target_ids_projects = []
target_date_projects_targetIDs = '2023-01-01T00:00:00Z'

target_ids_securityAlerts = []
target_date_securityAlerts_targetIDs = '2023-01-01T00:00:00Z'

target_ids_workflowRuns = []
target_date_workflowRuns_targetIDs = '2023-01-01T00:00:00Z'
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# NO EDITS NEEDED BELOW THIS POINT

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
def is_date_before_or_equal(date_str, cutoff_date_str):
    date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
    cutoff = datetime.strptime(cutoff_date_str, '%Y-%m-%dT%H:%M:%SZ')
    return date <= cutoff
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
    if edit_issueComments and (not use_cutoff_date_issueComments or is_date_before_or_equal(repo_data.get('issueComments', ''), cutoff_date_issueComments)):
        repo_data['issueComments'] = target_date_general_issueComments
    if edit_issueEvents and (not use_cutoff_date_issueEvents or is_date_before_or_equal(repo_data.get('issueEvents', ''), cutoff_date_issueEvents)):
        repo_data['issueEvents'] = target_date_general_issueEvents
    if edit_issues and (not use_cutoff_date_issues or is_date_before_or_equal(repo_data.get('issues', ''), cutoff_date_issues)):
        repo_data['issues'] = target_date_general_issues
    if edit_projects and (not use_cutoff_date_projects or is_date_before_or_equal(repo_data.get('projects', ''), cutoff_date_projects)):
        repo_data['projects'] = target_date_general_projects
    if edit_securityAlerts and (not use_cutoff_date_securityAlerts or is_date_before_or_equal(repo_data.get('securityAlerts', ''), cutoff_date_securityAlerts)):
        repo_data['securityAlerts'] = target_date_general_securityAlerts
    if edit_workflowRuns and (not use_cutoff_date_workflowRuns or is_date_before_or_equal(repo_data.get('workflowRuns', ''), cutoff_date_workflowRuns)):
        repo_data['workflowRuns'] = target_date_general_workflowRuns
    if repo_id in target_ids_issueComments and (not use_cutoff_date_issueComments or is_date_before_or_equal(repo_data.get('issueComments', ''), cutoff_date_issueComments)):
        repo_data['issueComments'] = target_date_issueComments_targetIDs
    if repo_id in target_ids_issueEvents and (not use_cutoff_date_issueEvents or is_date_before_or_equal(repo_data.get('issueEvents', ''), cutoff_date_issueEvents)):
        repo_data['issueEvents'] = target_date_issueEvents_targetIDs
    if repo_id in target_ids_issues and (not use_cutoff_date_issues or is_date_before_or_equal(repo_data.get('issues', ''), cutoff_date_issues)):
        repo_data['issues'] = target_date_issues_targetIDs
    if repo_id in target_ids_projects and (not use_cutoff_date_projects or is_date_before_or_equal(repo_data.get('projects', ''), cutoff_date_projects)):
        repo_data['projects'] = target_date_projects_targetIDs
    if repo_id in target_ids_securityAlerts and (not use_cutoff_date_securityAlerts or is_date_before_or_equal(repo_data.get('securityAlerts', ''), cutoff_date_securityAlerts)):
        repo_data['securityAlerts'] = target_date_securityAlerts_targetIDs
    if repo_id in target_ids_workflowRuns and (not use_cutoff_date_workflowRuns or is_date_before_or_equal(repo_data.get('workflowRuns', ''), cutoff_date_workflowRuns)):
        repo_data['workflowRuns'] = target_date_workflowRuns_targetIDs
with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)
