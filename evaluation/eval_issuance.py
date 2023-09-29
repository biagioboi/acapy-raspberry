import http.client
import json
import time

for x in range(0, 20):
    start = time.time()

    connection_id = "8a34ccb2-c370-47cb-9140-38227b7a7457"
    conn = http.client.HTTPConnection("localhost", 11000)
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
            "issuer": "did:key:z6MkidPpQgcidH1d8bLszYGpHtAWAp2BSJuULcDKBHnex6Zo",
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
