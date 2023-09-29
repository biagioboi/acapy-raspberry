import http.client
import json

conn = http.client.HTTPConnection("localhost", 11001)
payload = json.dumps({
  "comment": "test proof request for json-ld",
  "connection_id": "337559e1-87e9-4cfd-a4b9-799cd0e6e6b1",
  "presentation_request": {
    "dif": {
      "options": {
        "challenge": "3fa85f64-5717-4562-b3fc-2c963f66afa7",
        "domain": "4jt78h47fh47"
      },
      "presentation_definition": {
        "id": "32f54163-7166-48f1-93d8-ff217bdb0654",
        "format": {
          "ldp_vp": {
            "proof_type": [
              "Ed25519Signature2018"
            ]
          }
        },
        "input_descriptors": [
          {
            "id": "citizenship_input_1",
            "name": "EU Driver's License",
            "schema": [
              {
                "uri": "https://www.w3.org/2018/credentials#VerifiableCredential"
              }
            ],
            "constraints": {
              "is_holder": [{
                    "directive": "required",
                    "field_id": [
                        "1f44d55f-f161-4938-a659-f8026467f126",
                        "332be361-823a-4863-b18b-c3b930c5623e"
                    ],
              }],
              "fields": [
                {
                  "id": "1f44d55f-f161-4938-a659-f8026467f126",
                  "path": [
                    "$.credentialSubject.familyName"
                  ],
                  "purpose": "The claim must be from one of the specified person"
                },
                {
                  "id": "332be361-823a-4863-b18b-c3b930c5623e",
                  "path": [
                    "$.credentialSubject.givenName"
                  ],
                  "purpose": "The claim must be from one of the specified person"
                }
              ]
            }
          }
        ]
      }
    }
  }
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/present-proof-2.0/send-request", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))