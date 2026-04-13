import discord

print(f"discord.py-self v{discord.__version__} is installed and ready.")
print("This is a Python library for interacting with Discord's user API.")
print()
print("Available top-level classes:")
classes = [name for name in dir(discord) if not name.startswith('_') and name[0].isupper()]
for cls in sorted(classes)[:20]:
    print(f"  - discord.{cls}")
print(f"  ... and {len(classes) - 20} more")
print()
print("See the examples/ directory for usage examples.")
