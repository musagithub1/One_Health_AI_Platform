# 🚀 One Health AI Platform - Installation Guide

## System Requirements

### Minimum Requirements
- **Operating System**: Windows 10, macOS 10.14, or Ubuntu 18.04+
- **Python**: Version 3.8 or higher
- **RAM**: 4GB minimum (8GB recommended for AI features)
- **Storage**: 2GB free disk space
- **Internet**: Required for initial setup and AI model downloads

### Recommended Specifications
- **RAM**: 8GB or more for optimal AI performance
- **CPU**: Multi-core processor (4+ cores recommended)
- **Storage**: SSD for faster database operations
- **Browser**: Chrome, Firefox, Safari, or Edge (latest versions)

## Quick Installation

### Step 1: Extract the Project
```bash
# Extract the downloaded zip file
unzip one_health_ai_platform_enhanced.zip
cd one_health_ai_platform
```

### Step 2: Install Python Dependencies
```bash
# Install required packages
pip install -r enhanced_requirements.txt

# Alternative: Install basic requirements only
pip install streamlit plotly pandas qrcode[pil]
```

### Step 3: Initialize the Database (Optional)
```bash
# Generate sample data for testing
python generate_sample_data.py
# Select option 1 when prompted
```

### Step 4: Run the Application
```bash
# Start the enhanced version
streamlit run enhanced_app.py

# Or run the original version for comparison
streamlit run app.py
```

### Step 5: Access the Platform
Open your web browser and navigate to: `http://localhost:8501`

## Detailed Installation Instructions

### For Windows Users

1. **Install Python**
   - Download Python 3.8+ from python.org
   - Ensure "Add Python to PATH" is checked during installation
   - Verify installation: `python --version`

2. **Install Dependencies**
   ```cmd
   pip install -r enhanced_requirements.txt
   ```

3. **Run the Application**
   ```cmd
   streamlit run enhanced_app.py
   ```

### For macOS Users

1. **Install Python** (if not already installed)
   ```bash
   # Using Homebrew
   brew install python

   # Or download from python.org
   ```

2. **Install Dependencies**
   ```bash
   pip3 install -r enhanced_requirements.txt
   ```

3. **Run the Application**
   ```bash
   streamlit run enhanced_app.py
   ```

### For Linux Users

1. **Install Python and pip**
   ```bash
   # Ubuntu/Debian
   sudo apt update
   sudo apt install python3 python3-pip

   # CentOS/RHEL
   sudo yum install python3 python3-pip
   ```

2. **Install Dependencies**
   ```bash
   pip3 install -r enhanced_requirements.txt
   ```

3. **Run the Application**
   ```bash
   streamlit run enhanced_app.py
   ```

## Docker Installation (Alternative)

### Using Docker Compose
```bash
# Build and run with Docker Compose
docker-compose up -d

# Access at http://localhost:8501
```

### Using Docker Directly
```bash
# Build the image
docker build -t one-health-ai .

# Run the container
docker run -p 8501:8501 one-health-ai
```

## Configuration Options

### Environment Variables
Create a `.env` file in the project root:
```env
# Database Configuration
DATABASE_URL=sqlite:///pet_health.db

# Application Settings
APP_SECRET_KEY=your_secret_key_here
DEBUG_MODE=False

# AI Service Settings
AI_CONFIDENCE_THRESHOLD=0.8
ENABLE_AI_FEATURES=True

# External Services (Optional)
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

### Streamlit Configuration
Create `.streamlit/config.toml`:
```toml
[server]
port = 8501
address = "0.0.0.0"
maxUploadSize = 200

[theme]
primaryColor = "#667eea"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
```

## Troubleshooting

### Common Installation Issues

#### 1. Python Version Conflicts
```bash
# Check Python version
python --version

# Use specific Python version
python3.8 -m pip install -r enhanced_requirements.txt
python3.8 -m streamlit run enhanced_app.py
```

#### 2. Permission Errors
```bash
# Install with user permissions
pip install --user -r enhanced_requirements.txt

