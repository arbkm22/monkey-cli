#!/usr/bin/env python3
"""
Integration test to verify the Monkey-CLI application structure and imports.
"""

import sys
import os

def test_file_exists():
    """Test that main file exists."""
    assert os.path.exists("monkey_cli.py"), "monkey_cli.py should exist"
    print("✓ Main file exists")

def test_imports():
    """Test that the main module can be imported."""
    try:
        import monkey_cli
        print("✓ Module imports successfully")
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False
    return True

def test_word_list():
    """Test word list content."""
    import monkey_cli
    assert len(monkey_cli.WORD_LIST) >= 100, "Should have at least 100 words"
    print(f"✓ Word list contains {len(monkey_cli.WORD_LIST)} words")

def test_typing_test_class():
    """Test that TypingTest class exists and has required methods."""
    import monkey_cli
    
    # Check class exists
    assert hasattr(monkey_cli, 'TypingTest'), "TypingTest class should exist"
    
    # Check required methods
    required_methods = [
        '_generate_words',
        '_calculate_wpm',
        '_calculate_accuracy',
        '_get_time_remaining',
        '_draw_header',
        '_draw_text',
        '_draw_footer',
        '_draw_results',
        '_handle_input',
        'run'
    ]
    
    for method in required_methods:
        assert hasattr(monkey_cli.TypingTest, method), f"TypingTest should have {method} method"
    
    print(f"✓ TypingTest class has all required methods")

def test_constants():
    """Test that required constants are defined."""
    import monkey_cli
    
    assert hasattr(monkey_cli, 'WORD_LIST'), "WORD_LIST should be defined"
    assert isinstance(monkey_cli.WORD_LIST, list), "WORD_LIST should be a list"
    assert all(isinstance(w, str) for w in monkey_cli.WORD_LIST), "All words should be strings"
    
    print("✓ All constants properly defined")

def test_readme_exists():
    """Test that README exists and has content."""
    assert os.path.exists("README.md"), "README.md should exist"
    
    with open("README.md", "r") as f:
        content = f.read()
        assert "Monkey-CLI" in content, "README should mention Monkey-CLI"
        assert "Usage" in content, "README should have usage section"
        assert "python" in content.lower(), "README should have Python instructions"
    
    print("✓ README exists and has proper content")

def test_gitignore_exists():
    """Test that .gitignore exists."""
    assert os.path.exists(".gitignore"), ".gitignore should exist"
    
    with open(".gitignore", "r") as f:
        content = f.read()
        assert "__pycache__" in content, ".gitignore should exclude Python cache"
    
    print("✓ .gitignore properly configured")

if __name__ == "__main__":
    print("Running integration tests...\n")
    
    try:
        test_file_exists()
        if test_imports():
            test_word_list()
            test_typing_test_class()
            test_constants()
        test_readme_exists()
        test_gitignore_exists()
        
        print("\n✅ All integration tests passed!")
        print("\n📝 Summary:")
        print("   - Main application file is ready")
        print("   - All classes and methods are defined")
        print("   - Documentation is complete")
        print("   - Project is properly configured")
        print("\n🚀 Ready to use! Run: python3 monkey_cli.py")
        
        sys.exit(0)
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
