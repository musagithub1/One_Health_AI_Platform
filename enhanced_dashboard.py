"""
Enhanced Dashboard Module for One Health AI Platform
Integrates AI services and provides advanced analytics and visualizations
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import random
from ai_services import ai_insights, health_prediction, breed_detection

class EnhancedDashboard:
    """Enhanced dashboard with AI-powered insights and analytics"""
    
    def __init__(self, database):
        self.db = database
        self.ai_insights_service = ai_insights

    def show_main_dashboard(self):
        """Display the main enhanced dashboard"""
        
        # AI-powered insights section
        st.markdown("### 🤖 AI-Powered Insights")
        
        col1, col2 = st.columns(2)
        
        with col1:
            self._show_ai_health_insights()
        
        with col2:
            self._show_ai_recovery_insights()
        
        # Real-time metrics
        st.markdown("### 📊 Real-Time Platform Metrics")
        self._show_realtime_metrics()
        
        # Advanced analytics
        st.markdown("### 📈 Advanced Analytics")
        self._show_advanced_analytics()
        
        # Predictive models section
        st.markdown("### 🔮 Predictive Analytics")
        self._show_predictive_analytics()

    def _show_ai_health_insights(self):
        """Display AI-generated health insights"""
        st.markdown("""
        <div class="metric-card">
            <h4>🏥 Health Intelligence</h4>
            <p><strong>Community Health Score:</strong> 8.7/10</p>
            <p><strong>Vaccination Compliance:</strong> 94.2%</p>
            <p><strong>At-Risk Pets Identified:</strong> 23</p>
            <p><strong>Health Alerts:</strong> 5 active</p>
            <div class="ai-badge">🤖 AI Analyzed</div>
        </div>
        """, unsafe_allow_html=True)

    def _show_ai_recovery_insights(self):
        """Display AI-generated recovery insights"""
        st.markdown("""
        <div class="metric-card">
            <h4>🔍 Recovery Intelligence</h4>
            <p><strong>AI Match Accuracy:</strong> 96.8%</p>
            <p><strong>Average Recovery Time:</strong> 2.3 days</p>
            <p><strong>Active Cases:</strong> 12</p>
            <p><strong>Success Rate (30d):</strong> 97.1%</p>
            <div class="ai-badge">🎯 AI Powered</div>
        </div>
        """, unsafe_allow_html=True)

    def _show_realtime_metrics(self):
        """Display real-time platform metrics"""
        
        # Generate sample real-time data
        col1, col2, col3, col4, col5 = st.columns(5)
        
        metrics = [
            ("👥 Active Users", "1,247", "+12%"),
            ("🐕 New Registrations", "89", "+8%"),
            ("🔍 Active Searches", "23", "+15%"),
            ("💊 Health Alerts", "5", "-20%"),
            ("📱 QR Scans", "156", "+25%")
        ]
        
        for i, (label, value, change) in enumerate(metrics):
            with [col1, col2, col3, col4, col5][i]:
                delta_color = "normal" if "+" in change else "inverse"
                st.metric(label, value, change, delta_color=delta_color)

    def _show_advanced_analytics(self):
        """Display advanced analytics with interactive charts"""
        
        tab1, tab2, tab3 = st.tabs(["📊 Population Analytics", "🏥 Health Trends", "🔍 Recovery Analytics"])
        
        with tab1:
            self._show_population_analytics()
        
        with tab2:
            self._show_health_trends()
        
        with tab3:
            self._show_recovery_analytics()

    def _show_population_analytics(self):
        """Show pet population analytics"""
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Species distribution
            species_data = {
                'Species': ['Dogs', 'Cats', 'Birds', 'Rabbits', 'Others'],
                'Count': [567, 423, 89, 67, 101],
                'Percentage': [45.4, 33.8, 7.1, 5.4, 8.1]
            }
            
            fig = px.pie(
                values=species_data['Count'], 
                names=species_data['Species'],
                title="Pet Species Distribution",
                color_discrete_sequence=['#667eea', '#764ba2', '#f093fb', '#ff6b6b', '#feca57']
            )
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Inter, sans-serif")
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Age distribution
            age_data = {
                'Age Group': ['0-1 years', '1-3 years', '3-7 years', '7+ years'],
                'Dogs': [89, 234, 189, 89],
                'Cats': [67, 156, 134, 78]
            }
            
            fig = go.Figure()
            fig.add_trace(go.Bar(name='Dogs', x=age_data['Age Group'], y=age_data['Dogs'], marker_color='#667eea'))
            fig.add_trace(go.Bar(name='Cats', x=age_data['Age Group'], y=age_data['Cats'], marker_color='#764ba2'))
            
            fig.update_layout(
                title="Age Distribution by Species",
                barmode='group',
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Inter, sans-serif")
            )
            st.plotly_chart(fig, use_container_width=True)

    def _show_health_trends(self):
        """Show health trend analytics"""
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Health score trends
            dates = pd.date_range(start='2024-01-01', periods=12, freq='M')
            health_scores = [8.2, 8.4, 8.1, 8.6, 8.3, 8.7, 8.5, 8.8, 8.4, 8.6, 8.9, 8.7]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=dates, 
                y=health_scores,
                mode='lines+markers',
                name='Average Health Score',
                line=dict(color='#10b981', width=3),
                fill='tonexty'
            ))
            
            fig.update_layout(
                title="Community Health Score Trends",
                yaxis=dict(range=[7.5, 9.5]),
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Inter, sans-serif")
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Common health issues
            health_issues = {
                'Condition': ['Dental Disease', 'Obesity', 'Allergies', 'Joint Issues', 'Heart Disease'],
                'Prevalence': [28.5, 23.1, 18.7, 15.2, 8.9],
                'Trend': ['↗️', '↘️', '➡️', '↗️', '↘️']
            }
            
            fig = px.bar(
                x=health_issues['Prevalence'],
                y=health_issues['Condition'],
                orientation='h',
                title="Most Common Health Issues",
                color=health_issues['Prevalence'],
                color_continuous_scale='Reds'
            )
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Inter, sans-serif")
            )
            st.plotly_chart(fig, use_container_width=True)

    def _show_recovery_analytics(self):
        """Show recovery analytics"""
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Recovery success rate over time
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            success_rates = [94.2, 96.1, 97.8, 95.5, 98.2, 97.1, 96.8, 98.5, 97.3, 96.9, 98.1, 97.7]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=months,
                y=success_rates,
                mode='lines+markers',
                name='Success Rate',
                line=dict(color='#667eea', width=3),
                fill='tonexty'
            ))
            
            fig.update_layout(
                title="Monthly Recovery Success Rate (%)",
                yaxis=dict(range=[90, 100]),
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Inter, sans-serif")
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Recovery time distribution
            recovery_times = {
                'Time Period': ['< 24 hours', '1-3 days', '4-7 days', '1-2 weeks', '> 2 weeks'],
                'Percentage': [35.2, 28.7, 21.3, 12.1, 2.7]
            }
            
            fig = px.pie(
                values=recovery_times['Percentage'],
                names=recovery_times['Time Period'],
                title="Recovery Time Distribution",
                color_discrete_sequence=['#10b981', '#34d399', '#6ee7b7', '#a7f3d0', '#d1fae5']
            )
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Inter, sans-serif")
            )
            st.plotly_chart(fig, use_container_width=True)

    def _show_predictive_analytics(self):
        """Show predictive analytics and forecasting"""
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🔮 Health Risk Predictions")
            
            # Risk prediction chart
            risk_categories = ['Obesity', 'Dental', 'Joint', 'Heart', 'Kidney']
            current_risk = [23.1, 28.5, 15.2, 8.9, 6.3]
            predicted_risk = [25.8, 26.2, 17.1, 9.5, 7.1]
            
            fig = go.Figure()
            fig.add_trace(go.Bar(
                name='Current Risk %',
                x=risk_categories,
                y=current_risk,
                marker_color='#667eea'
            ))
            fig.add_trace(go.Bar(
                name='Predicted Risk %',
                x=risk_categories,
                y=predicted_risk,
                marker_color='#ff6b6b'
            ))
            
            fig.update_layout(
                title="Health Risk Predictions (6 months)",
                barmode='group',
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Inter, sans-serif")
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("#### 📈 Platform Growth Forecast")
            
            # Growth prediction
            months = pd.date_range(start='2024-01-01', periods=18, freq='M')
            historical_users = [800, 850, 920, 980, 1050, 1120, 1200, 1280, 1350, 1420, 1500, 1580]
            predicted_users = [1650, 1720, 1800, 1880, 1960, 2050]
            
            fig = go.Figure()
            
            # Historical data
            fig.add_trace(go.Scatter(
                x=months[:12],
                y=historical_users,
                mode='lines+markers',
                name='Historical',
                line=dict(color='#667eea', width=3)
            ))
            
            # Predicted data
            fig.add_trace(go.Scatter(
                x=months[11:],
                y=[historical_users[-1]] + predicted_users,
                mode='lines+markers',
                name='Predicted',
                line=dict(color='#ff6b6b', width=3, dash='dash')
            ))
            
            fig.update_layout(
                title="User Growth Forecast",
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Inter, sans-serif")
            )
            st.plotly_chart(fig, use_container_width=True)

    def show_analytics(self):
        """Display comprehensive analytics dashboard"""
        
        # AI-generated insights
        st.markdown("### 🧠 AI-Generated Platform Insights")
        
        # Generate sample insights
        platform_data = {"sample": "data"}  # In real implementation, this would be actual platform data
        insights = self.ai_insights_service.generate_platform_insights(platform_data)
        
        # Display insights summary
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 📊 Key Performance Indicators")
            
            kpis = insights["insights"]["pet_population_analysis"]
            st.markdown(f"""
            <div class="metric-card">
                <h4>Population Analytics</h4>
                <p><strong>Total Pets:</strong> {kpis['total_pets']:,}</p>
                <p><strong>Growth Rate:</strong> {kpis['growth_rate']:.1f}%</p>
                <p><strong>Dogs:</strong> {kpis['species_distribution']['dogs']:.1f}%</p>
                <p><strong>Cats:</strong> {kpis['species_distribution']['cats']:.1f}%</p>
                <div class="ai-badge">📈 Analytics</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("#### 🏥 Health Analytics")
            
            health_data = insights["insights"]["health_trends"]
            st.markdown(f"""
            <div class="metric-card">
                <h4>Community Health</h4>
                <p><strong>Avg Health Score:</strong> {health_data['average_health_score']:.1f}/10</p>
                <p><strong>Vaccination Rate:</strong> {health_data['vaccination_compliance']:.1f}%</p>
                <p><strong>Preventive Care:</strong> {health_data['preventive_care_adoption']:.1f}%</p>
                <div class="ai-badge">🏥 Health AI</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Display recommendations
        st.markdown("#### 💡 AI Recommendations")
        
        recommendations = insights["recommendations"]
        for i, rec in enumerate(recommendations[:3]):
            priority_color = {
                "High": "#ff6b6b",
                "Medium": "#feca57",
                "Low": "#48cae4"
            }.get(rec["priority"], "#667eea")
            
            st.markdown(f"""
            <div class="enhancement-highlight" style="border-left: 4px solid {priority_color};">
                <strong>{rec['area']}:</strong> {rec['recommendation']}<br>
                <small><strong>Priority:</strong> {rec['priority']} | <strong>Impact:</strong> {rec['impact']}</small>
            </div>
            """, unsafe_allow_html=True)
        
        # Advanced charts
        self._show_advanced_analytics()

    def show_breed_analytics(self):
        """Display breed-specific analytics"""
        
        st.markdown("### 🐕 Breed Intelligence Dashboard")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Most popular breeds
            breeds = ['Golden Retriever', 'Labrador', 'German Shepherd', 'Persian', 'Maine Coon']
            counts = [156, 134, 98, 87, 76]
            
            fig = px.bar(
                x=counts,
                y=breeds,
                orientation='h',
                title="Most Popular Breeds",
                color=counts,
                color_continuous_scale='Blues'
            )
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Inter, sans-serif")
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Breed health scores
            breed_health = {
                'Breed': ['Mixed Breed', 'Golden Retriever', 'Labrador', 'German Shepherd', 'Persian'],
                'Health Score': [8.9, 8.7, 8.5, 8.2, 7.8],
                'Sample Size': [234, 156, 134, 98, 87]
            }
            
            fig = px.scatter(
                x=breed_health['Health Score'],
                y=breed_health['Breed'],
                size=breed_health['Sample Size'],
                title="Breed Health Scores",
                color=breed_health['Health Score'],
                color_continuous_scale='RdYlGn'
            )
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Inter, sans-serif")
            )
            st.plotly_chart(fig, use_container_width=True)

    def show_geographic_analytics(self):
        """Display geographic analytics"""
        
        st.markdown("### 🗺️ Geographic Intelligence")
        
        # Sample geographic data
        regions = ['Urban Core', 'Suburbs', 'Rural Areas', 'College Towns', 'Coastal Areas']
        registrations = [456, 789, 234, 167, 298]
        recovery_rates = [96.2, 97.8, 94.1, 98.5, 95.7]
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.bar(
                x=regions,
                y=registrations,
                title="Pet Registrations by Region",
                color=registrations,
                color_continuous_scale='Viridis'
            )
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Inter, sans-serif")
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = px.line(
                x=regions,
                y=recovery_rates,
                title="Recovery Rates by Region",
                markers=True
            )
            fig.update_traces(line_color='#667eea', line_width=3)
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Inter, sans-serif"),
                yaxis=dict(range=[90, 100])
            )
            st.plotly_chart(fig, use_container_width=True)

