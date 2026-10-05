from yandex_music import Client


def on_code(code):
    print(f'Open {code.verification_url} and enter code: {code.user_code}')


client = Client()
token = client.device_auth(on_code=on_code)

print(f'access_token:  {token.access_token}')
print(f'refresh_token: {token.refresh_token}')
print(f'expires_in:    {token.expires_in}')