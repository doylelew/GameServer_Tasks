#!/usr/bin/bash

##################################################################
# Import Settings from congif.sh
##################################################################
. ../Server_settings/config.sh

logfile="../Logs/$logfile_name"

##################################################################
# functions for logging the DDNS attempts
##################################################################
function serverLog (){
	echo -e "$(date +"%Y-%m-%d %T"): \t$1">>$logfile
}

function logbreak(){
	echo -e "\n--------------------------------------\n">>$logfile
}



##################################################################
#get the record of the existing A name
##################################################################
logbreak
serverLog "Searching for record labeled $record_name"

record=$(curl -s -X GET "https://api.cloudflare.com/client/v4/zones/$zone_identifier/dns_records?type=A&name=$record_name" \
	-H "X-Auth Email: $auth_email" \
	-H "Authorization: Bearer $auth_key" \
	-H "Content-Type: application/json")



##################################################################
# collect necessary variables from the "Get"
##################################################################
record_identifier=$(echo "$record" | sed -E 's/.*"id":"(\w+)".*/\1/')
old_ip=$(echo "$record" | sed -E 's/.*"content":"(([0-9]{1,3}\.){3}[0-9]{1,3})".*/\1/')
serverLog "Found $record_name with identifier $record_identifier"



##################################################################
# Get IP address
##################################################################
ipv4_regex='([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])'
ip=$(curl -s -4 https://cloudflare.com/cdn-cgi/trace | grep -E '^ip'); ret=$?
if [[ ! $ret == 0 ]]; then # In the case that cloudflare failed to return an ip.
    # Attempt to get the ip from other websites.
    ip=$(curl -s https://api.ipify.org || curl -s https://ipv4.icanhazip.com)
else
    # Extract just the ip from the ip line from cloudflare.
    ip=$(echo $ip | sed -E "s/^ip=($ipv4_regex)$/\1/")
fi

# Use regex to check for proper IPv4 format.
if [[ ! $ip =~ ^$ipv4_regex$ ]]; then
    serverLog "DDNS Updater: Failed to find a valid IP."
    exit 2
fi



#################################################################
# Check if updating is necessary 
#################################################################
if [[ $ip == $old_ip ]]; then
	serverLog "DDNS Updater: IP ($ip) for record ($record_identifier) has not changed."
	exit 1
fi



##################################################################
# Update the DNS Records
##################################################################
JSON_STRING=$( jq -n \
	--arg RcName "$record_name" \
	--arg ipAddress "$ip" \
	--arg dateTime "$(date +"%Y-%m-%d %T")" \
	'{type:"A", name: $RcName, content: $ipAddress, ttl:3600, proxied:false, comment:$dateTime}' )
serverLog "Submitting Json:\n$JSON_STRING"

response=$(curl -v -X PUT "https://api.cloudflare.com/client/v4/zones/$zone_identifier/dns_records/$record_identifier" \
	-H "X-Auth-Email: $auth_email" \
	-H "Authorization: Bearer $auth_key" \
	-H "Content-Type: application/json" \
	--data "$JSON_STRING")

serverLog "Returned response of:\n$response"

exit 0

