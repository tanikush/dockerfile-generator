import os
import sys
from analyzer import analyze_project
from llm_handler import generate_dockerfile_ollama

def main():
    print("=" * 50)
    print("Dockerfile Generator using Local LLM")
    print("=" * 50)
    
    # Get project path
    if len(sys.argv) > 1:
        project_path = sys.argv[1]
    else:
        project_path = input("\nEnter project path: ").strip()
    
    # Analyze project
    print(f"\nAnalyzing project: {project_path}")
    project_info = analyze_project(project_path)
    
    if not project_info:
        print("Error: Project path not found!")
        return
    
    if project_info['type'] == 'unknown':
        print("Error: Could not detect project type!")
        print("Supported: Python (requirements.txt), Node.js (package.json), Java (pom.xml), Go (go.mod)")
        return
    
    print(f"Detected: {project_info['type']} project")
    if project_info['dependencies']:
        print(f"Dependencies: {len(project_info['dependencies'])} found")
    
    # Generate Dockerfile
    print("\nGenerating Dockerfile using Ollama (llama3)...")
    dockerfile_content = generate_dockerfile_ollama(project_info)
    
    # Save Dockerfile
    output_path = os.path.join('generated', 'Dockerfile')
    os.makedirs('generated', exist_ok=True)
    
    with open(output_path, 'w') as f:
        f.write(dockerfile_content)
    
    print(f"\nDockerfile generated successfully!")
    print(f"Saved to: {output_path}")
    print("\n" + "=" * 50)
    print("Generated Dockerfile:")
    print("=" * 50)
    print(dockerfile_content)
    print("=" * 50)

if __name__ == "__main__":
    main()
