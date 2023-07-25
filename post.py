import deso
from decouple import config

PUBLIC_KEY = config("PUBLIC_KEY")
SEED_HEX = config("SEED_HEX")

desoSocial = deso.Social(publicKey=PUBLIC_KEY, seedHex=SEED_HEX)
body = "Hi, I am testing DeSo py\nThanks @itsaditya for making it!"

status = desoSocial.submitPost(body)
print(f'Post status {status.status_code}')