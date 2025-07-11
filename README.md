# Panic Button - an app for fighting indecision and inertia with video games

>Ever felt too overwhelmed by your Steam backlog? 

>Do you shudder at having to actually choose a video game to play when it's late night and you're super tired, and opt to just fall back to the same comfort zone of opening up <insert your comfort game here> a hundred times in a row instead?

>Do you feel like you're stuck in an infinite loop of buying new games, thinking you'll play them, and then seeing them pile up over time with no end in sight?

>All of this because you have unbelievable inertia?
 

Then this project might help you! 

I've built a mini-roulette to help me pick a video game when I'm too overwhelmed to pick one myself! (this is a natural progression of things when you own 100+ games I'm afraid)

# How to run

1. You will need your Steam API key - which you can get if you have an account on Steam by following this link: https://steamcommunity.com/dev/apikey. You will also need your Steam ID, which is a long string of numbers you can find in your profile settings on Steam.

2. Make sure to either place both in your .env file or export them through the terminal like such:

   ````
   export STEAM_API_KEY=""
   export STEAM_ID=""
   ````
   
3. Ensure Streamlit is installed (I'll create a requirements.txt later to help with that).

4. In the root of the repo, run:

   ````
   streamlit run app.py
   ````
   
   to run the app!

Now, you can finally enjoy freedom away from the depths of indecision :) because if you cannot pick a game due to an insurmountable backlog, this tool might just be the one to help you!

# Current app view

![](https://github.com/karikowska/steam-panic-button/blob/master/Screenshot%202025-07-12%20001655.png)

# Current features & plans:
- [x] Streamlit UI
- [x] The actual random game-picking mechanism
- [x] Special tabs underneath which add a few more game recommendations like 'here's a game you've never played, how about you give it a chance?'
- [ ] Smart game recommendations based on recent play - could be a side tab
- [ ] Maybe a nice dashboard & stats page to do with your Steam account too! :) (currently this is in progress)
- [ ] Login screen for inputting your steam API key
- [ ] Actual Streamlit deployment (perhaps)
