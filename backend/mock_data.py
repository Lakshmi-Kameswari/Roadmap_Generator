# High-quality predefined roadmaps for SkillPath AI
# These represent comprehensive, professional-grade blueprints.

MOCK_ROADMAPS = {
    "python programming": {
        "skill_name": "Python Programming",
        "estimated_duration": "4-5 Months",
        "daily_study_time": "2 Hours",
        "final_outcome": "Build production-ready CLI apps, automate file systems, write OOP code, and build REST APIs with FastAPI.",
        "phases": [
            {
                "phase_number": 1,
                "title": "Python Syntax & Foundations",
                "practice_schedule": "1 Hour Daily",
                "topics": [
                    {
                        "name": "Variables & Basic Types",
                        "subtopics": ["Integer & Float variables", "String manipulation and formatting", "Boolean logic", "Data type casting"]
                    },
                    {
                        "name": "Control Flow & Loops",
                        "subtopics": ["if-elif-else conditional statements", "for loop iteration", "while conditional loop", "break, continue and pass statements"]
                    },
                    {
                        "name": "Functions & Modules",
                        "subtopics": ["Function parameters & return values", "Scope: local vs global", "Importing math/random standard libraries", "Creating custom modules"]
                    }
                ],
                "mini_project": {
                    "title": "Interactive Console Calculator",
                    "description": "Create a console calculator that runs in a loop, parses math symbols, handles decimal calculations, and catches zero-division errors.",
                    "skills_used": ["Variables", "Conditionals", "Loops", "Input Parsing"]
                },
                "major_project": {
                    "title": "Student Registry Directory",
                    "description": "Develop a CLI contact management directory that performs CRUD operations, storing records in a local JSON file.",
                    "skills_used": ["Functions", "JSON Module", "File handling", "Error catching"]
                },
                "milestones": [
                    "Declare variables and perform operations with types",
                    "Construct conditional structures and nesting logic",
                    "Write reusable functions with parameter validation",
                    "Implement basic file reading/writing safely"
                ]
            },
            {
                "phase_number": 2,
                "title": "Object-Oriented Programming (OOP) & Structures",
                "practice_schedule": "1.5 Hours Daily",
                "topics": [
                    {
                        "name": "Advanced Data Structures",
                        "subtopics": ["Lists & standard list index methods", "Tuples & immutable storage", "Dictionaries for key-value", "Sets for unique collections"]
                    },
                    {
                        "name": "Classes & Instances",
                        "subtopics": ["__init__ constructor", "Self parameter and attributes", "Instance vs Class variables", "Dunder/special methods (__str__, __len__)"]
                    },
                    {
                        "name": "OOP Pillars",
                        "subtopics": ["Single & Multiple Inheritance", "Polymorphism & method overriding", "Encapsulation & private attributes", "Abstract base classes"]
                    }
                ],
                "mini_project": {
                    "title": "Library Cataloging Application",
                    "description": "Model a library system containing Book, Member, and Transaction classes to track checkout states using lists and dictionaries.",
                    "skills_used": ["Classes", "Inheritance", "Object associations"]
                },
                "milestones": [
                    "Define user classes and model relationships between objects",
                    "Enforce security via encapsulation using private attributes",
                    "Leverage inheritance to reuse code structure across classes"
                ]
            },
            {
                "phase_number": 3,
                "title": "File Systems, Libraries & APIs",
                "practice_schedule": "2 Hours Daily",
                "topics": [
                    {
                        "name": "Advanced Python Features",
                        "subtopics": ["List and dictionary comprehensions", "Lambda functions & map/filter", "Decorators & custom logging", "Generators & yield"]
                    },
                    {
                        "name": "File Systems & Web Requests",
                        "subtopics": ["Working with the 'os' and 'pathlib' modules", "Handling CSV/Excel data using python libraries", "HTTP request processing with the 'requests' module", "JSON API parsing"]
                    }
                ],
                "mini_project": {
                    "title": "Automated Weather Reporter",
                    "description": "Construct a Python script that calls a public Weather API, retrieves regional conditions, processes coordinates, and writes a neat Markdown weather report to a local folder.",
                    "skills_used": ["requests module", "JSON parsing", "File writes", "Error handling"]
                },
                "milestones": [
                    "Perform API calls and consume JSON responses",
                    "Use file path operations for cross-platform compatibility",
                    "Optimize lists and collections using comprehensions"
                ]
            },
            {
                "phase_number": 4,
                "title": "Web Frameworks & Databases",
                "practice_schedule": "2 Hours Daily",
                "topics": [
                    {
                        "name": "FastAPI Web Apps",
                        "subtopics": ["HTTP Request/Response cycle", "FastAPI app setup", "REST API routes & request bodies", "Path and query parameters"]
                    },
                    {
                        "name": "Databases & ORMs",
                        "subtopics": ["SQLite local database", "SQLAlchemy ORM models", "Database migrations", "CRUD query execution"]
                    }
                ],
                "mini_project": {
                    "title": "Random Password Generator API",
                    "description": "Construct a FastAPI endpoint that takes parameters for length, numbers, and symbols and returns a generated secure string.",
                    "skills_used": ["FastAPI", "Secrets module", "JSON response"]
                },
                "major_project": {
                    "title": "Personal Book List API Service",
                    "description": "Create a fully functional REST API with FastAPI supporting CRUD actions for books, storing them in a local SQLite database using SQLAlchemy.",
                    "skills_used": ["FastAPI", "SQLite", "SQLAlchemy ORM", "JSON serialization"]
                },
                "milestones": [
                    "Spin up a local web server and expose working HTTP API endpoints",
                    "Model database tables and run relationships using SQLAlchemy",
                    "Configure security headers and cross-origin resource sharing (CORS)"
                ]
            }
        ]
    },
    "machine learning & ai": {
        "skill_name": "Machine Learning & AI",
        "estimated_duration": "6-8 Months",
        "daily_study_time": "2 Hours",
        "final_outcome": "Analyze datasets, build and evaluate ML classifiers/regressors, deploy neural networks, and integrate LLM agents.",
        "phases": [
            {
                "phase_number": 1,
                "title": "Math Foundations & Data Analysis",
                "practice_schedule": "1.5 Hours Daily",
                "topics": [
                    {
                        "name": "Linear Algebra & Calculus",
                        "subtopics": ["Vectors, matrices and dot products", "Matrix transposition & inversion", "Partial derivatives & gradient descent", "Eigenvalues and Eigenvectors"]
                    },
                    {
                        "name": "Probability & Statistics",
                        "subtopics": ["Mean, median, mode and variance", "Probability distributions (Normal, Binomial)", "Bayes' Theorem", "Hypothesis testing & p-values"]
                    },
                    {
                        "name": "Python Data Libraries",
                        "subtopics": ["NumPy array operations", "Pandas DataFrame data manipulation", "Matplotlib & Seaborn data visualization", "Data cleaning & handling missing values"]
                    }
                ],
                "mini_project": {
                    "title": "Exploratory Data Analysis (EDA) on Housing Prices",
                    "description": "Download a public housing dataset, clean empty entries, find correlations between features, and plot price distributions and scatter plots.",
                    "skills_used": ["Pandas", "Matplotlib", "Seaborn", "Statistical Analysis"]
                },
                "milestones": [
                    "Perform matrix calculations programmatically",
                    "Load, clean, filter, and aggregate CSV datasets with Pandas",
                    "Create clean statistical visualizations to uncover data trends"
                ]
            },
            {
                "phase_number": 2,
                "title": "Classical Machine Learning",
                "practice_schedule": "2 Hours Daily",
                "topics": [
                    {
                        "name": "Supervised Learning - Regression",
                        "subtopics": ["Simple and Multiple Linear Regression", "Cost functions & Mean Squared Error", "Regularization: Ridge and Lasso", "Model evaluation metrics"]
                    },
                    {
                        "name": "Supervised Learning - Classification",
                        "subtopics": ["Logistic Regression", "Decision Trees & Random Forests", "Support Vector Machines (SVM)", "Evaluation: Accuracy, Precision, Recall, F1-Score, ROC-AUC"]
                    },
                    {
                        "name": "Unsupervised Learning & Preprocessing",
                        "subtopics": ["K-Means clustering", "Dimensionality reduction: Principal Component Analysis (PCA)", "Feature scaling & One-Hot Encoding", "Cross-validation & Hyperparameter tuning (GridSearchCV)"]
                    }
                ],
                "mini_project": {
                    "title": "Customer Churn Predictor",
                    "description": "Build a binary classifier using Scikit-Learn to predict whether a customer will leave a service based on usage patterns. Evaluate using a confusion matrix.",
                    "skills_used": ["Scikit-Learn", "Logistic Regression", "Feature Scaling", "Model Evaluation"]
                },
                "major_project": {
                    "title": "Car Price Valuation Engine",
                    "description": "Construct an end-to-end regression model to estimate used car prices. Train multiple models (Linear, Random Forest), tune hyperparameters, and compare performance.",
                    "skills_used": ["Scikit-Learn", "Random Forest Regressor", "GridSearchCV", "Pipeline"]
                },
                "milestones": [
                    "Preprocess raw text and numeric columns for machine learning compatibility",
                    "Build and validate classification and regression models using Scikit-Learn",
                    "Tune model hyperparameters to resolve overfitting and underfitting"
                ]
            },
            {
                "phase_number": 3,
                "title": "Deep Learning & Neural Networks",
                "practice_schedule": "2 Hours Daily",
                "topics": [
                    {
                        "name": "Neural Network Fundamentals",
                        "subtopics": ["Artificial Neurons (Perceptron)", "Activation functions (Sigmoid, ReLU, Softmax)", "Backpropagation & weights optimization", "Loss functions & Optimizers (Adam, SGD)"]
                    },
                    {
                        "name": "Computer Vision & CNNs",
                        "subtopics": ["Convolutional layers & pooling", "Building image classifiers with PyTorch/TensorFlow", "Data augmentation techniques", "Transfer Learning (ResNet)"]
                    },
                    {
                        "name": "Sequence Models",
                        "subtopics": ["Recurrent Neural Networks (RNN)", "Long Short-Term Memory (LSTM) cells", "Natural Language Processing (NLP) text tokenization", "Word Embeddings (Word2Vec)"]
                    }
                ],
                "mini_project": {
                    "title": "MNIST Digit Classifier",
                    "description": "Train a simple feedforward neural network in PyTorch or TensorFlow to classify handwritten digits (0-9) from the MNIST dataset with >97% accuracy.",
                    "skills_used": ["TensorFlow/PyTorch", "Dense Layers", "Optimizers", "MNIST Dataset"]
                },
                "milestones": [
                    "Explain activation functions, backpropagation, and deep network architectures",
                    "Train a Convolutional Neural Network (CNN) for image recognition",
                    "Implement a text classifier using tokenization and embeddings"
                ]
            },
            {
                "phase_number": 4,
                "title": "Generative AI & LLMs",
                "practice_schedule": "2 Hours Daily",
                "topics": [
                    {
                        "name": "Transformers Architecture",
                        "subtopics": ["Attention mechanism", "Encoder-Decoder structure", "BERT and GPT series models overview"]
                    },
                    {
                        "name": "LLM Application Engineering",
                        "subtopics": ["Prompt engineering techniques", "Retrieval-Augmented Generation (RAG)", "Vector databases (ChromaDB, Pinecone)", "LangChain or LlamaIndex frameworks"]
                    },
                    {
                        "name": "AI Model Deployment",
                        "subtopics": ["Serving models via FastAPI", "Containerizing ML models with Docker", "Gradio/Streamlit interface creation"]
                    }
                ],
                "mini_project": {
                    "title": "PDF Q&A Assistant (RAG)",
                    "description": "Build an app that reads a local PDF, creates text chunks, saves embeddings to a vector DB, and allows users to query the document using a local/free LLM API.",
                    "skills_used": ["LangChain", "Vector DB", "Embeddings", "Streamlit UI"]
                },
                "major_project": {
                    "title": "End-to-End Medical Imaging Diagnostic API",
                    "description": "Build a FastAPI backend hosting a fine-tuned CNN model. Create a React frontend to upload chest X-ray images, serve model classification, and explain results with a text model.",
                    "skills_used": ["FastAPI", "Deep Learning Model", "Docker containerization", "React"]
                },
                "milestones": [
                    "Construct a Retrieval-Augmented Generation pipeline for custom data queries",
                    "Dockerize an ML/AI model service with a web server API",
                    "Deploy an interactive web UI for end-users to interact with an AI model"
                ]
            }
        ]
    },
    "full stack web dev": {
        "skill_name": "Full Stack Web Dev",
        "estimated_duration": "5-6 Months",
        "daily_study_time": "2 Hours",
        "final_outcome": "Build responsive frontend user interfaces, develop scalable server-side REST APIs, model databases, and deploy full applications to the cloud.",
        "phases": [
            {
                "phase_number": 1,
                "title": "Frontend Essentials (HTML, CSS & JS)",
                "practice_schedule": "1.5 Hours Daily",
                "topics": [
                    {
                        "name": "HTML5 & CSS3 Layouts",
                        "subtopics": ["Semantic HTML tags", "CSS Flexbox & Grid systems", "Media queries & Mobile-First Responsive Design", "CSS Variables & Animations"]
                    },
                    {
                        "name": "Modern JavaScript (ES6+)",
                        "subtopics": ["Variables (let/const) & arrow functions", "Array helper methods (map, filter, reduce)", "Asynchronous JS: Promises, Async/Await", "DOM Manipulation & event listeners"]
                    }
                ],
                "mini_project": {
                    "title": "Personal Portfolio Website",
                    "description": "Create a fully responsive, modern portfolio site containing pages for project showcasing, structured contact forms, and custom CSS animations.",
                    "skills_used": ["HTML5", "CSS Grid/Flexbox", "Responsive Design", "Basic DOM Events"]
                },
                "milestones": [
                    "Write semantic, clean, structure-based HTML documents",
                    "Construct responsive interfaces that display correctly on mobile and desktop",
                    "Perform asynchronous HTTP fetch requests to load and display data in JS"
                ]
            },
            {
                "phase_number": 2,
                "title": "Modern Frontend Frameworks (React)",
                "practice_schedule": "2 Hours Daily",
                "topics": [
                    {
                        "name": "React.js Core Concepts",
                        "subtopics": ["Components (Functional) & JSX syntax", "Props (data passing) & State (internal variables)", "React Hooks (useState, useEffect, useRef, useContext)", "Handling forms and form validation"]
                    },
                    {
                        "name": "Ecosystem and Styling",
                        "subtopics": ["React Router for page transitions", "Tailwind CSS integration in React", "Global state management using Zustand or Context API"]
                    }
                ],
                "mini_project": {
                    "title": "Task Planner Board",
                    "description": "Create a Kanban-style task organizer dashboard that allows users to create, delete, and drag tasks between columns, preserving state in local storage.",
                    "skills_used": ["React Components", "State & Effect Hooks", "Tailwind CSS", "Local Storage"]
                },
                "milestones": [
                    "Design and structure reusable React components",
                    "Manage local and global application states across multiple routes",
                    "Apply layout utility styles using Tailwind CSS components"
                ]
            },
            {
                "phase_number": 3,
                "title": "Backend Development & API Design",
                "practice_schedule": "2 Hours Daily",
                "topics": [
                    {
                        "name": "Node.js & Express Server",
                        "subtopics": ["Node.js runtime environment", "Express.js framework setup", "Writing middleware functions", "Exposing REST API CRUD endpoints"]
                    },
                    {
                        "name": "Databases & Schemas",
                        "subtopics": ["SQL (PostgreSQL) vs NoSQL (MongoDB)", "Relational design & database tables", "Mongoose ORM / Prisma Client ORM", "Writing basic queries and aggregations"]
                    },
                    {
                        "name": "Security & Auth",
                        "subtopics": ["Password hashing with bcrypt", "JSON Web Token (JWT) sessionless authentication", "CORS policy and secure API headers"]
                    }
                ],
                "mini_project": {
                    "title": "Secure Expense Tracker API",
                    "description": "Build an Express.js backend that registers users, hashes passwords, verifies logins via JWT, and offers protected endpoints to log expenses.",
                    "skills_used": ["Node.js", "Express", "JWT", "MongoDB / Mongoose"]
                },
                "milestones": [
                    "Build a working local backend server using Node.js and Express",
                    "Implement a secure user registration and JWT-based authentication flow",
                    "Connect an API server to a database and perform structured CRUD queries"
                ]
            },
            {
                "phase_number": 4,
                "title": "Integration, Cloud & Deploy",
                "practice_schedule": "2 Hours Daily",
                "topics": [
                    {
                        "name": "Full Stack Connection",
                        "subtopics": ["Connecting React frontend with Express backend", "Handling cookies and authorization headers", "Error boundary handling & global loading skeletons"]
                    },
                    {
                        "name": "Deployment & DevOps Basics",
                        "subtopics": ["Dockerizing full stack applications", "Hosting Frontends on Vercel/Netlify", "Hosting Backends on Render/Railway", "CI/CD setup using GitHub Actions"]
                    }
                ],
                "major_project": {
                    "title": "Collaborative Workspace Hub",
                    "description": "Construct a full-stack real-time project management dashboard. Includes JWT auth, a database connection to store projects and tasks, real-time update notifications, and a responsive frontend.",
                    "skills_used": ["React", "Express.js", "MongoDB", "Tailwind CSS", "JWT Auth", "Docker"]
                },
                "milestones": [
                    "Dockerize a full-stack application for dev/production parity",
                    "Deploy a connected client-server app securely to cloud platforms",
                    "Expose health checkpoints and configure automated pipelines"
                ]
            }
        ]
    },
    "cybersecurity analyst": {
        "skill_name": "Cybersecurity Analyst",
        "estimated_duration": "6-7 Months",
        "daily_study_time": "2 Hours",
        "final_outcome": "Conduct network security audits, perform basic penetration testing, analyze system logs, and implement defense controls.",
        "phases": [
            {
                "phase_number": 1,
                "title": "Networking & Systems Foundations",
                "practice_schedule": "1.5 Hours Daily",
                "topics": [
                    {
                        "name": "Networking Protocols",
                        "subtopics": ["TCP/IP model vs OSI model layers", "Routing & IP addressing (IPv4, IPv6, Subnetting)", "DNS, HTTP, HTTPS, SSH, FTP protocols", "DHCP and NAT functionality"]
                    },
                    {
                        "name": "Operating Systems (Linux & Windows)",
                        "subtopics": ["Linux Terminal & command-line commands", "Bash scripting for automation", "Active Directory & Windows permission models", "User privilege configuration"]
                    }
                ],
                "mini_project": {
                    "title": "Bash Network Monitoring Script",
                    "description": "Write a bash shell script that runs on Linux, pings hosts, checks for open ports on the local subnet, and outputs anomalies to a log file.",
                    "skills_used": ["Bash Scripting", "Linux Networking Tools", "File Redirection", "Cron Jobs"]
                },
                "milestones": [
                    "Explain routing, subnet masks, and network protocol layers",
                    "Perform intermediate file system and configuration tasks in the Linux CLI",
                    "Automate basic monitoring routines using shell scripts"
                ]
            },
            {
                "phase_number": 2,
                "title": "Defensive Security & Traffic Analysis",
                "practice_schedule": "2 Hours Daily",
                "topics": [
                    {
                        "name": "Security Architecture & Controls",
                        "subtopics": ["Firewalls: Stateful, Stateless, WAF", "IDS/IPS systems (Snort, Suricata)", "Cryptography: Symmetric vs Asymmetric, Hashing (SHA256, MD5)", "VPNs and SSL/TLS handshakes"]
                    },
                    {
                        "name": "Network Packet Capture",
                        "subtopics": ["Capturing packets using Wireshark", "Filtering traffic by protocol and IP address", "Detecting network scans (SYN scans, NULL scans)", "Analyzing unencrypted text transfers"]
                    }
                ],
                "mini_project": {
                    "title": "Wireshark Packet Analysis Lab",
                    "description": "Capture traffic during a mock attack on a local testing sandbox. Use Wireshark filters to isolate the attacking IP address, identify downloaded malicious files, and trace compromised credentials.",
                    "skills_used": ["Wireshark", "Packet Filtering", "Traffic Analysis", "Threat Identification"]
                },
                "milestones": [
                    "Distinguish and apply symmetric/asymmetric cryptographic concepts",
                    "Analyze packet streams using Wireshark to locate system vulnerabilities",
                    "Configure basic firewall rules on Linux (ufw/iptables) or Windows"
                ]
            },
            {
                "phase_number": 3,
                "title": "Offensive Security & Pen Testing Basics",
                "practice_schedule": "2 Hours Daily",
                "topics": [
                    {
                        "name": "Reconnaissance & Scanning",
                        "subtopics": ["Nmap scanning techniques & port states", "DNS enumerations & directory busting (Gobuster)", "Social engineering concepts & vectors"]
                    },
                    {
                        "name": "Vulnerability Assessment",
                        "subtopics": ["OWASP Top 10 web vulnerabilities (SQL Injection, XSS, CSRF)", "Using vulnerability scanners (Nessus, OpenVAS)", "Exploitation frameworks (Metasploit) on local labs"]
                    }
                ],
                "mini_project": {
                    "title": "Web Application Penetration Lab",
                    "description": "Set up a vulnerable web application (like DVWA) in a Docker container. Perform SQL Injection to retrieve passwords and exploit XSS to trigger alert cookies.",
                    "skills_used": ["Nmap", "SQL Injection", "XSS", "Docker Labs", "Burp Suite"]
                },
                "milestones": [
                    "Perform network service discovery and enumeration with Nmap",
                    "Explain and demonstrate OWASP Top 10 vulnerabilities in a test sandbox",
                    "Formulate mitigation strategies to patch identified application flaws"
                ]
            },
            {
                "phase_number": 4,
                "title": "Incident Response & SIEM Security Operations",
                "practice_schedule": "2 Hours Daily",
                "topics": [
                    {
                        "name": "SIEM Tools & Log Management",
                        "subtopics": ["Introduction to SIEM (Splunk, Elastic Security)", "Analyzing Windows Event Logs and Linux auth.log files", "Correlating events to discover indicators of compromise (IoC)"]
                    },
                    {
                        "name": "Incident Response Life Cycle",
                        "subtopics": ["NIST Incident Response Framework steps", "Containment, Eradication, and Recovery tactics", "Post-incident analysis & report drafting"]
                    }
                ],
                "major_project": {
                    "title": "SOC Log Analyzer & Alert Pipeline",
                    "description": "Deploy a local instance of Splunk or Elastic. Forward authentication logs from a Linux client. Design search dashboards to flag brute-force SSH logins and alert upon unauthorized root commands.",
                    "skills_used": ["SIEM Dashboarding", "Log Forwarding", "KQL / Splunk Queries", "Threat Detection"]
                },
                "milestones": [
                    "Query logs in a SIEM platform to map user activity and identify anomalies",
                    "Apply NIST guidelines to contain and document simulated breaches",
                    "Generate standard, concise post-incident analytical security reports"
                ]
            }
        ]
    },
    "cloud devops architect": {
        "skill_name": "Cloud DevOps Architect",
        "estimated_duration": "6-8 Months",
        "daily_study_time": "2 Hours",
        "final_outcome": "Design highly available cloud infrastructure on AWS, containerize apps with Docker, write Terraform configs, and set up CI/CD pipelines.",
        "phases": [
            {
                "phase_number": 1,
                "title": "Linux, Git & Scripting Foundations",
                "practice_schedule": "1.5 Hours Daily",
                "topics": [
                    {
                        "name": "Linux Admin & Scripting",
                        "subtopics": ["File permissions, ownership & processes", "User and group administration", "Shell scripting (Bash) for automation", "CRON jobs and systemd services"]
                    },
                    {
                        "name": "Git & GitHub Workflows",
                        "subtopics": ["Git commands (commit, branch, merge, rebase)", "Branching models: GitFlow, Trunk-Based Development", "Handling merge conflicts and writing pull requests"]
                    }
                ],
                "mini_project": {
                    "title": "Automated Backup & Git Upload Script",
                    "description": "Write a Bash script that zips config files on a schedule, stamps the file with the date, and pushes it to a secure repository.",
                    "skills_used": ["Bash Scripting", "Git CLI", "Systemd timers / Cron"]
                },
                "milestones": [
                    "Manage files, packages, and system processes in Linux",
                    "Resolve Git merge conflicts and organize branches according to development flows",
                    "Write robust shell scripts utilizing control statements"
                ]
            },
            {
                "phase_number": 2,
                "title": "Containerization & CI/CD Pipelines",
                "practice_schedule": "2 Hours Daily",
                "topics": [
                    {
                        "name": "Docker & Container Isolation",
                        "subtopics": ["Docker architecture, images and containers", "Writing optimized Dockerfiles", "Docker Compose for multi-container apps", "Container networking and data volumes"]
                    },
                    {
                        "name": "CI/CD Orchestration",
                        "subtopics": ["Continuous Integration/Continuous Deployment theories", "GitHub Actions workflows & runner configurations", "Automating testing suites and building Docker images upon code pushes"]
                    }
                ],
                "mini_project": {
                    "title": "Dockerized Multi-Service App",
                    "description": "Take a simple web app (React client, Node API, MongoDB database). Build optimized Docker images, connect them with Docker Compose, and set up persistent data volume storage.",
                    "skills_used": ["Docker", "Docker Compose", "Multi-stage builds", "Volumes"]
                },
                "milestones": [
                    "Write optimized, multi-stage Dockerfiles",
                    "Spin up connected services locally with a single docker-compose command",
                    "Configure GitHub Actions to build and push Docker images to registries on push events"
                ]
            },
            {
                "phase_number": 3,
                "title": "Orchestration & Cloud Platforms (AWS)",
                "practice_schedule": "2 Hours Daily",
                "topics": [
                    {
                        "name": "AWS Core Services",
                        "subtopics": ["Networking: VPC, Subnets, Route Tables, Internet Gateways", "Compute: EC2 instances, Auto Scaling Groups, Load Balancers (ALB)", "Storage: S3 buckets, IAM roles and policies"]
                    },
                    {
                        "name": "Kubernetes (K8s) Orchestration",
                        "subtopics": ["Kubernetes architecture (Control Plane, Nodes)", "Pods, Deployments, Services, ConfigMaps, Secrets", "Ingress controllers & routing", "Scaling applications with K8s"]
                    }
                ],
                "mini_project": {
                    "title": "Highly Available AWS VPC Setup",
                    "description": "Configure an AWS VPC manually or with a CLI, establishing public/private subnets across multiple availability zones, adding NAT gateways, and routing secure web traffic.",
                    "skills_used": ["AWS VPC", "AWS Networking", "Security Groups", "IAM Configuration"]
                },
                "major_project": {
                    "title": "Kubernetes Application Deployment",
                    "description": "Deploy a multi-replica web app to a local Minikube or cloud-managed EKS cluster. Configure rolling updates, load balancers, and external routing via Ingress controllers.",
                    "skills_used": ["Kubernetes YAML", "Deployment replicas", "K8s Services", "Ingress"]
                },
                "milestones": [
                    "Design and configure a secure, multi-subnet network architecture on AWS",
                    "Write declarative Kubernetes manifests to deploy self-healing apps",
                    "Set up service discovery and ingress routing within a cluster"
                ]
            },
            {
                "phase_number": 4,
                "title": "Infrastructure as Code (IaC) & Monitoring",
                "practice_schedule": "2 Hours Daily",
                "topics": [
                    {
                        "name": "Terraform (IaC)",
                        "subtopics": ["Terraform providers, resources, and state management", "Writing modular and dry Terraform configurations", "Terraform variables and outputs", "Deploying AWS structures with Terraform"]
                    },
                    {
                        "name": "Monitoring & Observability",
                        "subtopics": ["Prometheus for metrics collection", "Grafana dashboards for server metric plotting", "Log aggregation methods"]
                    }
                ],
                "major_project": {
                    "title": "GitOps Infrastructure & Automated Deploy Pipeline",
                    "description": "Write Terraform modules to provision an AWS VPC, EC2 nodes, and an EKS cluster. Set up GitHub Actions to apply Terraform configs on merge, and deploy a web app with metrics collection (Prometheus/Grafana).",
                    "skills_used": ["Terraform", "AWS EKS", "GitHub Actions", "Prometheus", "Grafana"]
                },
                "milestones": [
                    "Deploy full cloud infrastructures using declarative Terraform code",
                    "Implement remote state locking for collaborative infrastructure management",
                    "Build system metrics alerting and custom Grafana dashboards for monitoring"
                ]
            }
        ]
    },
    "react.js": {
        "skill_name": "React.js Framework",
        "estimated_duration": "2-3 Months",
        "daily_study_time": "2 Hours",
        "final_outcome": "Build scalable single-page applications, manage complex states, hook into web APIs, and write modular components using Next.js.",
        "phases": [
            {
                "phase_number": 1,
                "title": "React Core & Components",
                "practice_schedule": "1.5 Hours Daily",
                "topics": [
                    {
                        "name": "JSX & Functional Components",
                        "subtopics": ["JSX syntax rules", "Component composition", "Props passing and default values", "Styling methods (CSS Modules, Tailwind CSS)"]
                    },
                    {
                        "name": "State & Interactivity",
                        "subtopics": ["useState hook", "Event handlers (onClick, onChange)", "Conditional rendering", "Rendering lists using map() and key props"]
                    }
                ],
                "mini_project": {
                    "title": "Interactive Task Planner",
                    "description": "Create a task management layout where users add, complete, and filter tasks. Apply styles using Tailwind Utility classes.",
                    "skills_used": ["React Components", "useState", "Event Handlers", "Tailwind CSS"]
                },
                "milestones": [
                    "Compose nested functional components",
                    "Declare and manage local component states",
                    "Render collections of data using unique key attributes"
                ]
            },
            {
                "phase_number": 2,
                "title": "React Hooks & State Flow",
                "practice_schedule": "2 Hours Daily",
                "topics": [
                    {
                        "name": "Effect Hook & API Fetching",
                        "subtopics": ["useEffect lifecycle handling", "Dependency array configurations", "Fetching data inside useEffect with abort controllers", "Handling loading and error UI states"]
                    },
                    {
                        "name": "Shared State & Context API",
                        "subtopics": ["Lifting state up", "React Context API (createContext, useContext)", "Avoiding prop-drilling", "Performance hooks: useMemo, useCallback"]
                    }
                ],
                "mini_project": {
                    "title": "Global Settings Hub & Profile View",
                    "description": "Build an app featuring user profiles, custom dashboards, and theme toggling (dark/light) managed via React Context.",
                    "skills_used": ["React Context", "useEffect", "API calls", "Local storage syncing"]
                },
                "milestones": [
                    "Sync components with external data APIs using useEffect",
                    "Provide global configurations (themes, auth state) using Context",
                    "Optimize rendering performance using React memoization tools"
                ]
            },
            {
                "phase_number": 3,
                "title": "Routing & State Libraries",
                "practice_schedule": "2 Hours Daily",
                "topics": [
                    {
                        "name": "React Router",
                        "subtopics": ["Dynamic routes & parameters (/user/:id)", "Link, NavLink, useNavigate routing", "Protected routes for private pages", "Nested routes & Layout outlets"]
                    },
                    {
                        "name": "Global State Management",
                        "subtopics": ["Zustand setup and action functions", "Redux Toolkit slice configurations", "Async state management (React Query / TanStack Query)"]
                    }
                ],
                "mini_project": {
                    "title": "Crypto Watchlist Dashboard",
                    "description": "Build a multi-page app displaying live cryptocurrency charts. Users search, filter, and add items to a watchlist synced via Zustand and loaded via TanStack Query.",
                    "skills_used": ["React Router", "Zustand", "TanStack Query", "Recharts charts"]
                },
                "milestones": [
                    "Build clean client-side routing structures with nested subroutes",
                    "Manage complex application-wide state utilizing Zustand or Redux",
                    "Enable smart caching and automatic data refetching with React Query"
                ]
            },
            {
                "phase_number": 4,
                "title": "Next.js & Production Mastery",
                "practice_schedule": "2 Hours Daily",
                "topics": [
                    {
                        "name": "Next.js & Server Components",
                        "subtopics": ["Next.js App Router & layout structures", "Server vs Client Components", "Static Site Generation (SSG) & Server-Side Rendering (SSR)", "API Routes / Route Handlers"]
                    },
                    {
                        "name": "Testing & Deployment",
                        "subtopics": ["Unit testing components with Jest & React Testing Library", "Integration tests", "Performance audits using Lighthouse", "Vercel serverless deployment"]
                    }
                ],
                "major_project": {
                    "title": "E-Commerce Digital Marketplace",
                    "description": "Construct a Next.js digital storefront. Features static landing pages, server-side data fetching for products, client-side checkout cart, JWT user auth, API routes, and Jest testing.",
                    "skills_used": ["Next.js App Router", "Server Components", "Tailwind CSS", "Jest / RTL", "Vercel Deployment"]
                },
                "milestones": [
                    "Develop search engine optimized pages using Server-Side Rendering (SSR) in Next.js",
                    "Write robust component unit tests asserting user event outcomes",
                    "Deploy optimized Next.js structures to Vercel with clean build outputs"
                ]
            }
        ]
    },
    "go language": {
        "skill_name": "Go Language (Golang)",
        "estimated_duration": "3-4 Months",
        "daily_study_time": "2 Hours",
        "final_outcome": "Write idiomatic Go code, build high-performance concurrent programs, expose REST/gRPC microservices, and deploy CLI tools.",
        "phases": [
            {
                "phase_number": 1,
                "title": "Go Syntax & Foundations",
                "practice_schedule": "1.5 Hours Daily",
                "topics": [
                    {
                        "name": "Variables & Core Types",
                        "subtopics": ["Statically typed declarations", "Short variable declaration (:=)", "Zero values in Go", "Constants & iota enums"]
                    },
                    {
                        "name": "Control structures & Loops",
                        "subtopics": ["if-else evaluations", "switch conditions", "Go's single loop construct: for loops", "defer statement stack behavior"]
                    },
                    {
                        "name": "Composite Types & Structs",
                        "subtopics": ["Arrays vs Slices", "Slice manipulation (append, copy)", "Map structures", "Defining structs and field tags"]
                    }
                ],
                "mini_project": {
                    "title": "Interactive Contact Directory CLI",
                    "description": "Develop a CLI contact manager that stores contact details in memory, allows search, deletion, and updates, and parses input commands.",
                    "skills_used": ["Slices", "Structs", "Maps", "For Loops", "Input Parsing"]
                },
                "milestones": [
                    "Declare variables and write conditionals/loops in Go",
                    "Manipulate slices dynamically using slice expressions and append",
                    "Define custom structures and map collections for storing structured attributes"
                ]
            },
            {
                "phase_number": 2,
                "title": "Interfaces, Pointers & Web Servers",
                "practice_schedule": "2 Hours Daily",
                "topics": [
                    {
                        "name": "Pointers & Methods",
                        "subtopics": ["Pointer declarations and dereferencing", "Value vs Pointer receiver methods", "Struct embedding instead of inheritance"]
                    },
                    {
                        "name": "Interfaces & Errors",
                        "subtopics": ["Implicit interface satisfaction", "Empty interfaces (interface{})", "Go's explicit error handling pattern (val, err := ...)", "Creating custom errors"]
                    },
                    {
                        "name": "Standard HTTP Library",
                        "subtopics": ["net/http handler setups", "JSON encoding and decoding", "Path and query parsing", "Writing custom server middleware"]
                    }
                ],
                "mini_project": {
                    "title": "JSON API Server for Book Catalog",
                    "description": "Build an HTTP server utilizing the net/http module to perform CRUD actions on a list of books stored in memory. Enforce content-type middleware.",
                    "skills_used": ["net/http", "JSON Marshalling", "Interfaces", "Error Handling"]
                },
                "milestones": [
                    "Manage memory references utilizing Go pointers safely",
                    "Implement decoupling using implicit interfaces",
                    "Expose custom HTTP API endpoints that consume and return JSON payloads"
                ]
            },
            {
                "phase_number": 3,
                "title": "Concurrency & Performance Patterns",
                "practice_schedule": "2 Hours Daily",
                "topics": [
                    {
                        "name": "Goroutines & Channels",
                        "subtopics": ["Goroutine invocation (go keyword)", "Unbuffered vs Buffered Channels", "Channel synchronization & direction parameters", "Using range and close on channels"]
                    },
                    {
                        "name": "Concurrency Control",
                        "subtopics": ["select multiplexer", "sync.WaitGroup for task alignment", "sync.Mutex for data race prevention", "context package for timeout cancellations"]
                    }
                ],
                "mini_project": {
                    "title": "Concurrent URL Accessibility Auditor",
                    "description": "Write a program that takes a slice of URLs and audits them concurrently using goroutines. Implement channels to report status and a WaitGroup to await completion.",
                    "skills_used": ["Goroutines", "Channels", "sync.WaitGroup", "http.Get"]
                },
                "milestones": [
                    "Spawn goroutines to run tasks asynchronously",
                    "Implement safe memory communication using channels",
                    "Incorporate WaitGroups and Mutexes to align threads and prevent data races"
                ]
            },
            {
                "phase_number": 4,
                "title": "Databases & Microservices Architecture",
                "practice_schedule": "2 Hours Daily",
                "topics": [
                    {
                        "name": "Database Drivers & SQL",
                        "subtopics": ["Connecting to SQL databases with database/sql", "Executing queries and scanning rows", "Using SQL query builders or GORM"]
                    },
                    {
                        "name": "Microservices & Testing",
                        "subtopics": ["gRPC servers & Protobuf schemas", "Writing unit and benchmark tests using 'testing' module", "Mocking interfaces for testing databases", "Dockerizing Go binaries"]
                    }
                ],
                "major_project": {
                    "title": "Robust User Management Microservice",
                    "description": "Construct a production-grade microservice. Features a PostgreSQL connection, JWT-based user authorization, a full test suite with 80% coverage, benchmark tests, Docker containment, and gRPC endpoints.",
                    "skills_used": ["Go testing", "PostgreSQL", "gRPC", "Protobuf", "JWT", "Docker"]
                },
                "milestones": [
                    "Establish database connections and query SQL schemas safely from Go",
                    "Write automated tests and benchmarks using the built-in testing framework",
                    "Dockerize and deploy a compressed Go binary to cloud environments"
                ]
            }
        ]
    },
    "ui/ux design": {
        "skill_name": "UI/UX Design",
        "estimated_duration": "3-4 Months",
        "daily_study_time": "2 Hours",
        "final_outcome": "Understand user psychology, conduct UX research, design high-fidelity user interfaces, and build responsive interactive prototypes using Figma.",
        "phases": [
            {
                "phase_number": 1,
                "title": "UX Research & User Journeys",
                "practice_schedule": "1.5 Hours Daily",
                "topics": [
                    {
                        "name": "User-Centered Design Principles",
                        "subtopics": ["Design Thinking framework", "Cognitive load theories", "Gestalt visual principles", "Accessibility compliance (WCAG standards)"]
                    },
                    {
                        "name": "UX Research Methods",
                        "subtopics": ["Conducting user interviews & surveys", "Creating User Personas", "Empathy mapping", "Competitor analysis audits"]
                    },
                    {
                        "name": "Information Architecture",
                        "subtopics": ["Card sorting exercises", "Sitemaps and app structure layouts", "User flow mapping", "Low-fidelity paper wireframing"]
                    }
                ],
                "mini_project": {
                    "title": "Ride-Sharing UX Concept Study",
                    "description": "Conduct research for a local ride-sharing service. Formulate interview questions, compile 2 user personas, construct user journey maps, and draft wireframe mockups.",
                    "skills_used": ["UX Interviews", "User Personas", "Journey Mapping", "Low-Fi Wireframing"]
                },
                "milestones": [
                    "Draft user personas and maps representing qualitative user interviews",
                    "Construct logical user flows detailing navigation patterns",
                    "Formulate low-fidelity paper wireframes mapping core feature views"
                ]
            },
            {
                "phase_number": 2,
                "title": "Figma & UI Foundations",
                "practice_schedule": "2 Hours Daily",
                "topics": [
                    {
                        "name": "Visual Design Principles",
                        "subtopics": ["Color theory & color contrast accessibility", "Typography scale configurations", "Layout grid systems (8-point grid rules)", "Visual hierarchy and whitespace spacing"]
                    },
                    {
                        "name": "Figma Tool Foundations",
                        "subtopics": ["Frames vs Groups", "Vector networks & shape tools", "Auto Layout layout rules", "Figma Components & Variant configurations"]
                    }
                ],
                "mini_project": {
                    "title": "Recipe App Dashboard UI",
                    "description": "Design a responsive mobile layout for finding recipes in Figma. Utilize an 8-point grid, apply an accessible color palette, and implement reusable components.",
                    "skills_used": ["Figma Auto Layout", "Component Variant rules", "Grid Systems", "Typography scale"]
                },
                "milestones": [
                    "Design high-fidelity UI views utilizing Figma Auto Layout structures",
                    "Build reusable components and nested variants inside Figma workspaces",
                    "Apply color contrast guidelines matching WCAG AA recommendations"
                ]
            },
            {
                "phase_number": 3,
                "title": "Prototyping & Usability Testing",
                "practice_schedule": "2 Hours Daily",
                "topics": [
                    {
                        "name": "Figma Prototyping",
                        "subtopics": ["Transition types (Instant, Dissolve, Smart Animate)", "Interactive components (hover, active states)", "Overlay navigation configurations", "Scroll overflows and header pinning"]
                    },
                    {
                        "name": "Usability Auditing",
                        "subtopics": ["Formulating test scripts & scenarios", "Conducting moderated usability tests", "Analyzing heatmaps & recording feedback", "Iterative design improvements"]
                    }
                ],
                "mini_project": {
                    "title": "E-Commerce Checkout flow Prototype",
                    "description": "Create an interactive prototype of a shopping checkout flow in Figma. Conduct testing with 3 users and record changes based on user friction points.",
                    "skills_used": ["Figma Smart Animate", "Interactive Components", "Usability Testing", "Feedback loop iteration"]
                },
                "milestones": [
                    "Build high-fidelity prototypes demonstrating complex micro-interactions",
                    "Moderate usability testing sessions and gather target comments",
                    "Iterate and upgrade design solutions based on user testing findings"
                ]
            },
            {
                "phase_number": 4,
                "title": "Design Systems & Dev Handoff",
                "practice_schedule": "2 Hours Daily",
                "topics": [
                    {
                        "name": "Design Systems Scales",
                        "subtopics": ["Token definitions (Colors, spacing, text)", "Component libraries (Buttons, Forms, Alerts)", "Documentation structure layouts in Figma"]
                    },
                    {
                        "name": "Developer Alignment & Case Studies",
                        "subtopics": ["Exporting SVG assets", "Figma Dev Mode inspectors", "Documenting redlines", "Drafting UX Case Studies for portfolios"]
                    }
                ],
                "major_project": {
                    "title": "Full Design System & Saas App Case Study",
                    "description": "Build a comprehensive SaaS analytics dashboard design system. Includes design tokens, components with multiple states, responsive mobile/desktop layouts, and a case study detailing user research and testing results.",
                    "skills_used": ["Figma Design Systems", "Responsive layouts", "UX Research", "Figma Dev Mode", "Case Study Writing"]
                },
                "milestones": [
                    "Build a complete design system containing documented variables and tokens",
                    "Inspect and prepare visual layouts for web developers using Dev Mode inspections",
                    "Publish a detailed, end-to-end design case study outlining UX iterations"
                ]
            }
        ]
    }
}
