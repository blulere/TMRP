class Discord:
    DISCORD_VERSION = 3
    DISCORD_APPLICATION_MANAGER_VERSION = 1
    DISCORD_USER_MANAGER_VERSION = 1
    DISCORD_IMAGE_MANAGER_VERSION = 1
    DISCORD_ACTIVITY_MANAGER_VERSION = 1
    DISCORD_RELATIONSHIP_MANAGER_VERSION = 1
    DISCORD_LOBBY_MANAGER_VERSION = 1
    DISCORD_NETWORK_MANAGER_VERSION = 1
    DISCORD_OVERLAY_MANAGER_VERSION = 2
    DISCORD_STORAGE_MANAGER_VERSION = 1
    DISCORD_STORE_MANAGER_VERSION = 1
    DISCORD_VOICE_MANAGER_VERSION = 1
    DISCORD_ACHIEVEMENT_MANAGER_VERSION = 1

    class DiscordUser:
        id: int
        username: str
        discriminator: int
        avatar: str # Link to avatar.
        bot: bool
    class DiscordOAuth2Token:
        access_token: str
        scopes: str
        expires: int # Unix time.
    class DiscordPresence:
        status: int # FIXME: Change to a type!
        activity: str
    
    def Test():
        pass
    
    def Discord(CLIENT_ID, Discord.CreateFlags.Default):
        pass
