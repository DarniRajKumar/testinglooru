import requests
import pytest
import json
import string
import time
import random
base_url = "https://b2btesterscom.s1.my.looru.ai/api"
# headers = {"cookie": "sessionid=.eJxVjstOwzAQRf_Fa5L67aS7rFqqlgqxoLCxxi8SNUpQbVMkxL-TqFnQ1czV6Nw5P2jw3wmt0WqeK_SA2mzi55h0TJD8dDjk50Z-HY5Pm1MLzfD6_ra9stMVdhsp9i_8cUI05NTqHP1Fd25CKucFCMwLI4IqOFahAOF9AcArhYFYyfE9ZsCe_TCzcyyXGMtFptznS97e9mMzUfQebyG2819CKQuqwpJVwuPaeEWscwDBMeJqTI2A2tUgiMHW8kApYGUkFooRHiyfSuNoO-hv1T3EpPvxoxv--S1G6PcPkK9mYQ:1qWbWj:P1SZGdU_Tubf9t1HBaOEM6XEw4vB-f9263b18lteEJQ"}

# # API Test for List Workflows
# @pytest.mark.sanity
# def test_get_workflows():

#     url = base_url+"/workflows"

#     response = requests.get(url, headers=headers)

#     print("Print URL "+url)

#     response_body = response.json()
#     json_str = json.dumps(response_body, indent=4)
#     print("json POST response body: ", json_str)

#     # check for response status code
#     assert response.status_code == 200

#     # # Define expected values for assertions
#     # expected_http_code = 200
#     # expected_count = 1
#     # expected_name = "New workflow"
#     # expected_cron_expression = "0 9 * * 1"

#     # Key-level assertions
#     assert "http_code" in response_body
#     assert "metadata" in response_body
#     assert "method" in response_body
#     assert "request_id" in response_body
#     assert "data" in response_body

#     # Assertion for http_code
#     assert response_body["http_code"] == 200, "HTTP code should be 200"

#     # Assertion for metadata count
#     # assert response_body["metadata"]["count"] == 1, "Metadata count should be 1"

#     # Assertion for method
#     assert response_body["method"] == "GET", "Method should be GET"

#     # Assertion for workflow_id
#     assert response_body["data"][0]["workflow_id"] is not None

#     # Assertion for name
#     assert response_body["data"][0]["name"] is not None


# # API Test for single Workflow

# def test_get_workflow():

#     url = base_url+"/workflows/1ff8fdae-cd05-4cc6-983f-5e8d35e5ccfa"

#     response = requests.get(url, headers=headers)

#     print("Print URL "+url)

#     response_json = response.json()
#     json_str = json.dumps(response_json, indent=4)
#     print("json POST response body: ", json_str)

#     # check for response status code
#     assert response.status_code == 200

#     # Assertions to validate specific values within the JSON structure
#     assert response_json["http_code"] == 200, "Unexpected http_code"
#     assert response_json["method"] == "GET", "Unexpected method"
#     assert response_json["data"]["workflow_id"] == "1ff8fdae-cd05-4cc6-983f-5e8d35e5ccfa", "Unexpected workflow_id"

# @pytest.fixture(autouse=True)
# def clear_cookies():
#     requests.cookies.clear()

# Generate a random name
# def generate_random_name(length=6):
#     letters = string.ascii_letters
#     return ''.join(random.choice(letters) for _ in range(length))

random_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(4))


