import pyshorteners
s = pyshorteners.Shortener(
    api_key='', #API KEY
    user_id='', #USUARIO ID
    domain='ad.fly',
    group_id=12,
    type='int')

link = input("Escribe la url: ")
url =  s.adfly.short(f'{link}')


print(f"{url}")
