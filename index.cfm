<!-- index.cfm -->
<cfoutput>
    <cfset greetingMessage = greetUser("John")>
    #greetingMessage#
</cfoutput>

<cffunction name="greetUser" access="public" returntype="string">
    <cfargument name="userName" type="string" required="true">
    
    <cfset var message = "Hello, " & arguments.userName & "!" />
    
    <cfreturn message />
</cffunction>

<cfdump var="#greetUser('John')#">