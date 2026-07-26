# Getting and installing the skills

## 1. Get the repo

**If you have git:**

```bash
git clone https://github.com/chrizbo/red-team-thinking-ai-skills.git
cd red-team-thinking-ai-skills
```

**If you don't have git:**

1. Go to [github.com/chrizbo/red-team-thinking-ai-skills](https://github.com/chrizbo/red-team-thinking-ai-skills), click the green **Code** button, then **Download ZIP**. It saves to your Downloads folder.
2. Unzip it:
   - **Mac:** double-click the ZIP in Downloads. It extracts automatically into a new folder right there, named something like `red-team-thinking-ai-skills-main`.
   - **Windows:** right-click the ZIP in Downloads → **Extract All** → **Extract**. Same result, same location.
3. Open a terminal in that folder:
   - **Mac:** right-click the unzipped folder → **New Terminal at Folder**. (If that option is missing, open Terminal and run `cd ~/Downloads/red-team-thinking-ai-skills-main`.)
   - **Windows:** open the unzipped folder in File Explorer, click into the address bar, type `powershell`, and press Enter.

You don't need to move the folder anywhere else — Downloads is fine. The commands below run from inside it.

## 2. Install into your tool

Run the commands below from inside the `red-team-thinking-ai-skills` folder. All three skills install at once.

### Claude Code / Claude Desktop

**Mac or Linux (Terminal):**

```bash
mkdir -p ~/.claude/skills
cp -r skills/* ~/.claude/skills/
```

**Windows (PowerShell):**

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item -Path "skills\*" -Destination "$env:USERPROFILE\.claude\skills\" -Recurse -Force
```

(The `cp -r` / `mkdir -p` commands above are Mac/Linux syntax and will error in PowerShell — use the Windows block instead.)

Start a new Claude Code session (or restart Claude Desktop). Trigger a skill by typing `/assumptions-challenge` (or any other skill name), or just describe what you want — Claude will pick the right skill on its own.

### Codex CLI

```bash
mkdir -p ~/.codex/skills
cp -r skills/* ~/.codex/skills/
```

Invoke with `$assumptions-challenge` (or any other skill name), or let Codex trigger it automatically.

### Gemini CLI

```bash
mkdir -p ~/.gemini/commands
cp gemini/commands/*.toml ~/.gemini/commands/
```

Inside Gemini CLI, run `/commands reload`, then invoke with `/assumptions-challenge` (or any other skill name).

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
ls ~/.claude/skills        # Claude Code / Desktop (Mac/Linux, or PowerShell: dir $env:USERPROFILE\.claude\skills)
ls ~/.codex/skills         # Codex CLI
ls ~/.gemini/commands      # Gemini CLI
```

On Windows you can also just open `C:\Users\<you>\.claude\skills` in File Explorer and look.

Each should list all three skills (`assumptions-challenge`, `provocateur`, `socratic-partner`).

## Getting updates later

The commands above copy the files, so later changes to this repo won't show up automatically. To update:

```bash
cd red-team-thinking-ai-skills
git pull
```

Then re-run the install command for your tool from Step 2 to refresh your installed copies.

**If you'd rather your installed copies always stay current with the repo** (git users only), symlink instead of copying, once per skill:

```bash
ln -sf "$(pwd)/skills/assumptions-challenge" ~/.claude/skills/assumptions-challenge
```

Repeat for each skill folder, or for each tool's directory. With a symlink, a `git pull` updates the installed skill immediately — no re-copying needed.
