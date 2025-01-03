from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Minhaj's Portfolio</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background-color: #f7f7f7;
                    margin: 0;
                    padding: 0;
                    color: #333;
                }
                header {
                    background-color: #2c3e50;
                    color: white;
                    text-align: center;
                    padding: 50px 0;
                }
                header h1 {
                    font-size: 3em;
                    margin: 0;
                }
                section {
                    padding: 30px;
                    margin: 20px;
                }
                .intro {
                    text-align: center;
                }
                .skills, .projects, .contact {
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 20px;
                    margin-top: 40px;
                }
                .skills div, .projects div, .contact div {
                    background-color: #ecf0f1;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                }
                .skills h2, .projects h2, .contact h2 {
                    color: #2980b9;
                }
                footer {
                    background-color: #34495e;
                    color: white;
                    text-align: center;
                    padding: 20px;
                    margin-top: 40px;
                }
            </style>
        </head>
        <body>
            <header>
                <h1>Minhaj's Portfolio</h1>
                <p>DevOps Engineer | Data Scientist | Software Developer</p>
            </header>
            <section class="intro">
                <h2>About Me</h2>
                <p>Hi! I'm Minhaj, a passionate developer with a focus on DevOps and Data Science. I love solving complex problems and building efficient systems.</p>
            </section>
            <section class="skills">
                <div>
                    <h2>Skills</h2>
                    <ul>
                        <li>DevOps Tools</li>
                        <li>Docker, Kubernetes</li>
                        <li>AWS, GCP</li>
                        <li>Python, PHP, JavaScript</li>
                    </ul>
                </div>
                <div>
                    <h2>Experience</h2>
                    <p>I've worked with multiple technologies, including cloud computing, containerization, and automation. Currently focusing on optimizing cloud infrastructure.</p>
                </div>
            </section>
            <section class="projects">
                <div>
                    <h2>Projects</h2>
                    <ul>
                        <li>Magento Docker Setup</li>
                        <li>Elasticsearch Configuration for E-commerce</li>
                        <li>Data Science Projects on Kaggle</li>
                    </ul>
                </div>
                <div>
                    <h2>Contact</h2>
                    <p>Email: minhaj@example.com</p>
                    <p>LinkedIn: linkedin.com/in/minhaj</p>
                </div>
            </section>
            <footer>
                <p>&copy; 2025 Minhaj. All Rights Reserved.</p>
            </footer>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
