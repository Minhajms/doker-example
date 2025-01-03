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
                    font-family: 'Segoe UI', sans-serif;
                    margin: 0;
                    background: linear-gradient(135deg, #2c3e50, #4ca1af);
                    color: #f7f7f7;
                }
                header {
                    text-align: center;
                    padding: 50px 20px;
                    background-color: #1a252f;
                }
                header h1 {
                    font-size: 3.5em;
                    margin: 0;
                }
                header p {
                    font-size: 1.5em;
                    margin-top: 10px;
                }
                .container {
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 20px;
                }
                .section {
                    margin: 20px 0;
                    padding: 20px;
                    background: rgba(255, 255, 255, 0.1);
                    border-radius: 10px;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                }
                .section h2 {
                    color: #4ca1af;
                    font-size: 2em;
                    margin-bottom: 10px;
                }
                .grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                    gap: 20px;
                }
                .card {
                    background: #ffffff11;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.2);
                    color: #f7f7f7;
                }
                .card h3 {
                    color: #4ca1af;
                    margin-bottom: 10px;
                }
                footer {
                    text-align: center;
                    padding: 20px 0;
                    background: #1a252f;
                    margin-top: 20px;
                }
                footer a {
                    color: #4ca1af;
                    text-decoration: none;
                }
            </style>
        </head>
        <body>
            <header>
                <h1>Minhaj's Portfolio</h1>
                <p>Aspiring AWS Engineer | DevOps Enthusiast | Data Scientist</p>
            </header>
            <div class="container">
                <section class="section">
                    <h2>About Me</h2>
                    <p>Hi, I'm Minhaj! I specialize in cloud infrastructure, automation, and DevOps. With a strong foundation in AWS, Terraform, and CI/CD workflows, I strive to design scalable and efficient systems while optimizing performance.</p>
                </section>
                <section class="section">
                    <h2>Skills</h2>
                    <div class="grid">
                        <div class="card">
                            <h3>Cloud & DevOps</h3>
                            <ul>
                                <li>AWS (EC2, S3, RDS)</li>
                                <li>Terraform & CloudFormation</li>
                                <li>CI/CD (GitHub Actions)</li>
                                <li>Containerization (Docker, Kubernetes)</li>
                            </ul>
                        </div>
                        <div class="card">
                            <h3>Soft Skills</h3>
                            <ul>
                                <li>Collaboration & Leadership</li>
                                <li>Problem-Solving</li>
                                <li>Public Speaking</li>
                                <li>Adaptability</li>
                            </ul>
                        </div>
                    </div>
                </section>
                <section class="section">
                    <h2>Experience</h2>
                    <div class="card">
                        <p><strong>DevOps Intern - Sahaba Solutions LLP</strong></p>
                        <ul>
                            <li>Designed AWS architectures, reducing downtime by 20%.</li>
                            <li>Automated provisioning using Terraform, improving speed by 30%.</li>
                            <li>Optimized CI/CD pipelines with GitHub Actions.</li>
                            <li>Monitored cloud systems, boosting uptime by 25%.</li>
                        </ul>
                    </div>
                </section>
                <section class="section">
                    <h2>Projects</h2>
                    <div class="grid">
                        <div class="card">
                            <h3>Elasticsearch Setup for Magento</h3>
                            <p>Optimized Magento search with Elasticsearch, increasing performance by 25% and reaching 500+ developers through a published guide.</p>
                        </div>
                        <div class="card">
                            <h3>MySQL Backups to S3</h3>
                            <p>Implemented automated MySQL backups to S3 using AWS CLI and IAM, ensuring secure and efficient data retention.</p>
                        </div>
                    </div>
                </section>
                <section class="section">
                    <h2>Contact</h2>
                    <p>Email: minhajoutflow@gmail.com</p>
                    <p>Phone: 9562474580</p>
                    <p>LinkedIn: <a href="https://www.linkedin.com/in/minhajms" target="_blank">linkedin.com/in/minhajms</a></p>
                </section>
            </div>
            <footer>
                <p>&copy; 2025 Minhaj S. All Rights Reserved | <a href="https://github.com/Minhajms" target="_blank">GitHub</a></p>
            </footer>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