# Generate a random name with 8 characters
# random_name = generate_random_name(8)
# API Test for create schedule workflow of HubSpot
def test_create_workflow():

    headers_value = "sessionid=.eJxVjstOwzAQRf_Fa5L67aS7rFqqlgqxoLCxxi8SNUpQbVMkxL-TqFnQ1czV6Nw5P2jw3wmt0WqeK_SA2mzi55h0TJD8dDjk50Z-HY5Pm1MLzfD6_ra9stMVdhsp9i_8cUI05NTqHP1Fd25CKucFCMwLI4IqOFahAOF9AcArhYFYyfE9ZsCe_TCzcyyXGMtFptznS97e9mMzUfQebyG2819CKQuqwpJVwuPaeEWscwDBMeJqTI2A2tUgiMHW8kApYGUkFooRHiyfSuNoO-hv1T3EpPvxoxv--S1G6PcPkK9mYQ:1qWbWj:P1SZGdU_Tubf9t1HBaOEM6XEw4vB-f9263b18lteEJQ;base_url=https://b2btesterscom.s1.my.looru.ai"
    headers = {
    "cookie": headers_value}


    # headers={"cookie":"sessionid=.eJxVjstOwzAQRf_Fa5L67aS7rFqqlgqxoLCxxi8SNUpQbVMkxL-TqFnQ1czV6Nw5P2jw3wmt0WqeK_SA2mzi55h0TJD8dDjk50Z-HY5Pm1MLzfD6_ra9stMVdhsp9i_8cUI05NTqHP1Fd25CKucFCMwLI4IqOFahAOF9AcArhYFYyfE9ZsCe_TCzcyyXGMtFptznS97e9mMzUfQebyG2819CKQuqwpJVwuPaeEWscwDBMeJqTI2A2tUgiMHW8kApYGUkFooRHiyfSuNoO-hv1T3EpPvxoxv--S1G6PcPkK9mYQ:1qWbWj:P1SZGdU_Tubf9t1HBaOEM6XEw4vB-f9263b18lteEJQ",
    #          "cookie2":"base_url=https://b2btesterscom.s1.my.looru.ai"}
    url = base_url+"/workflows"
    post_payload = {
    "name": random_name,
    "description": "",
    "sor": "HUBSPOT",
    "sor_object_name": "deals",
    "actions": [
        {
            "type": "slack-message",
            "data": {
                "version": "v1",
                "type": "conversation",
                "msg_template": " hello",
                "msg_type": "RECORD",
                "report_desc": "",
                
                "conversations": [
                    "C05L4TVPFRD"
                ],
               
                "fields": [
                    "dealname",
                    "luru_deal_status",
                    "amount"
                ],
                "media_category": "reminder",
                "action_buttons": [
                    {
                        "type": "update-record",
                        "fields": [
                            "dealname",
                            "amount",
                            "dealstage"
                        ]
                    }
                ]
            }
        }
    ],
    "evaluation": {
        "type": "SCHEDULE",
        "data": {
            "cron_expression": "0 12 * * 1",
            "tz": "Asia/Calcutta"
        }
    },
    "filter": {
        "version": "v1",
        "data": {
            "and": [
                {
                    "and": [
                        {
                            "object_name": "deals",
                            "field": "amount",
                            "op": "=",
                            "value": 25000,
                            "originalOp": "equals"
                        }
                    ]
                },
                {
                    "or": []
                }
            ]
        }
    }
}
    print("print URL" + url)
    time.sleep(20)

    response = requests.post(url, json=post_payload, headers=headers)
    # Add a wait/delay of 5 seconds
    time.sleep(20)
    # Print the request headers
    # request_headers = response.request.headers
    # print("Request Headers:")
    # for key, value in request_headers.items():
    #    print(f"{key}: {value}")
    # # Print response headers
    # print("Response Headers:")
    # for key, value in response.headers.items():
    #   print(f"{key}: {value}")

    # check for response status code

    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json POST response body: ", json_str)
    workflow_id = json_data["data"]["workflow_id"]
    print("workflow_id ===>", workflow_id)
    assert response.status_code == 201

    return workflow_id


