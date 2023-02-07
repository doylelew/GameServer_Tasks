import imaplib
from ..Server_settings.config import Gmailconfig

###############################################################################
#Setting for Login
###############################################################################

config=Gmailconfig()

###############################################################################
#Login to Gmail
###############################################################################

Gmail_Connection = imaplib.IMAP4_SSL(config.SMPT_SERVER)
Gmail_Connection.login(config.username, config.password)


###############################################################################
#Find the correct email tab
###############################################################################

TabType, emailTab = Gmail_Connection.select(f"/ {config.tabName} /")

print(f"Results of the gmail tab\n {emailTab}")


###############################################################################
#close unfinished work and logout
###############################################################################
Gmail_Connection.close()
Gmail_Connection.logout()