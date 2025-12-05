from emoji import is_emoji

def emoji_helper(selected_user, df):
    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if is_emoji(c)])
    return emojis



###END#####