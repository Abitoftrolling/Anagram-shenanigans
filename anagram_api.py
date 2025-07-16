import requests

#API credentials from RapidAPI
api_host = "x-rapidapi-host: word-checker-api.p.rapidapi.com"
api_key = "c79c515bb3msh30d268472db25dap129bb0jsndee7029ec1f8"

#function to get anagrams for a given word using the Word Checker API
def get_words(word):
    url = f"https://word-checker-api.p.rapidapi.com/v1/tools/anagram-solver/{word}"

    #required headers for RapidAPI authentication
    headers = {
        "x-rapidapi-host": api_host,
        "x-rapidapi-key": api_key
    }

    #send a get request to the API
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        #gets list of anagrams from API response
        anagrams = data.get("anagrams", [])
        return anagrams
    else:
        #prints error if the request fails and return an empty list
        print(f"API error {response.status_code}")
        return []


