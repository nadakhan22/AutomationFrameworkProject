# DEMOBLAZE Automation Framework

## Overview

Welcome to the DEMOBLAZE Automation Framework! This project automates the testing of the DEMOBLAZE website, accessible at [https://www.demoblaze.com/index.html](https://www.demoblaze.com/index.html). The framework ensures that key functionalities of the website are thoroughly tested, providing confidence in the stability and performance of the application.

## Technologies Used

- **Selenium WebDriver**: Automates web browser interactions, enabling robust testing of web applications.
- **Pytest**: Framework for running test cases, generating reports, and managing test suites.
- **Page Object Model (POM)**: Design pattern used to create a maintainable and scalable test structure.
- **Poetry**: Dependency management and packaging tool that ensures a consistent and reproducible development environment.

## Features

- **Automated Test Cases**: Comprehensive test cases covering critical functionalities such as homepage loading, product search, cart management, checkout process, and user registration.
- **Modular Test Design**: Utilizes the Page Object Model to separate test logic from page interactions, enhancing code maintainability and readability.
- **Alert Handling**: Includes mechanisms to handle browser alerts during test execution.
- **Easy Setup**: Managed dependencies and environment using Poetry for a smooth setup process.

## Getting Started

### Prerequisites

- **Python 3.7+**: Ensure that Python is installed on your machine.
- **Poetry**: For managing dependencies and virtual environments. Install Poetry by following the instructions at [Poetry Installation](https://python-poetry.org/docs/#installation).

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/your-repository.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd your-repository
   ```

3. **Install Dependencies**

   ```bash
   poetry install
   ```

4. **Activate the Virtual Environment**

   ```bash
   poetry shell
   ```

### Running Tests

1. **Execute Test Cases**

   Run the test suite using Pytest:

   ```bash
   pytest
   ```

2. **Generate Test Reports**

   Test reports will be generated in the default format. To view detailed reports, check the `reports` directory.

## Usage

- **Test Cases**: The test cases are defined in the `tests` directory and organized using the Page Object Model.
- **Configuration**: Configuration settings for the test cases can be adjusted in the `config` directory.
- **Handling Alerts**: The framework includes mechanisms to handle various browser alerts during test execution.

## Challenges & Learnings

- **Automating Alerts**: Encountered challenges in handling browser alerts, which were addressed by implementing effective alert management strategies.
- **Page Object Model**: Improved test maintainability and reduced code duplication through the use of the Page Object Model.
- **Dependency Management**: Poetry facilitated a consistent development environment and simplified dependency management.

## Contributing

We welcome contributions to improve this framework. To contribute:

1. **Fork the Repository**
2. **Create a Feature Branch**

   ```bash
   git checkout -b feature/your-feature
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m "Add new feature"
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/your-feature
   ```

5. **Create a Pull Request**

   Submit a pull request to the `main` branch with a description of your changes.

