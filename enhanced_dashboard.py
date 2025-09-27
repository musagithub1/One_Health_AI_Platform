"""
Enhanced Dashboard Module for One Health AI Platform
Integrates AI services and provides advanced analytics and visualizations
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

# Mock AI services to replace the missing imports
class MockAIServices:
    """Mock AI services for demonstration"""
    
    @staticmethod
    def generate_platform_insights(data):
        return {
            "insights": {
                "pet_population_analysis": {
                    "total_pets": 1247,
                    "growth_rate": 12.5,
                    "species_distribution": {
                        "dogs": 45.4,
                        "cats": 33.8
                    }
                },
                "health_trends": {
                    "average_health_score": 8.7,
                    "vaccination_compliance": 94.2,
                    "preventive_care_adoption": 78.5
                }
            },
            "recommendations": [
                {
                    "area": "Vaccination",
                    "recommendation": "Increase vaccination campaigns in suburban areas",
                    "priority": "High",
                    "impact": "15% improvement"
                },
                {
                    "area": "Recovery",
                    "recommendation": "Implement AI-based recovery alerts",
                    "priority": "Medium",
                    "impact": "10% faster recovery"
                },
                {
                    "area": "Health",
                    "recommendation": "Introduce preventive care packages",
                    "priority": "High",
                    "impact": "20% better health scores"
                }
            ]
        }

# Initialize mock services
ai_insights = MockAIServices()
health_prediction = MockAIServices()
breed_detection = MockAIServices()

class EnhancedDashboard:
    """Enhanced dashboard with AI-powered insights and analytics"""
    
    def __init__(self, database=None):
        self.db = database
        self.ai_insights_service = ai_insights
        self._setup_custom_css()

    def _setup_custom_css(self):
        """Setup custom CSS for better text visibility and styling - IMPROVED VERSION"""
        st.markdown("""
        <style>
        /* FIXED METRIC CARD - ENSURED WHITE TEXT */
        .metric-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            padding: 20px;
            border-radius: 15px;
            color: #ffffff !important;
            margin: 10px 0;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        .metric-card h4 {
            color: #ffffff !important;
            font-weight: 700 !important;
            margin-bottom: 15px;
            font-size: 1.2em;
            text-shadow: 0 1px 2px rgba(0,0,0,0.2) !important;
        }
        
        .metric-card p {
            color: #ffffff !important;
            margin: 8px 0;
            font-size: 0.95em;
            text-shadow: 0 1px 2px rgba(0,0,0,0.1) !important;
        }
        
        .metric-card strong {
            color: #ffffff !important;
            font-weight: 600 !important;
        }
        
        /* FIXED AI BADGE - ENSURED WHITE TEXT */
        .ai-badge {
            background: rgba(255, 255, 255, 0.2) !important;
            padding: 5px 10px;
            border-radius: 20px;
            font-size: 0.8em;
            margin-top: 10px;
            display: inline-block;
            backdrop-filter: blur(10px);
            color: #ffffff !important;
            font-weight: 600 !important;
            text-shadow: 0 1px 2px rgba(0,0,0,0.2) !important;
        }
        
        /* FIXED ENHANCEMENT HIGHLIGHT - ENSURED WHITE TEXT */
        .enhancement-highlight {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%) !important;
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;
            color: #ffffff !important;
            border-left: 4px solid #ff6b6b;
        }
        
        .enhancement-highlight strong {
            color: #ffffff !important;
            font-weight: 600 !important;
            text-shadow: 0 1px 2px rgba(0,0,0,0.2) !important;
        }
        
        .enhancement-highlight small {
            color: #ffffff !important;
            text-shadow: 0 1px 2px rgba(0,0,0,0.1) !important;
        }
        
        /* Improve plotly chart text visibility */
        .js-plotly-plot .plotly .main-svg {
            background-color: transparent !important;
        }
        
        .js-plotly-plot .plotly .xtitle, .js-plotly-plot .plotly .ytitle {
            font-weight: 600 !important;
            font-size: 14px !important;
            color: #2c3e50 !important;
        }
        
        /* FIXED METRIC COMPONENT STYLING */
        .stMetric {
            background: rgba(102, 126, 234, 0.1) !important;
            padding: 15px;
            border-radius: 10px;
            border-left: 4px solid #667eea;
        }

        .stMetric label {
            color: #2d3748 !important;
            font-weight: 600 !important;
        }

        .stMetric div {
            color: #2d3748 !important;
        }

        .stMetric [data-testid="metric-container"] {
            color: #2d3748 !important;
        }

        .stMetric [data-testid="metric-container"] > div {
            color: #2d3748 !important;
        }
        
        /* FIXED TAB STYLING - IMPROVED TEXT VISIBILITY */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
        }
        
        .stTabs [data-baseweb="tab"] {
            background: rgba(102, 126, 234, 0.1) !important;
            border-radius: 8px 8px 0 0;
            padding: 10px 20px;
            border: 1px solid rgba(102, 126, 234, 0.2);
            color: #4a5568 !important;
            font-weight: 500 !important;
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            color: #ffffff !important;
            font-weight: 600 !important;
            text-shadow: 0 1px 2px rgba(0,0,0,0.2) !important;
        }

        .stTabs [aria-selected="true"] span {
            color: #ffffff !important;
        }

        .stTabs [aria-selected="true"] div {
            color: #ffffff !important;
        }
        
        /* Column spacing */
        .block-container {
            padding-top: 2rem;
            color: #2d3748 !important;
        }

        /* COMPREHENSIVE TEXT VISIBILITY FIXES */
        
        /* Ensure all regular text is dark for readability */
        h1, h2, h3, h4, h5, h6 {
            color: #1a202c !important;
        }
        
        p, div, span, label {
            color: #2d3748 !important;
        }
        
        .stMarkdown {
            color: #2d3748 !important;
        }
        
        .stMarkdown p {
            color: #2d3748 !important;
        }
        
        .stMarkdown div {
            color: #2d3748 !important;
        }

        /* FIXED BUTTON STYLES - IMPROVED TEXT VISIBILITY */
        .stButton > button {
            width: 100%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            color: #ffffff !important;
            border: none !important;
            padding: 0.75rem 1.5rem;
            border-radius: 12px;
            font-weight: 600 !important;
            font-size: 1rem !important;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
            text-shadow: 0 1px 2px rgba(0,0,0,0.2) !important;
        }

        .stButton > button:hover {
            background: linear-gradient(135deg, #764ba2 0%, #667eea 100%) !important;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
            color: #ffffff !important;
            text-shadow: 0 1px 2px rgba(0,0,0,0.3) !important;
        }

        .stButton > button:focus {
            color: #ffffff !important;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            text-shadow: 0 1px 2px rgba(0,0,0,0.2) !important;
        }

        .stButton > button:active {
            color: #ffffff !important;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            text-shadow: 0 1px 2px rgba(0,0,0,0.2) !important;
        }

        /* FIXED SELECTBOX STYLES */
        .stSelectbox > div > div {
            background: white !important;
            border-radius: 12px;
            border: 2px solid #e2e8f0;
            transition: all 0.3s ease;
            color: #2d3748 !important;
        }
        
        .stSelectbox > div > div:focus-within {
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }

        /* FIXED SELECTBOX TEXT COLOR */
        .stSelectbox div[data-baseweb="select"] > div {
            color: #2d3748 !important;
        }

        .stSelectbox div[data-baseweb="select"] span {
            color: #2d3748 !important;
        }

        .stSelectbox div[data-baseweb="select"] div[role="button"] {
            color: #2d3748 !important;
        }

        /* Input field text color - ENHANCED */
        .stTextInput input, .stTextArea textarea {
            color: #2d3748 !important;
            background-color: #ffffff !important;
        }
        
        .stNumberInput input {
            color: #2d3748 !important;
            background-color: #ffffff !important;
        }
        
        .stDateInput input {
            color: #2d3748 !important;
            background-color: #ffffff !important;
        }
        
        .stTimeInput input {
            color: #2d3748 !important;
            background-color: #ffffff !important;
        }

        /* File uploader text */
        .stFileUploader label {
            color: #2d3748 !important;
        }

        .stFileUploader div {
            color: #2d3748 !important;
        }

        .stFileUploader span {
            color: #2d3748 !important;
        }
        
        /* Data editor text */
        .stDataEditor {
            color: #2d3748 !important;
        }
        
        /* Expander text */
        .streamlit-expanderHeader {
            color: #2d3748 !important;
            font-weight: 600;
        }
        
        /* Success, warning, error messages */
        .stAlert {
            color: #2d3748 !important;
        }

        .stAlert div {
            color: #2d3748 !important;
        }

        .stAlert span {
            color: #2d3748 !important;
        }
        
        /* Code blocks */
        .stCodeBlock {
            color: #2d3748 !important;
        }
        
        /* Streamlit default text elements - COMPREHENSIVE */
        .stText, .stMarkdown, .stWrite {
            color: #2d3748 !important;
        }

        .stText div, .stMarkdown div, .stWrite div {
            color: #2d3748 !important;
        }

        .stText p, .stMarkdown p, .stWrite p {
            color: #2d3748 !important;
        }

        .stText span, .stMarkdown span, .stWrite span {
            color: #2d3748 !important;
        }
        
        /* Ensure all Streamlit text is visible */
        .element-container {
            color: #2d3748 !important;
        }

        .element-container div {
            color: #2d3748 !important;
        }

        .element-container p {
            color: #2d3748 !important;
        }

        .element-container span {
            color: #2d3748 !important;
        }

        /* ADDITIONAL FIXES FOR SPECIFIC STREAMLIT COMPONENTS */
        
        /* Radio button text */
        .stRadio label {
            color: #2d3748 !important;
        }

        .stRadio div {
            color: #2d3748 !important;
        }

        /* Checkbox text */
        .stCheckbox label {
            color: #2d3748 !important;
        }

        .stCheckbox div {
            color: #2d3748 !important;
        }

        /* Slider text */
        .stSlider label {
            color: #2d3748 !important;
        }

        .stSlider div {
            color: #2d3748 !important;
        }

        /* Progress bar text */
        .stProgress div {
            color: #2d3748 !important;
        }

        /* Caption text */
        .stCaption {
            color: #4a5568 !important;
        }

        /* Form labels */
        .stForm label {
            color: #2d3748 !important;
        }

        .stForm div {
            color: #2d3748 !important;
        }

        /* Dataframe text */
        .stDataFrame {
            color: #2d3748 !important;
        }

        /* JSON text */
        .stJson {
            color: #2d3748 !important;
        }

        /* OVERRIDE ANY REMAINING TEXT COLOR ISSUES */
        * {
            color: inherit !important;
        }

        /* But ensure specific elements maintain their intended white colors */
        .metric-card, .metric-card *,
        .ai-badge, .ai-badge *,
        .enhancement-highlight, .enhancement-highlight *,
        .stTabs [aria-selected="true"], .stTabs [aria-selected="true"] *,
        .stButton > button, .stButton > button *,
        div[style*="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%)"], 
        div[style*="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%)"] *,
        div[style*="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%)"], 
        div[style*="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%)"] * {
            color: #ffffff !important;
        }

        /* Ensure dark text for light backgrounds */
        .main .block-container, .main .block-container *,
        .element-container, .element-container *,
        .stMetric, .stMetric * {
            color: #2d3748 !important;
        }

        /* Exception for elements that should be white on colored backgrounds */
        .metric-card *, 
        .ai-badge *,
        .enhancement-highlight *,
        .stTabs [aria-selected="true"] *,
        .stButton > button *,
        div[style*="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%)"] *,
        div[style*="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%)"] * {
            color: #ffffff !important;
        }
        
        </style>
        """, unsafe_allow_html=True)

    def show_main_dashboard(self):
        """Display the main enhanced dashboard"""
        
        # Header with platform status
        st.markdown("""
        <div style='text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    border-radius: 15px; color: white; margin-bottom: 30px;'>
            <h1 style='color: white; margin: 0;'>🐾 One Health AI Dashboard</h1>
            <p style='color: rgba(255,255,255,0.9); margin: 5px 0 0 0; font-size: 1.1em;'>
                Real-time AI-powered pet health and recovery analytics
            </p>
        </div>
        """, unsafe_allow_html=True)
        
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
                'Count': [567, 423, 89, 67, 101]
            }
            
            fig = px.pie(
                values=species_data['Count'], 
                names=species_data['Species'],
                title="Pet Species Distribution",
                color_discrete_sequence=['#667eea', '#764ba2', '#f093fb', '#ff6b6b', '#feca57']
            )
            fig.update_layout(
                plot_bgcolor='rgba(255,255,255,1)',
                paper_bgcolor='rgba(255,255,255,1)',
                font=dict(family="Arial, sans-serif", size=12, color='#2c3e50'),
                title_font=dict(size=16, color='#2c3e50', family="Arial, sans-serif"),
                legend=dict(font=dict(size=10, color='#2c3e50'))
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
                plot_bgcolor='rgba(255,255,255,1)',
                paper_bgcolor='rgba(255,255,255,1)',
                font=dict(family="Arial, sans-serif", size=12, color='#2c3e50'),
                title_font=dict(size=16, color='#2c3e50', family="Arial, sans-serif")
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
                line=dict(color='#10b981', width=3)
            ))
            
            fig.update_layout(
                title="Community Health Score Trends",
                yaxis=dict(range=[7.5, 9.5]),
                plot_bgcolor='rgba(255,255,255,1)',
                paper_bgcolor='rgba(255,255,255,1)',
                font=dict(family="Arial, sans-serif", size=12, color='#2c3e50'),
                title_font=dict(size=16, color='#2c3e50', family="Arial, sans-serif")
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Common health issues
            health_issues = {
                'Condition': ['Dental Disease', 'Obesity', 'Allergies', 'Joint Issues', 'Heart Disease'],
                'Prevalence': [28.5, 23.1, 18.7, 15.2, 8.9]
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
                plot_bgcolor='rgba(255,255,255,1)',
                paper_bgcolor='rgba(255,255,255,1)',
                font=dict(family="Arial, sans-serif", size=12, color='#2c3e50'),
                title_font=dict(size=16, color='#2c3e50', family="Arial, sans-serif")
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
                line=dict(color='#667eea', width=3)
            ))
            
            fig.update_layout(
                title="Monthly Recovery Success Rate (%)",
                yaxis=dict(range=[90, 100]),
                plot_bgcolor='rgba(255,255,255,1)',
                paper_bgcolor='rgba(255,255,255,1)',
                font=dict(family="Arial, sans-serif", size=12, color='#2c3e50'),
                title_font=dict(size=16, color='#2c3e50', family="Arial, sans-serif")
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
                plot_bgcolor='rgba(255,255,255,1)',
                paper_bgcolor='rgba(255,255,255,1)',
                font=dict(family="Arial, sans-serif", size=12, color='#2c3e50'),
                title_font=dict(size=16, color='#2c3e50', family="Arial, sans-serif")
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
                plot_bgcolor='rgba(255,255,255,1)',
                paper_bgcolor='rgba(255,255,255,1)',
                font=dict(family="Arial, sans-serif", size=12, color='#2c3e50'),
                title_font=dict(size=16, color='#2c3e50', family="Arial, sans-serif")
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("#### 📈 Registration Forecast")
            
            # Registration forecast
            future_months = ['Jan 2025', 'Feb 2025', 'Mar 2025', 'Apr 2025', 'May 2025', 'Jun 2025']
            historical = [89, 94, 87, 102, 98, 105]
            forecast = [108, 112, 115, 119, 123, 127]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=future_months,
                y=historical,
                mode='lines+markers',
                name='Historical',
                line=dict(color='#667eea', width=3)
            ))
            fig.add_trace(go.Scatter(
                x=future_months,
                y=forecast,
                mode='lines+markers',
                name='Forecast',
                line=dict(color='#ff6b6b', width=3, dash='dash')
            ))
            
            fig.update_layout(
                title="Pet Registration Forecast",
                plot_bgcolor='rgba(255,255,255,1)',
                paper_bgcolor='rgba(255,255,255,1)',
                font=dict(family="Arial, sans-serif", size=12, color='#2c3e50'),
                title_font=dict(size=16, color='#2c3e50', family="Arial, sans-serif")
            )
            st.plotly_chart(fig, use_container_width=True)

    def show_analytics(self):
        """Show comprehensive analytics dashboard"""
        
        st.markdown("## 📊 Comprehensive Analytics Dashboard")
        
        # Key performance indicators
        st.markdown("### 🎯 Key Performance Indicators")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                label="Total Registered Pets",
                value="1,247",
                delta="89 this month",
                delta_color="normal"
            )
        
        with col2:
            st.metric(
                label="Recovery Success Rate",
                value="97.1%",
                delta="2.3% improvement",
                delta_color="normal"
            )
        
        with col3:
            st.metric(
                label="Average Health Score",
                value="8.7/10",
                delta="0.3 increase",
                delta_color="normal"
            )
        
        with col4:
            st.metric(
                label="Active Veterinarians",
                value="156",
                delta="12 new partners",
                delta_color="normal"
            )

        # Geographic distribution
        st.markdown("### 🗺️ Geographic Distribution")
        
        # Sample geographic data
        geo_data = {
            'Region': ['North', 'South', 'East', 'West', 'Central'],
            'Registered Pets': [234, 189, 298, 267, 259],
            'Recovery Rate': [96.2, 97.8, 98.1, 95.9, 97.3]
        }
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.bar(
                x=geo_data['Region'],
                y=geo_data['Registered Pets'],
                title="Registered Pets by Region",
                color=geo_data['Registered Pets'],
                color_continuous_scale='Blues'
            )
            fig.update_layout(
                plot_bgcolor='rgba(255,255,255,1)',
                paper_bgcolor='rgba(255,255,255,1)',
                font=dict(family="Arial, sans-serif", size=12, color='#2c3e50'),
                title_font=dict(size=16, color='#2c3e50', family="Arial, sans-serif")
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = px.bar(
                x=geo_data['Region'],
                y=geo_data['Recovery Rate'],
                title="Recovery Rate by Region (%)",
                color=geo_data['Recovery Rate'],
                color_continuous_scale='Greens'
            )
            fig.update_layout(
                plot_bgcolor='rgba(255,255,255,1)',
                paper_bgcolor='rgba(255,255,255,1)',
                font=dict(family="Arial, sans-serif", size=12, color='#2c3e50'),
                title_font=dict(size=16, color='#2c3e50', family="Arial, sans-serif"),
                yaxis=dict(range=[94, 100])
            )
            st.plotly_chart(fig, use_container_width=True)

        # AI insights and recommendations
        st.markdown("### 🤖 AI-Generated Insights & Recommendations")
        
        insights_data = self.ai_insights_service.generate_platform_insights({})
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 📈 Platform Insights")
            insights = insights_data['insights']
            
            st.markdown(f"""
            <div class="enhancement-highlight">
                <strong>🐾 Pet Population Analysis</strong><br>
                <small>Total pets: {insights['pet_population_analysis']['total_pets']:,}</small><br>
                <small>Growth rate: {insights['pet_population_analysis']['growth_rate']}%</small><br>
                <small>Dogs: {insights['pet_population_analysis']['species_distribution']['dogs']}%</small><br>
                <small>Cats: {insights['pet_population_analysis']['species_distribution']['cats']}%</small>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="enhancement-highlight">
                <strong>🏥 Health Trends</strong><br>
                <small>Avg health score: {insights['health_trends']['average_health_score']}/10</small><br>
                <small>Vaccination compliance: {insights['health_trends']['vaccination_compliance']}%</small><br>
                <small>Preventive care adoption: {insights['health_trends']['preventive_care_adoption']}%</small>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("#### 💡 AI Recommendations")
            recommendations = insights_data['recommendations']
            
            for rec in recommendations:
                priority_color = "#ff6b6b" if rec['priority'] == "High" else "#feca57"
                st.markdown(f"""
                <div class="enhancement-highlight" style="background: linear-gradient(135deg, {priority_color} 0%, #f093fb 100%);">
                    <strong>📋 {rec['area']}</strong><br>
                    <small>{rec['recommendation']}</small><br>
                    <small>Priority: {rec['priority']} | Impact: {rec['impact']}</small>
                </div>
                """, unsafe_allow_html=True)

        # Performance trends
        st.markdown("### 📈 Performance Trends")
        
        # Generate trend data
        dates = pd.date_range(start='2024-01-01', periods=12, freq='M')
        registrations = [45, 52, 48, 67, 73, 89, 95, 102, 87, 94, 108, 115]
        recoveries = [42, 49, 47, 65, 71, 87, 92, 100, 85, 91, 105, 112]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=dates,
            y=registrations,
            mode='lines+markers',
            name='New Registrations',
            line=dict(color='#667eea', width=3)
        ))
        fig.add_trace(go.Scatter(
            x=dates,
            y=recoveries,
            mode='lines+markers',
            name='Successful Recoveries',
            line=dict(color='#10b981', width=3)
        ))
        
        fig.update_layout(
            title="Monthly Registration vs Recovery Trends",
            plot_bgcolor='rgba(255,255,255,1)',
            paper_bgcolor='rgba(255,255,255,1)',
            font=dict(family="Arial, sans-serif", size=12, color='#2c3e50'),
            title_font=dict(size=16, color='#2c3e50', family="Arial, sans-serif"),
            xaxis_title="Month",
            yaxis_title="Count"
        )
        st.plotly_chart(fig, use_container_width=True)

# Create dashboard instance for external use
def create_dashboard(database=None):
    """Factory function to create dashboard instance"""
    return EnhancedDashboard(database)

# For backward compatibility
Dashboard = EnhancedDashboard
