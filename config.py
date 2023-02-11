import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "14318701")

API_HASH = os.environ.get("API_HASH", "078057f70624f9143c45b5506c8dd617")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5777835679:AAH5Ga4t9VhYXSB7tHr_dDdON9TGaNHiCn8") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Movie_Zone_C") 

DB_NAME = os.environ.get("DB_NAME","Gowthaman")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Gowthaman:@cluster0.ounmfkw.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "0"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get("PORT", "8080")
