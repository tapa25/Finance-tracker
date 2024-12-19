# 🛠️ Project Makefile

.PHONY: help requirements clean makemigrations migrate collectstatic runserver test

# 🎯 Default target
help:
	@echo "📖 Usage:"
	@echo "       make help           	- Show this help message"
	@echo "📦 Dependencies:"
	@echo "       make requirements   	- Generate requirements.txt"
	@echo "🧹 Cleanup:"
	@echo "       make clean          	- Clean up temporary files"
	@echo "🗄️ Django Management Commands:"
	@echo "       make runserver      	- Start the Django development server"
	@echo "🧪 Testing:"
	@echo "       make test           	- Run tests using pytest"

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
	@find . -name '*.pytest_cache' -exec rm -rf {} +
	@echo "✅ Cleanup complete!"

# 🗄️ Django Management Commands
runserver:
	@echo "🌐 Starting the Django development server..."
	@python manage.py makemigrations
	@python manage.py migrate
	@python manage.py collectstatic --noinput
	@python manage.py runserver
	@echo "✅ Server is running!"

# 🧪 Testing
test:
	@echo "🧪 Running tests with pytest..."
	@pytest
	@echo "✅ Tests completed!"
