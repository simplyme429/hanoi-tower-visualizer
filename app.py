import streamlit as st
import time

st.set_page_config(page_title="Tower of Hanoi Visualizer", layout="wide")
st.title("🗼 Tower of Hanoi Visualizer")
st.markdown("### Interactive Recursive Solution with Animation")

# Sidebar controls
st.sidebar.header("Controls")
num_disks = st.sidebar.slider("Number of Disks", min_value=3, max_value=8, value=4)
speed = st.sidebar.slider("Animation Speed (seconds)", 0.1, 1.0, 0.5)

if st.button("Solve Puzzle", type="primary"):
    st.session_state.moves = []
    st.session_state.solving = True

# Recursive function to solve Tower of Hanoi
def hanoi(n, source, target, auxiliary, moves):
    if n == 1:
        moves.append((source, target))
        return
    hanoi(n-1, source, auxiliary, target, moves)
    moves.append((source, target))
    hanoi(n-1, auxiliary, target, source, moves)

# Initialize
if 'moves' not in st.session_state:
    st.session_state.moves = []
if 'solving' not in st.session_state:
    st.session_state.solving = False

# Solve if button pressed
if st.session_state.solving and not st.session_state.moves:
    moves = []
    hanoi(num_disks, "A", "C", "B", moves)
    st.session_state.moves = moves

# Visualization
cols = st.columns(3)
peg_names = ["A", "B", "C"]

# Display pegs
for i, col in enumerate(cols):
    with col:
        st.subheader(f"Peg {peg_names[i]}")
        peg = st.empty()

# Animation
if st.session_state.moves:
    progress_bar = st.progress(0)
    for idx, (source, target) in enumerate(st.session_state.moves):
        progress_bar.progress((idx + 1) / len(st.session_state.moves))
        
        # Simple text animation for now
        st.info(f"Move disk from **{source}** to **{target}**")
        time.sleep(speed)
        
        # You can enhance this with better graphics later

    st.success(f"✅ Puzzle Solved in **{len(st.session_state.moves)}** moves!")
    st.session_state.solving = False

st.caption("Project - Interactive Tower of Hanoi Visualizer | Built with Streamlit")