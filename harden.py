#!/usr/bin/python

#run from server 'python harden.py domain'
#THis will run most commands in https://gridpane.com/kb/configuring-fail2ban-to-prevent-brute-force-attacks/ and https://gridpane.com/kb/Nginx-Site-Hardening-with-GP-CLI/
# Assumes Step 1 Custom rule stack is done in https://gridpane.com/kb/Nginx-Site-Hardening-with-GP-CLI/

import sys
from os import system
import crypt

def SiteHarden(domain):
    system('gp site ' + domain + ' -disable-xmlrpc')
    system('gp site ' + domain + ' -enable-wp-fail2ban')
    system('gp site ' + domain + ' -configure-wp-fail2ban -block-user-enumeration')
    system('gp site ' + domain + ' -configure-wp-fail2ban -block-stupid-usernames')
    system('gp site ' + domain + ' -configure-wp-fail2ban -guard-comments')
    system('gp site ' + domain + ' -configure-wp-fail2ban -guard-password-resets')
    system('gp site ' + domain + ' -configure-wp-fail2ban -guard-pingbacks')
    system('gp site ' + domain + ' -configure-wp-fail2ban -guard-spam')
    system('gp site ' + domain + ' -block-wp-content.php')
    system('gp site ' + domain + ' -block-wp-comments-post.php')
    system('gp site ' + domain + ' -block-wp-links-opml.php')
    system('gp site ' + domain + ' -block-wp-trackbacks.php')
    system('gp site ' + domain + ' -block-install.php')
    

def main(argv):
    #TODO
    #PARAMETER SANItisation

    SiteHarden(argv[0])

if __name__ == '__main__':
    main(sys.argv[1:])
