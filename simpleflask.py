from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Minhaj's Portfolio</title>
            <style>
                /* Base Reset */
                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }
                body {
                    font-family: 'Roboto', sans-serif;
                    background: #0f2027;
                    color: #f5f5f5;
                    overflow-x: hidden;
                }
                header {
                    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                    text-align: center;
                    padding: 80px 20px;
                    clip-path: polygon(0 0, 100% 0, 100% 85%, 0 100%);
                }
                header h1 {
                    font-size: 3.5rem;
                    margin-bottom: 20px;
                    color: #4caf50;
                    animation: fadeIn 1.5s ease-in-out;
                }
                header p {
                    font-size: 1.2rem;
                    color: #cfd8dc;
                    animation: fadeIn 2s ease-in-out;
                }
                .container {
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 20px;
                }
                .section {
                    margin: 40px 0;
                    padding: 30px;
                    background: #1a252f;
                    border-radius: 15px;
                    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.5);
                    transition: transform 0.3s, background 0.3s;
                }
                .section:hover {
                    transform: scale(1.03);
                    background: #243645;
                }
                .section h2 {
                    font-size: 2.5rem;
                    margin-bottom: 20px;
                    color: #4caf50;
                    border-bottom: 3px solid #4caf50;
                    display: inline-block;
                }
                .grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                    gap: 20px;
                }
                .card {
                    background: #243645;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
                    transition: transform 0.3s ease;
                }
                .card:hover {
                    transform: translateY(-10px);
                    background: #2c3e50;
                }
                .card h3 {
                    color: #4caf50;
                    margin-bottom: 15px;
                }
                footer {
                    background: linear-gradient(135deg, #0f2027, #1a252f);
                    text-align: center;
                    padding: 20px;
                    color: #cfd8dc;
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
                    from {
                        opacity: 0;
                        transform: translateY(-20px);
                    }
                    to {
                        opacity: 1;
                        transform: translateY(0);
                    }
                }
            </style>
        </head>
        <body>
            <header>
                <h1>Minhaj S.</h1>
                <p>Innovating the Future | DevOps | AWS | Cloud Architect</p>
            </header>
            <div class="container">
                <section class="section">
                    <h2>About Me</h2>
                    <p>
                        I'm Minhaj, an aspiring cloud engineer with expertise in AWS, Terraform, and CI/CD pipelines. 
                        I love leveraging technology to design scalable solutions and bring impactful changes to the digital space.
                    </p>
                </section>
                <section class="section">
                    <h2>Skills</h2>
                    <div class="grid">
                        <div class="card">
                            <h3>Technical Expertise</h3>
                            <ul>
                                <li>AWS (EC2, S3, RDS)</li>
                                <li>Terraform & CloudFormation</li>
                                <li>CI/CD (GitHub Actions)</li>
                                <li>Containerization: Docker & Kubernetes</li>
                            </ul>
                        </div>
                        <div class="card">
                            <h3>Core Strengths</h3>
                            <ul>
                                <li>Problem Solving</li>
                                <li>Collaboration & Leadership</li>
                                <li>Public Speaking</li>
                                <li>Adaptability & Innovation</li>
                            </ul>
                        </div>
                    </div>
                </section>
                <section class="section">
                    <h2>Experience</h2>
                    <div class="card">
                        <h3>DevOps Intern - Sahaba Solutions LLP</h3>
                        <ul>
                            <li>Reduced downtime by 20% by designing AWS architectures.</li>
                            <li>Automated provisioning with Terraform, improving speed by 30%.</li>
                            <li>Enhanced CI/CD pipelines for seamless deployments.</li>
                            <li>Boosted system uptime by 25% with effective monitoring.</li>
                        </ul>
                    </div>
                </section>
                <section class="section">
                    <h2>Projects</h2>
                    <div class="grid">
                        <div class="card">
                            <h3>Elasticsearch Setup for Magento</h3>
                            <p>Optimized Magento search functionality by 25% using Elasticsearch. Published a guide read by 500+ developers.</p>
                        </div>
                        <div class="card">
                            <h3>MySQL Backups to S3</h3>
                            <p>Developed automated MySQL backup workflows using AWS CLI and IAM, ensuring data security and scalability.</p>
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
                <p>&copy; 2025 Minhaj S. | <a href="https://github.com/Minhajms" target="_blank">GitHub</a></p>
            </footer>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
