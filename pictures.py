import requests

image = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Main_Building_at_the_University_of_Notre_Dame.jpg/437px-Main_Building_at_the_University_of_Notre_Dame.jpg'
    #image  = input('please input your desired image link')
    #still working on how to ask for input of a link
    #we will learn how to pull an image link and display it somewhere next

picture = requests.get(image)
print(picture.content)
with open('ryanc:\notredame.png','wb') as f:
    f.write(picture.content)