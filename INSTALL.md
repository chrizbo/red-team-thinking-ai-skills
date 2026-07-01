# Getting and installing the skills

## 1. Get the repo

**If you have git:**

```bash
git clone https://github.com/chrizbo/red-team-thinking-ai-skills.git
cd red-team-thinking-ai-skills
```

**If you don't have git:** go to [github.com/chrizbo/red-team-thinking-ai-skills](https://github.com/chrizbo/red-team-thinking-ai-skills), click the green **Code** button, choose **Download ZIP**, then unzip it and open a terminal in the unzipped folder.

## 2. Install into your tool

Run the commands below from inside the `red-team-thinking-ai-skills` folder. All five skills install at once.

### Claude Code / Claude Desktop

```bash
mkdir -p ~/.claude/skills
cp -r skills/* ~/.claude/skills/
```

Start a new Claude Code session (or restart Claude Desktop). Trigger a skill by typing `/assumptions-challenge-ai` (or any other skill name), or just describe what you want — Claude will pick the right skill on its own.

### Codex CLI

```bash
mkdir -p ~/.codex/skills
cp -r skills/* ~/.codex/skills/
```

Invoke with `$assumptions-challenge-ai` (or any other skill name), or let Codex trigger it automatically.

### Gemini CLI

```bash
mkdir -p ~/.gemini/commands
cp gemini/commands/*.toml ~/.gemini/commands/
```

Inside Gemini CLI, run `/commands reload`, then invoke with `/assumptions-challenge-ai` (or any other skill name).

### GitHub Copilot (Chat or CLI)

Run this inside the project where you want to use the skills (not this repo):

```bash
mkdir -p .github/prompts
cp /path/to/red-team-thinking-ai-skills/copilot/prompts/*.prompt.md .github/prompts/
```

In Copilot Chat, type `/` to see the prompt list and pick one, or type `#prompt:` and the file name.

### Gemini Gems, custom GPTs, or any other chat tool

No install step — open the matching file in `prompts/`, copy the whole thing, and paste it into:

- the Gem's (or custom assistant's) **Instructions** field, or
- the first message of a new chat.

## 3. Check it worked

```bash
ls ~/.claude/skills        # Claude Code / Desktop
ls ~/.codex/skills         # Codex CLI
ls ~/.gemini/commands      # Gemini CLI
```

Each should list all five skills (`assumptions-challenge-ai`, `ai-as-provocateur`, `argument-dissection-ai`, `four-ways-of-seeing-ai`, `devils-advocacy-ai`).

## Getting updates later

The commands above copy the files, so later changes to this repo won't show up automatically. To update:

```bash
cd red-team-thinking-ai-skills
git pull
```

Then re-run the install command for your tool from Step 2 to refresh your installed copies.

**If you'd rather your installed copies always stay current with the repo** (git users only), symlink instead of copying, once per skill:

```bash
ln -sf "$(pwd)/skills/assumptions-challenge-ai" ~/.claude/skills/assumptions-challenge-ai
```

Repeat for each skill folder, or for each tool's directory. With a symlink, a `git pull` updates the installed skill immediately — no re-copying needed.
