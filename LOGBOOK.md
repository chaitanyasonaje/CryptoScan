# 📖 CryptoScan Project - Logbook

**Project Title**: CryptoScan - AI-Powered Cryptographic Algorithm Identification
**Semester**: V (2024-25)
**Stage**: Project Stage-I
**Repository**: [CryptoScan GitHub Repo](https://github.com/chaitanyasonaje/CryptoScan)

---

# 🗕️ Weekly Summary Table 

| Week | Dates                   | Activities Completed                                         |
| :--: | ----------------------- | ------------------------------------------------------------ |
|   1  | 13/01/2025 - 18/01/2025 | Introduction, background, motivation, repo initialization    |
|   2  | 20/01/2025 - 25/01/2025 | Problem statement, objective definition, tech stack planning |
|   3  | 27/01/2025 - 01/02/2025 | Literature survey, limitations of existing systems           |
|   4  | 03/02/2025 - 15/02/2025 | Proposed system architecture, ML model planning              |
|   5  | 17/02/2025 - 22/02/2025 | Software/hardware requirement documentation                  |
|   6  | 24/02/2025 - 01/03/2025 | Implementation methodology and API setup                     |
|   7  | 03/03/2025 - 08/03/2025 | First module: File upload, feature extraction                |
|   8  | 10/03/2025 - 15/03/2025 | Second module: Prediction and dashboard integration          |
|   9  | 17/03/2025 - 22/03/2025 | Third module: Frontend-backend integration, testing          |
|  10  | 24/03/2025 - 29/03/2025 | Finalization, documentation, report writing, outcomes        |

---

# ✨ Weekly Progress Log

## 🗕️ Week 1 (13/01/2025 - 18/01/2025)

### 🔹 **Introduction**

* **Background**: Cryptographic algorithms are essential for securing digital communication and data. With an increasing amount of sensitive information being transferred online, there is a need for automated systems to identify the cryptographic algorithms used.
* **Motivation**: The project aims to leverage machine learning to automate the identification of cryptographic algorithms used in encrypted data. This could assist cybersecurity experts in detecting malicious activity and analyzing encrypted data in a faster, more efficient way.
* **Activities**:

  * Initialized GitHub repository for version control.
  * Defined core objectives and expected outcomes for the project.
  * Chose the tech stack (React.js for frontend, Flask for backend, TensorFlow for ML).

---

## 🗕️ Week 2 (20/01/2025 - 25/01/2025)

### 🔹 **Problem Statement & Objectives**

* Defined the problem: Building an AI-powered cryptographic algorithm identification system that can automatically identify the encryption algorithm used on a given ciphertext.
* Set clear objectives:

  * To build a machine learning model that can predict cryptographic algorithms.
  * To integrate this model into a web interface.
  * To use real-time data for model predictions.
* Decided on the tech stack: React.js, Flask, TensorFlow, MongoDB, and Scikit-learn for machine learning models.

---

## 🗕️ Week 3 (27/01/2025 - 01/02/2025)

### 🔹 **Literature Survey**

* Reviewed existing works on cryptanalysis and automated cryptographic algorithm detection.
* Examined several methods of detecting cryptographic algorithms, including statistical analysis and machine learning models.
* Identified the limitations of existing systems: Many current systems rely on static, predefined datasets and do not use AI models for real-time predictions.
* Summarized findings and documented key insights for future work.

---

## 🗕️ Week 4 (03/02/2025 - 15/02/2025)

### 🔹 **System Architecture and Model Planning**

* Designed the high-level architecture for CryptoScan.

  * **Frontend**: React.js for interactive UI.
  * **Backend**: Flask REST API for handling requests and predictions.
  * **ML Model**: TensorFlow and Scikit-learn for building the machine learning model.
  * **Database**: MongoDB for storing the encrypted files and metadata.
* Planned the feature extraction pipeline:

  * Extract statistical features such as entropy, frequency distribution, and key length from the ciphertext.
* Designed the prediction mechanism using a classification model (Logistic Regression, Random Forest).

---

## 🗕️ Week 5 (17/02/2025 - 22/02/2025)

### 🔹 **Software/Hardware Requirements**

* **Hardware Requirements**:

  * Machine with at least 8GB of RAM for handling large datasets.
  * NVIDIA GPU (for faster ML model training).
* **Software Requirements**:

  * Python 3.8 or higher.
  * TensorFlow for building machine learning models.
  * Flask for backend API.
  * MongoDB for the database.
  * Scikit-learn for model evaluation and feature extraction.

---

## 🗕️ Week 6 (24/02/2025 - 01/03/2025)

### 🔹 **Methodology and API Setup**

* **Model Development**:

  * Defined the machine learning pipeline, starting with data preprocessing and feature extraction.
  * Developed initial models (Logistic Regression, Random Forest).
  * Used Scikit-learn for initial model training.
* **Flask API Setup**:

  * Created the Flask app with endpoints for file uploads and model predictions.
  * Added routes for handling encrypted file uploads and returning predictions.

---

## 🗕️ Week 7 (03/03/2025 - 08/03/2025)

### 🔹 **First Module: File Upload & Feature Extraction**

* Implemented the file upload feature, allowing users to upload encrypted files.
* Developed the feature extraction logic to process the ciphertext and extract meaningful statistical features (e.g., entropy, distribution of byte values, etc.).
* Completed the preprocessing pipeline, making the data ready for model input.
* Trained the first set of models using the dataset of symmetric encryption algorithms.

---

## 🗕️ Week 8 (10/03/2025 - 15/03/2025)

### 🔹 **Second Module: Prediction and Dashboard Integration**

* Built the prediction engine, which takes the extracted features from an encrypted file and classifies it into the correct cryptographic algorithm.
* Integrated the prediction functionality into a frontend dashboard using React.js.
* Displayed results (including algorithm name and confidence level) on the dashboard.
* Added data visualization features (e.g., pie charts, bar graphs).

---

## 🗕️ Week 9 (17/03/2025 - 22/03/2025)

### 🔹 **Third Module: Frontend-Backend Integration and Testing**

* Completed the integration of frontend (React.js) with the Flask backend API.
* Conducted unit testing on individual components (file upload, feature extraction, prediction).
* Fixed bugs and ensured seamless communication between frontend and backend.
* Tested the model's performance and identified areas for improvement.

---

## 🗕️ Week 10 (24/03/2025 - 29/03/2025)

### 🔹 **Finalization and Report Writing**

* Completed the final testing of the system.
* Wrote the final project report, including:

  * Introduction and background.
  * System architecture and design.
  * Results and analysis of model performance.
  * Future work and improvements.
* Generated the final version of the `LOGBOOK.md`.
* Uploaded the final version of the code and documentation to GitHub.

---

# 🚀 Project Highlights

* **AI-Powered**: CryptoScan uses AI to automatically identify cryptographic algorithms, making the detection process faster and more accurate.
* **Modular Design**: The system is built using a modular approach, separating the frontend, backend, and ML layers for easier maintenance.
* **Visual Dashboard**: The dashboard provides a clear and interactive interface for users to upload files and view predictions.
* **Continuous Integration/Continuous Deployment (CI/CD)**: Integrated Jenkinsfile for automated testing and deployment.

---

# 📊 Commit History (Highlights)

* **28/04/2025**: Create `LOGBOOK.md`
* **27/04/2025**: Create `Jenkinsfile` for automated CI/CD pipeline
* **21/04/2025**: Merged remote main with local project
* **03/04/2025**: Model training file
* **03/04/2025**: Extract The Features
* **03/04/2025**: Add files via upload
* **02/03/2025**: Delete src/readme.md
* **02/03/2025**: Create README.MD
* **02/03/2025**: Create readme.md
* **02/03/2025**: Create Dataset for training the model
* **28/02/2025**: Generated Dataset
* **28/02/2025**: Dataset for training the model
* **28/02/2025**: Create main.yml

---

# 📚 Dataset Information

* **Dataset for Training**:
  The dataset includes ciphertexts generated using all symmetric encryption algorithms. These ciphertexts have been pre-processed to extract useful features (e.g., entropy, frequency distribution).
* **Future Plans**:
  The dataset will be expanded to include **hashing algorithms** (e.g., MD5, SHA-1, SHA-256) and **asymmetric encryption algorithms** (e.g., RSA, ECC), further broadening the scope of the model's detection capabilities.

---

# 🗓️ Next Semester Plan (VI - 2025)

* **UI/UX Upgrade**:
  Next semester, the frontend will transition from Flask to **Next.js** for better performance and scalability. Next.js offers server-side rendering, which will make the application faster and more SEO-friendly.
* **Algorithm Expansion**:
  The dataset will be updated to include **hashing algorithms** and **asymmetric encryption algorithms**.
* **Model Refinement**:
  The machine learning models will be fine-tuned with the expanded dataset to improve prediction accuracy.
* **Automation & Deployment**:
  CI/CD pipelines will be further automated using **GitHub Actions** for continuous integration and deployment.

---

# 📚 References

* **TensorFlow Documentation**: For machine learning model building.
* **Flask Web Dev Guide**: For setting up the backend.
* **Scikit-learn Library**: For implementing machine learning algorithms.
* **Cryptography Papers**: For understanding cryptographic algorithms and attack methods.

---

# 🏁 Conclusion

The CryptoScan project is moving toward a complete solution for identifying cryptographic algorithms using AI. With a solid foundation in place, future work will focus on enhancing the model's capabilities and improving the UI. Once the final improvements are made, CryptoScan will be an efficient tool for cryptographic analysis.

> 🔥 Stay tuned for the final release!

---

# 📨 Contact

**Chaitanya Sonaje**
📧 Email: [chaitanyasonaje0205@gmail.com](mailto:chaitanyasonaje0205@gmail.com)
🔗 GitHub: [CryptoScan Repo](https://github.com/chaitanyasonaje/CryptoScan)

---

# 🌟 Thank You for Reviewing! 🌟
