# 🐕🐱 One Health AI Platform

A comprehensive pet healthcare management system built with Streamlit, designed to revolutionize pet care through technology.

## ✨ Features

### 🐾 Pet Management
- **Pet Registration**: Complete pet profile management with photos and QR codes
- **Owner Information**: Store detailed owner contact and address information
- **Microchip Integration**: Track pets with microchip ID support
- **Breed & Species Tracking**: Comprehensive breed database for dogs, cats, and other pets

### 🏥 Medical Records
- **Digital Health Records**: Complete medical history tracking
- **Vaccination Management**: Automated vaccination schedules and reminders
- **Veterinarian Networks**: Connect with local veterinarians and clinics
- **Treatment Tracking**: Monitor treatments, medications, and recovery progress
- **Cost Management**: Track healthcare expenses and insurance claims

### 🚨 Lost Pet Recovery
- **Lost Pet Alerts**: Immediate notification system for missing pets
- **AI-Powered Matching**: Computer vision technology to match found pets with lost pet reports
- **Community Network**: Engage local communities in pet recovery efforts
- **Real-time Updates**: GPS tracking and location-based alerts
- **Emergency Contacts**: Multiple contact options for quick communication

### 📱 QR Code Integration
- **Smart Pet Tags**: Generate unique QR codes for instant pet identification
- **Emergency Information**: Quick access to pet and owner details
- **Medical Alert Tags**: Special tags for pets with medical conditions
- **Location Tracking**: Last known location when QR code is scanned

### 📊 Analytics & Insights
- **Health Analytics**: Track pet health trends and patterns
- **Vaccination Compliance**: Monitor community vaccination rates
- **Recovery Statistics**: Success rates for lost pet recoveries
- **Breed Analysis**: Popular breeds and health insights by region

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Quick Start

1. **Clone or Download the Project**
   ```bash
   git clone <repository-url>
   cd one_health_ai_platform
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the Database**
   ```bash
   python generate_sample_data.py
   ```
   Choose option 1 to generate sample data for testing.

4. **Run the Application**
   ```bash
   streamlit run app.py
   ```

5. **Open in Browser**
   Navigate to `http://localhost:8501` in your web browser.

## 📁 Project Structure

```
one_health_ai_platform/
├── app.py                    # Main Streamlit application
├── dashboard.py              # Dashboard components and analytics
├── database.py              # Database operations and models
├── pet_registration.py      # Pet registration functionality
├── lost_pet_recovery.py     # Lost pet management system
├── medical_records.py       # Health records and vaccination tracking
├── qr_utils.py              # QR code generation and management
├── generate_sample_data.py  # Sample data generator for testing
├── requirements.txt         # Python dependencies
├── README.md               # Project documentation
├── Dockerfile              # Docker container configuration
├── docker-compose.yml      # Docker Compose setup
└── pet_health.db           # SQLite database (created on first run)
```

## 💻 Usage Guide

### 🏠 Dashboard
- View system statistics and recent activity
- Quick access to all major functions
- Visual analytics and charts
- Health alerts and reminders

### 📝 Pet Registration
1. Navigate to "Pet Registration" from the sidebar
2. Fill in pet details (name, species, breed, age, etc.)
3. Add owner information
4. Upload pet photo (optional)
5. Submit to generate unique Pet ID and QR code

### 🔍 Lost Pet Recovery
1. **Report Lost Pet**: Select your registered pet and provide last seen details
2. **Report Found Pet**: Submit found pet information with description and photos
3. **Track Recovery**: Monitor active cases and recovery statistics

### 🏥 Medical Records
1. **Add Records**: Document vet visits, treatments, and diagnoses
2. **Vaccination Tracking**: Schedule and track all vaccinations
3. **View History**: Access complete medical history for any pet
4. **Health Summaries**: Generate health reports and statistics

### 📱 QR Code System
1. Generate QR codes during pet registration
2. Download printable pet tags
3. Create emergency QR codes for lost pets
4. Simulate QR code scanning to see what others see

## 🐳 Docker Deployment

### Using Docker Compose (Recommended)
```bash
docker-compose up -d
```

