#!/bin/bash

curl "http://localhost:8000/chats/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "chat": {
      "content": "'"${CONTENT}"'"
    }
  }'

echo
