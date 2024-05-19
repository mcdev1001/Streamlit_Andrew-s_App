import streamlit as st
import pandas as pd

# Placeholder for RSVP responses
if 'rsvps' not in st.session_state:
    st.session_state['rsvps'] = []

# Function to display the invitation
def display_invitation():
    st.title("You're Invited!")
    
    # Embed the video using an iframe
    video_html = """
    <div style="position: relative; width: 100%; height: 0; padding-top: 140.0000%;
     padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden;
     border-radius: 8px; will-change: transform;">
      <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
        src="https://www.canva.com/design/DAGFlygWz0w/rjhKT1cVmx1jmgnT4494BA/view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
      </iframe>
    </div>
    """
    st.markdown(video_html, unsafe_allow_html=True)

    st.header("RSVP below and let us know if the fam is coming")
    st.write("Contact Devon if you need anything @ 512-983-3869")

# Function to handle RSVP
def rsvp_form():
    with st.form(key='rsvp_form'):
        name = st.text_input("Your Name")
        num_people = st.number_input("Number of People Attending", min_value=1, step=1)
        attendees = st.text_area("Names of Attendees")
        comments = st.text_area("Any additional comments or requirements?")
        submit_button = st.form_submit_button(label='Submit RSVP')

        if submit_button:
            st.session_state['rsvps'].append({
                'name': name,
                'num_people': num_people,
                'attendees': attendees,
                'comments': comments
            })
            st.success("Thank you for your RSVP!")

# Function to display all RSVPs
def display_rsvps():
    if st.session_state['rsvps']:
        st.subheader("RSVP List")
        df = pd.DataFrame(st.session_state['rsvps'])
        st.table(df)
    else:
        st.write("No RSVPs yet.")

# Main function to run the Streamlit app
def main():
    display_invitation()
    rsvp_form()
    display_rsvps()

if __name__ == "__main__":
    main()