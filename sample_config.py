HEROKU = True   # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
if HEROKU:
    from os import environ
    API_ID = int(environ["7"])
    API_HASH = environ["f87a20613ac285f394cb2a949952698b"]
    SUDO_CHAT_ID = int(environ["-1001161613115"])
    OWNER_ID = int(environ["1957876808"])
    SESSION_STRING = environ["BQASzNPGVPHtfBIdcJtJTK_SZMVssB8unaOmwGisgS-zc5gVnQfQJhDR2PgJ-X7qWkRitc_lJMVTu1qouGpJRX2prHA0jnmzm01B97l07zH-icQlOeVAJipDnJ120yiu2VR8bqJmXBUZiNjwIklXKmWUmRFjLa4UwFoMaUV0jYIPnYBESxfJ3LLDVXMYQ8JflcTYK48TF0wQjDQOPrw9qPEassHYTyw_pbdQcJvGbVV5ybX3oJFSyVs0vg9HyxElnH1CqT8AVFxJTsUUT6SkmpIitk4WKvTIeLw_vQ66xw9VJF3TgD_IBGMGj7dXU0ifRwH0dWQa8U4NUxU0BISrcvdLLUSAA"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 14371
    API_HASH = "e46b6c854d2bf58a0"
    SUDO_CHAT_ID = -1001485876964
    OWNER_ID = 1243703097


# don't make changes below this line
ARQ_API = "http://35.240.133.234:8000"
