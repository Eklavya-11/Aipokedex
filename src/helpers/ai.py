from keras.models import load_model
from urllib.request import Request, urlopen
from PIL import Image
from io import BytesIO
from numpy import array, argmax

# Currently, the model is not included in the code
model = load_model("PokemonPerfection.h5")

# Predict given url
def solve(url):

    # Open url and predict
    open_url = urlopen(Request(url = url, headers = {"User-Agent": "Mozilla/5.0"}))
    image = Image.open(BytesIO(open_url.read())).resize((180, 180))
    img_array = (array(image) / 255.0).reshape(1, 180, 180, 3)
    prediction = argmax(model.predict(img_array))

    return prediction
