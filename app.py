from steam_api import steam_game_retrieve, games_by_time_played
import streamlit as st 
import random
import numpy as np
from components import display_games, choose_and_display_game_name, display_game_image
import math

def main():
    st.set_page_config(layout="wide")
    
    st.markdown("""
<style>
    .info-container {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 5px;
        border-radius: 10px;
        margin: 10px 0;
    }
    """, unsafe_allow_html=True)
    
    col1, col3, col2, col4 = st.columns([3, 0.75, 4, 3])
    
    with col1:
        with st.container():
            st.markdown('<div class="info-container">', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.subheader("Here are some fun stats...")
        
        st.markdown(f"**Total games in library:** {len(steam_game_retrieve())}")
        
        st.markdown(f"**Total unplayed games:** {len(games_by_time_played(0, 0))}")
        
        order = games_by_time_played(0, 9999999999)
        new_order = sorted(order, key=lambda x: x['playtime'], reverse=True)[0]['name']
        time_played = sorted(order, key=lambda x: x['playtime'], reverse=True)[0]['playtime']
        st.markdown(f"**Favourite game:** {new_order}")
        st.markdown(f"**You've played it for a total of {time_played/60} hours!**")
        if time_played/60 > 50:
            st.markdown(f"Wow, I'm impressed. So how does it feel to have spent more than **{math.floor(time_played/60/24)} days** of your life on this game?")

    
    with col2:
        st.title("🎰 The Steam Roulette")
        st.subheader("If you don't know what to play, then let me decide! >:D")
        
        games = steam_game_retrieve()
        
        st.markdown("Just press this:")
        if st.button("🎰 spin 2 win!", key="streamlit_spin"):
            with st.spinner("Spinning..."):
                import time
                time.sleep(2)
            
            result_idx = random.randint(0, len(games) - 1)
            result = games[result_idx]
            
            st.balloons()
            st.success(f"🎉 Tonight, you're playing *{result[0]}*! Yippee :D")
            if result[1]:
                st.image(result[1], width=700)
            else:
                st.markdown("No image available :( pretend there's a picture here!!!")
            st.markdown("<br>", unsafe_allow_html=True)
            
        if st.button("Filter", key="filter_games"):
            pass
            st.markdown("Tick the genres that strike your fancy today:")
            # genres = st.multiselect()

        with st.container():
            st.markdown('<div class="info-container">', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("> Also make sure to check out these completely unplayed games in your library:")
        
        display_games(0, 0, "No unplayed games found in your library. I guess you don't have a backlog, huh? Congrats! :D")
            
        with st.container():
            st.markdown('<div class="info-container">', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("> And here are games that you've only played a little bit (< 2 hours), maybe give them another go?")
        
        display_games(0.000001, 120, "No games were found for this time range.")

if __name__ == "__main__":
    main()