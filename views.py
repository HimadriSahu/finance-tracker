# hello/views.py
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    """Home page view for Finance Tracker"""
    return HttpResponse("""
    <html>
    <head>
        <title>Finance Tracker</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background-color: #f5f5f5; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { color: #2c3e50; text-align: center; }
            .nav { display: flex; gap: 20px; justify-content: center; margin: 20px 0; }
            .nav a { text-decoration: none; background: #3498db; color: white; padding: 10px 20px; border-radius: 5px; }
            .nav a:hover { background: #2980b9; }
            .features { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 30px 0; }
            .feature { padding: 20px; background: #ecf0f1; border-radius: 5px; text-align: center; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>💰 Finance Tracker</h1>
            <p style="text-align: center; font-size: 18px; color: #7f8c8d;">
                Welcome to your personal finance management system!
            </p>
            
            <div class="nav">
                <a href="/dashboard/">Dashboard</a>
                <a href="/transactions/">Transactions</a>
                <a href="/budget/">Budget</a>
                <a href="/reports/">Reports</a>
            </div>
            
            <div class="features">
                <div class="feature">
                    <h3>📊 Track Expenses</h3>
                    <p>Monitor your daily spending and categorize transactions</p>
                </div>
                <div class="feature">
                    <h3>💳 Manage Income</h3>
                    <p>Record and track all your income sources</p>
                </div>
                <div class="feature">
                    <h3>🎯 Set Budgets</h3>
                    <p>Create budgets and track your progress</p>
                </div>
                <div class="feature">
                    <h3>📈 View Reports</h3>
                    <p>Generate insights with detailed financial reports</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """)

def dashboard(request):
    """Dashboard view with financial overview"""
    return HttpResponse("""
    <html>
    <head>
        <title>Dashboard - Finance Tracker</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; background-color: #f8f9fa; }
            .container { max-width: 1200px; margin: 0 auto; }
            .header { background: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
            .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 30px; }
            .stat-card { background: white; padding: 25px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); text-align: center; }
            .stat-value { font-size: 32px; font-weight: bold; margin: 10px 0; }
            .income { color: #27ae60; }
            .expense { color: #e74c3c; }
            .balance { color: #3498db; }
            .nav-link { display: inline-block; margin: 10px; padding: 8px 16px; background: #3498db; color: white; text-decoration: none; border-radius: 5px; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>📊 Dashboard</h1>
                <a href="/" class="nav-link">← Back to Home</a>
                <a href="/transactions/" class="nav-link">Add Transaction</a>
            </div>
            
            <div class="stats">
                <div class="stat-card">
                    <h3>💰 Total Income</h3>
                    <div class="stat-value income">$0.00</div>
                    <p>This month</p>
                </div>
                <div class="stat-card">
                    <h3>💸 Total Expenses</h3>
                    <div class="stat-value expense">$0.00</div>
                    <p>This month</p>
                </div>
                <div class="stat-card">
                    <h3>💳 Current Balance</h3>
                    <div class="stat-value balance">$0.00</div>
                    <p>Available funds</p>
                </div>
            </div>
            
            <div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                <h3>Recent Transactions</h3>
                <p style="color: #7f8c8d; text-align: center; padding: 40px;">
                    No transactions yet. <a href="/transactions/">Add your first transaction!</a>
                </p>
            </div>
        </div>
    </body>
    </html>
    """)

def transactions(request):
    """Transactions view for adding/viewing transactions"""
    return HttpResponse("""
    <html>
    <head>
        <title>Transactions - Finance Tracker</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; background-color: #f8f9fa; }
            .container { max-width: 800px; margin: 0 auto; }
            .header { background: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
            .form-container { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
            .form-group { margin-bottom: 20px; }
            label { display: block; margin-bottom: 5px; font-weight: bold; color: #2c3e50; }
            input, select, textarea { width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 5px; font-size: 16px; }
            button { background: #27ae60; color: white; padding: 12px 30px; border: none; border-radius: 5px; font-size: 16px; cursor: pointer; }
            button:hover { background: #229954; }
            .nav-link { display: inline-block; margin: 10px; padding: 8px 16px; background: #3498db; color: white; text-decoration: none; border-radius: 5px; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>💳 Transactions</h1>
                <a href="/" class="nav-link">← Back to Home</a>
                <a href="/dashboard/" class="nav-link">Dashboard</a>
            </div>
            
            <div class="form-container">
                <h2>Add New Transaction</h2>
                <form method="post">
                    <div class="form-group">
                        <label for="type">Transaction Type:</label>
                        <select id="type" name="type" required>
                            <option value="">Select Type</option>
                            <option value="income">💰 Income</option>
                            <option value="expense">💸 Expense</option>
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label for="amount">Amount ($):</label>
                        <input type="number" id="amount" name="amount" step="0.01" min="0" required>
                    </div>
                    
                    <div class="form-group">
                        <label for="category">Category:</label>
                        <select id="category" name="category" required>
                            <option value="">Select Category</option>
                            <option value="food">🍔 Food & Dining</option>
                            <option value="transport">🚗 Transportation</option>
                            <option value="shopping">🛍️ Shopping</option>
                            <option value="bills">📄 Bills & Utilities</option>
                            <option value="entertainment">🎬 Entertainment</option>
                            <option value="health">🏥 Healthcare</option>
                            <option value="salary">💼 Salary</option>
                            <option value="freelance">💻 Freelance</option>
                            <option value="investment">📈 Investment</option>
                            <option value="other">📝 Other</option>
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label for="description">Description:</label>
                        <input type="text" id="description" name="description" placeholder="Brief description of transaction">
                    </div>
                    
                    <div class="form-group">
                        <label for="date">Date:</label>
                        <input type="date" id="date" name="date" required>
                    </div>
                    
                    <button type="submit">Add Transaction</button>
                </form>
            </div>
        </div>
        
        <script>
            // Set today's date as default
            document.getElementById('date').valueAsDate = new Date();
        </script>
    </body>
    </html>
    """)

