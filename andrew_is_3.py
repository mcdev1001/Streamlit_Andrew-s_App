import streamlit as st
import pandas as pd
import sqlite3

# SQLite database file
DB_FILE = 'rsvps.db'

# Initialize the database
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS rsvps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            num_people INTEGER,
            attendees TEXT,
            comments TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Function to load RSVP data from the database
def load_rsvps():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT * FROM rsvps')
    rsvps = c.fetchall()
    conn.close()
    return rsvps

# Function to save RSVP data to the database
def save_rsvps(name, num_people, attendees, comments):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        INSERT INTO rsvps (name, num_people, attendees, comments)
        VALUES (?, ?, ?, ?)
    ''', (name, num_people, attendees, comments))
    conn.commit()
    conn.close()

# Function to display the invitation
def display_invitation():
    st.title("You're Invited!")
    
    # Embed the video using an iframe
    video_html = """
    <div style="position: relative; width: 100%; height: 0; padding-top: 140.0000%;
 padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden;
 border-radius: 8px; will-change: transform;">
  <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
    src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAGFlygWz0w&#x2F;rjhKT1cVmx1jmgnT4494BA&#x2F;view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
    </iframe>
    </div>
    """
    st.markdown(video_html, unsafe_allow_html=True)

    st.header("RSVP below and let us know if the fam is coming!")
    st.write("Contact Devon if you need anything\n512-983-3869")

# Function to handle RSVP
def rsvp_form():
    with st.form(key='rsvp_form'):
        name = st.text_input("Your Name")
        num_people = st.number_input("Number of People Attending", min_value=1, step=1)
        attendees = st.text_area("Names of Attendees")
        comments = st.text_area("Anything additional you'd like to share?")
        submit_button = st.form_submit_button(label='Submit RSVP')

        if submit_button:
            save_rsvps(name, num_people, attendees, comments)
            st.success("Thank you for your RSVP!")

# Function to display all RSVPs
def display_rsvps():
    rsvps = load_rsvps()
    if rsvps:
        st.subheader("RSVP List")
        df = pd.DataFrame(rsvps, columns=['Name', 'Number of People', 'Attendees', 'Comments'])
        st.table(df)
    else:
        st.write("No RSVPs yet.")

# Main function to run the Streamlit app
def main():
    init_db()
    display_invitation()
    rsvp_form()
    display_rsvps()

if __name__ == "__main__":
    main()
