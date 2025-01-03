from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Minhaj's Portfolio</title>
            <style>
                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }
                body {
                    font-family: 'Arial', sans-serif;
                    background: #1e1e2f;
                    color: #ffffff;
                    line-height: 1.6;
                }
                header {
                    background: #4ca1af;
                    text-align: center;
                    padding: 50px 20px;
                }
                header h1 {
                    font-size: 3em;
                    margin-bottom: 10px;
                    color: #ffffff;
                }
                header p {
                    font-size: 1.2em;
                }
                .container {
                    max-width: 1200px;
                    margin: 20px auto;
                    padding: 20px;
                }
                .section {
                    margin: 20px 0;
                    background: #2e2e3e;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
                }
                .section h2 {
                    color: #4ca1af;
                    font-size: 2em;
                    margin-bottom: 10px;
                    border-bottom: 2px solid #4ca1af;
                    display: inline-block;
                }
                .grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                    gap: 20px;
                }
                .card {
                    background: #38384a;
                    border-radius: 8px;
                    padding: 20px;
                    color: #ffffff;
                    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.4);
                    transition: transform 0.3s ease-in-out;
                }
                .card:hover {
                    transform: scale(1.05);
                }
                .card h3 {
                    margin-bottom: 10px;
                    color: #4ca1af;
                }
                footer {
                    text-align: center;
                    padding: 20px;
                    background: #4ca1af;
                    color: #ffffff;
                }
                footer a {
                    color: #ffffff;
                    text-decoration: none;
                    font-weight: bold;
                }
                footer a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <header>
                <h1>Minhaj S.</h1>
                <p>Aspiring AWS Engineer | DevOps Enthusiast | Data Scientist</p>
            </header>
            <div class="container">
                <section class="section">
                    <h2>About Me</h2>
                    <p>
                        Hi! I'm Minhaj, a passionate professional with expertise in cloud infrastructure, DevOps, and data science. 
                        My goal is to design efficient systems and contribute to scalable projects leveraging cutting-edge technologies.
                    </p>
                </section>
                <section class="section">
                    <h2>Skills</h2>
                    <div class="grid">
                        <div class="card">
                            <h3>Technical</h3>
                            <ul>
                                <li>AWS (EC2, S3, RDS)</li>
                                <li>Terraform & CloudFormation</li>
                                <li>CI/CD (GitHub Actions)</li>
                                <li>Docker & Kubernetes</li>
                            </ul>
                        </div>
                        <div class="card">
                            <h3>Soft Skills</h3>
                            <ul>
                                <li>Collaboration & Leadership</li>
                                <li>Problem Solving</li>
                                <li>Public Speaking</li>
                                <li>Adaptability</li>
                            </ul>
                        </div>
                    </div>
                </section>
                <section class="section">
                    <h2>Experience</h2>
                    <div class="card">
                        <h3>DevOps Intern - Sahaba Solutions LLP</h3>
                        <ul>
                            <li>Designed AWS architectures to reduce downtime by 20%.</li>
                            <li>Automated resource provisioning using Terraform, improving speed by 30%.</li>
                            <li>Enhanced CI/CD pipelines, reducing manual interventions.</li>
                            <li>Monitored resources, improving uptime by 25%.</li>
                        </ul>
                    </div>
                </section>
                <section class="section">
                    <h2>Projects</h2>
                    <div class="grid">
                        <div class="card">
                            <h3>Elasticsearch Setup for Magento</h3>
                            <p>Optimized Magento search by 25% using Elasticsearch. Published a guide reaching 500+ developers.</p>
                        </div>
                        <div class="card">
                            <h3>MySQL Backups to S3</h3>
                            <p>Implemented automated MySQL backups with AWS CLI and IAM for secure data retention.</p>
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
