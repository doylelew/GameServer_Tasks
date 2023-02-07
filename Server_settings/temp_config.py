#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# RENAME FILE CONFIG.PY AND FILL VARIABLES BELOW WITH YOUR INFORMATION
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# ----------------------------------------------------------------------------

# ////////////////////////////////////////////////////////////////
# information for logging into and searching Gmail for emails
# ////////////////////////////////////////////////////////////////

class Gmailconfig:
    def __init__(self):
        self.username = ''                          # email address used for logging into Gmail
        self.password = ''                          # Password used for logging in through 'unsecure' Apps 
        self.SMPT_SERVER= "imap.gmail.com"          # If gmail then you do not need to change, otherwise whatever imap your email server uses
        self.SMPT_PORT = 993                        # If gmail then you do not need to change, otherwise whatever port your email server uses for imap
        self.tabName = ""                           # The tab you want to sort emails by


# ////////////////////////////////////////////////////////////////
# 
# ////////////////////////////////////////////////////////////////
