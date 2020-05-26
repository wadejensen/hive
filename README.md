# Hive
Hive boardgame engine server and AI agent clients

### Environment Setup
[Install direnv](https://direnv.net/). This will automatically setup and
activate a local virtualenv for you whenever you enter the project directory.
Be sure to setup the direnv hook for your respective shell.

On first setup `direnv allow`, and address any errors, eg. missing pyenv /
poetry installations, until you automatically enter the virtualenv when
entering the project directory.

Install project dependencies with
```
poetry install
```

Congratulations, you're ready to start coding.

If you are a zsh user [zsh-poetry](https://github.com/darvid/zsh-poetry)
is recommended to automatically deactivate the poetry virtualenv as
direnv will not handle this out of the box.
