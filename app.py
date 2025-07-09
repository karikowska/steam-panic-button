from steam_api import steam_game_retrieve, steam_game_unplayed
import streamlit as st 
import random
import numpy as np

def main():
    
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
    
    st.set_page_config(layout="wide")
    
    col1, col3, col2, col4 = st.columns([3, 0.75, 4, 3])
    
    with col1:
        with st.container():
            st.markdown('<div class="info-container">', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.subheader("Here are some fun stats...")
        
        st.markdown(f"**Total games in library:** {len(steam_game_retrieve())}")
        
        st.markdown(f"**Total unplayed games:** {len(steam_game_unplayed(0, 0))}")
        
        order = steam_game_unplayed(0, 9999999999)
        new_order = sorted(order, key=lambda x: x['playtime'], reverse=True)[0]['name']
        st.markdown(f"**Favourite game:** {new_order}")

    
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
        st.markdown("Also make sure to check out these completely unplayed games in your library:")
        
        try:
            unplayed = steam_game_unplayed(0,0)
            
            col1, col2, col3 = st.columns([1, 1, 1])
            
            with col1:
                game1 = random.choice(unplayed)
                st.markdown(f"**{game1['name']}**")
                
            with col2:
                game2 = random.choice(unplayed)
                st.markdown(f"**{game2['name']}**")
                
            with col3:
                game3 = random.choice(unplayed)
                st.markdown(f"**{game3['name']}**")
                
                
            col1, col2, col3 = st.columns([1, 1, 1])
            
            with col1:
                if game1['library_hero']:
                    st.image(game1['library_hero'], width=200)
                else:
                    st.markdown("No image available :( pretend there's a picture here!!!")
                
            with col2:
                if game2['library_hero']:
                    st.image(game2['library_hero'], width=200)
                else:
                    st.markdown("No image available :( pretend there's a picture here!!!")
                
            with col3:
                if game3['library_hero']:
                    st.image(game3['library_hero'], width=200)
                else:
                    st.markdown("No image available :( pretend there's a picture here!!!")
        except:
            st.markdown("No unplayed games found in your library. I guess you don't have a backlog, huh? Congrats! :D")
            
        with st.container():
            st.markdown('<div class="info-container">', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("And here are games that you've only played a little bit (< 2 hours), maybe give them another go?")
        
        col1, col2, col3 = st.columns([1, 1, 1])
        
        unplayed = steam_game_unplayed(0.000001,120)
        
        with col1:
            game4 = random.choice(unplayed)
            st.markdown(f"**{game4['name']}**")
            
        with col2:
            game5 = random.choice(unplayed)
            st.markdown(f"**{game5['name']}**")
            
        with col3:
            game6 = random.choice(unplayed)
            st.markdown(f"**{game6['name']}**")
            
            
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            if game4['library_hero']:
                st.image(game4['library_hero'], width=200)
            else:
                st.markdown("No image available :( pretend there's a picture here!!!")
            
        with col2:
            if game5['library_hero']:
                st.image(game5['library_hero'], width=200)
            else:
                st.markdown("No image available :( pretend there's a picture here!!!")
            
        with col3:
            if game6['library_hero']:
                st.image(game6['library_hero'], width=200)
            else:
                st.markdown("No image available :( pretend there's a picture here!!!")
        
        # Instructions
        st.markdown("---")
        st.markdown("""
        ### 📝 Implementation Notes:

        Building a mini-roulette to help me pick a video game when I'm too overwhelmed to pick one myself! (this is a natural progression of things when you own 100+ games I'm afraid)

        Plan:
        - ~Streamlit UI~
        - ~An actual roulette if I can get it animated~
        - ~a special 'here's a game you've never played, how about you give it a chance?'~
        - Smart game recommendations based on recent play
        - I want to differentiate this tool from just being the 'I'm feeling lucky' game picker from SteamDB by making it slightly more analytical and personalised
        - Maybe a nice dashboard & stats page to do with your Steam account too! :)

        """)

if __name__ == "__main__":
    main()