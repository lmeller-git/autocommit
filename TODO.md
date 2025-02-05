# TODO

## Setup
- write setup.sh, which installs necessary programs and sets up hooks + env vars (api tokens?)
- somehow package necessary programs (python + rust parts) to allow for installation
- support for Linux, Mac, Windows?

## Usage
- write commit-msg hooks and incorporate flags like force-msg or Vars like Replace/No-replace
- write docs

## Parsing
- write rust program to parse git diffs and puts them into some format fitting for llm input
- python bindings for key functions
- unit + integration tests

## Msg generation
- find fitting model
- use output from preprocessing and pipe it into some llm to generate commit msgs
- implement different styles for messages
- api tokens?

