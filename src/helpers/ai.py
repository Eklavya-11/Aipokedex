# Imports

# Solve function()

def solve(url):
  #downloads img & predicts it
  response = requests.get(url)
  file = open("pokemon.jpg", "wb")
  file.write(response.content)
  file.close()
  
  img = Image.open('pokemon.jpg')
  # Does something...
  return predicted_pokemon
