import os

def analyze_project(project_path):
    """Analyze project and detect type and dependencies"""
    
    if not os.path.exists(project_path):
        return None
    
    project_info = {
        'type': 'unknown',
        'dependencies': [],
        'files': []
    }
    
    # Check for Node.js
    if os.path.exists(os.path.join(project_path, 'package.json')):
        project_info['type'] = 'Node.js'
        project_info['files'].append('package.json')
    
    # Check for Python
    elif os.path.exists(os.path.join(project_path, 'requirements.txt')):
        project_info['type'] = 'Python'
        project_info['files'].append('requirements.txt')
        with open(os.path.join(project_path, 'requirements.txt'), 'r') as f:
            project_info['dependencies'] = [line.strip() for line in f if line.strip()]
    
    # Check for Java
    elif os.path.exists(os.path.join(project_path, 'pom.xml')):
        project_info['type'] = 'Java'
        project_info['files'].append('pom.xml')
    
    # Check for Go
    elif os.path.exists(os.path.join(project_path, 'go.mod')):
        project_info['type'] = 'Go'
        project_info['files'].append('go.mod')
    
    return project_info
