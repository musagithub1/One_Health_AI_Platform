import streamlit as st
import pandas as pd
from datetime import datetime
import uuid

class PetRegistration:
    def __init__(self, database):
        self.db = database

    def show_registration_form(self):
        """Display the pet registration form"""

        st.markdown("### 🐾 Register Your Pet")
        st.markdown("Fill out the form below to register your pet in our system.")

        with st.form("pet_registration_form"):
            # Pet basic information
            col1, col2 = st.columns(2)

            with col1:
                pet_name = st.text_input("🏷️ Pet Name *", placeholder="Enter your pet's name")
                species = st.selectbox("🐾 Species *", ["Dog", "Cat", "Bird", "Rabbit", "Other"])
                breed = st.text_input("🐕 Breed", placeholder="e.g., Golden Retriever")
                age = st.number_input("📅 Age (years)", min_value=0, max_value=30, value=0)
                weight = st.number_input("⚖️ Weight (kg)", min_value=0.0, max_value=200.0, value=0.0, step=0.1)

            with col2:
                color = st.text_input("🎨 Color/Markings", placeholder="e.g., Brown with white spots")
                microchip_id = st.text_input("💾 Microchip ID", placeholder="Enter microchip number if available")
                medical_conditions = st.text_area("🏥 Medical Conditions", placeholder="Any known medical conditions or allergies")

            # Owner information
            st.markdown("#### 👤 Owner Information")
            col3, col4 = st.columns(2)

            with col3:
                owner_name = st.text_input("👨‍👩‍👧‍👦 Owner Name *", placeholder="Enter your full name")
                owner_phone = st.text_input("📞 Phone Number", placeholder="Enter your phone number")

            with col4:
                owner_email = st.text_input("📧 Email", placeholder="Enter your email address")
                owner_address = st.text_area("🏠 Address", placeholder="Enter your complete address")

            # Photo upload section
            st.markdown("#### 📸 Pet Photo")
            uploaded_photo = st.file_uploader("Upload Pet Photo", type=['png', 'jpg', 'jpeg'])

            # Submit button
            submitted = st.form_submit_button("📝 Register Pet", use_container_width=True)

            if submitted:
                self._process_registration(
                    pet_name, species, breed, age, weight, color, microchip_id, 
                    medical_conditions, owner_name, owner_phone, owner_email, 
                    owner_address, uploaded_photo
                )

        # Show existing pets
        self._show_existing_pets()

    def _process_registration(self, pet_name, species, breed, age, weight, color, 
                           microchip_id, medical_conditions, owner_name, owner_phone, 
                           owner_email, owner_address, uploaded_photo):
        """Process the pet registration form submission"""

        # Validation
        if not pet_name or not species or not owner_name:
            st.error("❌ Please fill in all required fields (marked with *)")
            return

        # Generate unique QR code for this pet
        qr_code = str(uuid.uuid4())

        # Handle photo upload
        photo_path = None
        if uploaded_photo is not None:
            # In a real application, you would save the photo to a file system
            photo_path = f"photos/{pet_name}_{owner_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{uploaded_photo.name.split('.')[-1]}"

        # Prepare data for database
        pet_data = (
            pet_name, species, breed or None, age if age > 0 else None, 
            weight if weight > 0 else None, color or None, owner_name, 
            owner_phone or None, owner_email or None, owner_address or None,
            microchip_id or None, qr_code, photo_path, medical_conditions or None
        )

        try:
            # Insert into database
            pet_id = self.db.insert_pet(pet_data)

            if pet_id:
                st.success(f"✅ {pet_name} has been successfully registered! Pet ID: {pet_id}")

                # Show QR code information
                st.info(f"🔗 QR Code Generated: {qr_code}")
                st.markdown("*Save this QR code for quick pet identification!*")

                # Optionally clear the form by rerunning
                st.balloons()

            else:
                st.error("❌ Registration failed. Please try again.")

        except Exception as e:
            if "UNIQUE constraint failed" in str(e):
                st.error("❌ This microchip ID is already registered to another pet.")
            else:
                st.error(f"❌ Registration failed: {str(e)}")

    def _show_existing_pets(self):
        """Display existing registered pets"""

        st.markdown("---")
        st.markdown("### 📋 Registered Pets")

        pets_df = self.db.get_all_pets()

        if pets_df.empty:
            st.info("🌟 No pets registered yet. Register your first pet above!")
            return

        # Search functionality
        search_term = st.text_input("🔍 Search pets by name, breed, or owner")

        if search_term:
            pets_df = self.db.search_pets(search_term)
            if pets_df.empty:
                st.warning(f"No pets found matching '{search_term}'")
                return

        # Display pets in a nice format
        for _, pet in pets_df.iterrows():
            with st.expander(
                f"🐕 {pet['name']} ({pet['species']}) - Owner: {pet['owner_name']}"
            ):
                col1, col2, col3 = st.columns(3)

                with col1:
                    st.markdown("**Pet Information:**")
                    st.write(f"**Name:** {pet['name']}")
                    st.write(f"**Species:** {pet['species']}")
                    st.write(f"**Breed:** {pet.get('breed', 'Not specified')}")
                    st.write(f"**Age:** {pet.get('age', 'Unknown')} years")
                    st.write(f"**Weight:** {pet.get('weight', 'Not recorded')} kg")
                    st.write(f"**Color:** {pet.get('color', 'Not specified')}")

                with col2:
                    st.markdown("**Owner Information:**")
                    st.write(f"**Name:** {pet['owner_name']}")
                    st.write(f"**Phone:** {pet.get('owner_phone', 'Not provided')}")
                    st.write(f"**Email:** {pet.get('owner_email', 'Not provided')}")
                    st.write(f"**Address:** {pet.get('owner_address', 'Not provided')}")

                with col3:
                    st.markdown("**Registration Details:**")
                    st.write(f"**Pet ID:** {pet['id']}")
                    st.write(f"**Registered:** {pet['registration_date'][:10] if pet['registration_date'] else 'Unknown'}")
                    st.write(f"**Microchip:** {pet.get('microchip_id', 'Not available')}")
                    st.write(f"**QR Code:** {pet.get('qr_code', 'Not generated')}")
                    st.write(f"**Status:** {'🚨 Lost' if pet.get('is_lost', 0) else '✅ Safe'}")

                if pet.get('medical_conditions'):
                    st.markdown(f"**Medical Conditions:** {pet['medical_conditions']}")

        # Summary statistics
        st.markdown("---")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total Registered Pets", len(pets_df))

        with col2:
            species_counts = pets_df['species'].value_counts()
            most_common_species = species_counts.index[0] if not species_counts.empty else "None"
            st.metric("Most Common Species", most_common_species)

        with col3:
            lost_count = pets_df['is_lost'].sum() if 'is_lost' in pets_df.columns else 0
            st.metric("Currently Lost", lost_count)
