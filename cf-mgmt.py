import requests
import json

"""
This API token will need to be crafted to lock it down to only do what it needs to.

This has been tested with a API token with the following permissions:

Account.Access: Organizations, Identity Providers, and Groups
Account.Workers KV Storage
Account.Workers Scripts
Account.Load Balancing: Monitors And Pools
Account.Account Firewall Access Rules
Account.DNS Firewall
Account.Stream
Account.Billing
Account.Account Settings
Zone.Zone Settings
Zone.Zone
Zone.DNS
Zone.Workers Routes
Zone.SSL and Certificates
Zone.Logs
Zone.Page Rules
Zone.Load Balancers
Zone.Firewall Services
Zone.Analytics
Zone.Access: Apps and Policies
"""
api_token = 'your_api_token_here'
auth_headers = {
    'Authorization': 'Bearer '+api_token
    }

base_url = 'https://api.cloudflare.com/client/v4/'
access_rules = 'firewall/access_rules/rules'
firewall_rules = 'firewall/rules'
dns_records = 'dns_records'

# Basic function to remove this snippet of code out of every other function.
def api_call(request_url):
    return requests.get(
        request_url,
        headers=auth_headers
        ).json()['result']

# Returns the zone for the specified zone name, or all zones.
def get_zone(zone_id=None):
    request_url = base_url+'zones'

    if zone_id is not None:
        request_url += '/'+zone_id
    
    return api_call(request_url)

# Returns the account for the specified account name, or all accounts.
def get_account(account_id=None):
    request_url = base_url+'accounts'

    if account_id is not None:
        request_url += '/'+account_id
    
    return api_call(request_url)

### ZONE GETS
def get_firewall_rules(zone_id, rule_id=None):
    request_url = base_url+'zones/'+zone_id+'/'+firewall_rules

    if rule_id is not None:
        request_url += '/'+rule_id+'?id='+rule_id
    
    return api_call(request_url)

def get_dns(zone_id, filter=None):
    request_url = base_url+'zones/'+zone_id+'/'+dns_records

    if filter is not None:
        request_url += '?per_page=100&content=contains:'+filter+'&match=any'

    return api_call(request_url)
        
### ACCOUNT GETS
def get_access_rules(account_id, rule_id=None):
    request_url = base_url+'accounts/'+account_id+'/'+access_rules

    if rule_id is not None:
        request_url += '/'+rule_id+'?id='+rule_id
    
    return api_call(request_url)