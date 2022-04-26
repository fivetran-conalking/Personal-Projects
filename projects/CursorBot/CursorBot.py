# Plug in your values here
myName = "Jake-dalton"
connectorName = "stripe_123"
groupId = "unknown_cat"
service = "stripe"
connectorId = "routing_cod"
ticketNumber = 81168
isFree = "true" #Is the resync going to be free? Almost always "true"

# ----------------------------------------------------------------------------------
#Only edit below here if you'd like to change your formatting

# File name format
print("**File name:**")
print("Reset-" +connectorName+ "-cursor-" +groupId+ ".json\n")
fileName = "Reset-" +connectorName+ "-cursor-" +groupId+ ".json"

# Commit title format
print("**Commit title:**")
print("modify-" +service+ "-" +connectorName+ "-cursor-" +groupId+ "\n")

# Commit body format
print('**Commit body:**')
print('Changes: ')
print('Reason: ')
print('group_id:', groupId)
print('Connector:', connectorName)
print('Zendesk: https://fivetran1813.zendesk.com/agent/tickets/'+str(ticketNumber)+ "\n")

# Branch title
print("**Branch title:**")
print(myName+ "-modify-" + service + "-" +connectorName+ "-cursor-" +groupId+ "\n")

print("------------------------------------------------------------------------------------------")

# SALAMe
print("**SALAMe Command:**")
print("salame jobs create", str(ticketNumber), "standard modify_state -f " +fileName+ "\n\n")

print("------------------------------------------------------------------------------------------")

#Modify state insert
print("**Modify state insert**")
print('{')
print('    "resync":'+isFree+',')
print('    "where_clause": {')
print('        "owner": "'+groupId+'",')
print('        "service": "'+service+'",')
print('        "id": "'+connectorId+'",')
print('        "schema_name": "'+connectorName+'"')
print('    },')
print('    "state":')
print('}\n\n')

print("------------------------------------------------------------------------------------------")

#Cursor Query
print("**Cursor Query**")
print("SELECT i.service, i.owner, i.schema_name, c.integration_id, c.value, , i.service_version")
print("FROM  public.connector_cursors c")
print("FULL JOIN public.integrations i ON c.integration_id = i.id")
print("	WHERE i.owner = '"+groupId+"'")
print("    AND i.schema_name = '"+connectorName+"';")
