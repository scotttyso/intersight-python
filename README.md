# Intersight API with Python SDK or Requests

- It is recommend to add the following secure variables to your environment before running the script

## Intersight Variables

- Linux

```bash
export INTERSIGHT_API_KEY_ID="<your_intersight_api_key>"
export INTERSIGHT_API_PRIVATE_KEY="/home/<username>/Downloads/SecretKey.txt"
```

- Windows

```shell
$env:INTERSIGHT_API_KEY_ID="<your_intersight_api_key>"
$env:INTERSIGHT_API_PRIVATE_KEY="C:\Users\<username>\Downloads\SecretKey.txt"
```

Run the Script

- Linux

```bash
./ip_pool_with_sdk.py
./ip_pool_with_requests.py
```

- Windows

```shell
python3 .\ip_pool_with_sdk.py
python3 .\ip_pool_with_requests.py
```

The purpose of this is to show an example of using the Intersight API via either the intersight Python SDK or using requests.