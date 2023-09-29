import http.client
import json
import time

for x in range(0, 2):
    start = time.time()

    connection_id = "337559e1-87e9-4cfd-a4b9-799cd0e6e6b1"
    conn = http.client.HTTPConnection("localhost", 11001)
    payload = json.dumps({
      "auto_remove": True,
      "auto_issue": True,
      "comment": "string",
      "connection_id": connection_id,
      "credential_preview": {
        "@type": "issue-credential/2.0/credential-preview",
        "attributes": [
          {
            "mime-type": "image/jpeg",
            "name": "favourite_drink",
            "value": "martini"
          }
        ]
      },
      "filter": {
        "ld_proof": {
          "credential": {
            "@context": [
              "https://www.w3.org/2018/credentials/v1",
              "https://w3id.org/citizenship/v1"
            ],
            "credentialSubject": {
              "familyName": "SMITH",
              "gender": "Male",
              "givenName": "JOHN",
              "type": [
                "PermanentResident",
                "Person"
              ]
            },
            "description": "Government of Example Permanent Resident Card.",
            "identifier": "83627465",
            "issuanceDate": "2019-12-03T12:19:52Z",
            "issuer": "did:key:z6MkfWbcmcawPXh91q9vn5LFrrr3wca96yWL5iWsx3UG7pBD",
            "name": "Permanent Resident Card",
            "type": [
              "VerifiableCredential",
              "PermanentResidentCard"
            ]
          },
          "options": {
            "proofType": "Ed25519Signature2018"
          }
        }
      }
    })
    headers = {
      'Content-Type': 'application/json'
    }
    conn.request("POST", "/issue-credential-2.0/send", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

    end = time.time()
    print(end - start)
    time.sleep(1)
