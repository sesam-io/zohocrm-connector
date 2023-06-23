import requests
import os
import sys

modules = ["Leads", "Accounts", "Contacts", "Deals", "Campaigns", "Tasks", "Cases", "Events", "Calls", "Solutions",
           "Products", "Vendors", "Price Books", "Quotes", "Sales Orders", "Purchase Orders", "Invoices",
           "Custom", "Appointments", "Appointments Rescheduled History", "Services", "Activities"]

access_token = os.environ.get("ACCESS_TOKEN")
if access_token is None:
    print("You need to get and set the ACCESS_TOKEN env var before running this script")
    sys.exit(1)

for module_api_name in modules:
    url = f"https://www.zohoapis.eu/crm/v3/settings/fields?module={module_api_name}"
    headers = {
        f"Authorization": f"Zoho-oauthtoken {access_token}"
    }
    r = requests.get(url, headers=headers)

    data = r.json()

    if "fields" in data:
        res = sorted([item["api_name"] for item in data["fields"]])
        print(module_api_name, ":", ','.join(res))
    else:
        print(f"No 'fields' for module '{module_api_name}: {data}'")

#        url = f"https://www.zohoapis.eu/crm/v3/settings/modules/{module_api_name}"
#        headers = {
#            f"Authorization": f"Zoho-oauthtoken {access_token}"
#        }
#        r = requests.get(url, headers=headers)
#        try:
#            print(r.json())
#        except BaseException as e:
#            print(r.content)