# # API Test for update WorkFlow
# @pytest.mark.sanity
# def test_update_workflow():
#     headers = {"cookie": "sessionid=.eJxVkN1qg0AQhd_F62pmddfV3qWF2EBoKEVaeiOzfyqxKu4KaUvfvS6RklzNHJhvzpn5CXp9dsF9sPF1E9wFFjttzTBJHQ44uyaurEOnlxE49TAd62EPU9I5Kouiq0sF-4_UuvHNjgvczMKOg_tHCnnICOy-d_LrOc3BCcLK7Qt7OH--i1coHxek8ibVbPVUtWpBMqUZMqChYIaHFLgJkWkdItKMAxKZUrjFBMqT7j3rZbRKG61hosM8zU-X_rj1F93iDdrG-5I4TgzPIE0ypiEXmhOpFKJRCVE5xIJhrnJkRICU1MQxAhcpMJ4QaiT1rxtki91ldYfWVd1Qt_1VvjVR8PsHaod6_A:1qTETy:q0RzXZqNJoa7xnvNRfkUywLCnPcZdj2pOye25LnV0ag", 
#                "cookie2": "base_url=https://b2btesterscom.s1.my.looru.ai"}
#     url = base_url + f"/notes/{test_create_workflow()}"
#     put_payload = {
#         "name": "hub3",
#         "description": "",
#         "sor": "HUBSPOT",
#         "sor_object_name": "deals",
#         "actions": [
#             {
#                 "type": "slack-message",
#                 "data": {
#                     "version": "v1",
#                     "type": "conversation",
#                     "msg_template": " hello",
#                     "msg_type": "RECORD",
#                     "report_desc": "",
#                     "report_config": {
#                         "grouped": false,
#                         "grouped_field": null
#                     },
#                     "conversations": [
#                         "C05L4TVPFRD"
#                     ],
#                     "users": null,
#                     "fields": [
#                         "dealname",
#                         "luru_deal_status",
#                         "amount"
#                     ],
#                     "media_category": "reminder",
#                     "action_buttons": [
#                         {
#                             "type": "update-record",
#                             "fields": [
#                                 "dealname",
#                                 "amount",
#                                 "dealstage"
#                             ]
#                         }
#                     ]
#                 }
#             }
#         ],
#         "evaluation": {
#             "type": "SCHEDULE",
#             "data": {
#                 "cron_expression": "0 12 * * 1",
#                 "tz": "Asia/Calcutta"
#             }
#         },
#         "filter": {
#             "version": "v1",
#             "data": {
#                 "and": [
#                     {
#                         "and": [
#                             {
#                                 "object_name": "deals",
#                                 "field": "amount",
#                                 "op": "=",
#                                 "value": 25000,
#                                 "originalOp": "equals"
#                             }
#                         ]
#                     },
#                     {
#                         "or": []
#                     }
#                 ]
#             }
#         }
#     }
#     response = requests.put(url, json=put_payload, headers=headers)

#     print("print URL" + url)

#     # check for response status code
#     assert response.status_code == 202

#     data = response.json()
#     json_str = json.dumps(data, indent=4)
#     workflow_id = data["data"]["workflow_id"]
#     print("workflow_id ===>", workflow_id)
#     return workflow_id

# # API Test for pause WorkFlow
# @pytest.mark.sanity
# def test_unpause_workflow():
#     url = base_url + f"/notes/{test_update_workflow()}/unpause"
#     put_payload = {{
#         "name": "hub2",
#         "description": "",
#         "sor": "HUBSPOT",
#         "sor_object_name": "deals",
#         "actions": [
#             {
#                 "type": "slack-message",
#                 "data": {
#                     "version": "v1",
#                     "type": "conversation",
#                     "msg_template": " hello",
#                     "msg_type": "RECORD",
#                     "report_desc": "",
#                     "report_config": {
#                         "grouped": false,
#                         "grouped_field": null
#                     },
#                     "conversations": [
#                         "C05L4TVPFRD"
#                     ],
#                     "users": null,
#                     "fields": [
#                         "dealname",
#                         "luru_deal_status",
#                         "amount"
#                     ],
#                     "media_category": "reminder",
#                     "action_buttons": [
#                         {
#                             "type": "update-record",
#                             "fields": [
#                                 "dealname",
#                                 "amount",
#                                 "dealstage"
#                             ]
#                         }
#                     ]
#                 }
#             }
#         ],
#         "evaluation": {
#             "type": "SCHEDULE",
#             "data": {
#                 "cron_expression": "0 12 * * 1",
#                 "tz": "Asia/Calcutta"
#             }
#         },
#         "filter": {
#             "version": "v1",
#             "data": {
#                 "and": [
#                     {
#                         "and": [
#                             {
#                                 "object_name": "deals",
#                                 "field": "amount",
#                                 "op": "=",
#                                 "value": 25000,
#                                 "originalOp": "equals"
#                             }
#                         ]
#                     },
#                     {
#                         "or": []
#                     }
#                 ]
#             }
#         }
#     }
#     }    
#     response = requests.put(url, json=put_payload, headers=headers)

#     print("print URL" + url)

#     # check for response status code
#     assert response.status_code == 200

#     response_body = response.json()
#     json_str = json.dumps(response_body, indent=4)

