import requests


#API Test for error handling of creating new Looru Note
base_url = "https://b2btesterscom.s1.my.looru.ai/api"
url = f"{base_url}/notes?type=luru"
api_params = {"type": "luru"}

headers = {"cookie": "sessionid=.eJxVjstOwzAQRf_Fa5L67aS7rFqqlgqxoLCxxi8SNUpQbVMkxL-TqFnQ1czV6Nw5P2jw3wmt0WqeK_SA2mzi55h0TJD8dDjk50Z-HY5Pm1MLzfD6_ra9stMVdhsp9i_8cUI05NTqHP1Fd25CKucFCMwLI4IqOFahAOF9AcArhYFYyfE9ZsCe_TCzcyyXGMtFptznS97e9mMzUfQebyG2819CKQuqwpJVwuPaeEWscwDBMeJqTI2A2tUgiMHW8kApYGUkFooRHiyfSuNoO-hv1T3EpPvxoxv--S1G6PcPkK9mYQ:1qWbWj:P1SZGdU_Tubf9t1HBaOEM6XEw4vB-f9263b18lteEJQ"}

post_payload = {"body": "[{'type': 'paragraph', 'data': 'This note was created using LURU, the fastest way to take notes. To get more from this note, goto https://app.luru.com:3000/home/170f3615-820c-4066-b868-34d95e8567cc'}, {'type': 'paragraph', 'data': ''}, {'type': 'paragraph', 'data': '/'}, {'type': 'paragraph', 'data': ''}, {'type': 'paragraph', 'data': 'Whatsup!'}]"}

def send_post_request(url, headers, payload):
    # try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise HTTPError if response status is not 2xx
        return response

def test_post_main():
    try:
        response = send_post_request(url, headers, post_payload)
        print("Response:", response.status_code, response.json())
    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", str(e))
    except requests.exceptions.RequestException as e:
        print("Request error:", str(e))





#API Test for error handling of updating new Looru Note


base_url = "https://b2btesterscom.s1.my.looru.ai/api"
note_id = "195fea3c-7a25-4e3d-be6f-4d511926697b"
url = f"{base_url}/notes/{note_id}"

headers = {"cookie": "sessionid=.eJxVjstOwzAQRf_Fa5L67aS7rFqqlgqxoLCxxi8SNUpQbVMkxL-TqFnQ1czV6Nw5P2jw3wmt0WqeK_SA2mzi55h0TJD8dDjk50Z-HY5Pm1MLzfD6_ra9stMVdhsp9i_8cUI05NTqHP1Fd25CKucFCMwLI4IqOFahAOF9AcArhYFYyfE9ZsCe_TCzcyyXGMtFptznS97e9mMzUfQebyG2819CKQuqwpJVwuPaeEWscwDBMeJqTI2A2tUgiMHW8kApYGUkFooRHiyfSuNoO-hv1T3EpPvxoxv--S1G6PcPkK9mYQ:1qWbWj:P1SZGdU_Tubf9t1HBaOEM6XEw4vB-f9263b18lteEJQ"}

put_payload = {"body": "[{'type': 'paragraph', 'data': 'This note was created using LURU, the fastest way to take notes. To get more from this note, goto https://app.luru.com:3000/home/170f3615-820c-4066-b868-34d95e8567cc'}, {'type': 'paragraph', 'data': ''}, {'type': 'paragraph', 'data': '/'}, {'type': 'paragraph', 'data': ''}, {'type': 'paragraph', 'data': 'Whatsup!'}]"}

def send_put_request(url, headers, payload):
    # try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise HTTPError if response status is not 2xx
        return response

def test_put_main():
    try:
        response = send_put_request(url, headers, put_payload)
        print("Response:", response.status_code, response.json())
    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", str(e))
    except requests.exceptions.RequestException as e:
        print("Request error:", str(e))






























#API Test for error handling of getting specific  Note

# Define the URL and note_id

base_url = "https://b2btesterscom.s1.my.looru.ai/api/notes"
note_id = "195fea3c-7a25-4e3d-be6f-4d511926697b"
url = f"{base_url}/notes/{note_id}"

api_params = {"type": "luru"}

# Send the GET request
response = requests.get(url,headers=headers)
def test_get_notes_errorvalidation():
# Check the response status code
 if response.status_code == 200:
    print("Request was successful!")
    print("Response:", response.json())
 elif response.status_code == 404:
    print(f"Note with ID '{note_id}' was not found.")
    print("Response:", response.text)
 else:
    print(f"An error occurred. Status Code: {response.status_code}")
    print("Response:", response.text)





notes_id = "195fea3c-7a25-4e3d-be6f-4d511926697b"
url = f"{base_url}/notes/{notes_id}?propagate=true"
api_params = {"propagate": "true"}
headers = {"cookie": "sessionid=.eJxVjstOwzAQRf_Fa5L67aS7rFqqlgqxoLCxxi8SNUpQbVMkxL-TqFnQ1czV6Nw5P2jw3wmt0WqeK_SA2mzi55h0TJD8dDjk50Z-HY5Pm1MLzfD6_ra9stMVdhsp9i_8cUI05NTqHP1Fd25CKucFCMwLI4IqOFahAOF9AcArhYFYyfE9ZsCe_TCzcyyXGMtFptznS97e9mMzUfQebyG2819CKQuqwpJVwuPaeEWscwDBMeJqTI2A2tUgiMHW8kApYGUkFooRHiyfSuNoO-hv1T3EpPvxoxv--S1G6PcPkK9mYQ:1qWbWj:P1SZGdU_Tubf9t1HBaOEM6XEw4vB-f9263b18lteEJQ"}

response = requests.delete(url, params=api_params, headers=headers)
def test_delete_notes_errorvalidation():

  if response.status_code == 200:
    print("Note deleted successfully.")
  elif response.status_code == 404:
    print("Note not found.")
  elif response.status_code == 401:
    print("Unauthorized. Please check your authentication.")
  else:
    print(f"An error occurred with status code: {response.status_code}")
    print("Response content:", response.text)



































if __name__ == "__main__":
    test_get_notes_errorvalidation()
