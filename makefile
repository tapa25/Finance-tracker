# 🛠️ Project Makefile

.PHONY: help requirements clean

# 🎯 Default target
help:
	@echo "📖 Usage:"
	@echo "   make requirements   - Generate requirements.txt"
	@echo "   make clean          - Clean up temporary files"

# 📦 Dependencies
requirements:
	@echo "🚀 Generating requirements.txt..."
	@pip freeze > requirements.txt
	@echo "✅ requirements.txt has been created successfully!"

# 🧹 Cleanup
clean:
	@echo "🧹 Cleaning up temporary files..."
	@find . -name '__pycache__' -exec rm -rf {} +
	@find . -name '*.pyc' -exec rm -rf {} +
	@find . -name '*.pyo' -exec rm -rf {} +
	@echo "✅ Cleanup complete!"
