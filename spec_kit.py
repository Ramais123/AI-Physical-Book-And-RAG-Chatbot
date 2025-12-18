#!/usr/bin/env python3
"""
Simplified Spec-Kit for Hackathon
"""

import argparse
import os
from google import genai
from pathlib import Path
from dotenv import load_dotenv  # NEW: Add this

# Load environment variables
load_dotenv()  # NEW: This reads from .env file

# Get API key from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # CHANGED: From .env file

def generate_from_spec(spec_file, output_file):
    """Generate book content from specification"""
    
    # Check if API key exists
    if not GEMINI_API_KEY:
        print("❌ Error: GEMINI_API_KEY not found in .env file")
        print("Please create .env file with: GEMINI_API_KEY=your_key_here")
        return False
    
    # Read spec file
    with open(spec_file, 'r', encoding='utf-8') as f:
        spec_content = f.read()
    
    try:
        # Create client with API key - FIXED LINE
        client = genai.Client(api_key=GEMINI_API_KEY)  # FIXED: Removed " = "" "
        
        # Create prompt
        prompt = """Create a detailed textbook chapter based on this specification.
    
SPECIFICATION:
""" + spec_content + """
    
Create a comprehensive chapter with:
1. Clear explanations
2. Code examples where relevant  
3. Practical exercises
4. Learning objectives review

CHAPTER CONTENT:"""
        
        # Generate content
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )
        
        # Extract title from spec
        title = "Module"
        if "TITLE:" in spec_content:
            title_line = spec_content.split("TITLE:")[1]
            title = title_line.split("\n")[0].strip()
        
        # Create markdown
        markdown_content = f"# {title}\n\n{response.text}\n\n---\n*Generated using Spec-Kit Plus & Gemini AI*\n"
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        # Write output
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"✅ Chapter generated: {output_file}")
        return True
    
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Spec-Kit Plus: Generate textbook content')
    parser.add_argument('--input', required=True, help='Input specification file')
    parser.add_argument('--output', required=True, help='Output markdown file')
    
    args = parser.parse_args()
    
    # Generate content
    generate_from_spec(args.input, args.output)

if __name__ == '__main__':
    main()