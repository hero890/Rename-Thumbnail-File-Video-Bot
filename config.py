# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "22672907")

API_HASH = os.environ.get("API_HASH", "0ff15ae2153bd8e03b48cb293010bc6a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6509865087:AAF05LP6RUGqpPS2rUyDgpWN7DWWKx2aAcA") 

FORCE_SUB = os.environ.get("FORCE_SUB", "https://t.me/bots_repo") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "renamebot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://infotechhero890:7c2qvHdJUYqTOaMa@cluster0.veojhex.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6287591671').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
