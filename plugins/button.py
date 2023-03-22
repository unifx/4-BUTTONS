# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/userbotch & t.me/ramsupportt
# Add Code FROM 3-BUTTONS <https://github.com/ramadhani892/3-BUTTONS

from config import FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL2, FORCE_SUB_GROUP, FORCE_SUB_GROUP2
from pyrogram.types import InlineKeyboardButton


def start_button(client):
	#cond -> fsub nya ga dipake
	if not FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP and not FORCE_SUB_GROUP2:
		buttons = [
			[
				InlineKeyboardButton(text="• 𝗧𝗨𝗧𝗨𝗣 •", callback_data="close"),
			],
		]
		return buttons
	#cond -> fsub dipake 1
	if FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP and not FORCE_SUB_GROUP2:
		buttons = [
			[
				InlineKeyboardButton(text="• 𝗝𝗢𝗜𝗡 •", url=client.invitelink),
			],
			[
				InlineKeyboardButton(text="• 𝗧𝗨𝗧𝗨𝗣 •", callback_data="close"),
			],
		]
		return buttons
	#cond -> fsub dipake 2
	if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP and not FORCE_SUB_GROUP2:
		buttons = [
			[
				InlineKeyboardButton(text="• 𝗝𝗢𝗜𝗡 •", url=client.invitelink),
				InlineKeyboardButton(text="• 𝗝𝗢𝗜𝗡 •", url=client.invitelink2),
			],
			[
				InlineKeyboardButton(text="• 𝗧𝗨𝗧𝗨𝗣 •", callback_data="close"),
			],
		]
		return buttons
	#cond -> fsub dipake 3
	if  FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL2 and FORCE_SUB_GROUP and not FORCE_SUB_GROUP2:
		buttons = [
			[
				InlineKeyboardButton(text="• 𝗝𝗢𝗜𝗡 •", url=client.invitelink),
				InlineKeyboardButton(text="• 𝗝𝗢𝗜𝗡 •", url=client.invitelink2),
			],
			[
				InlineKeyboardButton(text="• 𝗝𝗢𝗜𝗡 •", url=client.invitelink3),
			],
			[
				InlineKeyboardButton(text="• 𝗧𝗨𝗧𝗨𝗣 •", callback_data="close"),
			],
		]
		return buttons
	#cond -> fsub dipake 4
	if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL2 and FORCE_SUB_GROUP and FORCE_SUB_GROUP2:
		buttons = [
			[
				InlineKeyboardButton(text="• 𝗝𝗢𝗜𝗡 •", url=client.invitelink),
				InlineKeyboardButton(text="• 𝗝𝗢𝗜𝗡 •", url=client.invitelink2),
			],
			[
				InlineKeyboardButton(text="• 𝗝𝗢𝗜𝗡 •", url=client.invitelink3),
				InlineKeyboardButton(text="• 𝗝𝗢𝗜𝗡 •", url=client.invitelink4),
			],
			[
				InlineKeyboardButton(text="• 𝗧𝗨𝗧𝗨𝗣 •", callback_data="close"),
			],
		]
		return buttons
	# if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP and not FORCE_SUB_GROUP2:
	#     buttons = [
	#         [
	#             InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink2),
	#             InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink3),
	#         ],
	#     ]
	#     return buttons
	# if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP and not FORCE_SUB_GROUP2:
	#     buttons = [
	#         [
	#             InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink),
	#         ],           
	#     ]
	#     return buttons
	# if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and not FORCE_SUB_GROUP2:
	#     buttons = [            
	#         [
	#             InlineKeyboardButton(text="CHANNEL I", url=client.invitelink),
	#             InlineKeyboardButton(text="CHANNEL II", url=client.invitelink2),
	#         ],
	#         [InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close")],
	#     ]
	#     return buttons
	# if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2:
	#     buttons = [           
	#         [
	#             InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink),
	#             InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink2),
	#         ],
	#         [
	#             InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink3),
	#         ],
	#         [
	#             InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
	#         ],
	#     ]
	#     return buttons

