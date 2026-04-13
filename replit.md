# selfcord

A modern, feature-rich, asynchronous Python wrapper for Discord's user API. This is a renamed fork of discord.py-self (originally discord.py by Rapptz), adapted to run as `selfcord` so it can coexist with other Discord libraries in the same project.

## Project Type
Python library (not a web application)

## Tech Stack
- **Language:** Python 3.10+
- **Core Dependencies:** aiohttp, curl_cffi, tzlocal, discord_protos
- **Build System:** setuptools (pyproject.toml)
- **Package Manager:** pip

## Setup
The package is installed in editable/development mode:
```bash
pip install -e .
```

## Usage
```python
import selfcord

client = selfcord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

client.run('your-token-here')
```

See the `examples/` directory for more usage examples.

## Project Structure
- `selfcord/` - Main library package (renamed from `discord/`)
  - `ext/commands/` - Command framework
  - `ext/tasks/` - Background task utilities
  - `types/` - TypedDict definitions
  - `webhook/` - Webhook support
- `examples/` - Usage examples
- `docs/` - Sphinx documentation source
- `tests/` - Test suite (pytest)

## Key Fixes Applied
1. Removed broken `@discord.utils.copy_doc(Message.message_commands)` decorator in `selfcord/ext/commands/context.py` (the `message_commands` attribute doesn't exist in this version)
2. Updated all internal imports across `selfcord/` from `discord.*` → `selfcord.*` so the package is fully self-contained under its new name

## Workflow
- **Start application**: Runs `python3 main.py` — verifies the library is installed and shows example usage

## Notes
- Automating user accounts may be against Discord's Terms of Service
- Optional extras: `voice`, `speed`, `docs`, `test`, `dev`
