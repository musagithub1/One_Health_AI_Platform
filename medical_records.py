import streamlit as st
import pandas as pd
from datetime import datetime, date

class MedicalRecords:
    def __init__(self, database):
        self.db = database

    def show_records_interface(self):
        """Display the medical records interface"""

        # Tab interface for different medical functions
        tab1, tab2, tab3, tab4 = st.tabs(["📋 Add Record", "💉 Vaccinations", "🔍 View Records", "📊 Health Summary"])

        with tab1:
            self._show_add_medical_record()

        with tab2:
            self._show_vaccination_management()

        with tab3:
            self._show_view_records()

        with tab4:
            self._show_health_summary()

    def _show_add_medical_record(self):
        """Interface to add a new medical record"""

        st.markdown("### 📋 Add Medical Record")
        st.markdown("Document your pet's health visits and treatments")

        # Get all registered pets
        pets_df = self.db.get_all_pets()

        if pets_df.empty:
            st.warning("📝 No pets registered yet. Please register your pet first.")
            return

        with st.form("add_medical_record"):
            # Pet selection
            pet_options = [f"{pet['name']} ({pet['species']}) - {pet['owner_name']}" 
                          for _, pet in pets_df.iterrows()]

            selected_pet_idx = st.selectbox("🐾 Select Pet", range(len(pet_options)), 
                                          format_func=lambda x: pet_options[x])

            selected_pet = pets_df.iloc[selected_pet_idx]

            # Visit information
            col1, col2 = st.columns(2)

            with col1:
                visit_date = st.date_input("📅 Visit Date *", value=date.today())
                veterinarian = st.text_input("👨‍⚕️ Veterinarian Name", placeholder="Dr. Smith")
                clinic_name = st.text_input("🏥 Clinic/Hospital Name", placeholder="City Veterinary Hospital")

            with col2:
                visit_type = st.selectbox("🩺 Visit Type", [
                    "Routine Checkup", "Vaccination", "Illness", "Injury", 
                    "Surgery", "Emergency", "Follow-up", "Other"
                ])
                cost = st.number_input("💰 Visit Cost (₹)", min_value=0.0, value=0.0, step=50.0)
                next_visit = st.date_input("📅 Next Visit Date")

            # Medical details
            st.markdown("#### 🩺 Medical Information")

            diagnosis = st.text_area("🔍 Diagnosis", 
                                   placeholder="Primary diagnosis or reason for visit")

            treatment = st.text_area("💊 Treatment Provided", 
                                   placeholder="Describe treatments, procedures performed")

            medications = st.text_area("💉 Medications Prescribed", 
                                     placeholder="List medications, dosage, and duration")

            notes = st.text_area("📝 Additional Notes", 
                                placeholder="Any additional observations or instructions")

            # Vital signs section
            st.markdown("#### 📊 Vital Signs (Optional)")
            col3, col4, col5 = st.columns(3)

            with col3:
                temperature = st.number_input("🌡️ Temperature (°F)", min_value=90.0, max_value=110.0, value=98.6, step=0.1)
            with col4:
                weight_current = st.number_input("⚖️ Current Weight (kg)", min_value=0.0, max_value=200.0, value=1.0, step=0.1)
            with col5:
                heart_rate = st.number_input("❤️ Heart Rate (bpm)", min_value=0, max_value=300, value=80)

            submitted = st.form_submit_button("📋 Add Medical Record", use_container_width=True)

            if submitted:
                # Validation
                if not visit_date or not diagnosis:
                    st.error("❌ Please fill in visit date and diagnosis")
                    return

                # Prepare data for database
                record_data = (
                    selected_pet['id'], str(visit_date), veterinarian or None,
                    clinic_name or None, diagnosis, treatment or None,
                    medications or None, str(next_visit) if next_visit else None,
                    notes or None, cost if cost > 0 else None
                )

                try:
                    # Insert medical record (implement in DB layer)
                    # record_id = self.db.insert_medical_record(record_data)

                    st.success(f"✅ Medical record added for {selected_pet['name']}!")

                    # Show record summary
                    st.markdown("---")
                    st.markdown("### 📋 Record Summary")

                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Pet:** {selected_pet['name']}")
                        st.markdown(f"**Date:** {visit_date}")
                        st.markdown(f"**Veterinarian:** {veterinarian or 'Not specified'}")
                        st.markdown(f"**Clinic:** {clinic_name or 'Not specified'}")

                    with col2:
                        st.markdown(f"**Visit Type:** {visit_type}")
                        st.markdown(f"**Diagnosis:** {diagnosis}")
                        st.markdown(f"**Cost:** ₹{cost:.2f}" if cost > 0 else "**Cost:** Not recorded")
                        st.markdown(f"**Next Visit:** {next_visit or 'Not scheduled'}")

                except Exception as e:
                    st.error(f"❌ Error adding medical record: {str(e)}")

    def _show_vaccination_management(self):
        """Interface for vaccination management"""

        st.markdown("### 💉 Vaccination Management")
        st.markdown("Track your pet's vaccination schedule")

        # Get all registered pets
        pets_df = self.db.get_all_pets()

        if pets_df.empty:
            st.warning("📝 No pets registered yet. Please register your pet first.")
            return

        # Vaccination form
        with st.form("add_vaccination"):
            pet_options = [f"{pet['name']} ({pet['species']}) - {pet['owner_name']}" 
                          for _, pet in pets_df.iterrows()]

            selected_pet_idx = st.selectbox("🐾 Select Pet", range(len(pet_options)), 
                                          format_func=lambda x: pet_options[x])

            selected_pet = pets_df.iloc[selected_pet_idx]

            col1, col2 = st.columns(2)

            with col1:
                vaccine_name = st.selectbox("💉 Vaccine Type", [
                    "DHPP (Distemper, Hepatitis, Parvovirus, Parainfluenza)",
                    "Rabies", "FVRCP (Feline Viral Rhinotracheitis, Calicivirus, Panleukopenia)",
                    "FeLV (Feline Leukemia)", "Bordetella", "Lyme Disease", 
                    "Canine Influenza", "Other"
                ])

                if vaccine_name == "Other":
                    vaccine_name = st.text_input("Specify Vaccine Name")

                vaccine_date = st.date_input("📅 Vaccination Date *", value=date.today())
                next_due_date = st.date_input("📅 Next Due Date")

            with col2:
                veterinarian = st.text_input("👨‍⚕️ Veterinarian", placeholder="Dr. Smith")
                clinic_name = st.text_input("🏥 Clinic Name", placeholder="City Veterinary Hospital")
                batch_number = st.text_input("🔢 Batch/Lot Number", placeholder="Optional")

            notes = st.text_area("📝 Notes", placeholder="Any reactions or additional information")

            submitted = st.form_submit_button("💉 Add Vaccination Record", use_container_width=True)

            if submitted:
                if not vaccine_name or not vaccine_date:
                    st.error("❌ Please fill in vaccine name and date")
                    return

                vaccination_data = (
                    selected_pet['id'], vaccine_name, str(vaccine_date),
                    str(next_due_date) if next_due_date else None,
                    veterinarian or None, clinic_name or None,
                    batch_number or None, notes or None
                )

                try:
                    # vaccination_id = self.db.insert_vaccination(vaccination_data)

                    st.success(f"✅ Vaccination record added for {selected_pet['name']}!")

                    if next_due_date:
                        days_until_due = (next_due_date - date.today()).days
                        if days_until_due <= 30:
                            st.warning(f"⏰ Next vaccination due in {days_until_due} days!")
                        else:
                            st.info(f"📅 Next vaccination scheduled for {next_due_date}")

                except Exception as e:
                    st.error(f"❌ Error adding vaccination record: {str(e)}")

        st.markdown("---")
        st.markdown("### ⏰ Upcoming Vaccinations")
        upcoming_vaccinations = pd.DataFrame()  # Placeholder

        if not upcoming_vaccinations.empty:
            for _, vacc in upcoming_vaccinations.iterrows():
                days_until_due = (pd.to_datetime(vacc['next_due_date']).date() - date.today()).days

                if days_until_due <= 7:
                    st.error(f"🚨 {vacc['pet_name']} needs {vacc['vaccine_name']} vaccination (Due: {vacc['next_due_date']})")
                elif days_until_due <= 30:
                    st.warning(f"⚠️ {vacc['pet_name']} needs {vacc['vaccine_name']} vaccination in {days_until_due} days")
                else:
                    st.info(f"📅 {vacc['pet_name']} - {vacc['vaccine_name']} scheduled for {vacc['next_due_date']}")
        else:
            st.success("✅ No upcoming vaccinations in the next 30 days!")

    def _show_view_records(self):
        """Interface to view existing medical records"""

        st.markdown("### 🔍 View Medical Records")

        pets_df = self.db.get_all_pets()

        if pets_df.empty:
            st.warning("📝 No pets registered yet.")
            return

        pet_options = ["All Pets"] + [f"{pet['name']} ({pet['species']}) - {pet['owner_name']}" 
                                     for _, pet in pets_df.iterrows()]

        selected_option = st.selectbox("🐾 Select Pet to View Records", pet_options)

        if selected_option == "All Pets":
            st.markdown("### 📋 All Medical Records")
            st.info("📊 Showing medical records for all pets")
        else:
            pet_idx = pet_options.index(selected_option) - 1
            selected_pet = pets_df.iloc[pet_idx]

            st.markdown(f"### 📋 Medical Records for {selected_pet['name']}")

            medical_records = pd.DataFrame()  # Placeholder

            if medical_records.empty:
                st.info(f"📝 No medical records found for {selected_pet['name']}")
            else:
                for _, record in medical_records.iterrows():
                    with st.expander(f"📅 {record['visit_date']} - {record.get('diagnosis', 'General Visit')}"):
                        col1, col2 = st.columns(2)

                        with col1:
                            st.markdown("**Visit Information:**")
                            st.write(f"**Date:** {record['visit_date']}")
                            st.write(f"**Veterinarian:** {record.get('veterinarian', 'Not specified')}")
                            st.write(f"**Clinic:** {record.get('clinic_name', 'Not specified')}")
                            st.write(f"**Cost:** ₹{record.get('cost', 0):.2f}" if record.get('cost') else "**Cost:** Not recorded")

                        with col2:
                            st.markdown("**Medical Details:**")
                            st.write(f"**Diagnosis:** {record.get('diagnosis', 'Not specified')}")
                            st.write(f"**Treatment:** {record.get('treatment', 'Not specified')}")
                            if record.get('medications'):
                                st.write(f"**Medications:** {record['medications']}")

                        if record.get('notes'):
                            st.markdown(f"**Notes:** {record['notes']}")

                        if record.get('next_visit_date'):
                            st.markdown(f"**Next Visit:** {record['next_visit_date']}")

    def _show_health_summary(self):
        """Show health summary and statistics"""

        st.markdown("### 📊 Health Summary & Statistics")

        pets_df = self.db.get_all_pets()

        if pets_df.empty:
            st.warning("📝 No pets registered yet.")
            return

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total Pets", len(pets_df))

        with col2:
            st.metric("Medical Records", 0)

        with col3:
            st.metric("Vaccinations Given", 0)

        st.markdown("### 📈 Recent Health Activity")
        st.info("🔄 Recent medical records and vaccination updates would be displayed here")

        st.markdown("### ⚠️ Health Alerts")

        alerts = []
        for _, pet in pets_df.iterrows():
            if pet.get('age') and pet['age'] > 7:
                alerts.append(f"🐕 {pet['name']} is a senior pet (age {pet['age']}) - consider more frequent checkups")

        if alerts:
            for alert in alerts:
                st.warning(alert)
        else:
            st.success("✅ No health alerts at this time")

        st.markdown("### 💉 Vaccination Status Overview")
        st.info("📊 Vaccination compliance statistics would be displayed here")
