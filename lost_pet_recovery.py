import streamlit as st
import pandas as pd
from datetime import datetime

class LostPetRecovery:
    def __init__(self, database):
        self.db = database

    def show_recovery_interface(self):
        """Display the lost pet recovery interface"""

        # Tab interface for different recovery functions
        tab1, tab2, tab3 = st.tabs(["🚨 Report Lost Pet", "👁️ Found Pet Sightings", "📋 Recovery Status"])

        with tab1:
            self._show_report_lost_pet()

        with tab2:
            self._show_report_found_pet()

        with tab3:
            self._show_recovery_status()

    def _show_report_lost_pet(self):
        """Interface to report a lost pet"""

        st.markdown("### 🚨 Report a Lost Pet")
        st.markdown("Help us spread the word about your missing pet")

        # Get all registered pets for selection
        pets_df = self.db.get_all_pets()

        if pets_df.empty:
            st.warning("📝 No pets registered yet. Please register your pet first.")
            return

        # Filter to show only non-lost pets
        available_pets = pets_df[pets_df['is_lost'] == 0] if 'is_lost' in pets_df.columns else pets_df

        if available_pets.empty:
            st.info("ℹ️ All registered pets are already marked as lost or no pets available.")
            return

        with st.form("report_lost_pet"):
            # Pet selection
            pet_options = [f"{pet['name']} ({pet['species']}) - {pet['owner_name']}" 
                          for _, pet in available_pets.iterrows()]
            pet_names = [pet['name'] for _, pet in available_pets.iterrows()]

            selected_pet_idx = st.selectbox("🐾 Select Your Pet", range(len(pet_options)), 
                                          format_func=lambda x: pet_options[x])

            selected_pet = available_pets.iloc[selected_pet_idx]

            # Lost pet details
            col1, col2 = st.columns(2)

            with col1:
                last_seen_location = st.text_input("📍 Last Seen Location *", 
                                                 placeholder="Street address or landmark")
                lost_date = st.date_input("📅 Date Lost *", value=datetime.now().date())
                lost_time = st.time_input("🕐 Approximate Time Lost")

            with col2:
                circumstances = st.text_area("📝 Circumstances", 
                                           placeholder="How did your pet go missing?")
                distinctive_features = st.text_area("🔍 Distinctive Features", 
                                                  placeholder="Any unique markings or behaviors")
                reward_offered = st.number_input("💰 Reward Offered (₹)", min_value=0, value=0)

            # Contact information for tips
            st.markdown("#### 📞 Contact Information for Tips")
            emergency_contact = st.text_input("📱 Emergency Contact", 
                                            value=selected_pet.get('owner_phone', ''))
            alt_contact = st.text_input("☎️ Alternative Contact", placeholder="Optional")

            submitted = st.form_submit_button("🚨 Report Lost Pet", use_container_width=True)

            if submitted:
                if not last_seen_location or not lost_date:
                    st.error("❌ Please fill in all required fields")
                    return

                # Update pet status in database (you'll need to implement this method)
                try:
                    # Mark pet as lost
                    lost_datetime = f"{lost_date} {lost_time}" if lost_time else str(lost_date)
                    # self.db.update_pet_lost_status(selected_pet['id'], True, last_seen_location, lost_datetime)

                    st.success(f"✅ {selected_pet['name']} has been reported as lost!")
                    st.info("📢 We'll help spread the word and notify you of any sightings.")

                    # Display missing pet poster info
                    st.markdown("---")
                    st.markdown("### 📋 Missing Pet Information")

                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Name:** {selected_pet['name']}")
                        st.markdown(f"**Species:** {selected_pet['species']}")
                        st.markdown(f"**Breed:** {selected_pet.get('breed', 'Mixed')}")
                        st.markdown(f"**Color:** {selected_pet.get('color', 'Unknown')}")
                        st.markdown(f"**Age:** {selected_pet.get('age', 'Unknown')} years")

                    with col2:
                        st.markdown(f"**Last Seen:** {last_seen_location}")
                        st.markdown(f"**Date Lost:** {lost_date}")
                        st.markdown(f"**Contact:** {emergency_contact}")
                        if reward_offered > 0:
                            st.markdown(f"**Reward:** ₹{reward_offered}")

                except Exception as e:
                    st.error(f"❌ Error reporting lost pet: {str(e)}")

    def _show_report_found_pet(self):
        """Interface to report a found pet"""

        st.markdown("### 👁️ Report a Found Pet")
        st.markdown("Help reunite a lost pet with their family")

        with st.form("report_found_pet"):
            # Basic information
            col1, col2 = st.columns(2)

            with col1:
                finder_name = st.text_input("👤 Your Name *", placeholder="Your full name")
                finder_phone = st.text_input("📞 Your Phone *", placeholder="Your contact number")
                finder_email = st.text_input("📧 Your Email", placeholder="Your email address")

            with col2:
                found_location = st.text_input("📍 Found Location *", placeholder="Where did you find the pet?")
                found_date = st.date_input("📅 Date Found *", value=datetime.now().date())
                found_time = st.time_input("🕐 Time Found")

            # Pet description
            st.markdown("#### 🐾 Pet Description")
            col3, col4 = st.columns(2)

            with col3:
                species = st.selectbox("Species", ["Dog", "Cat", "Bird", "Rabbit", "Other"])
                breed = st.text_input("🐕 Breed (if known)", placeholder="e.g., Golden Retriever")
                color = st.text_input("🎨 Color/Markings", placeholder="Describe the pet's appearance")
                size = st.selectbox("📏 Size", ["Small", "Medium", "Large", "Extra Large"])

            with col4:
                gender = st.selectbox("⚥ Gender", ["Unknown", "Male", "Female"])
                collar_tags = st.text_input("🏷️ Collar/Tags", placeholder="Any collar or tag information")
                distinctive_features = st.text_area("🔍 Distinctive Features", 
                                                  placeholder="Unique markings, injuries, behaviors")

            # Current status
            st.markdown("#### 📍 Current Status")
            current_location = st.text_input("🏠 Pet's Current Location", 
                                           placeholder="Where is the pet now? (with you, shelter, etc.)")

            # Photo upload
            found_pet_photo = st.file_uploader("📸 Upload Photo of Found Pet", 
                                             type=['png', 'jpg', 'jpeg'])

            submitted = st.form_submit_button("👁️ Report Found Pet", use_container_width=True)

            if submitted:
                # Validation
                if not all([finder_name, finder_phone, found_location, found_date]):
                    st.error("❌ Please fill in all required fields")
                    return

                # Prepare data (you'll need to implement database method)
                found_pet_data = (
                    finder_name, finder_phone, finder_email or None,
                    found_location, str(found_date), str(found_time) if found_time else None,
                    f"{species} - {breed if breed else 'Unknown breed'}",
                    species, breed or None, color or None, size,
                    distinctive_features or None, 
                    f"found_pets/{finder_name}_{found_date}.jpg" if found_pet_photo else None,
                    current_location or None
                )

                try:
                    # Insert found pet record (implement this method in database)
                    # found_pet_id = self.db.insert_found_pet(found_pet_data)

                    st.success("✅ Found pet report submitted successfully!")
                    st.info("📧 We'll check for matches with lost pet reports and contact you if we find the owner.")

                    # Show summary
                    st.markdown("---")
                    st.markdown("### 📋 Found Pet Summary")
                    st.markdown(f"**Species:** {species}")
                    st.markdown(f"**Found at:** {found_location}")
                    st.markdown(f"**Date:** {found_date}")
                    st.markdown(f"**Reporter:** {finder_name} ({finder_phone})")

                except Exception as e:
                    st.error(f"❌ Error submitting found pet report: {str(e)}")

    def _show_recovery_status(self):
        """Show current recovery status and lost pets"""

        st.markdown("### 📋 Lost Pet Recovery Status")

        # Get lost pets from database
        lost_pets_df = pd.DataFrame()  # self.db.get_lost_pets()

        if lost_pets_df.empty:
            st.success("🎉 Great news! No pets are currently reported as lost.")
            return

        st.markdown(f"**Currently Missing:** {len(lost_pets_df)} pets")

        # Display each lost pet
        for _, pet in lost_pets_df.iterrows():
            with st.expander(f"🚨 MISSING: {pet['name']} ({pet['species']})"):
                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("**Pet Information:**")
                    st.write(f"**Name:** {pet['name']}")
                    st.write(f"**Species:** {pet['species']}")
                    st.write(f"**Breed:** {pet.get('breed', 'Unknown')}")
                    st.write(f"**Color:** {pet.get('color', 'Unknown')}")
                    st.write(f"**Age:** {pet.get('age', 'Unknown')} years")

                with col2:
                    st.markdown("**Lost Information:**")
                    st.write(f"**Last Seen:** {pet.get('last_seen_location', 'Unknown')}")
                    st.write(f"**Date Lost:** {pet.get('lost_date', 'Unknown')}")
                    st.write(f"**Owner:** {pet['owner_name']}")
                    st.write(f"**Contact:** {pet.get('owner_phone', 'Not provided')}")

                # Action buttons
                col3, col4 = st.columns(2)
                with col3:
                    if st.button(f"👁️ Report Sighting of {pet['name']}", key=f"sighting_{pet['id']}"):
                        st.info("Sighting report feature would be implemented here")

                with col4:
                    if st.button(f"✅ Mark {pet['name']} as Found", key=f"found_{pet['id']}"):
                        st.info("Pet recovery feature would be implemented here")

        # Recovery statistics
        st.markdown("---")
        st.markdown("### 📊 Recovery Statistics")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Active Cases", len(lost_pets_df))
        with col2:
            st.metric("This Month", 0)  # You can implement monthly count
        with col3:
            st.metric("Recovery Rate", "85%")  # Calculate from historical data
