import streamlit as st
import pandas as pd
from datetime import datetime
import os
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from database import Database
from pet_registration import PetRegistration
from lost_pet_recovery import LostPetRecovery
from medical_records import MedicalRecords
from dashboard import Dashboard
from qr_utils import QRCodeGenerator

# Configure page settings
st.set_page_config(
    page_title="🐕🐱 One Health AI Platform - Advanced Demo",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced Custom CSS with improved text visibility
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .main {
        font-family: 'Inter', sans-serif;
        background-color: #f8fafc;
    }
    
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="25" cy="25" r="1" fill="white" opacity="0.1"/><circle cx="75" cy="75" r="1" fill="white" opacity="0.1"/><circle cx="50" cy="10" r="0.5" fill="white" opacity="0.1"/><circle cx="10" cy="60" r="0.5" fill="white" opacity="0.1"/><circle cx="90" cy="40" r="0.5" fill="white" opacity="0.1"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
        pointer-events: none;
    }
    
    .main-header h1 {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        color: white;
    }
    
    .main-header p {
        font-size: 1.2rem;
        font-weight: 300;
        opacity: 0.9;
        color: white;
    }

    .metric-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        color: #2d3748;
    }
    
    .metric-card h4 {
        color: #1a202c;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    
    .metric-card p {
        color: #4a5568;
        margin-bottom: 0.5rem;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        background: linear-gradient(180deg, #667eea, #764ba2);
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 48px rgba(0,0,0,0.15);
    }

    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #f8fafc 0%, #e2e8f0 100%);
        border-radius: 0 20px 20px 0;
    }
    
    .sidebar .sidebar-content .block-container {
        padding-top: 2rem;
    }

    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
        color: white;
    }
    
    .stSelectbox > div > div {
        background: white;
        border-radius: 12px;
        border: 2px solid #e2e8f0;
        transition: all 0.3s ease;
        color: #2d3748;
    }
    
    .stSelectbox > div > div:focus-within {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    .feature-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.3);
        transition: all 0.3s ease;
        text-align: center;
        position: relative;
        overflow: hidden;
        color: #2d3748;
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(102, 126, 234, 0.05) 0%, transparent 70%);
        transition: all 0.3s ease;
        transform: scale(0);
    }
    
    .feature-card:hover::before {
        transform: scale(1);
    }
    
    .feature-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 50px rgba(0,0,0,0.15);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        display: block;
    }
    
    .feature-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #1a202c;
        margin-bottom: 1rem;
    }
    
    .feature-description {
        color: #4a5568;
        line-height: 1.6;
    }
    
    .stats-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .stat-item {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        border: 1px solid rgba(255,255,255,0.2);
        transition: all 0.3s ease;
        color: #2d3748;
    }
    
    .stat-item:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.12);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: #667eea;
        display: block;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        color: #4a5568;
        font-weight: 500;
        text-transform: uppercase;
        font-size: 0.875rem;
        letter-spacing: 0.05em;
    }
    
    .ai-badge {
        background: linear-gradient(135deg, #ff6b6b 0%, #feca57 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.875rem;
        font-weight: 600;
        display: inline-block;
        margin: 0.5rem 0;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3);
    }
    
    .demo-banner {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
        padding: 1rem 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        color: #2d3748;
        font-weight: 600;
        box-shadow: 0 5px 20px rgba(255, 154, 158, 0.3);
    }
    
    .enhancement-highlight {
        background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        color: #2d3748;
        font-weight: 500;
        border-left: 4px solid #10b981;
    }
    
    /* Improved text visibility for all elements */
    h1, h2, h3, h4, h5, h6 {
        color: #1a202c !important;
    }
    
    p, div, span {
        color: #4a5568 !important;
    }
    
    .stMarkdown {
        color: #4a5568;
    }
    
    /* Sidebar text improvements */
    .sidebar .sidebar-content {
        color: #2d3748;
    }
    
    .sidebar .sidebar-content h1,
    .sidebar .sidebar-content h2,
    .sidebar .sidebar-content h3,
    .sidebar .sidebar-content p {
        color: #2d3748 !important;
    }
    
    /* Chart container improvements */
    .js-plotly-plot .plotly {
        color: #2d3748;
    }
    
    /* Tab improvements */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #f8fafc;
        border-radius: 10px 10px 0 0;
        gap: 1px;
        padding: 10px 20px;
        color: #4a5568;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #667eea;
        color: white !important;
    }
    
    /* Input field text color */
    .stTextInput input, .stTextArea textarea {
        color: #2d3748 !important;
    }
    
    .stNumberInput input {
        color: #2d3748 !important;
    }
    
    .stDateInput input {
        color: #2d3748 !important;
    }
    
    .stTimeInput input {
        color: #2d3748 !important;
    }
    
    /* Select box text color */
    .stSelectbox div[data-baseweb="select"] {
        color: #2d3748 !important;
    }
    
    /* File uploader text */
    .stFileUploader label {
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
        color: #2d3748;
    }
    
    /* Code blocks */
    .stCodeBlock {
        color: #2d3748;
    }
    
    /* Animation classes */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .fade-in-up {
        animation: fadeInUp 0.6s ease-out;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-header h1 {
            font-size: 2rem;
        }
        
        .main-header p {
            font-size: 1rem;
        }
        
        .stats-container {
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 1rem;
        }
        
        .feature-card {
            padding: 1rem;
        }
        
        .metric-card {
            padding: 1.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

class EnhancedOneHealthApp:
    def __init__(self):
        self.db = Database()
        self.pet_registration = PetRegistration(self.db)
        self.lost_pet_recovery = LostPetRecovery(self.db)
        self.medical_records = MedicalRecords(self.db)
        self.dashboard = Dashboard(self.db)
        self.qr_generator = QRCodeGenerator()

    def run(self):
        # Demo banner
        st.markdown("""
        <div class="demo-banner fade-in-up">
            🚀 <strong>ADVANCED DEMO VERSION</strong> - Enhanced with AI capabilities, modern UI, and interactive features
        </div>
        """, unsafe_allow_html=True)

        # Main header with enhanced styling
        st.markdown("""
        <div class="main-header fade-in-up">
            <h1>🐕🐱 One Health AI Platform</h1>
            <p>Next-Generation Pet Healthcare Management System</p>
            <div class="ai-badge">✨ AI-Powered</div>
        </div>
        """, unsafe_allow_html=True)

        # Enhanced sidebar navigation
        st.sidebar.markdown("""
        <div style="text-align: center; padding: 1rem 0;">
            <h2 style="color: #667eea; margin-bottom: 0.5rem;">🏥 Navigation</h2>
            <p style="color: #4a5568; font-size: 0.875rem;">Advanced Demo Features</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.sidebar.markdown("---")

        page = st.sidebar.selectbox(
            "Choose a page:",
            [
                "🏠 Enhanced Dashboard",
                "📝 Smart Pet Registration", 
                "🔍 AI Pet Recovery",
                "🏥 Digital Medical Records",
                "📊 Advanced Analytics",
                "🎯 AI Features Demo",
                "ℹ️ About Platform"
            ]
        )

        # Add feature highlights in sidebar
        st.sidebar.markdown("### 🌟 New Features")
        st.sidebar.markdown("""
        <div style="background: linear-gradient(135deg, #667eea, #764ba2); padding: 1rem; border-radius: 10px; color: white; margin: 1rem 0;">
            <strong>🤖 AI Breed Detection</strong><br>
            <small>Upload photos for instant breed identification</small>
        </div>
        """, unsafe_allow_html=True)
        
        st.sidebar.markdown("""
        <div style="background: linear-gradient(135deg, #ff6b6b, #feca57); padding: 1rem; border-radius: 10px; color: white; margin: 1rem 0;">
            <strong>📈 Predictive Analytics</strong><br>
            <small>Health trend predictions and insights</small>
        </div>
        """, unsafe_allow_html=True)

        # Main content based on selection
        if page == "🏠 Enhanced Dashboard":
            self.show_enhanced_dashboard()
        elif page == "📝 Smart Pet Registration":
            self.show_smart_pet_registration()
        elif page == "🔍 AI Pet Recovery":
            self.show_ai_pet_recovery()
        elif page == "🏥 Digital Medical Records":
            self.show_digital_medical_records()
        elif page == "📊 Advanced Analytics":
            self.show_advanced_analytics()
        elif page == "🎯 AI Features Demo":
            self.show_ai_features_demo()
        elif page == "ℹ️ About Platform":
            self.show_enhanced_about()

    def show_enhanced_dashboard(self):
        """Display the enhanced dashboard with modern UI"""
        st.markdown('<h2 class="fade-in-up">📊 Enhanced Dashboard Overview</h2>', unsafe_allow_html=True)
        
        # Quick stats with modern cards
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class="stat-item fade-in-up">
                <span class="stat-number">1,247</span>
                <span class="stat-label">Registered Pets</span>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="stat-item fade-in-up">
                <span class="stat-number">98.5%</span>
                <span class="stat-label">Recovery Rate</span>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="stat-item fade-in-up">
                <span class="stat-number">3,456</span>
                <span class="stat-label">Health Records</span>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class="stat-item fade-in-up">
                <span class="stat-number">24/7</span>
                <span class="stat-label">AI Monitoring</span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Interactive charts
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📈 Pet Registration Trends")
            # Create sample data for demo
            dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='M')
            registrations = [45, 52, 48, 67, 73, 89, 95, 102, 87, 94, 108, 115]
            
            fig = px.line(x=dates, y=registrations, 
                         title="Monthly Pet Registrations",
                         color_discrete_sequence=['#667eea'])
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Inter, sans-serif"),
                title_font_color="#1a202c",
                xaxis_title_font_color="#4a5568",
                yaxis_title_font_color="#4a5568"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("### 🐕 Pet Species Distribution")
            species_data = {'Species': ['Dogs', 'Cats', 'Birds', 'Rabbits', 'Others'],
                           'Count': [567, 423, 89, 67, 101]}
            
            fig = px.pie(values=species_data['Count'], names=species_data['Species'],
                        color_discrete_sequence=['#667eea', '#764ba2', '#f093fb', '#ff6b6b', '#feca57'])
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Inter, sans-serif"),
                title_font_color="#1a202c"
            )
            st.plotly_chart(fig, use_container_width=True)

        # Feature showcase
        st.markdown("### 🌟 Platform Features")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="feature-card fade-in-up">
                <span class="feature-icon">🤖</span>
                <div class="feature-title">AI-Powered Matching</div>
                <div class="feature-description">Advanced computer vision algorithms for lost pet identification and matching with 95% accuracy rate.</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="feature-card fade-in-up">
                <span class="feature-icon">📱</span>
                <div class="feature-title">Smart QR Codes</div>
                <div class="feature-description">Dynamic QR codes with real-time updates, GPS tracking, and emergency contact information.</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="feature-card fade-in-up">
                <span class="feature-icon">📊</span>
                <div class="feature-title">Predictive Analytics</div>
                <div class="feature-description">Machine learning models predict health trends and provide personalized care recommendations.</div>
            </div>
            """, unsafe_allow_html=True)

        # Call original dashboard for additional functionality
        self.dashboard.show_main_dashboard()

    def show_smart_pet_registration(self):
        """Enhanced pet registration with AI features"""
        st.markdown('<h2 class="fade-in-up">📝 Smart Pet Registration</h2>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="enhancement-highlight">
            🎯 <strong>Enhanced Features:</strong> AI breed detection, smart form validation, and automated health recommendations
        </div>
        """, unsafe_allow_html=True)
        
        # Add AI breed detection demo
        st.markdown("### 🤖 AI Breed Detection")
        uploaded_file = st.file_uploader("Upload pet photo for AI breed identification", type=['jpg', 'jpeg', 'png'])
        
        if uploaded_file is not None:
            col1, col2 = st.columns(2)
            with col1:
                st.image(uploaded_file, caption="Uploaded Photo", use_column_width=True)
            with col2:
                st.markdown("""
                <div class="metric-card">
                    <h4>🎯 AI Analysis Results</h4>
                    <p><strong>Detected Breed:</strong> Golden Retriever</p>
                    <p><strong>Confidence:</strong> 94.7%</p>
                    <p><strong>Secondary Match:</strong> Labrador Retriever (87.3%)</p>
                    <div class="ai-badge">✨ AI Powered</div>
                </div>
                """, unsafe_allow_html=True)
        
        # Original registration form
        self.pet_registration.show_registration_form()

    def show_ai_pet_recovery(self):
        """Enhanced lost pet recovery with AI matching"""
        st.markdown('<h2 class="fade-in-up">🔍 AI-Powered Pet Recovery</h2>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="enhancement-highlight">
            🤖 <strong>AI Enhancement:</strong> Computer vision matching, similarity scoring, and automated alerts
        </div>
        """, unsafe_allow_html=True)
        
        # AI matching demo
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📸 Lost Pet Photo")
            st.image("https://via.placeholder.com/300x200/667eea/white?text=Lost+Pet", caption="Lost: Golden Retriever")
        
        with col2:
            st.markdown("### 🎯 AI Match Results")
            st.markdown("""
            <div class="metric-card">
                <h4>🔍 Potential Matches Found</h4>
                <p><strong>Match 1:</strong> 96.8% similarity</p>
                <p><strong>Match 2:</strong> 89.2% similarity</p>
                <p><strong>Match 3:</strong> 76.5% similarity</p>
                <div class="ai-badge">🤖 AI Analyzed</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Original recovery interface
        self.lost_pet_recovery.show_recovery_interface()

    def show_digital_medical_records(self):
        """Enhanced medical records with health predictions"""
        st.markdown('<h2 class="fade-in-up">🏥 Digital Medical Records</h2>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="enhancement-highlight">
            📊 <strong>Predictive Health:</strong> AI-powered health trend analysis and early warning system
        </div>
        """, unsafe_allow_html=True)
        
        # Health prediction demo
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📈 Health Trend Analysis")
            # Sample health data
            dates = pd.date_range(start='2024-01-01', periods=12, freq='M')
            weight = [25.2, 25.5, 25.8, 26.1, 26.0, 25.9, 25.7, 25.8, 26.2, 26.5, 26.8, 27.1]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=dates, y=weight, mode='lines+markers',
                                   name='Weight (kg)', line=dict(color='#667eea', width=3)))
            fig.update_layout(
                title="Pet Weight Trend",
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Inter, sans-serif"),
                title_font_color="#1a202c",
                xaxis_title_font_color="#4a5568",
                yaxis_title_font_color="#4a5568"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("### 🎯 AI Health Insights")
            st.markdown("""
            <div class="metric-card">
                <h4>🤖 Predictive Analysis</h4>
                <p><strong>Health Score:</strong> 8.7/10</p>
                <p><strong>Risk Level:</strong> Low</p>
                <p><strong>Recommendation:</strong> Maintain current diet</p>
                <p><strong>Next Checkup:</strong> 3 months</p>
                <div class="ai-badge">🔮 Predictive AI</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Original medical records interface
        self.medical_records.show_records_interface()

    def show_advanced_analytics(self):
        """Advanced analytics with interactive visualizations"""
        st.markdown('<h2 class="fade-in-up">📊 Advanced Analytics Dashboard</h2>', unsafe_allow_html=True)
        
        # Multi-metric dashboard
        col1, col2, col3 = st.columns(3)
        
        with col1:
            # Vaccination compliance chart
            st.markdown("### 💉 Vaccination Compliance")
            compliance_data = {'Status': ['Up to Date', 'Due Soon', 'Overdue'],
                             'Count': [789, 156, 67]}
            
            fig = px.bar(x=compliance_data['Status'], y=compliance_data['Count'],
                        color=compliance_data['Status'],
                        color_discrete_sequence=['#10b981', '#f59e0b', '#ef4444'])
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Inter, sans-serif"),
                title_font_color="#1a202c",
                showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Age distribution - FIXED: Use px.pie with hole parameter for donut chart
            st.markdown("### 🎂 Age Distribution")
            age_data = {'Age Group': ['0-1 years', '1-3 years', '3-7 years', '7+ years'],
                       'Count': [234, 456, 389, 168]}
            
            fig = px.pie(values=age_data['Count'], names=age_data['Age Group'],
                        hole=0.4,  # This creates the donut chart effect
                        color_discrete_sequence=['#667eea', '#764ba2', '#f093fb', '#ff6b6b'])
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Inter, sans-serif"),
                title_font_color="#1a202c"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col3:
            # Recovery success rate
            st.markdown("### 🎯 Recovery Success Rate")
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
            success_rate = [94.2, 96.1, 97.8, 95.5, 98.2, 97.1]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=months, y=success_rate, mode='lines+markers',
                                   fill='tonexty', line=dict(color='#10b981', width=3)))
            fig.update_layout(
                title="Monthly Recovery Success Rate (%)",
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Inter, sans-serif"),
                title_font_color="#1a202c",
                yaxis=dict(range=[90, 100])
            )
            st.plotly_chart(fig, use_container_width=True)

        # Original analytics
        self.dashboard.show_analytics()

    def show_ai_features_demo(self):
        """Showcase AI features and capabilities"""
        st.markdown('<h2 class="fade-in-up">🎯 AI Features Demonstration</h2>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="demo-banner">
            🤖 Experience the power of AI in pet healthcare management
        </div>
        """, unsafe_allow_html=True)
        
        # AI feature tabs
        tab1, tab2, tab3, tab4 = st.tabs(["🔍 Breed Detection", "🎯 Pet Matching", "📊 Health Prediction", "🧠 Smart Insights"])
        
        with tab1:
            st.markdown("### 🤖 AI Breed Detection Engine")
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                **How it works:**
                1. Upload pet photo
                2. AI analyzes visual features
                3. Matches against breed database
                4. Provides confidence scores
                
                **Supported Features:**
                - 200+ dog breeds
                - 50+ cat breeds
                - Mixed breed detection
                - Age estimation
                """)
            
            with col2:
                st.markdown("""
                <div class="metric-card">
                    <h4>🎯 Demo Results</h4>
                    <p><strong>Breed:</strong> Golden Retriever</p>
                    <p><strong>Confidence:</strong> 94.7%</p>
                    <p><strong>Age Estimate:</strong> 3-4 years</p>
                    <p><strong>Size Category:</strong> Large</p>
                    <div class="ai-badge">✨ AI Powered</div>
                </div>
                """, unsafe_allow_html=True)
        
        with tab2:
            st.markdown("### 🎯 Advanced Pet Matching Algorithm")
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                **Matching Criteria:**
                - Visual similarity (95% weight)
                - Location proximity (3% weight)
                - Time correlation (2% weight)
                
                **AI Technologies:**
                - Computer Vision
                - Feature Extraction
                - Similarity Scoring
                - Pattern Recognition
                """)
            
            with col2:
                # Matching visualization
                fig = go.Figure()
                categories = ['Visual Features', 'Location', 'Time', 'Breed Match', 'Size Match']
                scores = [96.8, 89.2, 94.5, 98.1, 92.7]
                
                fig.add_trace(go.Scatterpolar(
                    r=scores,
                    theta=categories,
                    fill='toself',
                    name='Match Score',
                    line=dict(color='#667eea')
                ))
                
                fig.update_layout(
                    polar=dict(
                        radialaxis=dict(
                            visible=True,
                            range=[0, 100]
                        )),
                    showlegend=False,
                    title="Pet Matching Score Analysis",
                    font=dict(family="Inter, sans-serif"),
                    title_font_color="#1a202c"
                )
                st.plotly_chart(fig, use_container_width=True)
        
        with tab3:
            st.markdown("### 📊 Predictive Health Analytics")
            
            # Health prediction visualization
            fig = make_subplots(
                rows=2, cols=2,
                subplot_titles=('Weight Trend', 'Activity Level', 'Health Score', 'Risk Factors'),
                specs=[[{"secondary_y": False}, {"secondary_y": False}],
                       [{"secondary_y": False}, {"secondary_y": False}]]
            )
            
            # Weight trend
            dates = pd.date_range(start='2024-01-01', periods=12, freq='M')
            weight = [25.2, 25.5, 25.8, 26.1, 26.0, 25.9, 25.7, 25.8, 26.2, 26.5, 26.8, 27.1]
            fig.add_trace(go.Scatter(x=dates, y=weight, name='Weight'), row=1, col=1)
            
            # Activity level
            activity = [8.2, 8.5, 7.8, 8.1, 8.0, 7.9, 8.3, 8.2, 7.8, 8.1, 8.4, 8.2]
            fig.add_trace(go.Scatter(x=dates, y=activity, name='Activity'), row=1, col=2)
            
            # Health score
            health_score = [8.5, 8.7, 8.3, 8.6, 8.4, 8.2, 8.8, 8.6, 8.1, 8.3, 8.7, 8.5]
            fig.add_trace(go.Scatter(x=dates, y=health_score, name='Health Score'), row=2, col=1)
            
            # Risk factors
            risk_categories = ['Obesity', 'Dental', 'Joint', 'Heart', 'Kidney']
            risk_scores = [15, 8, 12, 5, 3]
            fig.add_trace(go.Bar(x=risk_categories, y=risk_scores, name='Risk %'), row=2, col=2)
            
            fig.update_layout(height=600, showlegend=False, title_text="Comprehensive Health Analytics")
            st.plotly_chart(fig, use_container_width=True)
        
        with tab4:
            st.markdown("### 🧠 Smart Insights & Recommendations")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                <div class="metric-card">
                    <h4>🎯 Personalized Recommendations</h4>
                    <p><strong>Diet Adjustment:</strong> Reduce daily intake by 10%</p>
                    <p><strong>Exercise:</strong> Increase walks to 45 min/day</p>
                    <p><strong>Checkup:</strong> Schedule dental exam</p>
                    <p><strong>Vaccination:</strong> Rabies due in 2 months</p>
                    <div class="ai-badge">🤖 AI Generated</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                <div class="metric-card">
                    <h4>📊 Health Trends</h4>
                    <p><strong>Weight Trend:</strong> ↗️ Gradual increase</p>
                    <p><strong>Activity:</strong> ➡️ Stable</p>
                    <p><strong>Appetite:</strong> ↗️ Increased</p>
                    <p><strong>Energy Level:</strong> ↘️ Slightly decreased</p>
                    <div class="ai-badge">📈 Trend Analysis</div>
                </div>
                """, unsafe_allow_html=True)

    def show_enhanced_about(self):
        """Enhanced about page with modern design"""
        st.markdown('<h2 class="fade-in-up">ℹ️ About One Health AI Platform</h2>', unsafe_allow_html=True)

        # Platform overview
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            <div class="feature-card">
                <span class="feature-icon">🎯</span>
                <div class="feature-title">Our Mission</div>
                <div class="feature-description">
                    Revolutionizing pet healthcare through cutting-edge AI technology, 
                    connecting pet owners, veterinarians, and communities for better pet health outcomes.
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="feature-card">
                <span class="feature-icon">🌟</span>
                <div class="feature-title">Key Innovations</div>
                <div class="feature-description">
                    AI-powered breed detection, predictive health analytics, smart pet matching, 
                    and comprehensive digital health records management.
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Technology stack
        st.markdown("### 🔧 Advanced Technology Stack")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            **Frontend Technologies:**
            - Streamlit with custom CSS
            - Plotly for interactive charts
            - Responsive design
            - Modern UI components
            """)
        
        with col2:
            st.markdown("""
            **AI & Machine Learning:**
            - Computer Vision models
            - Breed classification
            - Predictive analytics
            - Pattern recognition
            """)
        
        with col3:
            st.markdown("""
            **Backend & Database:**
            - Python with SQLite
            - RESTful API design
            - Real-time data processing
            - Secure data storage
            """)

        # Demo features highlight
        st.markdown("### 🚀 Demo Enhancements")
        
        enhancements = [
            ("🎨 Modern UI/UX", "Completely redesigned interface with gradient backgrounds, smooth animations, and responsive design"),
            ("🤖 AI Integration", "Simulated AI features including breed detection, health predictions, and smart matching algorithms"),
            ("📊 Interactive Analytics", "Advanced data visualizations with Plotly charts, real-time updates, and comprehensive dashboards"),
            ("📱 Mobile Responsive", "Optimized for all device sizes with touch-friendly interfaces and adaptive layouts"),
            ("⚡ Performance", "Enhanced loading speeds, smooth transitions, and optimized user experience"),
            ("🔒 Security", "Improved data protection, secure authentication, and privacy-first design")
        ]
        
        for title, description in enhancements:
            st.markdown(f"""
            <div class="enhancement-highlight">
                <strong>{title}:</strong> {description}
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("""
        <div class="demo-banner">
            🎉 <strong>This is an advanced demo version</strong> showcasing the potential of AI-powered pet healthcare management
        </div>
        """, unsafe_allow_html=True)

# Initialize and run the enhanced application
if __name__ == "__main__":
    app = EnhancedOneHealthApp()
    app.run()