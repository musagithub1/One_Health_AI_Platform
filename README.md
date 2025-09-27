# One Health AI Platform 🐾

[![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.28.0+-red.svg)](https://streamlit.io/)
[![Docker](https://img.shields.io/badge/docker-available-blue.svg)](https://hub.docker.com/r/musagithub1/one-health-ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docker Hub](https://img.shields.io/docker/pulls/musagithub1/one-health-ai.svg)](https://hub.docker.com/r/musagithub1/one-health-ai)

An advanced AI-driven platform for comprehensive pet healthcare management, designed to revolutionize the way veterinarians, pet owners, and animal shelters manage pet care, track health records, and ensure pet safety.

## 🌟 Overview

The One Health AI Platform is a cutting-edge solution that combines artificial intelligence with practical pet healthcare management. Built with modern web technologies, this platform provides a seamless interface for managing pet registrations, tracking vaccinations, integrating microchip data, monitoring health records, and facilitating lost pet recovery.

### Key Highlights

- **AI-Powered Analytics**: Advanced machine learning algorithms for health pattern analysis
- **Comprehensive Pet Management**: Complete pet lifecycle tracking from registration to medical history
- **Multi-User Support**: Designed for veterinarians, pet owners, and animal shelters
- **Real-time Dashboard**: Interactive visualizations and reporting capabilities
- **Microchip Integration**: Seamless microchip data management and tracking
- **Lost Pet Recovery System**: Advanced search and recovery mechanisms

## ✨ Features

### 🏥 Healthcare Management
- **Pet Registration**: Comprehensive pet profile creation and management
- **Medical Records**: Detailed health history tracking and management
- **Vaccination Tracking**: Automated vaccination schedules and reminders
- **Health Analytics**: AI-powered health pattern analysis and insights

### 🔍 Advanced Tracking
- **Microchip Integration**: Complete microchip data management system
- **Owner Details Management**: Comprehensive owner information tracking
- **QR Code Generation**: Quick access QR codes for pet identification
- **Lost Pet Recovery**: Advanced search algorithms for lost pet identification

### 📊 Dashboard & Analytics
- **Interactive Dashboard**: Real-time data visualization and reporting
- **Enhanced Analytics**: Advanced statistical analysis and reporting
- **Data Export**: Multiple format data export capabilities
- **Custom Reports**: Tailored reporting for different user types

### 🔧 Technical Features
- **Docker Support**: Containerized deployment for easy scaling
- **Sample Data Generation**: Built-in tools for testing and demonstration
- **Database Management**: Efficient data storage and retrieval systems
- **Responsive Design**: Mobile-friendly interface design

## 🛠️ Tech Stack

### Core Technologies
- **Python 3.8+**: Primary programming language
- **Streamlit**: Web application framework for interactive dashboards
- **Docker**: Containerization for deployment and scalability

### Data Science & AI Libraries
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing and array operations
- **matplotlib**: Data visualization and plotting
- **scikit-learn**: Machine learning algorithms and tools
- **seaborn**: Statistical data visualization

### Additional Libraries
- **Pillow**: Image processing capabilities
- **requests**: HTTP library for API integrations
- **python-dotenv**: Environment variable management
- **streamlit-option-menu**: Enhanced navigation components

## 🚀 Installation Instructions

### Prerequisites
- Python 3.8 or higher
- Git
- Docker (optional, for containerized deployment)

### Local Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/musagithub1/One_Health_AI_Platform.git
   cd One_Health_AI_Platform
   ```

2. **Create Virtual Environment**
   ```bash
   # Using venv
   python -m venv one_health_env
   
   # Activate virtual environment
   # On Windows
   one_health_env\Scripts\activate
   
   # On macOS/Linux
   source one_health_env/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   streamlit run enhanced_app.py
   ```

5. **Access the Platform**
   - Open your web browser and navigate to `http://localhost:8501`
   - The One Health AI Platform dashboard will be available

## 🐳 Docker Support

### Quick Start with Docker

**Pull and Run from Docker Hub:**
```bash
docker pull musagithub1/one-health-ai:latest
docker run -p 8501:8501 musagithub1/one-health-ai:latest
```

### Building from Source

1. **Build Docker Image**
   ```bash
   docker build -t musagithub1/one-health-ai .
   ```

2. **Run Docker Container**
   ```bash
   docker run -p 8501:8501 musagithub1/one-health-ai
   ```

3. **Push to Docker Hub** (for maintainers)
   ```bash
   docker tag musagithub1/one-health-ai musagithub1/one-health-ai:latest
   docker push musagithub1/one-health-ai:latest
   ```

### Docker Hub
[![Docker Hub](https://img.shields.io/badge/Docker%20Hub-musagithub1%2Fone--health--ai-blue?logo=docker)](https://hub.docker.com/r/musagithub1/one-health-ai)

Access the official Docker image: `musagithub1/one-health-ai`

## 📁 File Structure

```
One_Health_AI_Platform/
├── enhanced_app.py              # Main Streamlit application entry point
├── Dockerfile                   # Docker containerization configuration
├── requirements.txt             # Python dependencies and libraries
├── README.md                   # Project documentation (this file)
├── qr_utils.py                 # QR code generation and processing utilities
├── generate_sample_data.py     # Sample data generation for testing
├── database.py                 # Database connection and management
├── lost_pet_recovery.py        # Lost pet search and recovery algorithms
├── enhanced_dashboard.py       # Advanced dashboard components and analytics
├── medical_records.py          # Medical records management system
├── dashboard.py                # Core dashboard functionality
└── pet_registration.py         # Pet registration and profile management
```

### File Descriptions

| File | Description |
|------|-------------|
| `enhanced_app.py` | Main application file containing the Streamlit interface and navigation |
| `pet_registration.py` | Handles pet registration, profile creation, and basic information management |
| `medical_records.py` | Manages comprehensive medical history, treatments, and health records |
| `dashboard.py` | Core dashboard with basic analytics and data visualization |
| `enhanced_dashboard.py` | Advanced dashboard with AI-powered insights and comprehensive reporting |
| `lost_pet_recovery.py` | Implements search algorithms and recovery systems for lost pets |
| `database.py` | Database operations, connections, and data persistence layer |
| `qr_utils.py` | QR code generation, processing, and pet identification utilities |
| `generate_sample_data.py` | Creates sample datasets for testing and demonstration purposes |

## 📖 Usage

### Getting Started

1. **Launch the Application**
   - Start the application using either local installation or Docker
   - Access the web interface at `http://localhost:8501`

2. **Navigate the Dashboard**
   - Use the sidebar navigation to access different modules
   - Select your user type (Veterinarian, Pet Owner, or Animal Shelter)

### Main Modules

#### 🐕 Pet Registration
- Register new pets with comprehensive details
- Upload pet photos and documents
- Generate unique pet IDs and QR codes
- Manage owner information and contact details

#### 🏥 Medical Records
- Track vaccination history and schedules
- Record medical treatments and procedures
- Monitor health metrics and vital signs
- Generate health reports and certificates

#### 📊 Dashboard Analytics
- View comprehensive health statistics
- Monitor vaccination compliance rates
- Track pet population demographics
- Generate custom reports and insights

#### 🔍 Lost Pet Recovery
- Report lost pets with detailed descriptions
- Search database for found pets
- Match pets using AI algorithms
- Coordinate recovery efforts

### User Types

- **Veterinarians**: Full access to medical records, treatment history, and professional tools
- **Pet Owners**: Access to their pets' information, health records, and recovery services
- **Animal Shelters**: Bulk pet management, adoption tracking, and population analytics

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help improve the One Health AI Platform:

### How to Contribute

1. **Fork the Repository**
   ```bash
   git fork https://github.com/musagithub1/One_Health_AI_Platform.git
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**
   - Follow Python PEP 8 style guidelines
   - Add comments and documentation
   - Include unit tests for new features

4. **Commit and Push**
   ```bash
   git commit -m "Add: Description of your feature"
   git push origin feature/your-feature-name
   ```

5. **Submit a Pull Request**
   - Provide a clear description of changes
   - Reference any related issues
   - Ensure all tests pass

### Development Guidelines

- **Code Style**: Follow PEP 8 Python style guide
- **Documentation**: Update README and inline comments
- **Testing**: Include unit tests for new functionality
- **Compatibility**: Ensure compatibility with Python 3.8+

### Areas for Contribution

- 🔧 New AI/ML algorithms for health analysis
- 🎨 UI/UX improvements and enhancements
- 📱 Mobile responsiveness optimization
- 🔒 Security and privacy enhancements
- 🌐 Internationalization and localization
- 📊 Advanced analytics and reporting features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 One Health AI Platform

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 📞 Contact & Support

### 🔗 Links
- **GitHub Repository**: [https://github.com/musagithub1/One_Health_AI_Platform](https://github.com/musagithub1/One_Health_AI_Platform)
- **Docker Hub**: [https://hub.docker.com/r/musagithub1/one-health-ai](https://hub.docker.com/r/musagithub1/one-health-ai)

### 💬 Get Help
- **Issues**: Report bugs and request features via [GitHub Issues](https://github.com/musagithub1/One_Health_AI_Platform/issues)
- **Discussions**: Join community discussions on [GitHub Discussions](https://github.com/musagithub1/One_Health_AI_Platform/discussions)

### 🚀 Quick Links
- [Installation Guide](#-installation-instructions)
- [Docker Setup](#-docker-support)
- [Contributing Guidelines](#-contributing)
- [File Structure](#-file-structure)

---

<div align="center">

**Made with ❤️ for the One Health Community**

[![GitHub stars](https://img.shields.io/github/stars/musagithub1/One_Health_AI_Platform.svg?style=social&label=Star)](https://github.com/musagithub1/One_Health_AI_Platform)
[![GitHub forks](https://img.shields.io/github/forks/musagithub1/One_Health_AI_Platform.svg?style=social&label=Fork)](https://github.com/musagithub1/One_Health_AI_Platform)

</div>