def budget(request):
    """Budget management view"""
    return HttpResponse("""
    <html>
    <head>
        <title>Budget - Finance Tracker</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; background-color: #f8f9fa; }
            .container { max-width: 900px; margin: 0 auto; }
            .header { background: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
            .budget-card { background: white; padding: 25px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 20px; }
            .nav-link { display: inline-block; margin: 10px; padding: 8px 16px; background: #3498db; color: white; text-decoration: none; border-radius: 5px; }
            .progress-bar { width: 100%; height: 20px; background: #ecf0f1; border-radius: 10px; overflow: hidden; margin: 10px 0; }
            .progress { height: 100%; background: #27ae60; transition: width 0.3s; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🎯 Budget Management</h1>
                <a href="/" class="nav-link">← Back to Home</a>
                <a href="/dashboard/" class="nav-link">Dashboard</a>
            </div>
            
            <div class="budget-card">
                <h2>Monthly Budget Overview</h2>
                <p>Set and track your monthly spending limits by category.</p>
                
                <div style="margin: 20px 0;">
                    <h3>🍔 Food & Dining</h3>
                    <div class="progress-bar">
                        <div class="progress" style="width: 0%;"></div>
                    </div>
                    <p>$0 of $500 spent (0%)</p>
                </div>
                
                <div style="margin: 20px 0;">
                    <h3>🚗 Transportation</h3>
                    <div class="progress-bar">
                        <div class="progress" style="width: 0%;"></div>
                    </div>
                    <p>$0 of $300 spent (0%)</p>
                </div>
                
                <div style="margin: 20px 0;">
                    <h3>🛍️ Shopping</h3>
                    <div class="progress-bar">
                        <div class="progress" style="width: 0%;"></div>
                    </div>
                    <p>$0 of $200 spent (0%)</p>
                </div>
                
                <p style="text-align: center; color: #7f8c8d; margin-top: 30px;">
                    Start adding transactions to see your budget progress!
                </p>
            </div>
        </div>
    </body>
    </html>
    """)

def reports(request):
    """Financial reports and analytics view"""
    return HttpResponse("""
    <html>
    <head>
        <title>Reports - Finance Tracker</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; background-color: #f8f9fa; }
            .container { max-width: 1000px; margin: 0 auto; }
            .header { background: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
            .report-card { background: white; padding: 25px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 20px; }
            .nav-link { display: inline-block; margin: 10px; padding: 8px 16px; background: #3498db; color: white; text-decoration: none; border-radius: 5px; }
            .chart-placeholder { height: 200px; background: #ecf0f1; border-radius: 5px; display: flex; align-items: center; justify-content: center; color: #7f8c8d; margin: 20px 0; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>📈 Financial Reports</h1>
                <a href="/" class="nav-link">← Back to Home</a>
                <a href="/dashboard/" class="nav-link">Dashboard</a>
            </div>
            
            <div class="report-card">
                <h2>Spending Analysis</h2>
                <div class="chart-placeholder">
                    📊 Spending by Category Chart
                    <br>
                    (Data will appear after adding transactions)
                </div>
            </div>
            
            <div class="report-card">
                <h2>Income vs Expenses</h2>
                <div class="chart-placeholder">
                    📈 Monthly Trend Chart
                    <br>
                    (Data will appear after adding transactions)
                </div>
            </div>
            
            <div class="report-card">
                <h2>Monthly Summary</h2>
                <p>Total Income: <strong style="color: #27ae60;">$0.00</strong></p>
                <p>Total Expenses: <strong style="color: #e74c3c;">$0.00</strong></p>
                <p>Net Savings: <strong style="color: #3498db;">$0.00</strong></p>
                <p style="color: #7f8c8d; margin-top: 20px;">
                    Add some transactions to see detailed reports and insights!
                </p>
            </div>
        </div>
    </body>
    </html>
    """)