def fsub_button(client, message):
	#cond -> fsub 1
	if FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP and not FORCE_SUB_GROUP2:
		buttons = [
			[
				InlineKeyboardButton(text="𝗝𝗢𝗜𝗡 𝗦𝗘𝗞𝗔𝗥𝗔𝗡𝗚", url=client.invitelink),
			],
		]
		try:
			buttons.append(
				[
					InlineKeyboardButton(
							text="𝗖𝗢𝗕𝗔 𝗟𝗔𝗚𝗜",
							url=f"https://t.me/{client.username}?start={message.command[1]}",
						)
				]
			)
		except IndexError:
			pass
		return buttons
	#cond -> fsub 2
	if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP and not FORCE_SUB_GROUP2:
		buttons = [
			[
			  InlineKeyboardButton(text="𝗝𝗢𝗜𝗡 𝗦𝗘𝗞𝗔𝗥𝗔𝗡𝗚", url=client.invitelink),
			  InlineKeyboardButton(text="𝗝𝗢𝗜𝗡 𝗦𝗘𝗞𝗔𝗥𝗔𝗡𝗚", url=client.invitelink2),  
			],
		]
		try:
			buttons.append(
				[
					InlineKeyboardButton(
							text="𝗖𝗢𝗕𝗔 𝗟𝗔𝗚𝗜",
							url=f"https://t.me/{client.username}?start={message.command[1]}",
						)
				]
			)
		except IndexError:
			pass
		return buttons
	#cond -> fsub 3
	if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL2 and FORCE_SUB_GROUP and not FORCE_SUB_GROUP2:
		 buttons = [
			[
			  InlineKeyboardButton(text="𝗝𝗢𝗜𝗡 𝗦𝗘𝗞𝗔𝗥𝗔𝗡𝗚", url=client.invitelink),
			  InlineKeyboardButton(text="𝗝𝗢𝗜𝗡 𝗦𝗘𝗞𝗔𝗥𝗔𝗡𝗚", url=client.invitelink2),  
			],
			[
			  InlineKeyboardButton(text="𝗝𝗢𝗜𝗡 𝗦𝗘𝗞𝗔𝗥𝗔𝗡𝗚", url=client.invitelink3),
			],
		]
		try:
			buttons.append(
				[
					InlineKeyboardButton(
							text="𝗖𝗢𝗕𝗔 𝗟𝗔𝗚𝗜",
							url=f"https://t.me/{client.username}?start={message.command[1]}",
						)
				]
			)
		except IndexError:
			pass
		return buttons
	#cond -> fsub 4
	if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL2 and FORCE_SUB_GROUP and FORCE_SUB_GROUP2:
		buttons = [
			[
			  InlineKeyboardButton(text="𝗝𝗢𝗜𝗡 𝗦𝗘𝗞𝗔𝗥𝗔𝗡𝗚", url=client.invitelink),
			  InlineKeyboardButton(text="𝗝𝗢𝗜𝗡 𝗦𝗘𝗞𝗔𝗥𝗔𝗡𝗚", url=client.invitelink2),  
			],
			[
			  InlineKeyboardButton(text="𝗝𝗢𝗜𝗡 𝗦𝗘𝗞𝗔𝗥𝗔𝗡𝗚", url=client.invitelink3),
			  InlineKeyboardButton(text="𝗝𝗢𝗜𝗡 𝗦𝗘𝗞𝗔𝗥𝗔𝗡𝗚", url=client.invitelink4),
			],
		]
		try:
			buttons.append(
				[
					InlineKeyboardButton(
							text="𝗖𝗢𝗕𝗔 𝗟𝗔𝗚𝗜",
							url=f"https://t.me/{client.username}?start={message.command[1]}",
						)
				]
			)
		except IndexError:
			pass
		return buttons
	# if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and not FORCE_SUB_GROUP2:
	#     buttons = [
	#         [
	#             InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink2),
	#         ],
	#     ]
	#     try:
	#         buttons.append(
	#             [
	#                 InlineKeyboardButton(
	#                     text="ᴄᴏʙᴀ ʟᴀɢɪ",
	#                     url=f"https://t.me/{client.username}?start={message.command[1]}",
	#                 )
	#             ]
	#         )
	#     except IndexError:
	#         pass
	#     return buttons
	# if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP and not FORCE_SUB_GROUP2:
	#     buttons = [
	#         [
	#             InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink),
	#         ],
	#     ]
	#     try:
	#         buttons.append(
	#             [
	#                 InlineKeyboardButton(
	#                     text="ᴄᴏʙᴀ ʟᴀɢɪ",
	#                     url=f"https://t.me/{client.username}?start={message.command[1]}",
	#                 )
	#             ]
	#         )
	#     except IndexError:
	#         pass
	#     return buttons
	# if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and not FORCE_SUB_GROUP2:
	#     buttons = [
	#         [
	#             InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink),
	#             InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink2),
	#         ],
	#     ]
	#     try:
	#         buttons.append(
	#             [
	#                 InlineKeyboardButton(
	#                     text="ᴄᴏʙᴀ ʟᴀɢɪ",
	#                     url=f"https://t.me/{client.username}?start={message.command[1]}",
	#                 )
	#             ]
	#         )
	#     except IndexError:
	#         pass
	#     return buttons
	# if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2:
	#     buttons = [
	#         [
	#             InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink),
	#             InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink2),
	#         ],
	#         [
	#             InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink3),
	#         ],
	#     ]
	#     try:
	#         buttons.append(
	#             [
	#                 InlineKeyboardButton(
	#                     text="ᴄᴏʙᴀ ʟᴀɢɪ",
	#                     url=f"https://t.me/{client.username}?start={message.command[1]}",
	#                 )
	#             ]
	#         )
	#     except IndexError:
	#         pass
	#     return buttons
