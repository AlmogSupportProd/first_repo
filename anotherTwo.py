    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    contents = {"clientId": "0c3f8188-f7e1-4d2b-9988-2ee8ded1edde", "secret": "16b4ab82-e417-4716-b305-7839f4d58d1g"}
    contents = json.dumps(contents)
    r = requests.post("https://api.cycode.com/api/v1/auth/api-token", data=contents, headers=headers, timeout=3*60)
