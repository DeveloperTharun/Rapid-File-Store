# (c) @JAsuran2p0

import os


class Config(object):
	API_ID = 8754146
	API_HASH = "8b56a6989f6d04f6f4fe78133ade02fd"
	BOT_TOKEN = "5997800222:AAHNBHD4nUiw1FGG2Y099dqom1WasNbmXgc"
	BOT_USERNAME = "Ultra_File_Store_Bot"
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001509431270"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "5669934860"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://SkMedia:Tharunraj1828@cluster0.vbdxs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = -1001509431270
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
**ᴛʜɪs ɪs ᴀ ᴘᴇʀᴍᴀɴᴇɴᴛ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ.
sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴍᴇᴅɪᴀ ᴏʀ ғɪʟᴇ. ɪ ᴄᴀɴ ᴡᴏʀᴋ ɪɴ ᴄʜᴀɴɴᴇʟ ᴛᴏᴏ ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ ᴇᴅɪᴛ ᴘᴇʀᴍɪssɪᴏɴ, ɪ ᴡɪʟʟ ᴀᴅᴅ sᴀᴠᴇ ᴜᴘʟᴏᴀᴅᴇᴅ ғɪʟᴇ ɪɴ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ sʜᴀʀᴇ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ. 

╭────[ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ]────⍟
├⍟ ʙᴏᴛ ɴᴀᴍᴇ : [ғɪʟᴇ sᴛᴏʀᴇ](https://telegram.me/{BOT_USERNAME})
├⍟ ᴏᴡɴᴇʀ : [sᴋᴛㅤ〆ㅤᴀᴅᴍɪɴ](https://telegram.me/SKxTharun)
├⍟ ʟᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ 3](https://www.python.org)
├⍟ ᴅᴇᴠᴇʟᴏᴘᴇʀ : [ʀᴀᴘɪᴅ ʙᴏᴛs](https://telegram.me/Rapid_Bots)
├⍟ ᴍᴏᴠɪᴇꜱ : [ᴛᴀᴍɪʟsᴋ ᴍᴏᴠɪᴇᴢ](https://telegram.me/TamilSk_Moviez)
├⍟ ʙᴏᴛ ʟɪsᴛ : [ʀᴀᴘɪᴅ ʙᴏᴛs](https://telegram.me/Rapid_Bots)
├⍟ ʙᴏᴛ ᴛᴜᴛᴏʀɪᴀʟ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://youtu.be/7iG_4iBWBGs)
╰─────────────────────⍟**
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** [𝐑𝐚𝐩𝐢𝐝 𝐁𝐨𝐭𝐬](https://t.me/Rapid_Bots) 

𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐢𝐬 𝐒𝐮𝐩𝐞𝐫 𝐍𝐨𝐨𝐛. 𝐉𝐮𝐬𝐭 𝐋𝐞𝐚𝐫𝐧𝐢𝐧𝐠 𝐟𝐫𝐨𝐦 𝐎𝐟𝐟𝐢𝐜𝐢𝐚𝐥 𝐃𝐨𝐜𝐬. 𝐀𝐧𝐝 𝐒𝐞𝐞𝐤𝐢𝐧𝐠 𝐇𝐞𝐥𝐩 𝐅𝐫𝐨𝐦 𝐏𝐫𝐨 𝐂𝐨𝐝𝐞𝐫𝐬

𝐈𝐟 𝐘𝐨𝐮 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐃𝐨𝐧𝐚𝐭𝐞 𝐎𝐮𝐫 𝐇𝐚𝐫𝐝 𝐖𝐨𝐫𝐤. 𝐘𝐨𝐮 𝐂𝐚𝐧 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐓𝐡𝐞 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫. 

𝐀𝐥𝐬𝐨 𝐫𝐞𝐦𝐞𝐦𝐛𝐞𝐫 𝐭𝐡𝐚𝐭 𝐝𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐰𝐢𝐥𝐥 𝐃𝐞𝐥𝐞𝐭𝐞 𝐀𝐝𝐮𝐥𝐭 𝐂𝐨𝐧𝐭𝐞𝐧𝐭𝐬 𝐟𝐫𝐨𝐦 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞. 𝐒𝐨 𝐛𝐞𝐭𝐭𝐞𝐫 𝐝𝐨𝐧'𝐭 𝐒𝐭𝐨𝐫𝐞 𝐓𝐡𝐨𝐬𝐞 𝐊𝐢𝐧𝐝 𝐨𝐟 𝐓𝐡𝐢𝐧𝐠𝐬.
"""
	HOME_TEXT = """
**нєℓℓσ, [{}](tg://user?id={})\n\nᴛʜɪs ɪs ᴀ ᴘᴇʀᴍᴀɴᴇɴᴛ ғɪʟᴇsᴛᴏʀᴇ ʙᴏᴛ.
ʜᴏᴡ ᴛᴏ ᴜsᴇ ʙᴏᴛ & ɪᴛ's ʙᴇɴᴇғɪᴛs ??

📢 sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ & ɪᴛ ᴡɪʟʟ ʙᴇ ᴜᴘʟᴏᴀᴅᴇᴅ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ & ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ᴛʜᴇ ғɪʟᴇ ʟɪɴᴋ.

⚠️ ʙᴇɴᴇғɪᴛs: ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴏᴠɪᴇ ᴄʜᴀɴɴᴇʟ ᴏʀ ᴀɴʏ ᴄᴏᴘʏʀɪɢʜᴛ ᴄʜᴀɴɴᴇʟ, ᴛʜᴇɴ ɪᴛs ᴜsᴇғᴜʟ ғᴏʀ ᴅᴀɪʟʏ ᴜsᴀɢᴇ, ʏᴏᴜ ᴄᴀɴ sᴇɴᴅ ᴍᴇ ʏᴏᴜʀ ғɪʟᴇ & ɪ ᴡɪʟʟ sᴇɴᴅ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ ᴛᴏ ʏᴏᴜ & ᴄʜᴀɴɴᴇʟ ᴡɪʟʟ ʙᴇ sᴀғᴇ ғʀᴏᴍ ᴄᴏᴘʏʀɪɢʜᴛ ɪɴғʀɪɴɢᴇᴍᴇɴᴛ ɪssᴜᴇ. ɪ sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ ᴀʟsᴏ ʏᴏᴜ ᴄᴀɴ ᴄʜᴇᴄᴋ ᴀʙᴏᴜᴛ ʙᴏᴛ.

❌ ᴘᴏʀɴᴏɢʀᴀᴘʜʏ ᴄᴏɴᴛᴇɴᴛs ᴀʀᴇ sᴛʀɪᴄᴛʟʏ ᴘʀᴏʜɪʙɪᴛᴇᴅ & ɢᴇᴛ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ.

👀 ʙᴏᴛ ᴛᴜᴛᴏʀɪᴀʟ: [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐓𝐨 𝐖𝐚𝐭𝐜𝐡](https://youtu.be/7iG_4iBWBGs)**
"""
