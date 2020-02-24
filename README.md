# random-team

Discord bot to split players into random teams.

## Add bot to server
`https://discordapp.com/api/oauth2/authorize?client_id=678602247709524024&permissions=16779264&scope=bot`

## Usage
```
$rng help


Bot that splits members into teams.

Random:
  shuffle      Splits players into 2 teams. And writes them to the chat.
  shuffle-move Splits players into 2 teams, moves 2nd team to selected channel.
No Category:
  help         Shows this message

Type $rng help command for more info on a command.
You can also type $rng help category for more info on a category.
```

## Development

### Requirements
`Python 3.7.*`

### Instalation
```bash
pip install pipenv
pipenv install --skip-lock
```
### Usage
`pipenv run python random-team/bot.py`
