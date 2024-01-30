# Read Me

## Description
These python scripts allow you to modify the infamously terrifying Github cursor.
Each takes the file path and has changeable variables for options and functionality depending on your use case.

## How do I use this?

Please refer to the Slab article (coming soon) for detailed instructions

## Which one do I choose?

`GithubStateModifier.py` Is for general use. It allows a user to specify target endpoints for modification.
Modifiable endpoints are `issueComments`, `issueEvents`, `issues`, `projects`, `securityAlerts`, `workflowRuns`
**General Date Modification**: Users can apply a target date to all entries within the specified endpoints by setting the `edit_target_date_general_<endpoint>` flags to True and providing the new date in the `target_date_general_<endpoint>` variables.
**Specific Date Modification**: For more granular control, users can specify repository IDs and assign different target dates to these specific repositories. This is done by modifying the `target_ids_<endpoint>` lists with the target repository IDs and setting the target date in `target_date_<endpoint>_targetIDs`.


`GitHubStateModifier_CutoffDate.py` extends the functionality of the above general script by allowing users to specify new epoch dates for dates before the cutoff. In other words, if the cutoff date is `2023-01-01T00:00:00Z`, any cursor before this date will be modified to match this cutoff date. This becomes useful when customers do not need their data to sync from the actual epoch or need the sync to complete quickly.
Modifiable endpoints are `issueComments`, `issueEvents`, `issues`, `projects`, `securityAlerts`, `workflowRuns`.

`GithubStateModifier_commitsByBranch.py` Is specialized to modify the dates of all branches within `commitsByBranch` cursors. It also includes the above-described cutoff date feature.

