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
                    background-color: #f4f6f8;
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
                header p {
                    margin: 10px 0;
                    font-size: 1.2em;
                }
                section {
                    padding: 30px;
                    margin: 20px;
                }
                .grid-container {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                    gap: 20px;
                }
                .grid-item {
                    background-color: #ecf0f1;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                }
                h2 {
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
                <p>Aspiring AWS Engineer | Data Scientist | DevOps Enthusiast</p>
            </header>
            <section>
                <h2>About Me</h2>
                <p>
                    Hi, I'm Minhaj! With hands-on experience in cloud infrastructure and automation, I specialize in AWS, Terraform, and CI/CD workflows. 
                    I am passionate about designing efficient systems, solving complex problems, and optimizing performance.
                </p>
            </section>
            <section>
                <h2>Skills</h2>
                <div class="grid-container">
                    <div class="grid-item">
                        <h3>Technical</h3>
                        <ul>
                            <li>AWS (EC2, S3, RDS)</li>
                            <li>Terraform, CloudFormation</li>
                            <li>CI/CD (GitHub Actions)</li>
                            <li>Bash Scripting, Troubleshooting</li>
                        </ul>
                    </div>
                    <div class="grid-item">
                        <h3>Soft Skills</h3>
                        <ul>
                            <li>Team Collaboration</li>
                            <li>Leadership</li>
                            <li>Public Speaking</li>
                            <li>Adaptability</li>
                        </ul>
                    </div>
                </div>
            </section>
            <section>
                <h2>Experience</h2>
                <p>
                    <strong>DevOps Intern, Sahaba Solutions LLP</strong> <br>
                    Designed AWS architectures, automated resource provisioning, and enhanced CI/CD pipelines. Boosted system uptime by 25% and 
                    streamlined MySQL backups to S3 for secure data retention.
                </p>
            </section>
            <section>
                <h2>Projects</h2>
                <div class="grid-container">
                    <div class="grid-item">
                        <h3>Elasticsearch Setup for Magento</h3>
                        <p>
                            Published a detailed guide on configuring Docker for Elasticsearch. Improved Magento search performance for 100+ users and 
                            reduced setup errors by 30%.
                        </p>
                    </div>
                </div>
            </section>
            <section>
                <h2>Contact</h2>
                <p>Email: minhajoutflow@gmail.com</p>
                <p>Phone: 9562474580</p>
                <p>LinkedIn: <a href="https://www.linkedin.com/in/minhajms" target="_blank">linkedin.com/in/minhajms</a></p>
            </section>
            <footer>
                <p>&copy; 2025 Minhaj S. All Rights Reserved.</p>
            </footer>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
