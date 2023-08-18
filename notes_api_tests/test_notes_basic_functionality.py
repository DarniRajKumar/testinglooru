import requests
import pytest
import json
import string
import time

note_id = 0
base_url = "https://b2btesterscom.s1.my.looru.ai/api"
headers = {"cookie":"sessionid=.eJxVjstOwzAQRf_Fa5L67aS7rFqqlgqxoLCxxi8SNUpQbVMkxL-TqFnQ1czV6Nw5P2jw3wmt0WqeK_SA2mzi55h0TJD8dDjk50Z-HY5Pm1MLzfD6_ra9stMVdhsp9i_8cUI05NTqHP1Fd25CKucFCMwLI4IqOFahAOF9AcArhYFYyfE9ZsCe_TCzcyyXGMtFptznS97e9mMzUfQebyG2819CKQuqwpJVwuPaeEWscwDBMeJqTI2A2tUgiMHW8kApYGUkFooRHiyfSuNoO-hv1T3EpPvxoxv--S1G6PcPkK9mYQ:1qWbWj:P1SZGdU_Tubf9t1HBaOEM6XEw4vB-f9263b18lteEJQ"}


#API Test for getting all notes
@pytest.mark.sanity
def test_get_notes():
    global note_id

    url = base_url+"/notes?type=luru"
    api_params = {"type":"luru"}
  
    response = requests.get(url,params=api_params,headers=headers)
    
    print("Print URL "+url)

    # check for response status code
    assert response.status_code == 200
    
    # check if no errors from the response data
    if(response.json()['error_data'] == None):
        assert response.json() is not None
    
        # Check for notes in the reponse
        if (len(response.json()['data']) > 0):
            #get the note_id for checking the correct values in the response
            note_id = response.json()['data'][0]['note_id']           
            assert response.json()['data'][0]['note_id'] is not None


# API Test for single note
@pytest.mark.sanity
def test_get_note():
    global note_id

    notes_id = "195fea3c-7a25-4e3d-be6f-4d511926697b"
    url = base_url+"/notes/"+notes_id
    api_params = {"type":"luru"}
  
    response = requests.get(url,params=api_params,headers=headers)
    
    print("Print URL "+url)

    # check for response status code
    assert response.status_code == 200
    
    # check if no errors from the response data
    if(response.json()['error_data'] == None):
        assert response.json() is not None
    
        # Check for notes in the reponse
        if (response.json()['data'] is not None):
            #get the note_id for checking the correct values in the response
            api_note_id = response.json()['data']['note_id']
            assert api_note_id == notes_id     
            #assert response.json()['data'][0]['note_id'] is not None


#API Test for creating new Looru Note
@pytest.mark.sanity
def test_create_note():

    url = base_url+"/notes"
    post_payload = {"title": "testing raj","body": "[{'type': 'paragraph', 'data': 'This note was created using LURU, the fasted way to take notes. To get more from this note, goto https://app.luru.com:3000/home/170f3615-820c-4066-b868-34d95e8567cc'}, {'type': 'paragraph', 'data': ''}, {'type': 'paragraph', 'data': '/'}, {'type': 'paragraph', 'data': ''}, {'type': 'paragraph', 'data': 'Whatsup!'}]"}
    response=requests.post(url,json=post_payload,headers=headers)
    
    print("print URL" + url)

    # check for response status code

    assert response.status_code==201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json POST response body: ", json_str)
    note_id = json_data["data"]["note_id"]
    print("note_id ===>", note_id)

    
    # Assertions for each key and value
    assert json_data["http_code"] == 201
    assert json_data["metadata"] == None
    assert json_data["method"] == "POST"
    assert json_data["request_id"] is not None
    assert json_data["data"]["note_id"] is not None
    assert json_data["data"]["sync_state"] == "private"
    assert json_data["data"]["title"] == "testing raj"
    assert json_data["data"]["template_id"] == None
    assert json_data["data"]["created_by"]["id"] == "8de5a504-b5f7-407f-a5ee-aa4870a1c640"
    assert json_data["data"]["created_by"]["sor_id"] == None
    assert json_data["data"]["created_by"]["email"] == "rajkumardarni@b2btesters.com"
    assert json_data["data"]["created_by"]["name"] == "Rajkumar Darni"
    assert json_data["data"]["updated_by"]["id"] == "8de5a504-b5f7-407f-a5ee-aa4870a1c640"
    assert json_data["data"]["updated_by"]["sor_id"] == None
    assert json_data["data"]["updated_by"]["email"] == "rajkumardarni@b2btesters.com"
    assert json_data["data"]["updated_by"]["name"] == "Rajkumar Darni"
    assert json_data["data"]["connections"] == []
    assert json_data["error_data"] == None    
    return note_id


