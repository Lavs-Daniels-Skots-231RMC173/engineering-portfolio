# How to publish this portfolio to GitHub

This folder is a fully prepared portfolio repository — ready to push to your GitHub account `Lavs-Daniels-Skots-231RMC173`.

## Steps

```bash
# 1. Open this folder in a terminal
cd "C:\Users\dino3\Documents\Claude\Projects\CV creating\github-portfolio"

# 2. Initialise git
git init
git branch -M main

# 3. Add files
git add .
git commit -m "Initial commit — engineering portfolio (11 projects)"

# 4. Create the repository on github.com:
#    - go to https://github.com/new
#    - name: engineering-portfolio  (or whatever you prefer)
#    - public, no README/license/gitignore (we already have them)

# 5. Connect and push (replace REPO_NAME if you used something else)
git remote add origin https://github.com/Lavs-Daniels-Skots-231RMC173/engineering-portfolio.git
git push -u origin main
```

## Notes
- The `.gitignore` excludes build artifacts (`Debug/`, `*.elf`, `__pycache__/`, IDE folders) AND the CS50 `movies.db` / `fiftyville.db` assignment datasets (not your own data; can be re-downloaded if needed).
- Each project folder has its own `README.md` rendered nicely on GitHub.
- Top-level `README.md` is the portfolio landing page.

## Large files
- `01_WPL_Station/WPL_Station.rspag` (~66 MB) and `01_WPL_Station/Cycle_demo.mp4` (~26 MB) are below GitHub's 100 MB per-file limit but make the repo larger.
- If the push gets slow or you want a tidier repo, you can:
  - Use **Git LFS** for binary files (`git lfs install`, `git lfs track "*.rspag" "*.mp4"`), or
  - Upload them as GitHub **Releases** instead of committing to the repo.
