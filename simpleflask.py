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
                    font-family: 'Roboto', sans-serif;
                    background: #121212;
                    color: #ffffff;
                    line-height: 1.6;
                    overflow-x: hidden;
                }
                header {
                    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                    text-align: center;
                    padding: 60px 20px;
                    clip-path: polygon(0 0, 100% 0, 100% 85%, 0 100%);
                }
                header h1 {
                    font-size: 3.5em;
                    margin-bottom: 10px;
                    color: #4caf50;
                    animation: fadeIn 2s ease-in-out;
                }
                header p {
                    font-size: 1.5em;
                    color: #9e9e9e;
                    animation: fadeIn 2s ease-in-out;
                }
                .container {
                    max-width: 1200px;
                    margin: 20px auto;
                    padding: 20px;
                }
                .section {
                    margin: 30px 0;
                    background: #1e1e1e;
                    padding: 30px;
                    border-radius: 15px;
                    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
                    transition: transform 0.3s ease, background 0.3s ease;
                }
                .section:hover {
                    transform: scale(1.02);
                    background: #2e2e2e;
                }
                .section h2 {
                    color: #4caf50;
                    font-size: 2.5em;
                    margin-bottom: 20px;
                    border-bottom: 3px solid #4caf50;
                    display: inline-block;
                }
                .grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                    gap: 20px;
                }
                .card {
                    background: #282828;
                    border-radius: 10px;
                    padding: 20px;
                    color: #ffffff;
                    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.4);
                    transition: transform 0.3s ease-in-out;
                }
                .card:hover {
                    transform: translateY(-10px);
                    background: #333333;
                }
                .card h3 {
                    margin-bottom: 10px;
                    color: #4caf50;
                }
                footer {
                    text-align: center;
                    padding: 20px;
                    background: #0f2027;
                    color: #ffffff;
                    margin-top: 30px;
                }
                footer a {
                    color: #4caf50;
                    text-decoration: none;
                    font-weight: bold;
                }
                footer a:hover {
                    text-decoration: underline;
                }
                @keyframes fadeIn {
                    0% {
                        opacity: 0;
                        transform: translateY(-20px);
                    }
                    100% {
                        opacity: 1;
                        transform: translateY(0);
                    }
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
                        Hi, I'm Minhaj! A tech enthusiast with hands-on experience in AWS, DevOps, and automation. I aim to innovate and build scalable, efficient systems that solve real-world challenges.
                    </p>
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
                            <li>Designed AWS architectures, reducing downtime by 20%.</li>
                            <li>Automated provisioning with Terraform, improving speed by 30%.</li>
                            <li>Enhanced CI/CD pipelines for faster deployments.</li>
                            <li>Monitored resources, increasing uptime by 25%.</li>
                        </ul>
                    </div>
                </section>
                <section class="section">
                    <h2>Projects</h2>
                    <div class="grid">
                        <div class="card">
                            <h3>Elasticsearch Setup for Magento</h3>
                            <p>Optimized Magento search performance by 25% using Elasticsearch. Published a guide read by 500+ developers.</p>
                        </div>
                        <div class="card">
                            <h3>MySQL Backups to S3</h3>
                            <p>Implemented secure MySQL backups using AWS CLI and IAM, ensuring efficient data retention.</p>
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
