"""

Write a Python program to make a request to a web page, and test the status code, and display the HTML code of
the specified web page.

Sample Output:
Web page status: <Response [200]>
HTML code of the above web page:
<!doctype html>
<html>
<head>
<title>Example Domain</title>
<meta charset="utf-8" />
<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
</head>
<body>
<div>
<h1>Example Domain</h1>
<p>This domain is for use in illustrative examples in documents. You may use this
domain in literature without prior coordination or asking for permission.</p>
<p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>

"""

# Import the 'requests' module for making HTTP requests.
import requests


def main():
    # Define the URL of the web page to be accessed.
    url = 'https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-117.php'

    # Use the 'get' method from the 'requests' module to make an HTTP request to the specified URL with headers.
    request = requests.get(url)

    # Print the status of the web page request.
    print("Web page status: ", request)

    # Print HTML code of the web page if the request was successful (status code 200).
    print("\nHTML code of the above web page:")
    if request.ok:
        print(request.text)


if __name__ == "__main__":
    main()
