# validate_postcode

Validating UK post codes as per: https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting

## Usage

Installation: Nothing to install.

Execute the following:

```bash
~ python .\validate_postcode\server.py
```

and hit the following endpoint: http://localhost:8080/api/?post_code=EC1%201BB

The response should be a HTTP 200 success message and the following message in JSON:

```json
{"status": "success", "message": "Valid post code."}
```

## Tests

Execute the following:

```bash
~ python -m unittest discover
```

## Known Issues

There is a bug in the implementation for some London districts, one of the example can be seen on the linked Wiki page above: `EC1A 1BB` (The tests are catching the issue)