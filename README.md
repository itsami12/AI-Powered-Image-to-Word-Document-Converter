# 📝 Image to Word Document Converter

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.28%2B-red)
![Groq](https://img.shields.io/badge/groq-0.4%2B-green)
![License](https://img.shields.io/badge/license-MIT-yellow)

### AI-Powered Notes Extraction using Groq Vision + Streamlit

Transform images containing text, equations, diagrams, and handwritten notes into downloadable Microsoft Word documents with the power of AI.

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage-instructions) • [Demo](#-screenshots)

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Run the App](#️-run-the-app)
- [How It Works](#-how-it-works)
- [Use Cases](#-use-cases)
- [Usage Instructions](#-usage-instructions)
- [Technical Details](#️-technical-details)
- [Security & Privacy](#-security--privacy)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)
- [Contact](#-contact)

---

## 🌟 Overview

This project is a **simple and powerful Streamlit web application** that converts images containing **text, equations, diagrams, and handwritten notes** into a downloadable **Microsoft Word (.docx)** document.

Powered by **Groq's Vision LLaMA-4 Scout 17B model**, the app extracts content **exactly as it appears** in the uploaded images, without modifying, correcting, summarizing, or adding anything extra.

Whether you're a student digitizing lecture notes, a researcher documenting findings, or a professional converting scanned documents, this tool makes the process fast, accurate, and effortless.

---

## 🚀 Features

### 🔍 AI Vision Extraction
- ✅ Processes text, formulas, symbols, bullets, diagrams, and annotations  
- ✅ Extracts content *exactly* as seen (no correction or rewriting)  
- ✅ Supports handwriting, printed text, and mixed content  
- ✅ Handles complex layouts and multiple columns
- ✅ Recognizes mathematical equations and scientific notation

### 📤 Multi-Image Support
- ✅ Upload multiple JPG/JPEG/PNG/WebP files at once
- ✅ Preview all uploaded images before processing
- ✅ Process images in batch mode
- ✅ Support for high-resolution images

### 📄 Word Document Export
- ✅ Automatically generates a `.docx` file  
- ✅ Clean formatting using python-docx  
- ✅ One-click download
- ✅ Preserves structure and organization
- ✅ Ready for further editing

### ⚡ Fast & Efficient
- ✅ Uses **Groq API** for ultra-fast inference  
- ✅ Progress bar for real-time status  
- ✅ Error handling for smooth user experience
- ✅ Optimized image processing
- ✅ Minimal memory footprint

---

## 📁 Project Structure

```
image-to-word-groq/
│
├── app1.py                 # Main Streamlit application
├── requirements.txt        # Project dependencies
├── .env                    # Environment variables (not committed)
├── .gitignore             # Git ignore file
├── README.md              # This documentation file
├── LICENSE                # MIT License file
│
├── screenshots/           # Screenshots for documentation
│   ├── main.png
│   ├── upload.png
│   ├── preview.png
│   └── download.png
│
└── .streamlit/            # Streamlit configuration (optional)
    └── secrets.toml       # API keys (alternative to .env)
```

---

## 📦 Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher** ([Download Python](https://www.python.org/downloads/))
- **pip** (Python package installer)
- **Groq API Key** ([Get it here](https://console.groq.com/))

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/image-to-word-groq.git
cd image-to-word-groq
```

### Step 2: Create a Virtual Environment (Recommended)

Creating a virtual environment helps isolate project dependencies.

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install all required packages:
- `streamlit` - Web framework
- `groq` - Groq API client
- `python-docx` - Word document generation
- `Pillow` - Image processing
- `python-dotenv` - Environment variable management

---

## 🔧 Configuration

### Get Your Groq API Key

1. Visit [Groq Console](https://console.groq.com/)
2. Sign up or log in to your account
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key (you won't see it again!)

### Set Up Environment Variables

You need to configure your Groq API key. Choose **one** of the following methods:

#### Option 1: Using .env File (Recommended)

Create a `.env` file in the project root directory:

```env
GROQ_API_KEY=gsk_your_actual_api_key_here
```

#### Option 2: Export Environment Variable

**On Windows (Command Prompt):**
```cmd
set GROQ_API_KEY=gsk_your_actual_api_key_here
```

**On Windows (PowerShell):**
```powershell
$env:GROQ_API_KEY="gsk_your_actual_api_key_here"
```

**On macOS/Linux:**
```bash
export GROQ_API_KEY="gsk_your_actual_api_key_here"
```

**Make it permanent (macOS/Linux):**
Add to your `~/.bashrc` or `~/.zshrc`:
```bash
echo 'export GROQ_API_KEY="gsk_your_actual_api_key_here"' >> ~/.bashrc
source ~/.bashrc
```

#### Option 3: Streamlit Secrets

Create `.streamlit/secrets.toml` in your project directory:

```toml
GROQ_API_KEY = "gsk_your_actual_api_key_here"
```

---

## ▶️ Run the App

Once installation and configuration are complete, run:

```bash
streamlit run app1.py
```

The app will automatically open in your default browser at:
```
http://localhost:8501
```

If it doesn't open automatically, copy the URL from the terminal and paste it into your browser.

**To stop the app:** Press `Ctrl+C` in the terminal.

---

## 🧠 How It Works

The application follows a simple yet powerful workflow:

```
┌─────────────────┐
│  Upload Images  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Base64 Encoding │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Groq Vision AI │
│   Processing    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Extract Content │
│  • Text         │
│  • Equations    │
│  • Diagrams     │
│  • Symbols      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Display Preview │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Generate .docx  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Download File │
└─────────────────┘
```

### Detailed Process:

1. **User uploads one or more images** (JPG, JPEG, PNG, WebP)
2. **The app base64-encodes them** for secure API transmission
3. **Groq Vision model analyzes and extracts:**
   - Printed text in any font
   - Handwritten notes and annotations
   - Mathematical equations and formulas
   - Symbols and special characters
   - Diagrams, flowcharts, and drawings
   - Arrows, lines, and connections
   - Tables and structured data
   - Lists and bullet points
4. **Extracted content is displayed** in an interactive preview
5. **Word document is generated** with proper formatting
6. **User downloads the .docx file** with a single click

---

## 💡 Use Cases

This tool is perfect for:

### 📚 Education & Learning
- **Digitizing handwritten notes** from lectures or meetings
- **Extracting textbook content** for study materials
- **Converting math equations** to editable format
- **Creating digital flashcards** from written notes
- **Archiving exam papers** and assignments

### 🔬 Research & Academia
- **Research documentation** from lab notebooks
- **Digitizing field notes** and observations
- **Converting scientific diagrams** to text descriptions
- **Extracting data from charts** and graphs
- **Archiving historical documents**

### 💼 Business & Professional
- **Converting scanned documents** into Word format
- **Business card scanning** and data extraction
- **Meeting notes digitization**
- **Whiteboard capture** after brainstorming sessions
- **Invoice and receipt processing**

### 🎨 Creative & Design
- **Extracting text from design mockups**
- **Converting sketches** to textual descriptions
- **Documenting wireframes** and prototypes
- **Archiving creative notes** and ideas

---

## 📋 Usage Instructions

### Step-by-Step Guide

#### 1. Launch the Application

```bash
streamlit run app1.py
```

#### 2. Upload Images

- Click the **"Browse files"** button or **drag-and-drop** images
- Select one or multiple images from your computer
- **Supported formats:** JPG, JPEG, PNG, WebP
- **Recommended:** Images under 10MB for faster processing

#### 3. Preview Your Images

- All uploaded images will be displayed in the interface
- Review each image to ensure they're clear and readable
- You can upload additional images if needed

#### 4. Extract Content

- Click the **"Extract & Convert to Word"** button
- A progress bar will show the extraction status
- Wait for the AI to process all images (usually takes 5-15 seconds per image)

#### 5. Review Extracted Text

- The extracted content will appear in a text preview area
- Review the content for accuracy
- Check if all text, equations, and symbols were captured

#### 6. Download Word Document

- Click the **"Download Word Document"** button
- The `.docx` file will be saved to your downloads folder
- Open the file in Microsoft Word, Google Docs, or any compatible editor

### Tips for Best Results

✅ **Use high-quality images** with good lighting and contrast  
✅ **Ensure text is clearly visible** and not blurry  
✅ **Avoid extreme angles** - keep images as straight as possible  
✅ **Clean backgrounds** work better than cluttered ones  
✅ **Separate complex pages** into multiple images if needed  

---

## 🛠️ Technical Details

### Model Specifications

- **Model Name:** `llama-4-scout-17b-vision-preview`
- **Provider:** Groq Cloud
- **Parameters:** 17 billion
- **Capabilities:** 
  - Vision-language understanding
  - Optical Character Recognition (OCR)
  - Layout analysis
  - Handwriting recognition
  - Mathematical notation understanding

### Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Frontend** | Streamlit | Web interface and user interaction |
| **AI Model** | Groq Vision LLaMA-4 | Image analysis and text extraction |
| **Document Generation** | python-docx | Word document creation |
| **Image Processing** | Pillow (PIL) | Image manipulation and encoding |
| **Environment Management** | python-dotenv | Configuration and secrets |

### API Details

- **Endpoint:** Groq Cloud API
- **Authentication:** API Key-based
- **Rate Limits:** Check [Groq documentation](https://console.groq.com/docs/rate-limits)
- **Image Encoding:** Base64
- **Max Image Size:** Varies by plan (typically 10-20MB)

### System Requirements

- **OS:** Windows 10/11, macOS 10.14+, Linux (Ubuntu 18.04+)
- **RAM:** Minimum 4GB (8GB recommended)
- **Storage:** 500MB for application and dependencies
- **Internet:** Stable connection required for API calls

---

## 🔒 Security & Privacy

Your data security and privacy are our top priorities:

### ✅ Security Measures

- **API keys stored in environment variables** - Never hardcoded in source code
- **Images processed securely** via encrypted HTTPS connection to Groq API
- **No data stored on server** - All processing is done in memory
- **Local processing** - Images never saved to disk during processing
- **`.env` file excluded** from version control via `.gitignore`

### 📜 Data Handling

- Images are sent to Groq API for processing
- Groq's data retention policy applies (typically not stored long-term)
- Extracted text is only displayed in your browser
- Downloaded Word documents are saved locally on your machine
- No third-party tracking or analytics

### 🔐 Best Practices

- **Never share your API key** publicly or commit it to repositories
- **Rotate API keys** regularly for enhanced security
- **Use environment variables** instead of hardcoding credentials
- **Keep dependencies updated** to patch security vulnerabilities

---

## 🐛 Troubleshooting

### Common Issues and Solutions

#### Issue 1: Module Not Found Error

**Error Message:**
```
ModuleNotFoundError: No module named 'groq'
```

**Solution:**
```bash
pip install -r requirements.txt
```

Make sure you're in the project directory and your virtual environment is activated.

---

#### Issue 2: API Key Not Found

**Error Message:**
```
API key not found or invalid
```

**Solution:**
1. Verify your `.env` file exists in the project root
2. Ensure it contains: `GROQ_API_KEY=your_actual_key_here`
3. Check for typos in the key
4. Restart the Streamlit app after adding the key

**Verify API key is loaded:**
```python
import os
from dotenv import load_dotenv
load_dotenv()
print(os.getenv("GROQ_API_KEY"))  # Should print your key
```

---

#### Issue 3: Image Upload Fails

**Error Message:**
```
Error uploading image or unsupported file type
```

**Solution:**
- Check file format (must be JPG, JPEG, PNG, or WebP)
- Reduce image size if larger than 10MB
- Ensure image is not corrupted
- Try converting to a different supported format

**Reduce image size:**
```bash
# Using ImageMagick
convert input.jpg -resize 50% output.jpg
```

---

#### Issue 4: Slow Processing

**Symptoms:** Extraction takes longer than expected

**Solution:**
- Check your internet connection speed
- Reduce image resolution before upload
- Process fewer images at once
- Verify Groq API status at [status.groq.com](https://status.groq.com)

---

#### Issue 5: Streamlit Won't Start

**Error Message:**
```
Command 'streamlit' not found
```

**Solution:**
```bash
# Ensure streamlit is installed
pip install streamlit

# Or run with python -m
python -m streamlit run app1.py
```

---

#### Issue 6: Port Already in Use

**Error Message:**
```
Port 8501 is already in use
```

**Solution:**
```bash
# Use a different port
streamlit run app1.py --server.port 8502

# Or kill the process using the port (Windows)
netstat -ano | findstr :8501
taskkill /PID <PID> /F

# Or kill the process using the port (macOS/Linux)
lsof -ti:8501 | xargs kill -9
```

---

#### Issue 7: Extraction Accuracy Issues

**Symptoms:** Missing or incorrect text in output

**Solution:**
- Use higher resolution images
- Ensure good lighting and contrast
- Avoid blurry or angled photos
- For handwriting, write clearly and legibly
- Try processing problematic sections separately

---

### Getting Help

If you encounter issues not listed here:

1. Check the [Groq documentation](https://console.groq.com/docs)
2. Review [Streamlit documentation](https://docs.streamlit.io)
3. Open an issue on [GitHub](https://github.com/your-username/image-to-word-groq/issues)
4. Contact support at your.email@example.com

---

## 🤝 Contributing

Contributions are welcome and appreciated! Here's how you can help improve this project:

### How to Contribute

1. **Fork the repository**
   ```bash
   # Click the "Fork" button on GitHub
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/your-username/image-to-word-groq.git
   cd image-to-word-groq
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```

4. **Make your changes**
   - Write clean, documented code
   - Follow existing code style
   - Add comments where necessary

5. **Test your changes**
   ```bash
   streamlit run app1.py
   ```

6. **Commit your changes**
   ```bash
   git add .
   git commit -m 'Add some AmazingFeature'
   ```

7. **Push to your fork**
   ```bash
   git push origin feature/AmazingFeature
   ```

8. **Open a Pull Request**
   - Go to the original repository on GitHub
   - Click "New Pull Request"
   - Describe your changes clearly

### Contribution Guidelines

- Follow PEP 8 style guide for Python code
- Write clear commit messages
- Update documentation for new features
- Add tests if applicable
- Keep pull requests focused on a single feature/fix

### Areas for Contribution

- 🐛 Bug fixes
- ✨ New features
- 📝 Documentation improvements
- 🎨 UI/UX enhancements
- 🧪 Test coverage
- 🌍 Internationalization
- ⚡ Performance optimizations

---

## 📄 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2024 Your Name

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

See the [LICENSE](LICENSE) file for full details.

---

## 🙏 Acknowledgments

This project wouldn't be possible without these amazing technologies and communities:

- **[Groq](https://groq.com/)** - For providing the ultra-fast Vision LLaMA API and making AI accessible
- **[Streamlit](https://streamlit.io/)** - For the incredible web framework that makes building data apps a breeze
- **[python-docx](https://python-docx.readthedocs.io/)** - For reliable Word document generation capabilities
- **[Pillow](https://python-pillow.org/)** - For powerful image processing functionality
- **The Open Source Community** - For continuous inspiration and support

### Special Thanks

- All contributors who help improve this project
- The Streamlit community for sharing knowledge and best practices
- Groq team for their excellent documentation and support

---

## 📧 Contact

**Your Name**

- 🐙 GitHub: [@your-username](https://github.com/your-username)
- 📧 Email: your.email@example.com
- 🐦 Twitter: [@your-twitter](https://twitter.com/your-twitter)
- 💼 LinkedIn: [Your Name](https://linkedin.com/in/your-profile)

**Project Link:** [https://github.com/your-username/image-to-word-groq](https://github.com/your-username/image-to-word-groq)

---

## 🌟 Star This Repository

If you find this project useful, please consider giving it a ⭐ on GitHub! It helps others discover the project and motivates continued development.

---

## 📸 Screenshots

### Main Interface
![Main Interface](screenshots/main.png)
*Clean and intuitive user interface with easy navigation*

### Image Upload
![Image Upload](screenshots/upload.png)
*Drag-and-drop or browse to upload multiple images*

### Extracted Content Preview
![Preview](screenshots/preview.png)
*Real-time preview of extracted text before downloading*

### Download Word Document
![Download](screenshots/download.png)
*One-click download of formatted Word document*

---

## 🔮 Future Enhancements

Planned features and improvements:

- [ ] **PDF file support** - Upload and process PDF documents
- [ ] **Batch processing with ZIP upload** - Process entire folders at once
- [ ] **Multiple export formats:**
  - [ ] Markdown (.md)
  - [ ] Plain text (.txt)
  - [ ] HTML (.html)
  - [ ] PDF (.pdf)
- [ ] **Custom formatting options** - Choose fonts, sizes, and styles
- [ ] **Language translation** - Translate extracted text to different languages
- [ ] **Cloud storage integration:**
  - [ ] Google Drive
  - [ ] Dropbox
  - [ ] OneDrive
- [ ] **OCR confidence scores** - Show accuracy metrics for each extraction
- [ ] **Advanced table extraction** - Better handling of complex tables
- [ ] **LaTeX equation rendering** - Export equations in LaTeX format
- [ ] **Image annotation** - Mark areas for selective extraction
- [ ] **Template support** - Save and reuse formatting templates
- [ ] **API endpoint** - RESTful API for programmatic access
- [ ] **Mobile app** - Native iOS and Android applications
- [ ] **Collaborative features** - Share and collaborate on documents

---

## 📊 Version History

### v1.0.0 (2024-01-22)
- ✅ Initial release
- ✅ Basic image to Word conversion functionality
- ✅ Multi-image upload support
- ✅ Groq Vision LLaMA-4 Scout integration
- ✅ Real-time preview of extracted content
- ✅ One-click Word document download
- ✅ Support for JPG, JPEG, PNG, WebP formats
- ✅ Progress indicators for user feedback
- ✅ Error handling and validation

---

## 📈 Project Stats

![GitHub stars](https://img.shields.io/github/stars/your-username/image-to-word-groq?style=social)
![GitHub forks](https://img.shields.io/github/forks/your-username/image-to-word-groq?style=social)
![GitHub issues](https://img.shields.io/github/issues/your-username/image-to-word-groq)
![GitHub pull requests](https://img.shields.io/github/issues-pr/your-username/image-to-word-groq)

---

## 🎯 Goals

Our mission is to make document digitization:

- **Fast** - Process images in seconds, not minutes
- **Accurate** - Extract content exactly as it appears
- **Accessible** - Free and open-source for everyone
- **Easy** - No technical knowledge required
- **Privacy-focused** - Your data stays yours

---

## 💬 FAQ

**Q: Is this free to use?**  
A: Yes! The project is open-source under MIT license. You only need a free Groq API key.

**Q: How accurate is the extraction?**  
A: Groq's Vision LLaMA-4 Scout model is highly accurate, especially with clear, high-quality images.

**Q: Can I use this for commercial purposes?**  
A: Yes, the MIT license allows commercial use. Check Groq's terms for API usage.

**Q: What's the maximum image size?**  
A: Typically 10-20MB depending on your Groq API plan. We recommend optimizing images first.

**Q: Does it work offline?**  
A: No, an internet connection is required to access the Groq API.

**Q: Can I extract text from PDFs?**  
A: Not yet, but PDF support is planned for future releases.

**Q: Is my data secure?**  
A: Yes, images are processed via secure HTTPS and not stored permanently.

---

<div align="center">

### Made with ❤️ using Streamlit and Groq AI

**Star ⭐ this repo if you find it useful!**

[Report Bug](https://github.com/your-username/image-to-word-groq/issues) • [Request Feature](https://github.com/your-username/image-to-word-groq/issues) • [Documentation](https://github.com/your-username/image-to-word-groq/wiki)

</div>
