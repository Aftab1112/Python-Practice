import requests


def fetch_random_quote():
    url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"
    respone = requests.get(url)
    data = respone.json()

    if data["success"] and "data" in data:
        quote_data = data["data"]
        author = quote_data["author"]
        quote = quote_data["content"]
        tag = quote_data["tags"][0]
        return (
            author,
            quote,
            tag,
        )
    else:
        raise Exception("Failed to fetch quote")


def main():
    (
        author,
        quote,
        tag,
    ) = fetch_random_quote()
    print(f"Quote : {quote}\nAuthor : {author}\nTag : {tag}")


if __name__ == "__main__":
    main()
