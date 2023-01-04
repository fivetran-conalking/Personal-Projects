# Plug in your values here
ticketNumber = 119439
groupId = "jealously_unrushed"
connectorName = "fivetran__ironclad"
service = "ironclad"
# ----------------------------------------------------------------------------------
#Only edit below here if you'd like to change your formatting

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

#Cursor Query
print("**Cursor Query**")
print("SELECT i.service, i.owner, i.schema_name, c.integration_id, c.value, i.service_version")
print("FROM  public.connector_cursors c")
print("FULL JOIN public.integrations i ON c.integration_id = i.id")
print("	WHERE i.owner = '"+groupId+"'")
print("    AND i.schema_name = '"+connectorName+"';")