# Or use virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r enhanced_requirements.txt
```

#### 3. Package Installation Failures
```bash
# Update pip first
pip install --upgrade pip

# Install packages individually if bulk install fails
pip install streamlit
pip install plotly
pip install pandas
pip install qrcode[pil]
```

#### 4. Port Already in Use
```bash
# Use different port
streamlit run enhanced_app.py --server.port 8502

# Or kill existing process
lsof -ti:8501 | xargs kill -9  # On Unix systems
```

### Performance Issues

#### 1. Slow Loading
- Ensure sufficient RAM (8GB+ recommended)
- Close unnecessary applications
- Use SSD storage for better performance
- Check internet connection for initial AI model downloads

#### 2. AI Features Not Working
- Verify all dependencies are installed
- Check system resources (RAM and CPU)
- Ensure internet connectivity for AI services
- Review error logs in terminal

#### 3. Database Errors
- Check file permissions in project directory
- Ensure sufficient disk space
- Verify SQLite installation
- Try regenerating the database with sample data

## Advanced Configuration

### Custom AI Models
```python
# In ai_services.py, modify model configurations
BREED_DETECTION_CONFIG = {
    'confidence_threshold': 0.85,
    'max_predictions': 5,
    'enable_age_estimation': True
}

HEALTH_PREDICTION_CONFIG = {
    'prediction_horizon': 6,  # months
    'risk_threshold': 0.7,
    'enable_recommendations': True
}
```

### Database Customization
```python
# Switch to PostgreSQL (in database.py)
DATABASE_URL = "postgresql://user:password@localhost/pet_health"

# Or use MySQL
DATABASE_URL = "mysql://user:password@localhost/pet_health"
```

### UI Customization
```css
/* Add to enhanced_app.py CSS section */
.custom-theme {
    --primary-color: #your-color;
    --secondary-color: #your-color;
    --background-color: #your-color;
}
```

## Production Deployment

### Cloud Deployment Options

#### 1. Heroku
```bash
# Install Heroku CLI and login
heroku create your-app-name
git push heroku main
```

#### 2. AWS EC2
```bash
# Launch EC2 instance
# Install dependencies
# Configure security groups for port 8501
# Use PM2 or systemd for process management
```

#### 3. Google Cloud Platform
```bash
# Use Google App Engine or Compute Engine
# Configure load balancing for high availability
```

#### 4. DigitalOcean
```bash
# Create droplet
# Install Docker and run containerized version
```

### Security Considerations
- Use HTTPS in production
- Configure proper authentication
- Set up database backups
- Monitor system resources
- Implement rate limiting
- Use environment variables for secrets

## Maintenance and Updates

### Regular Maintenance
```bash
# Update dependencies
pip install --upgrade -r enhanced_requirements.txt

# Backup database
cp pet_health.db pet_health_backup_$(date +%Y%m%d).db

# Clear temporary files
rm -rf __pycache__/
rm -rf .streamlit/
```

### Monitoring
- Monitor system resources (CPU, RAM, disk)
- Check application logs regularly
- Monitor user activity and performance metrics
- Set up alerts for system issues

### Updates
- Check for new versions regularly
- Test updates in development environment first
- Backup data before applying updates
- Review changelog for breaking changes

## Support and Resources

### Getting Help
- Check the troubleshooting section above
- Review error messages in terminal
- Consult the DEMO_README.md for feature documentation
- Search online for Streamlit-specific issues

### Useful Commands
```bash
# Check installed packages
pip list

# View Streamlit version
streamlit version

# Run with debug mode
streamlit run enhanced_app.py --logger.level debug

# Clear Streamlit cache
streamlit cache clear
```

### Additional Resources
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly Documentation](https://plotly.com/python/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

---

**🎯 Ready to explore the future of pet healthcare management? Follow this guide to get started with the One Health AI Platform!**