### Using Docker
```bash
# Build the image
docker build -t one-health-ai .

# Run the container
docker run -p 8501:8501 one-health-ai
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root:
```
DATABASE_URL=sqlite:///pet_health.db
APP_SECRET_KEY=your_secret_key_here
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

### Database Configuration
The application uses SQLite by default. For production, consider:
- PostgreSQL for better performance
- MySQL for compatibility
- Cloud databases (AWS RDS, Google Cloud SQL)

## 🎨 Customization

### Adding New Features
1. Create new module in the project directory
2. Import in `app.py`
3. Add navigation option in sidebar
4. Implement feature-specific UI components

### Styling
- Modify CSS in `app.py` for custom themes
- Update color schemes and layouts
- Add custom fonts and animations

### Database Schema
- Extend tables in `database.py`
- Add new fields to existing models
- Create migration scripts for schema updates

## 📊 Sample Data

The project includes a comprehensive sample data generator:

```bash
python generate_sample_data.py
```

Options:
- Generate sample pets (20+ realistic entries)
- Create lost pet scenarios
- Add found pet reports
- Generate medical records and vaccinations
- Clear all data for fresh start

## 🔒 Security Features

- **Data Encryption**: Sensitive information is encrypted
- **Access Control**: Role-based permissions
- **Audit Logging**: Track all system activities
- **Backup Systems**: Automated data backups
- **GDPR Compliance**: Privacy-first design

## 🌟 Advanced Features

### AI Integration
- **Image Recognition**: Automatic breed identification from photos
- **Smart Matching**: AI-powered lost/found pet matching
- **Health Predictions**: Predictive analytics for pet health
- **Behavioral Analysis**: Monitor pet activity patterns

### Mobile Integration
- **PWA Support**: Progressive Web App functionality
- **Mobile Responsive**: Optimized for all device sizes
- **Offline Mode**: Basic functionality without internet
- **Push Notifications**: Real-time alerts and updates

### Community Features
- **Social Network**: Connect with other pet owners
- **Local Services**: Find nearby veterinarians and pet services
- **Event Calendar**: Pet-related events and appointments
- **Knowledge Base**: Pet care tips and resources

## 🚀 Roadmap

### Version 2.1 (Coming Soon)
- [ ] Mobile app (iOS/Android)
- [ ] Advanced AI pet matching
- [ ] Integration with veterinary clinics
- [ ] Telemedicine features
- [ ] Insurance integration

### Version 2.2
- [ ] Multi-language support
- [ ] Voice commands
- [ ] AR pet tag scanning
- [ ] Blockchain pet identity
- [ ] IoT device integration

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the Repository**
2. **Create Feature Branch**: `git checkout -b feature/new-feature`
3. **Commit Changes**: `git commit -m 'Add new feature'`
4. **Push to Branch**: `git push origin feature/new-feature`
5. **Submit Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Add unit tests for new features
- Update documentation
- Use meaningful commit messages

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

### Getting Help
- **Documentation**: Check this README and code comments
- **Issues**: Report bugs on GitHub Issues
- **Discussions**: Join community discussions
- **Email**: Contact support@onehealth-ai.com

### Common Issues
1. **Database Errors**: Ensure proper permissions and disk space
2. **Port Conflicts**: Change port in Streamlit config if 8501 is busy
3. **Dependencies**: Use virtual environment for clean installations
4. **Performance**: Increase system resources for large datasets

## 🙏 Acknowledgments

- **Streamlit Team**: For the amazing web framework
- **Pet Care Community**: For insights and feedback
- **Open Source Contributors**: For various libraries and tools
- **Veterinary Professionals**: For medical expertise and guidance

## 📈 Statistics

- **Pet Records Supported**: Unlimited
- **Database Performance**: Optimized for 10,000+ records
- **Response Time**: < 2 seconds for most operations
- **Uptime**: 99.9% availability target
- **Security**: Bank-level encryption standards

---

**🐾 One Health AI Platform - Connecting Pets, Owners, and Communities for Better Pet Health! 🐾**

Made with ❤️ for pet lovers worldwide.
