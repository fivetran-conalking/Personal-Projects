import json

# Specify the file path where you saved the state
file_path = '/Users/jake.dalton/Documents/Customer_example_state.json'

# Specify which target endpoints you intend to modify by setting to True
edit_issueComments = True
edit_issueEvents = True
edit_issues = True
edit_projects = True
edit_securityAlerts = True
edit_workflowRuns = True
# -----------------------------------------------------------------------------------------------

# Would you like to apply target dates to ALL dates within the endpoints?
# Target endpoints two sections below WITH specified repo IDs will be excluded from this
edit_target_date_general_issueComments = True
edit_target_date_general_issueEvents = True
edit_target_date_general_issues = True
edit_target_date_general_projects = True
edit_target_date_general_securityAlerts = True
edit_target_date_general_workflowRuns = True
# Specify the dates to change for above section
# Only those marked as True will be considered
target_date_general_issueComments = '1970-01-01T00:00:00Z'
target_date_general_issueEvents = '1970-01-01T00:00:00Z'
target_date_general_issues = '1970-01-01T00:00:00Z'
target_date_general_projects = '1970-01-01T00:00:00Z'
target_date_general_securityAlerts = '1970-01-01T00:00:00Z'
target_date_general_workflowRuns = '1970-01-01T00:00:00Z'
# -----------------------------------------------------------------------------------------------

# Specify the target repo IDs and their respective dates IF you have target repo IDs
# Empty the list for targeted endpoints IF you do not have specific target repo IDs and intend to just change all IDs with the above general section
# The IDs should be inserted into the list as so [repo_id1, repo_id2]
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
# Opens state file
with open(file_path) as f:
    data = json.load(f)
# Updates general target dates
for repo_data in data['repos'].values():
    if edit_issueComments and repo_data.get('id') not in target_ids_issueComments and edit_target_date_general_issueComments:
        repo_data['issueComments'] = target_date_general_issueComments
    if edit_issueEvents and repo_data.get('id') not in target_ids_issueEvents and edit_target_date_general_issueEvents:
        repo_data['issueEvents'] = target_date_general_issueEvents
    if edit_issues and repo_data.get('id') not in target_ids_issues and edit_target_date_general_issues:
        repo_data['issues'] = target_date_general_issues
    if edit_projects and repo_data.get('id') not in target_ids_projects and edit_target_date_general_projects:
        repo_data['projects'] = target_date_general_projects
    if edit_securityAlerts and repo_data.get('id') not in target_ids_securityAlerts and edit_target_date_general_securityAlerts:
        repo_data['securityAlerts'] = target_date_general_securityAlerts
    if edit_workflowRuns and repo_data.get('id') not in target_ids_workflowRuns and edit_target_date_general_workflowRuns:
        repo_data['workflowRuns'] = target_date_general_workflowRuns
# Updates target IDs' target dates
for repo_id, repo_data in data['repos'].items():
    if edit_issueComments and repo_id in target_ids_issueComments:
        repo_data['issueComments'] = target_date_issueComments_targetIDs
    if edit_issueEvents and repo_id in target_ids_issueEvents:
        repo_data['issueEvents'] = target_date_issueEvents_targetIDs
    if edit_issues and repo_id in target_ids_issues:
        repo_data['issues'] = target_date_issues_targetIDs
    if edit_projects and repo_id in target_ids_projects:
        repo_data['projects'] = target_date_projects_targetIDs
    if edit_securityAlerts and repo_id in target_ids_securityAlerts:
        repo_data['securityAlerts'] = target_date_securityAlerts_targetIDs
    if edit_workflowRuns and repo_id in target_ids_workflowRuns:
        repo_data['workflowRuns'] = target_date_workflowRuns_targetIDs
# Saves the modified JSON back to the file with original formatting
with open(file_path, 'w') as f:
    json.dump(data, f, indent=None, separators=(',', ': '))
