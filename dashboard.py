import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

class Dashboard:
    def __init__(self, database):
        self.db = database

    def show_main_dashboard(self):
        """Display the main dashboard with key metrics and charts"""

        # Get statistics from database
        stats = self.db.get_statistics()

        # Display key metrics
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown(
                f'''
                <div class="metric-card">
                    <h3>🐾 Total Pets</h3>
                    <h1>{stats.get("total_pets", 0)}</h1>
                    <p>Registered in system</p>
                </div>
                ''', 
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f'''
                <div class="metric-card">
                    <h3>🚨 Lost Pets</h3>
                    <h1>{stats.get("lost_pets", 0)}</h1>
                    <p>Currently missing</p>
                </div>
                ''', 
                unsafe_allow_html=True
            )

        with col3:
            st.markdown(
                f'''
                <div class="metric-card">
                    <h3>📋 Medical Records</h3>
                    <h1>{stats.get("medical_records", 0)}</h1>
                    <p>Total health entries</p>
                </div>
                ''', 
                unsafe_allow_html=True
            )

        with col4:
            st.markdown(
                f'''
                <div class="metric-card">
                    <h3>📈 New This Month</h3>
                    <h1>{stats.get("recent_registrations", 0)}</h1>
                    <p>Recent registrations</p>
                </div>
                ''', 
                unsafe_allow_html=True
            )

        st.markdown("<br>", unsafe_allow_html=True)

        # Show recent pets if any exist
        pets_df = self.db.get_all_pets()
        if not pets_df.empty:
            st.subheader("📊 Recent Pet Registrations")

            # Show recent pets in a nice format
            recent_pets = pets_df.head(5)
            for _, pet in recent_pets.iterrows():
                with st.expander(f"🐕 {pet['name']} - {pet['species']} ({pet.get('breed', 'Unknown breed')})"):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"**Owner:** {pet['owner_name']}")
                        st.write(f"**Age:** {pet.get('age', 'Unknown')} years")
                        st.write(f"**Color:** {pet.get('color', 'Not specified')}")
                    with col2:
                        st.write(f"**Phone:** {pet.get('owner_phone', 'Not provided')}")
                        st.write(f"**Registered:** {pet['registration_date'][:10] if pet['registration_date'] else 'Unknown'}")
                        st.write(f"**Status:** {'🚨 Lost' if pet.get('is_lost', 0) else '✅ Safe'}")

        else:
            st.info("🌟 No pets registered yet. Start by registering your first pet!")

        # Quick actions
        st.subheader("⚡ Quick Actions")
        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("📝 Register New Pet", use_container_width=True):
                st.session_state['page'] = "📝 Pet Registration"
                st.rerun()

        with col2:
            if st.button("🔍 Report Lost Pet", use_container_width=True):
                st.session_state['page'] = "🔍 Lost Pet Recovery"
                st.rerun()

        with col3:
            if st.button("🏥 Add Medical Record", use_container_width=True):
                st.session_state['page'] = "🏥 Medical Records"
                st.rerun()

    def show_analytics(self):
        """Display detailed analytics and charts"""

        pets_df = self.db.get_all_pets()

        if pets_df.empty:
            st.warning("📊 No data available for analytics. Please register some pets first!")
            return

        # Species distribution
        st.subheader("📈 Pet Species Distribution")
        species_counts = pets_df['species'].value_counts()

        if not species_counts.empty:
            fig_pie = px.pie(
                values=species_counts.values, 
                names=species_counts.index, 
                title="Distribution of Pet Species",
                color_discrete_sequence=['#667eea', '#764ba2', '#f093fb', '#f5576c', '#4facfe']
            )
            st.plotly_chart(fig_pie, use_container_width=True)

        # Registration trends
        st.subheader("📅 Registration Trends")

        # Convert registration dates and create monthly counts
        pets_df['reg_date'] = pd.to_datetime(pets_df['registration_date'], errors='coerce')
        pets_df['reg_month'] = pets_df['reg_date'].dt.to_period('M').astype(str)

        monthly_registrations = pets_df.groupby('reg_month').size().reset_index(name='count')

        if not monthly_registrations.empty:
            fig_line = px.line(
                monthly_registrations, 
                x='reg_month', 
                y='count',
                title="Monthly Pet Registrations",
                markers=True
            )
            fig_line.update_layout(xaxis_title="Month", yaxis_title="Number of Registrations")
            st.plotly_chart(fig_line, use_container_width=True)

        # Breed popularity (if breeds are available)
        if 'breed' in pets_df.columns:
            breed_counts = pets_df['breed'].value_counts().head(10)
            if not breed_counts.empty:
                st.subheader("🐕 Top Pet Breeds")
                fig_bar = px.bar(
                    x=breed_counts.index, 
                    y=breed_counts.values,
                    title="Most Popular Pet Breeds",
                    labels={'x': 'Breed', 'y': 'Number of Pets'}
                )
                st.plotly_chart(fig_bar, use_container_width=True)

        # Lost pets status
        st.subheader("🚨 Pet Safety Status")
        lost_status = pets_df['is_lost'].value_counts()
        status_labels = {0: 'Safe', 1: 'Lost'}

        fig_status = go.Figure(data=[
            go.Bar(
                x=[status_labels.get(idx, f'Status {idx}') for idx in lost_status.index],
                y=lost_status.values,
                marker_color=['#00CC96', '#FF6B6B']
            )
        ])
        fig_status.update_layout(
            title="Pet Safety Overview",
            xaxis_title="Status",
            yaxis_title="Number of Pets"
        )
        st.plotly_chart(fig_status, use_container_width=True)