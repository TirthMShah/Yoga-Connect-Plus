# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC6c4aa1e1ef0b1744bd5de3a464b636b2"
auth_token = "dc7e21278890bee786e7fa34a4cd96af"
verify_sid = "VA4eb1fb6a34fd62066dc14f081344c049"
verified_number = "+919429302825"

client = Client(account_sid, auth_token)

verification = client.verify.v2.services(verify_sid) \
  .verifications \
  .create(to=verified_number, channel="sms")
print(verification.status)

otp_code = input("Please enter the OTP:")

verification_check = client.verify.v2.services(verify_sid) \
  .verification_checks \
  .create(to=verified_number, code=otp_code)
print(verification_check.status)