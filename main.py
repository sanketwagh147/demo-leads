import requests


def collect_leads():
    # SuiteCRM credentials
    url = "https://suitecrmdemo.dtbc.eu/service/v4/rest.php"
    username = "Demo"
    password = "Demo"

    # API endpoint for fetching leads
    endpoint = url + "/module/Leads"

    # Fields to collect
    fields = ["phone_work", "first_name", "last_name"]

    # Authenticate with SuiteCRM
    session = requests.Session()
    session.post(
        url + "/login",
        data={"user_auth": {"user_name": username, "password": password}},
    )

    # Fetch leads data
    response = session.get(
        endpoint, params={"fields": ",".join(fields), "max_num": 10000}
    )

    if response.status_code == 200:
        leads_data = response.json()["entry_list"]
        # print(response.text)
        leads = []

        # Extract required fields from leads data
        for lead_data in leads_data:
            lead = {}
            for field in fields:
                if field in lead_data["name_value_list"]:
                    lead[field] = lead_data["name_value_list"][field]["value"]
                else:
                    lead[field] = None
            leads.append(lead)


print(collect_leads())
