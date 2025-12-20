# 🐳 Dockerfile Generator using Local LLM

Automate Dockerfile generation for any project using locally hosted LLM (Ollama). This tool automatically creates optimized Dockerfiles based on your project specifications - completely FREE and offline!

## 🌟 Features

- ✅ **Automatic Project Detection** - Detects Python, Node.js, Java, and Go projects
- ✅ **AI-Powered Generation** - Uses Llama3 via Ollama for intelligent Dockerfile creation
- ✅ **100% FREE** - No API costs, runs completely offline
- ✅ **Best Practices** - Generates production-ready Dockerfiles with optimization
- ✅ **Zero Configuration** - Just point to your project and go!

## 🛠️ Tech Stack

- **Ollama** - Local LLM runtime (FREE)
- **Llama3** - AI model for Dockerfile generation
- **Python** - Automation scripting
- **Docker** - Container platform

## 📋 Prerequisites

- Python 3.7+
- Ollama installed
- 8GB+ RAM recommended
- 5GB+ free disk space (for Llama3 model)

## 🚀 Installation

### Step 1: Install Ollama

**Windows:**
```bash
# Download from https://ollama.com/download
# Run OllamaSetup.exe
```

**Mac/Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Step 2: Download Llama3 Model

```bash
ollama pull llama3
```

### Step 3: Clone & Setup Project

```bash
git clone https://github.com/yourusername/dockerfile-generator.git
cd dockerfile-generator
pip install -r requirements.txt
```

## 💻 Usage

### Basic Usage

```bash
python main.py /path/to/your/project
```

### Interactive Mode

```bash
python main.py
# Enter project path when prompted
```

### Example

```bash
python main.py C:\Users\YourName\my-flask-app
```

**Output:**
```
==================================================
🐳 Dockerfile Generator using Local LLM
==================================================

📂 Analyzing project: C:\Users\YourName\my-flask-app
✅ Detected: Python project
📦 Dependencies: 3 found

🤖 Generating Dockerfile using Ollama (llama3)...

✅ Dockerfile generated successfully!
📁 Saved to: generated\Dockerfile
```

## 📁 Project Structure

```
dockerfile-generator/
├── main.py              # Main entry point
├── analyzer.py          # Project type detection
├── llm_handler.py       # Ollama LLM integration
├── requirements.txt     # Python dependencies
├── generated/           # Generated Dockerfiles
├── README.md           # This file
└── CODE_EXPLANATION.md # Detailed code explanation
```

## 🎯 Supported Project Types

| Project Type | Detection File | Status |
|-------------|----------------|--------|
| Python | `requirements.txt` | ✅ Supported |
| Node.js | `package.json` | ✅ Supported |
| Java | `pom.xml` | ✅ Supported |
| Go | `go.mod` | ✅ Supported |

## 📖 How It Works

1. **Analyze** - Scans project directory for language-specific files
2. **Detect** - Identifies project type and dependencies
3. **Generate** - Sends context to Llama3 via Ollama
4. **Optimize** - AI creates production-ready Dockerfile
5. **Save** - Outputs to `generated/Dockerfile`

## 🎓 What You'll Learn

- Container automation fundamentals
- CI/CD pipeline basics
- LLM integration in real-world applications
- Docker best practices
- Python automation scripting

## 🔧 Configuration

The tool works out-of-the-box with sensible defaults. To customize:

- **Change LLM Model**: Edit `llm_handler.py` → `model='llama3'`
- **Add Project Types**: Edit `analyzer.py` → Add detection logic
- **Modify Prompts**: Edit `llm_handler.py` → Update prompt template

## 🐛 Troubleshooting

### Ollama not found
```bash
# Restart terminal after installation
# Or add to PATH manually
```

### Model not downloaded
```bash
ollama pull llama3
```

### Connection error
```bash
# Start Ollama service
ollama serve
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add support for more languages
- Improve prompt engineering
- Enhance error handling
- Add tests

## 📝 License

MIT License - Feel free to use in your projects!

## 🙏 Acknowledgments

- [Ollama](https://ollama.com/) - Local LLM runtime
- [Meta AI](https://ai.meta.com/) - Llama3 model
- Docker community for best practices

## 📧 Contact

For questions or suggestions, open an issue on GitHub!

---

**⭐ If this project helped you, please star it on GitHub!**

Made with ❤️ by Tanisha Kushwah
