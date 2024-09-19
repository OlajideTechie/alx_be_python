#Prompt the user to select a weather of the day. 
prompt = input("What's the weather like today? (sunny/rainy/cold):  ").strip().lower()  

# Provide clothing recommendations based on the weather.
if prompt == 'sunny': 
    print('Wear a t-shirt and sunglasses.')
elif prompt == 'rainy':
      print("Don't forget your umbrella and a raincoat.")
elif prompt == 'cold':
        print(' Make sure to wear a warm coat and a scarf')
else:
        print("Sorry, I don't have recommendations for this weather.")