import pytest
import requests
import uuid

base_url = "https://b2btesterscom.s1.my.looru.ai/api"

# url = f"{base_url}/notes"
headers = {"cookie": "sessionid=.eJxVjstOwzAQRf_Fa5L67aS7rFqqlgqxoLCxxi8SNUpQbVMkxL-TqFnQ1czV6Nw5P2jw3wmt0WqeK_SA2mzi55h0TJD8dDjk50Z-HY5Pm1MLzfD6_ra9stMVdhsp9i_8cUI05NTqHP1Fd25CKucFCMwLI4IqOFahAOF9AcArhYFYyfE9ZsCe_TCzcyyXGMtFptznS97e9mMzUfQebyG2819CKQuqwpJVwuPaeEWscwDBMeJqTI2A2tUgiMHW8kApYGUkFooRHiyfSuNoO-hv1T3EpPvxoxv--S1G6PcPkK9mYQ:1qWbWj:P1SZGdU_Tubf9t1HBaOEM6XEw4vB-f9263b18lteEJQ"}

# post_payload = {"body": "[{'type': 'paragraph', 'data': 'This note was created using LURU, the fastest way to take notes. To get more from this note, goto https://app.luru.com:3000/home/170f3615-820c-4066-b868-34d95e8567cc'}, {'type': 'paragraph', 'data': ''}, {'type': 'paragraph', 'data': '/'}, {'type': 'paragraph', 'data': ''}, {'type': 'paragraph', 'data': 'Whatsup!'}]"}


# def validate_payload(payload):
#     required_keys = ["title", "body"]
#     missing_keys = [key for key in required_keys if key not in payload]
#     if missing_keys:
#         raise ValueError(
#             f"Payload is missing required keys: {', '.join(missing_keys)}")


# def send_post_request(url, headers, payload):
#     response = requests.post(url, headers=headers, json=payload)
#     return response


# def test_main():
#     try:
#         validate_payload(post_payload)
#         response = send_post_request(url, headers, post_payload)
#         print("Response:", response.status_code, response.json())
#     except ValueError as e:
#         print("Input validation error:", str(e))
#     except requests.exceptions.RequestException as e:
#         print("Request error:", str(e))





#API Testing 
# def test_validate_uuid(uuid_string):
#     try:
#         # Try converting the UUID string to UUID object
#         uuid.UUID(uuid_string)
#         return True
#     except ValueError:
#         return False

# # Define the notes_id
# notes_id = "195fea3c-7a25-4e3d-be6f-4d511926697b"

# # Validate the notes_id
# if not test_validate_uuid(notes_id):
          
#     print("Invalid notes_id format")
# else:
#     url = base_url+"/notes/"+notes_id

#     response = requests.get(url,headers=headers)

#           # Perform assertions on the response
#     assert response.status_code == 200
#            # Additional assertions as needed



#  API test for get Notes 

# Input validation function
def test_validate_uuid(uuid_str):
    try:
        # Check if the given string is a valid UUID
        uuid_obj = uuid.UUID(uuid_str)
        return str(uuid_obj)
    except ValueError:
        return None

# Base URL and headers
notes_id = "195fea3c-7a25-4e3d-be6f-4d511926697b"
url = base_url+"/notes/"+notes_id
validated_notes_id = test_validate_uuid(notes_id)

if validated_notes_id is None:
    print("Invalid notes ID format.")
else:
    url = f"{base_url}/notes/{validated_notes_id}"
    api_params = {"type": "luru"}

    response = requests.get(url, params=api_params, headers=headers)

    if response.status_code == 200:
        print("Request successful.")
    else:
        print(f"Request failed with status code: {response.status_code}")


# test_validate_uuid(notes_id)

# # if __name__ == "__main__":
# #     test_main()

if __name__ == "__main__":
    pytest.main(["-v", "test_notes_input_validation.py"])