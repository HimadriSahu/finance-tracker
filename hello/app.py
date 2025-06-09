# ====================================================================
# OPTION 1: Main Application Entry Point (Most Common)
# File: app.py (in your project root)
# ====================================================================

import os
import sys
import django
from django.core.management import execute_from_command_line
from django.core.wsgi import get_wsgi_application

# Add project directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finance.settings')

# Initialize Django
django.setup()

class FinanceApp:
    """Main application class for Django Finance App"""
    
    def __init__(self):
        self.application = get_wsgi_application()
    
    def run_server(self, host='127.0.0.1', port=8000):
        """Run development server"""
        print(f"Starting Django Finance App on {host}:{port}")
        execute_from_command_line(['manage.py', 'runserver', f'{host}:{port}'])
    
    def run_migrations(self):
        """Apply database migrations"""
        print("Applying database migrations...")
        execute_from_command_line(['manage.py', 'migrate'])
    
    def create_superuser(self):
        """Create superuser interactively"""
        print("Creating superuser...")
        execute_from_command_line(['manage.py', 'createsuperuser'])
    
    def collect_static(self):
        """Collect static files"""
        print("Collecting static files...")
        execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])
    
    def run_tests(self):
        """Run all tests"""
        print("Running tests...")
        execute_from_command_line(['manage.py', 'test'])

# ====================================================================
# OPTION 2: Flask-style App Factory Pattern
# File: app.py (in your project root)
# ====================================================================

import os
import django
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

def create_app(config_name='development'):
    """Create and configure Django application"""
    
    # Set environment-specific settings
    if config_name == 'production':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finance.settings.production')
    elif config_name == 'testing':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finance.settings.testing')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finance.settings.development')
    
    # Initialize Django
    django.setup()
    
    # Run initial setup
    setup_database()
    
    return get_wsgi_application()

def setup_database():
    """Initialize database with migrations"""
    try:
        call_command('migrate', verbosity=0)
        print("Database migrations applied successfully")
    except Exception as e:
        print(f"Migration error: {e}")

# ====================================================================
# OPTION 3: API Management and Utilities
# File: app.py (in your project root)
# ====================================================================

import os
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finance.settings')
django.setup()

from accounts.models import Account
from budget.models import Budget
from transactions.models import Transaction
from django.contrib.auth.models import User

class FinanceAppManager:
    """Utility class for managing finance app operations"""
    
    @staticmethod
    def create_sample_data():
        """Create sample data for testing"""
        # Create test user
        user, created = User.objects.get_or_create(
            username='testuser',
            defaults={'email': 'test@example.com'}
        )
        
        # Create sample accounts
        checking = Account.objects.get_or_create(
            name='Checking Account',
            defaults={'balance': 5000.00, 'account_type': 'checking'}
        )[0]
        
        savings = Account.objects.get_or_create(
            name='Savings Account', 
            defaults={'balance': 10000.00, 'account_type': 'savings'}
        )[0]
        
        # Create sample transactions
        Transaction.objects.get_or_create(
            account=checking,
            amount=-50.00,
            defaults={'description': 'Grocery Store', 'category': 'food'}
        )
        
        Transaction.objects.get_or_create(
            account=checking,
            amount=-25.00,
            defaults={'description': 'Gas Station', 'category': 'transport'}
        )
        
        # Create sample budget
        Budget.objects.get_or_create(
            name='Monthly Budget',
            defaults={'amount': 3000.00, 'period': 'monthly'}
        )
        
        print("Sample data created successfully!")
    
    @staticmethod
    def get_account_summary():
        """Get summary of all accounts"""
        accounts = Account.objects.all()
        total_balance = sum(acc.balance for acc in accounts)
        
        print("=== ACCOUNT SUMMARY ===")
        for account in accounts:
            print(f"{account.name}: ${account.balance}")
        print(f"Total Balance: ${total_balance}")
        
        return {
            'accounts': accounts,
            'total_balance': total_balance
        }
    
    @staticmethod
    def get_recent_transactions(limit=10):
        """Get recent transactions"""
        transactions = Transaction.objects.order_by('-created_at')[:limit]
        
        print(f"=== RECENT {limit} TRANSACTIONS ===")
        for trans in transactions:
            print(f"{trans.date}: {trans.description} - ${trans.amount}")
        
        return transactions
    
    @staticmethod
    def check_budgets():
        """Check budget status"""
        budgets = Budget.objects.all()
        
        print("=== BUDGET STATUS ===")
        for budget in budgets:
            # Calculate spent amount (this depends on your model structure)
            print(f"{budget.name}: ${budget.amount} allocated")
        
        return budgets

# ====================================================================
# OPTION 4: Command Line Interface
# File: app.py (in your project root)
# ====================================================================

import argparse
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finance.settings')
django.setup()

def main():
    """Main CLI interface for finance app"""
    parser = argparse.ArgumentParser(description='Finance App CLI')
    parser.add_argument('command', choices=[
        'runserver', 'migrate', 'test', 'createuser', 
        'sample-data', 'summary', 'backup'
    ])
    parser.add_argument('--host', default='127.0.0.1', help='Server host')
    parser.add_argument('--port', default='8000', help='Server port')
    
    args = parser.parse_args()
    
    if args.command == 'runserver':
        from django.core.management import execute_from_command_line
        execute_from_command_line(['manage.py', 'runserver', f'{args.host}:{args.port}'])
    
    elif args.command == 'migrate':
        from django.core.management import execute_from_command_line
        execute_from_command_line(['manage.py', 'migrate'])
    
    elif args.command == 'test':
        from django.core.management import execute_from_command_line
        execute_from_command_line(['manage.py', 'test'])
    
    elif args.command == 'createuser':
        from django.core.management import execute_from_command_line
        execute_from_command_line(['manage.py', 'createsuperuser'])
    
    elif args.command == 'sample-data':
        FinanceAppManager.create_sample_data()
    
    elif args.command == 'summary':
        FinanceAppManager.get_account_summary()
        FinanceAppManager.get_recent_transactions()
    
    elif args.command == 'backup':
        # Implement backup logic
        print("Backup functionality not implemented yet")

# ====================================================================
# USAGE EXAMPLES
# ====================================================================

if __name__ == '__main__':
    # Option 1 Usage:
    # app = FinanceApp()
    # app.run_server()
    
    # Option 2 Usage:
    # application = create_app('development')
    
    # Option 3 Usage:
    # manager = FinanceAppManager()
    # manager.create_sample_data()
    # manager.get_account_summary()
    
    # Option 4 Usage (CLI):
    main()

# ====================================================================
# RUN COMMANDS:
# ====================================================================
# python app.py runserver
# python app.py migrate  
# python app.py sample-data
# python app.py summary
# python app.py test