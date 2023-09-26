import json

# Specify the file path where you saved the state
file_path = '/Users/jake.dalton/Documents/githubstate.json'

# Specify which target endpoints you intend to modify by setting to True
edit_issueComments = True
edit_issueEvents = True
edit_issues = True
edit_projects = True
# -----------------------------------------------------------------------------------------------

# Would you like to apply target dates to ALL dates within the endpoints EXCEPT those with target repo IDs two sections below?
edit_target_date_general_issueComments = True
edit_target_date_general_issueEvents = True
edit_target_date_general_issues = True
edit_target_date_general_projects = True
# Specify the general target dates for above section
# Only those marked as True will be considered
target_date_general_issueComments = '2023-01-01T00:00:00Z'
target_date_general_issueEvents = '2023-01-01T00:00:00Z'
target_date_general_issues = '2023-01-01T00:00:00Z'
target_date_general_projects = '2023-01-01T00:00:00Z'
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

# -----------------------------------------------------------------------------------------------

# Do not change any of the following; this is the execution
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
    elif edit_issueComments and repo_id not in target_ids_issueComments and edit_target_date_general_issueComments:
        repo_data['issueComments'] = target_date_general_issueComments
    elif edit_issueEvents and repo_id not in target_ids_issueEvents and edit_target_date_general_issueEvents:
        repo_data['issueEvents'] = target_date_general_issueEvents
    elif edit_issues and repo_id not in target_ids_issues and edit_target_date_general_issues:
        repo_data['issues'] = target_date_general_issues
    elif edit_projects and repo_id not in target_ids_projects and edit_target_date_general_projects:
        repo_data['projects'] = target_date_general_projects
# Saves the modified JSON back to the file with original formatting
with open(file_path, 'w') as f:
    json.dump(data, f, indent=None, separators=(',', ': '))
