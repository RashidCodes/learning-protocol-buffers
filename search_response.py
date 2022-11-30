import search_response_pb2 

response = search_response_pb2.Result()
response.url = "https://google.com"
response.title = "Fav website"

# repeated string 
# print(dir(response.snippets))
response.snippets.extend("kingmoh is a legend".split()) 

for str_ in response.snippets:
    print(str_)
