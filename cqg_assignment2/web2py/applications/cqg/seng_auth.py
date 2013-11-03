#!/usr/bin/python

import ldap
import errorlog

# given a username and their plain-text password:
# -return 0 if they match according to ENGR accounts
# -return 1 if password is wrong
# -return 2 if username is not valid
# -return 3 if error occured talking to LDAP server
def authenticate(username, password):
    base_dn = "dc=seng,dc=uvic,dc=ca"
    scope = ldap.SCOPE_SUBTREE
    filter = "(&(objectClass=posixAccount)(uid=" + username + "))"
    attrs = None
    try:
    # 1. see if user exists in ldap
    #    return 2 if not found
        conn = ldap.initialize("ldap://ldap.seng.uvic.ca")
        ldap_result_id = conn.search(base_dn, scope, filter, attrs)
        result_type, result_data = conn.result(ldap_result_id, 0)
        if (result_data == []):
            return 2 # no user found
    except ldap.LDAPError, e:
        errolog.write("ldap exception from seng_auth: "+str(e))
        return 3 # LDAP Server error
    # 2. try authenticated bind as user
    #    return 1 if failed
    try:
        dn = "uid=" + username + ",ou=People," + base_dn
        conn.bind_s(dn, password)
    except ldap.INVALID_CREDENTIALS, e:
        return 1 # bad password
    conn.unbind()
    return 0 # bind worked