#API Test for update Note
@pytest.mark.sanity
def test_update_Note():
    url = base_url + f"/notes/{test_create_note()}"
    put_payload = {"body": [{"type":"paragraph","data":"HAi"}],"title": "Rajkumar",}
    response = requests.put(url, json=put_payload, headers=headers)

    print("print URL" + url)
    
    # check for response status code
    assert response.status_code == 202
    
    data = response.json()
    json_str = json.dumps(data, indent=4)
    print("json PUT response body: ", json_str)
    note_id = data["data"]["note_id"]
    print("note_id ===>", note_id)

    # Assertions for each key and value
    assert data["http_code"] == 202
    assert data["metadata"] == None
    assert data["method"] == "PUT"
    assert data["request_id"] is not None 
    assert data["data"]["sync_state"] == "private"
    assert data["data"]["title"] == "Rajkumar"
    assert data["data"]["template_id"] == None
    assert data["data"]["created_by"]["id"] == "8de5a504-b5f7-407f-a5ee-aa4870a1c640"
    assert data["data"]["created_by"]["sor_id"] == None
    assert data["data"]["created_by"]["email"] == "rajkumardarni@b2btesters.com"
    assert data["data"]["created_by"]["name"] == "Rajkumar Darni"
    assert data["data"]["updated_by"]["id"] == "8de5a504-b5f7-407f-a5ee-aa4870a1c640"
    assert data["data"]["updated_by"]["sor_id"] == None
    assert data["data"]["updated_by"]["email"] == "rajkumardarni@b2btesters.com"
    assert data["data"]["updated_by"]["name"] == "Rajkumar Darni"
    assert data["data"]["connections"] == []
    assert data["error_data"] == None
    return note_id



#API Test for Add Note Connection
def test_add_note_connection():

    url = base_url + f"/notes/{test_update_Note()}/connections"
    headers = {"cookie":"sessionid=.eJxVkN1qg0AQhd_F62pmddfV3qWF2EBoKEVaeiOzfyqxKu4KaUvfvS6RklzNHJhvzpn5CXp9dsF9sPF1E9wFFjttzTBJHQ44uyaurEOnlxE49TAd62EPU9I5Kouiq0sF-4_UuvHNjgvczMKOg_tHCnnICOy-d_LrOc3BCcLK7Qt7OH--i1coHxek8ibVbPVUtWpBMqUZMqChYIaHFLgJkWkdItKMAxKZUrjFBMqT7j3rZbRKG61hosM8zU-X_rj1F93iDdrG-5I4TgzPIE0ypiEXmhOpFKJRCVE5xIJhrnJkRICU1MQxAhcpMJ4QaiT1rxtki91ldYfWVd1Qt_1VvjVR8PsHaod6_A:1qTETy:q0RzXZqNJoa7xnvNRfkUywLCnPcZdj2pOye25LnV0ag"}
    data = {
    "sor": "HUBSPOT",
    "sor_record_id": "8231466211",
    "sor_object_name": "companies",
    "sor_record_name": "b2b"
            }
    response = requests.post(url, json=data,headers=headers)
    print("print URL:" + url)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json POST response body: ", json_str)
    
    # Assertions for keys
    assert "http_code" in json_data
    assert "metadata" in json_data
    assert "method" in json_data
    assert "request_id" in json_data
    assert "data" in json_data
    assert "error_data" in json_data

    # Assertions for values
    assert json_data["http_code"] == 200
    assert json_data["metadata"] is None
    assert json_data["method"] == "POST"
    assert json_data["request_id"] is not None

    # assertions for values within the "data" dictionary and its nested dictionaries/lists
    data = json_data["data"]
    assert "note_id" in data
    assert "sync_state" in data

    # Assertions for the nested "created_by" and "updated_by" dictionaries
    created_by = data["created_by"]
    assert "id" in created_by
    assert "sor_id" in created_by
    assert "email" in created_by
    assert "name" in created_by

    updated_by = data["updated_by"]
    assert "id" in updated_by
    assert "sor_id" in updated_by
    assert "email" in updated_by
    assert "name" in updated_by

   # Assertions for the nested "connections" list
    connections = data["connections"]
    assert isinstance(connections, list)
    assert len(connections) > 0  

    # Assertions for the "error_data" key
    assert json_data["error_data"] is None



#API Test for delete Note
@pytest.mark.sanity
def test_delete_note():

    url = base_url+ f"/notes/{test_update_Note()}?propagate=true"
    api_params = {"propagate":"true"}
    response = requests.delete(url,params=api_params,headers=headers)

    print("print URL" + url)

    # print response body
    data = response.json()
    json_str = json.dumps(data, indent=4)

    print("json delete response body: ", json_str)

    assert response.status_code == 200

    # Assertion for each key and value 
    assert data["http_code"] == 200
    assert data["metadata"] is None
    assert data["method"] == "DELETE"
    assert data["request_id"] is not None
    assert data["error_data"] is None








if __name__ == "__main__":
    pytest.main(["-v", "test_notes_basic_functionality.py"])