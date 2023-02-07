#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# RENAME FILE CONFIG.sh AND FILL VARIABLES BELOW WITH YOUR INFORMATION
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# ----------------------------------------------------------------------------

################################################################
# Cloudflare DDNS Settings
################################################################

auth_email=""                               # The email used to login
auth_method=""                              # Set to "global" for Global API Key or "token" for Scoped API Token
auth_key=""                				    # Your API Token or Global API Key
zone_identifier=""                          # Can be found in the "Overview" tab of your domain
record_name=""                              # Which record you want to be synced
ttl="3600"                                  # Set the DNS TTL (seconds)
logfile_name=""				                # The file where records of server DDNS attempts will be kept


