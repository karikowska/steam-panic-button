# ✨ Karo's Steam(y) Dashboard ✨

### Great for quick stats on your game library & helps with choosing a game to play!

![](https://github.com/karikowska/steam-panic-button/blob/master/img/Screenshot%202025-07-12%20001655.png)

>Ever felt too overwhelmed by your Steam backlog? 

>Do you shudder at having to actually choose a video game to play when it's late night and you're super tired, and opt to just fall back to the same comfort zone of opening up <insert your comfort game here> a hundred times in a row instead?

>Do you feel like you're stuck in an infinite loop of buying new games, thinking you'll play them, and then seeing them pile up over time with no end in sight?

>All of this because you have unbelievable inertia?
 

Then this project might help you! 

I've built a mini-roulette to help me pick a video game when I'm too overwhelmed to pick one myself! (this is a natural progression of things when you own 100+ games I'm afraid)

# Features

- displays simple stats about your game library
- serves you a game roulette that chooses a random game from your library
- serves two widgets with video games that you 1. have never touched and 2. you've played for less than 2 hours, if these exist

# How to run

1. You will need your Steam API key - which you can get if you have an account on Steam by following this link: https://steamcommunity.com/dev/apikey. You will also need your Steam ID, which is a long string of numbers you can find in your profile settings on Steam.

2. Make sure to either place both in your .env file or export them through the terminal like such:

   ````
   export STEAM_API_KEY=""
   export STEAM_ID=""
   ````

3. Install packages from the requirements.txt with this command:

   ````
   pip install -r requirements.txt
   ````

4. In the root of the repo, run:

   ````
   streamlit run app.py
   ````

to run the app!

Now, you can finally enjoy freedom away from the depths of indecision :) because if you cannot pick a game due to an insurmountable backlog, this tool might just be the one to help you!

In the future I plan to deploy this app on Streamlit Cloud so users will be able to log in without having to run the app themselves.
# Current features & plans:
- [x] Create Streamlit UI
- [x] Implement the actual random game-picking mechanism
- [x] Add special tabs underneath which add a few more game recommendations like 'here's a game you've never played, how about you give it a chance?'
- [ ] Smart game recommendations based on recent play - could be a side tab
- [ ] Add a dashboard & stats page to do with your Steam account (for the nerds)
- [ ] Add CI/CD with Github Actions
- [x] Add login screen for inputting your steam API key
- [ ] Deploy on Streamlit Cloud/another provider
