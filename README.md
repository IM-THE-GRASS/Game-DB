# Game DB

A site built in [Reflex](https://reflex.dev) that uses the [IGDB](https://igdb.com) api for searching through practically all characters, games and consoles.




### Self hosting:
To self host and for developmentyou need python 3.11 or above[^1] 
in terminal, navigate to the `Game-DB` folder and run 

`python -m pip install -r /requirements.txt`

Once done, create a file called `.env` and using notepad write

`clientid={YOUR CLIENT ID HERE}`

`
token={YOUR IGDB KEY HERE}
`

and replace the placeholders with an details from the [IDGB api](https://api-docs.igdb.com)

to run just write `python -m reflex run` in the command line 



[^1]:version 3.11 or above is fine, older versions may work but I haven't tested them

### Demo / screenshots:

![image](https://github.com/user-attachments/assets/cdb90aed-2ac9-44af-a01d-a4ec47bdd209)

![video](https://cloud-pbjxv0508-hack-club-bot.vercel.app/02024-08-26_22-41-56.mp4)

##### The site was built for [Hack Club Arcade](https://hackclub.com/arcade/)
