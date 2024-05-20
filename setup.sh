#!/bin/bash

# Function to install packages on macOS using Homebrew
install_mac() {
    # Check if Homebrew is installed, install it if not
    if ! command -v brew &> /dev/null; then
        echo "Homebrew not found. Installing Homebrew..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi

    # Update Homebrew
    echo "Updating Homebrew..."
    brew update

    # Install make and Python 3
    echo "Installing make and Python 3..."
    brew install make python
}

# Function to install packages on Windows using Chocolatey (Git Bash/WSL)
install_windows() {
    # Check if Chocolatey is installed, install it if not
    if ! command -v choco &> /dev/null; then
        echo "Chocolatey not found. Installing Chocolatey..."
        set-executionpolicy bypass -scope process -force; iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))
    fi

    # Install make and Python 3
    echo "Installing make and Python 3..."
    choco install make python -y
}

# Function to install packages on Linux (Debian-based)
install_linux() {
    # Update package lists
    echo "Updating package lists..."
    sudo apt-get update

    # Install make and Python 3
    echo "Installing make and Python 3..."
    sudo apt-get install -y make python3 python3-pip
}

# Detect the OS and install accordingly
case "$OSTYPE" in
    darwin*)  install_mac ;;
    linux*)   install_linux ;;
    msys*)    install_windows ;;  # Git Bash
    cygwin*)  install_windows ;;  # Cygwin
    win*)     install_windows ;;  # WSL
    *)        echo "Unsupported OS: $OSTYPE" ;;
esac

echo "Installation complete."