#    # Asserting the presence of keys and their values
#     assert response_body["http_code"] == 200
#     assert response_body["method"] == "POST"
#     assert response_body["data"]["workflow_id"] == "1ff8fdae-cd05-4cc6-983f-5e8d35e5ccfa"
#     assert response_body["data"]["name"] is not None
#     assert response_body["data"]["description"] == ""
#     assert response_body["data"]["sor"] == "HUBSPOT"
#     assert response_body["data"]["sor_object_name"] == "deals"
#     assert response_body["data"]["state"] == "INACTIVE"
#     assert response_body["data"]["created_by"] == "8de5a504-b5f7-407f-a5ee-aa4870a1c640"
#     assert response_body["data"]["updated_by"] == "8de5a504-b5f7-407f-a5ee-aa4870a1c640"
#     assert response_body["data"]["evaluation"]["type"] == "SCHEDULE"
#     # assert response_body["data"]["evaluation"]["data"]["cron_expression"] == "0 9 * * 1"
#     # ... (similar assertions for other keys and values)

#     # Assertion for the number of actions
#     # assert len(response_body["data"]["actions"]) == 1

#     # You can use try-except blocks to handle missing keys or potential errors
#     try:
#         assert response_body["data"]["actions"][0]["type"] == "slack-message"
#     except KeyError:
#         print("Key 'type' not found in the 'actions' data")


# # API Test for pause WorkFlow
# @pytest.mark.sanity
# def test_pause_workflow():
#     url = base_url + f"/notes/{test_update_workflow()}/pause"
#     put_payload = {{
#         "name": "hub2",
#         "description": "",
#         "sor": "HUBSPOT",
#         "sor_object_name": "deals",
#         "actions": [
#             {
#                 "type": "slack-message",
#                 "data": {
#                     "version": "v1",
#                     "type": "conversation",
#                     "msg_template": " hello",
#                     "msg_type": "RECORD",
#                     "report_desc": "",
#                     "report_config": {
#                         "grouped": false,
#                         "grouped_field": null
#                     },
#                     "conversations": [
#                         "C05L4TVPFRD"
#                     ],
#                     "users": null,
#                     "fields": [
#                         "dealname",
#                         "luru_deal_status",
#                         "amount"
#                     ],
#                     "media_category": "reminder",
#                     "action_buttons": [
#                         {
#                             "type": "update-record",
#                             "fields": [
#                                 "dealname",
#                                 "amount",
#                                 "dealstage"
#                             ]
#                         }
#                     ]
#                 }
#             }
#         ],
#         "evaluation": {
#             "type": "SCHEDULE",
#             "data": {
#                 "cron_expression": "0 12 * * 1",
#                 "tz": "Asia/Calcutta"
#             }
#         },
#         "filter": {
#             "version": "v1",
#             "data": {
#                 "and": [
#                     {
#                         "and": [
#                             {
#                                 "object_name": "deals",
#                                 "field": "amount",
#                                 "op": "=",
#                                 "value": 25000,
#                                 "originalOp": "equals"
#                             }
#                         ]
#                     },
#                     {
#                         "or": []
#                     }
#                 ]
#             }
#         }
#     }
#     }
#     response = requests.put(url, json=put_payload, headers=headers)

#     print("print URL" + url)

#     # check for response status code
#     assert response.status_code == 200

#     response_body = response.json()
#     json_str = json.dumps(response_body, indent=4)

#    # Asserting the presence of keys and their values
#     assert response_body["http_code"] == 200
#     assert response_body["method"] == "POST"
#     assert response_body["data"]["workflow_id"] == "1ff8fdae-cd05-4cc6-983f-5e8d35e5ccfa"
#     # ... (similar assertions for other keys and values)

#     # You can also perform assertions on nested structures
#     assert response_body["data"]["evaluation"]["type"] == "SCHEDULE"
#     assert response_body["data"]["filter"]["data"]["and"][0]["and"][0]["op"] == "="
#     # ... (similar assertions for other nested keys and values)

#     # Assertion for the number of actions
#     assert len(response_body["data"]["actions"]) == 1

#     # You can use try-except blocks to handle missing keys or potential errors
#     try:
#         assert response_body["data"]["actions"][0]["type"] == "slack-message"

#     except KeyError:

#         print("Key 'type' not found in the 'actions' data")


        

    
# # API Test for delete Note
# @pytest.mark.sanity
# def test_delete_workflow():

#     url = base_url + f"/workflows/{test_update_workflow()}"
#     response = requests.delete(url, headers=headers)

#     print("print URL" + url)

#     # print response body
#     data = response.json()
#     json_str = json.dumps(data, indent=4)

#     print("json delete response body: ", json_str)

#     assert response.status_code == 200

test_create_workflow()