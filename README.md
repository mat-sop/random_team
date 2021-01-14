# random-team
Discord bot to split players into random teams. Hosted on heroku.

## Add bot to server
`https://discordapp.com/api/oauth2/authorize?client_id=678602247709524024&permissions=16779264&scope=bot`

## Usage
```
Bot that splits members into teams.

Random:
  shuffle Takes list of voice channels. Splits players evenly into given chan...
​No Category:
  help    Shows this message

Type $rng help command for more info on a command.
You can also type $rng help category for more info on a category.
```

## Development/Hosting

### Docker
`cp .env.example .env`
Paste token into `.env`
`docker build . -f Dockerfile -t random-team`
`docker run -d random-team`

### Without docker

#### Requirements
`Python 3.8.3`

#### Instalation
```bash
python -m pip install -r requirements.txt
```
#### Run
```bash
export DISCORD_BOT_TOKEN="paste token here"
python random_team/bot.py
```
