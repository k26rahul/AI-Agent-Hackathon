#!/bin/bash

curl \
  -H 'Content-Type: application/json' \
  -d '{"contents":[{"parts":[{"text":"Explain how AI works"}]}]}' \
  -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyBoKwrxA9ggGEhHPNa_enkJONk99Qewzco'

# Wait for user input before exiting
echo "Press any key to exit..."
read -n 1 -s
