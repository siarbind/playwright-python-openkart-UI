import json

from playwright.sync_api import Playwright

def test_create_booking_external(playwright:Playwright):
    file=open("testdata/post_request_body.json","r")
    request_body=json.load(file)
    request_context=playwright.request.new_context()
    base_url = "https://restful-booker.herokuapp.com"
    response=request_context.post(f"{base_url}/booking",data=request_body)
    assert response.ok
    assert response.status_code == 200
    response_body=response.json()
    print(response_body)
