#!/bin/bash

# One Health AI Platform - Installation Script
# This script sets up the complete One Health AI Platform

echo "🐕🐱 One Health AI Platform - Installation Script"
echo "================================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Check if Python is installed
check_python() {
    if command -v python3 &> /dev/null; then
        python_version=$(python3 --version 2>&1 | awk '{print $2}')
        print_status "Python $python_version found"

        # Check if version is 3.8 or higher
        if python3 -c "import sys; exit(0 if sys.version_info >= (3, 8) else 1)"; then
            print_status "Python version is compatible (3.8+)"
        else
            print_error "Python 3.8 or higher is required. Current version: $python_version"
            exit 1
        fi
    else
        print_error "Python 3 is not installed. Please install Python 3.8 or higher."
        exit 1
    fi
}

# Check if pip is installed
check_pip() {
    if command -v pip3 &> /dev/null; then
        print_status "pip3 found"
    else
        print_warning "pip3 not found. Installing pip..."
        python3 -m ensurepip --upgrade
        if [ $? -eq 0 ]; then
            print_status "pip installed successfully"
        else
            print_error "Failed to install pip"
            exit 1
        fi
    fi
}

# Create virtual environment
create_venv() {
    if [ -d "venv" ]; then
        print_warning "Virtual environment already exists. Skipping creation."
    else
        print_info "Creating virtual environment..."
        python3 -m venv venv
        if [ $? -eq 0 ]; then
            print_status "Virtual environment created"
        else
            print_error "Failed to create virtual environment"
            exit 1
        fi
    fi
}

# Activate virtual environment and install dependencies
install_dependencies() {
    print_info "Activating virtual environment and installing dependencies..."

    # Activate virtual environment
    source venv/bin/activate

    # Upgrade pip
    python -m pip install --upgrade pip

    # Install requirements
    if [ -f "requirements.txt" ]; then
        pip install -r requirements.txt
        if [ $? -eq 0 ]; then
            print_status "Dependencies installed successfully"
        else
            print_error "Failed to install dependencies"
            exit 1
        fi
    else
        print_error "requirements.txt not found"
        exit 1
    fi
}

# Initialize database with sample data
init_database() {
    print_info "Initializing database with sample data..."
    source venv/bin/activate
    python generate_sample_data.py <<EOF
1
7
EOF
    if [ $? -eq 0 ]; then
        print_status "Database initialized with sample data"
    else
        print_warning "Database initialization completed (may have had minor issues)"
    fi
}

# Create necessary directories
create_directories() {
    print_info "Creating necessary directories..."
    mkdir -p photos qr_codes uploads backups logs
    print_status "Directories created"
}

# Check if Docker is available (optional)
check_docker() {
    if command -v docker &> /dev/null; then
        print_status "Docker found - You can also use Docker deployment"
        if command -v docker-compose &> /dev/null; then
            print_status "Docker Compose found - Ready for containerized deployment"
        else
            print_warning "Docker Compose not found - Install for easy container management"
        fi
    else
        print_info "Docker not found - Manual installation only"
    fi
}

# Main installation process
main() {
    echo ""
    print_info "Starting One Health AI Platform installation..."
    echo ""

    # Run checks and installation steps
    check_python
    check_pip
    create_venv
    install_dependencies
    create_directories
    init_database
    check_docker

    echo ""
    print_status "🎉 Installation completed successfully!"
    echo ""
    print_info "To start the application:"
    echo "  1. Activate virtual environment: source venv/bin/activate"
    echo "  2. Run the application: streamlit run app.py"
    echo "  3. Open browser to: http://localhost:8501"
    echo ""
    print_info "Alternative Docker deployment:"
    echo "  1. Build and run: docker-compose up -d"
    echo "  2. Access at: http://localhost:8501"
    echo ""
    print_info "For more information, see README.md"
    echo ""
}

# Run main function
main
