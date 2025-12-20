import ollama

def generate_dockerfile_ollama(project_info):
    """Generate Dockerfile using Ollama"""
    
    prompt = f"""Generate a production-ready Dockerfile for a {project_info['type']} project.

Project Details:
- Type: {project_info['type']}
- Dependencies: {', '.join(project_info['dependencies']) if project_info['dependencies'] else 'None specified'}"""

    try:
        response = ollama.chat(
            model='llama3',
            messages=[{
                'role': 'user',
                'content': prompt
            }]
        )
        
        dockerfile_content = response['message']['content']
        
        # Clean up the response
        if '```dockerfile' in dockerfile_content:
            dockerfile_content = dockerfile_content.split('```dockerfile')[1].split('```')[0].strip()
        elif '```' in dockerfile_content:
            dockerfile_content = dockerfile_content.split('```')[1].split('```')[0].strip()
        
        return dockerfile_content
    
    except Exception as e:
        return f"Error generating Dockerfile: {str(e)}"
