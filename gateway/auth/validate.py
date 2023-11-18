import os, requests

def token(request):

    print("in validate.token")
    if not "Authorization" in request.headers:
        return None, ("missing credentials", 401)

    print("Authzn")
    
    token = request.headers["Authorization"]

    print("token: ", token)

    if not token:
        return None, ("missing credentials", 401)
    
    response = requests.post(
        f"http://{os.environ.get('AUTH_SVC_ADDRESS')}/validate",
        headers={"Authorization": token},
    )

    print("response code: ", response.status_code)

    if response.status_code == 200:
        return response.text, None
    else:
        return None, (response.text, response.status_code)