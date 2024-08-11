

# Assignment Solver
This project is a web-based application designed to help users solve academic assignments. The application leverages OCR technology and AI models to process assignment files and generate solutions. The project consists of two main parts: a backend built with Flask and a frontend built with Angular.

## Table of Contents
### Features
### Setup Instructions
#### Windows Setup
##### Backend Setup (Windows)
1. **Navigate to the Backend Folder:**
    ```bash
    cd AssignmentSolver/AssignmentSolverBackend
    ```
2. **Install Required Packages:**
Run the following command to install all necessary Python packages:
    ```bash
    pip install -r requirements.txt
    ```

    Note: The installation can be quite large, requiring 5-6 GB of space. If you have a GPU, keep the paddlepaddle-gpu module for accelerated OCR. If not, remove this module from `requirements.txt` to save approximately 1.5 GB of space and bandwidth.


3. **Configure API Key:**

    In the AssignmentSolverBackend folder, locate the .env file.
    Add your Google Gemini API key to the .env file. The model used is gemini-1.5-flash.
4. **Start the Backend Server:**
After the installation is complete, start the server:
    ```bash
    python Pserver.py
    ```

   The backend server will run on port 5000.

##### Frontend Setup (Windows)
1. **Navigate to the Frontend Folder:**
    ```bash
    cd AssignmentSolver/Frontend_AssignmentSolver
    ```
2. **Install Angular CLI (if not already installed):**
    Ensure you have Angular CLI version 18 installed:
    ```bash
    npm install -g @angular/cli@18.1.0
    ```

3. **Install Dependencies:**
    Install all the necessary packages:
    ```bash
    npm install
    ```

   Start the Frontend Server:
    ```bash
    ng serve
    ```

   The frontend will run on port 4200.

### Ubuntu Setup

#### Backend Setup (Ubuntu)

1. **Navigate to the Backend Folder:**
    ```bash
    cd AssignmentSolver/Backend_Assignment-Solver
    ```
2. **Give Execute Permissions to the Setup Script:**
    ```bash
    chmod +x Ubuntusetup.sh
    ```

3. **Configure API Key:**

    In the AssignmentSolverBackend folder, locate the .env file.
    Add your Google Gemini API key to the .env file. The model used is gemini-1.5-flash.

4. **Run the Setup Script:**
    ```bash
    ./Ubuntusetup.sh
    ```

#### Frontend Setup (Ubuntu)

1. **Navigate to the Frontend Folder:**
    ```bash
    cd AssignmentSolver/Frontend_AssignmentSolver
    ```
2. **Install Angular CLI (if not already installed):**
    Ensure you have Angular CLI version 18 installed:
    ```bash
    npm install -g @angular/cli@18.1.0
    ```

3. **Install Dependencies:**
    Install all the necessary packages:
    ```bash
    npm install
    ```

   Note: If you encounter dependency errors on Ubuntu, try using `yarn install` instead:
    ```bash
    yarn install
    ```
4. **Start the Frontend Server:**
    After installing dependencies, start the frontend:
    ```bash
    ng serve
    ```

## Usage

1. Make sure the backend server is running on port 5000.
2. Correct syntax in this Markdown file
3. Start the frontend server using `ng serve`.
4. Open your browser and go to http://localhost:4200.

### Additional Notes
#### Additional Information Field:
The "Additional Information" field in the form is crucial if you want to customize the prompt further. However, be cautious when using it, as incorrect or irrelevant information might alter the output of the solution document.

