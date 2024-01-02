# Emoji-Discord-Messages
Takes a message written with the Latin alphabet and converts it into emoji form using Discord's regional indicator emojis.

Note: smart enough to recognise a string between colons is its own emoji, but not smart enough to recognise if that emoji is known by discord. E.g. an input slice such as ":afvxrjvtr:" will be interpreted as a discord emoji and left alone.