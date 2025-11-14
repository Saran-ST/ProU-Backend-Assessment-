from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>ProU Backend Assessment – API Dashboard</title>

        <!-- Google Font -->
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">

        <!-- Icons -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>

        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: 'Poppins', sans-serif;
                background: linear-gradient(135deg, #7E57C2, #5E35B1);
                color: #fff;
            }

            .container {
                max-width: 1100px;
                margin: 60px auto;
                padding: 20px;
            }

            .title {
                font-size: 36px;
                font-weight: 600;
                text-align: center;
                margin-bottom: 10px;
            }

            .subtitle {
                font-size: 18px;
                text-align: center;
                margin-bottom: 40px;
                opacity: 0.9;
            }

            .grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 25px;
            }

            .card {
                background: #ffffff;
                padding: 25px;
                border-radius: 12px;
                color: #333;
                text-align: center;
                box-shadow: 0 4px 20px rgba(0,0,0,0.15);
                transition: transform .2s, box-shadow .2s;
            }

            .card:hover {
                transform: translateY(-5px);
                box-shadow: 0 8px 25px rgba(0,0,0,0.25);
            }

            .card i {
                font-size: 40px;
                color: #6A1B9A;
                margin-bottom: 15px;
            }

            .card-title {
                font-size: 20px;
                font-weight: 600;
                margin-bottom: 10px;
            }

            .card a {
                text-decoration: none;
                padding: 10px 16px;
                background: #6A1B9A;
                color: #fff;
                border-radius: 6px;
                font-size: 14px;
                transition: 0.2s;
                display: inline-block;
                margin-top: 10px;
            }

            .card a:hover {
                background: #4A148C;
            }

            footer {
                text-align: center;
                margin-top: 50px;
                font-size: 14px;
                opacity: 0.9;
            }
        </style>
    </head>

    <body>
        <div class="container">
        
            <h1 class="title">ProU Backend Assessment – API Dashboard</h1>
            <p class="subtitle">Navigate through the backend API modules using the cards below.</p>

            <div class="grid">

                <div class="card">
                    <i class="fas fa-code"></i>
                    <div class="card-title">Swagger UI</div>
                    <p>Explore all API endpoints interactively.</p>
                    <a href="/swagger/">Open Swagger</a>
                </div>

                

                <div class="card">
                    <i class="fas fa-users"></i>
                    <div class="card-title">Employees API</div>
                    <p>Manage employee records (CRUD & filters).</p>
                    <a href="/api/employees/">View Employees</a>
                </div>

                <div class="card">
                    <i class="fas fa-tasks"></i>
                    <div class="card-title">Tasks API</div>
                    <p>Assign, update, and track employee tasks.</p>
                    <a href="/api/tasks/">View Tasks</a>
                </div>

                <div class="card">
                    <i class="fas fa-chart-line"></i>
                    <div class="card-title">Dashboard</div>
                    <p>View analytics for employees and tasks.</p>
                    <a href="/api/dashboard/">Open Dashboard</a>
                </div>

                <div class="card">
                    <i class="fas fa-key"></i>
                    <div class="card-title">JWT Token</div>
                    <p>Generate authentication token for API access.</p>
                    <a href="/api/token/">Get Token</a>
                </div>

            </div>

            <footer>
                SARAN ST
            </footer>

        </div>
    </body>
    </html>
    """)
