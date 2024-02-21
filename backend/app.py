from flask import Flask, request, jsonify
from flask_cors import CORS 
from modules.questions_generator import ExamQuestionGenerator
import json

app = Flask('Certibot')
CORS(app)

exams_by_company = {
    'GCP': ["Associate Cloud Engineer", 
               "Professional Cloud Architect", 
               "Professional Data Engineer",
               "Professional Cloud Developer",
               "Professional Cloud Network Engineer",
               "Professional Cloud Security Engineer",
               "Professional Collaboration Engineer",
               "Professional Machine Learning Engineer",
               "Professional Cloud Database Engineer",
               "Looker Business Analyst",
               "Looker Developer",
               "Looker LookML Developer",
               "G Suite Certification"],
    'AWS': ["AWS Certified Cloud Practitioner",
                "AWS Certified Solutions Architect Associate",
                "AWS Certified Developer Associate",
                "AWS Certified SysOps Administrator Associate",
                "AWS Certified Solutions Architect Professional",
                "AWS Certified DevOps Engineer Professional",
                "AWS Certified Security Specialty",
                "AWS Certified Big Data Specialty",
                "AWS Certified Advanced Networking Specialty",
                "AWS Certified Machine Learning Specialty",
                "AWS Certified Database Specialty",
                "AWS Certified Data Analytics Specialty"],
    'Microsoft': ["Microsoft Certified: Azure Fundamentals",
                  "Microsoft Certified: Azure Data Fundamentals",
                  "Microsoft Certified: Azure AI Fundamentals",
                  "Microsoft Certified: Azure Administrator Associate",
                  "Microsoft Certified: Azure Developer Associate",
                  "Microsoft Certified: Azure Security Engineer Associate",
                  "Microsoft Certified: Azure AI Engineer Associate",
                  "Microsoft Certified: Azure Data Scientist Associate",
                  "Microsoft Certified: Azure Data Engineer Associate",
                  "Microsoft Certified: Azure Database Administrator Associate",
                  "Microsoft Certified: Azure Solutions Architect Expert",
                  "Microsoft Certified: Azure DevOps Engineer Expert",
                  "Microsoft Certified: Security, Compliance, and Identity Fundamentals",
                  "Microsoft Certified: Security Operations Analyst Associate",
                  "Microsoft Certified: Identity and Access Administrator Associate",
                  "Microsoft Certified: Information Protection Administrator Associate",
                  "Microsoft Certified: Windows Server Hybrid Administrator Associate"]
}

# Mock data for exam outlines
exam_outlines = {
    'GCP': {'Professional Data Engineer': {
        'Section 1': "Designing Data Processing Systems: Security and Compliance: IAM, Data Security, Privacy, Regional Data Considerations, Compliance. Reliability and Fidelity: Data Cleaning, Monitoring Data Pipelines, Disaster Recovery, ACID Compliance, Data Validation. Flexibility and Portability: Mapping Business Requirements, Data/Application Portability, Data Staging/Cataloging. Data Migrations: Analyzing Stakeholder Needs, Migration Planning, Validation Strategy, Project/Dataset/Table Architecture.",
        'Section 2': "Ingesting and Processing Data: Planning Data Pipelines: Data Sources/Sinks, Transformation Logic, Networking, Encryption. Building Pipelines: Data Cleansing, Service Identification, Transformations (Batch/Streaming), Data Acquisition. Deploying Pipelines: Job Automation, CI/CD.",
        'Section 3': "Storing Data: Selecting Storage Systems: Data Access Patterns, Managed Services, Storage Costs/Performance, Data Lifecycle. Data Warehouse Usage: Data Model Design, Data Normalization, Business Requirements, Architecture for Data Access. Data Lakes: Management, Processing, Monitoring. Data Mesh: Building Data Mesh, Segmenting Data, Federated Governance Model.",
        'Section 4': "Preparing and Using Data for Analysis: Data Preparation for Visualization: Tool Connections, Field Precalculation, BigQuery Materialized Views, Granularity of Time Data. Sharing Data: Data Sharing Rules, Publishing Datasets/Reports, Analytics Hub. Data Exploration and Analysis: Data Preparation for Feature Engineering, Data Discovery.",
        'Section 5': "Maintaining and Automating Data Workloads: Optimizing Resources: Minimizing Costs, Resource Availability, Persistent/Jobbased Data Clusters. Designing Automation: Creating DAGs, Scheduling Jobs. Organizing Workloads: Pricing Models, Job Types. Monitoring and Troubleshooting: Observability, Usage Monitoring, Troubleshooting, Workload Management. Failure Awareness: Fault Tolerance, Multiregion Job Runs, Data Corruption Handling, Replication/Failover."
        },
        "Associate Cloud Engineer": {
        "Section 1": "Setting up cloud projects and accounts. Managing billing configuration. Installing and configuring the command line interface (CLI).",
        "Section 2": "Planning and estimating GCP product use using the Pricing Calculator. Planning and configuring compute resources, data storage options, and network resources.",
        "Section 3": "Deploying and implementing Compute Engine resources, Google Kubernetes Engine resources, App Engine, Cloud Run, and Cloud Functions resources. Deploying and implementing data solutions and networking resources.",
        "Section 4": "Managing Compute Engine resources. Managing Google Kubernetes Engine resources. Managing App Engine and Cloud Run resources. Managing storage and database solutions. Managing networking resources. Monitoring and logging.",
        "Section 5": "Managing identity and access management (IAM). Managing service accounts. Viewing audit logs for project and managed services."
        },
        "Professional Cloud Architect": {
        "Section 1": "Designing and planning a cloud solution architecture includes designing a solution infrastructure that meets business requirements with considerations for business use cases, product strategy, cost optimization, supporting application design, integration with external systems, movement of data, design decision tradeoffs, success measurements, compliance, and observability.",
        "Section 2": "Managing and provisioning a solution infrastructure involves configuring network topologies, extending to onpremises or multicloud environments, security protection, configuring individual storage systems, data storage allocation, compute provisioning, security and access management, network configuration for data transfer and latency, data retention, life cycle management, data growth management, and configuring compute systems.",
        "Section 3": "Designing for security and compliance focuses on identity and access management, resource hierarchy, data security, separation of duties, security controls, managing customermanaged encryption keys with Cloud KMS, and designing for compliance with legislation, commercial requirements, industry certifications, and audits.",
        "Section 4": "Analyzing and optimizing technology and business processes includes analyzing and defining technical processes like SDLC, CI/CD, troubleshooting, testing and validation of software and infrastructure, service catalogue and provisioning, business continuity, and disaster recovery, and analyzing and defining business processes including stakeholder management, change management, team assessment, decisionmaking process, customer success management, cost/resource optimization.",
        "Section 5": "Managing implementation entails advising development/operation teams for successful deployment, application development, API best practices, testing frameworks, data and system migration tooling, interacting with Google Cloud programmatically using Google Cloud Shell, Google Cloud SDK, and Cloud Emulators.",
        "Section 6": "Ensuring solution and operations reliability covers monitoring/logging/profiling/alerting solution, deployment and release management, and assisting with the support of solutions in operation."
        },
        "Professional Cloud Developer": {
        "Section 1": "Designing highly scalable, available, and reliable cloudnative applications. Covering microservices architectures, the use of Google recommended practices and patterns for application development.",
        "Section 2": "Building and testing applications. Understanding of best practices for building secure applications, using Google Cloud managed services for application storage, and deploying applications in containerized environments.",
        "Section 3": "Deploying applications. Skills in using Google Cloud services for application deployment, monitoring, management, and scaling. Understanding of continuous integration and continuous delivery (CI/CD) pipelines.",
        "Section 4": "Integrating Google Cloud services. Ability to integrate Google Cloud services with applications in ways that optimize performance and cost and create seamless user experiences.",
        "Section 5": "Managing application performance monitoring. Use of Google Cloud tools and technologies to monitor, troubleshoot, and optimize application performance."
        },
        "Professional Cloud Network Engineer": {
        "Section 1": "Designing, planning, and prototyping a Google Cloud network. Including considerations for high availability, failover, disaster recovery, DNS strategy, security, data exfiltration requirements, load balancing, quotas, hybrid connectivity, container networking, IAM roles, SaaS/PaaS/IaaS services, and microsegmentation.",
        "Section 2": "Implementing a Virtual Private Cloud (VPC). Covering IP address management, standalone vs. shared VPC, single vs. multi VPC, regional vs. multiregional considerations, VPC Network Peering, firewall configurations, custom routes, managed services integration, and thirdparty device insertion.",
        "Section 3": "Configuring network services. Focusing on load balancing configurations, Google Cloud Armor policies, Cloud CDN settings, and Cloud DNS management.",
        "Section 4": "Implementing hybrid Interconnectivity. Discussing configurations for Cloud Interconnect, sitetosite IPsec VPNs, and Cloud Router setup.",
        "Section 5": "Managing, monitoring, and optimizing network operations. Including logging and monitoring with Google Cloud’s operations suite, managing security, troubleshooting connectivity issues, and monitoring for latency and traffic flow."
        },
        "Professional Cloud Security Engineer": {
        "Section 1": "Configuring Access Within a Cloud Solution Environment: Understanding how to manage access to cloud resources effectively.",
        "Section 2": "Configuring Network Security: Knowledge of securing network architectures, including the use of firewalls, VPCs, and private access.",
        "Section 3": "Ensuring Data Protection: Implementing mechanisms to protect data at rest and in transit, including encryption and data lifecycle management.",
        "Section 4": "Managing Operations Within a Cloud Solution Environment: Overseeing the operational aspects of cloud solutions to ensure security and compliance.",
        "Section 5": "Ensuring Compliance: Ensuring cloud solutions adhere to legal, regulatory, and compliance requirements."
        },
        "Professional Machine Learning Engineer": {
         "Section 1": "ML Problem Framing: Define ML problems, frame ML problems.",
         "Section 2": "ML Solution Architecture: Design ML solutions, prepare and process data.",
         "Section 3": "ML Model Development: Develop ML models, automate and orchestrate ML pipelines.",
         "Section 4": "ML Model Deployment: Deploy ML models, monitor, optimize, and maintain ML models."  
        },
        "Professional Cloud Database Engineer": {
        "Section 1": "Database Services Overview: Overview of database services available in Google Cloud.",
        "Section 2": "Designing Database Solutions: Design solutions using Google Cloud databases.",
        "Section 3": "Implementing and Managing Databases: Implement and manage databases on Google Cloud.",
        "Section 4": "Monitoring and Optimizing Database Solutions: Monitor database performance, optimize database solutions."
        },
        "G Suite Certification": {
        "Section 1": "Proficiency in digital tools like G Suite is important for students to advance in school and in the job market. The G Suite certification allows students to demonstrate their knowledge of G Suite tools (e.g. Gmail, Drive, Docs, Sheets, Slides, Forms, and Hangouts Meet), which can be important for future universities and employers. The certification is available for K12 students.",
        "Section 2": "The G Suite certification tests students ages 13 and older on the same content as adults, requiring them to show competency of G Suite to help them succeed after school. A new version of the exam allows students to take the test from their classroom or school testing center, administered by their teacher or other faculty, and monitored remotely.",
        "Section 3": "Exclusive academic pricing extends the certification to students 13 and older. The student price for the exam is $37, a 50% discount off the list price of $75. Educators can register their class, and certified students receive a digital badge. The exam, currently only available in English, includes an exam guide, the Applied Digital Skills curriculum, and a G Suite certification practice lab on Qwiklabs."
        },
        "Looker LookML Developer": {
        "Section 1": "The Looker LookML Developer certification exam assesses an individual's proficiency in building, deploying, and managing LookML models within the Looker platform. It covers topics such as LookML syntax, model design, and optimization techniques.",
        "Section 2": "Candidates are tested on their ability to develop LookML models that support scalable and efficient data exploration, create derived tables and aggregate tables, manage project version control with Git, and implement security and access controls.",
        "Section 3": "The exam also evaluates knowledge in advanced LookML features such as extending and embedding Looker, creating custom visualizations, and utilizing Looker API for integration with other applications.",
        "Section 4": "Preparation for the exam includes handson experience with Looker and LookML, familiarity with SQL and database concepts, and understanding of data modeling practices. Looker offers documentation, tutorials, and training courses to aid in exam preparation.",
        "Section 5": "The Looker LookML Developer certification is intended for data analysts, data engineers, and developers who build data models and reports in Looker. It validates their expertise in leveraging the platform to transform data into actionable insights."
        },
        "Looker Developer": {
        "Section 1": "The Looker Developer certification exam evaluates an individual's skills in developing and implementing business intelligence solutions using the Looker platform. Key topics include understanding the Looker architecture, developing LookML models, and optimizing data models for performance.",
        "Section 2": "Candidates will be tested on their ability to utilize Looker's development features such as creating and managing LookML projects, designing robust and scalable data models, and implementing custom visualizations and dashboards tailored to business requirements.",
        "Section 3": "The exam also covers advanced Looker development practices, including integrating Looker with thirdparty tools and services, automating data workflows, and applying best practices for security and access control within Looker environments.",
        "Section 4": "To prepare for the exam, candidates should have handson experience with Looker and a solid understanding of SQL, data modeling, and business intelligence concepts. Looker's documentation, training courses, and community forums are valuable resources for exam preparation.",
        "Section 5": "This certification is aimed at data professionals, including business intelligence developers, data analysts, and data engineers, who use Looker to build and deploy analytics solutions. It demonstrates their ability to leverage Looker to drive datadriven decisionmaking across their organization."
        },
        "Looker Business Analyst": {
        "Section 1": "The Looker Business Analyst certification exam assesses an individual's proficiency in leveraging Looker to analyze and visualize data to support business decisionmaking. Key areas include navigating the Looker platform, understanding data models, and building reports and dashboards.",
        "Section 2": "Candidates will be evaluated on their ability to effectively use Looker's exploration features to extract insights from data, customize visualizations for various analytical needs, and share findings through Looker dashboards and reports.",
        "Section 3": "The exam covers critical competencies in data analysis, such as applying filters and pivots for advanced data segmentation, performing cohort and time series analyses, and utilizing Looker's embedded analytics capabilities to disseminate insights.",
        "Section 4": "Preparation for the exam should focus on gaining practical experience with Looker, including exploring data, creating calculated fields, and designing impactful visualizations. Looker's online documentation, interactive tutorials, and community resources are recommended study materials.",
        "Section 5": "This certification targets business analysts, data analysts, and other roles focused on business intelligence, data reporting, and analytics. It validates their skill set in using Looker to drive datainformed strategies and achieve business objectives."
        },
        "Professional Collaboration Engineer": {
        "Section 1": "Planning and implementing G Suite authorization and access: Understanding G Suite's identity and access management (IAM), configuring access controls, and managing user, group, and organizational unit structures.",
        "Section 2": "Managing user, resource, and Team Drive lifecycles: Creating and managing users and groups, automating lifecycle management, and understanding the best practices for Team Drives.",
        "Section 3": "Controlling and configuring G Suite services: Configuring and managing services for G Suite, including Gmail, Calendar, Docs, and Drive, with an emphasis on security settings and compliance.",
        "Section 4": "Configuring and managing endpoint access: Understanding endpoint management policies, deploying and managing G Suite on various devices, and ensuring secure access to company data.",
        "Section 5": "Monitoring organizational operations and advance G Suite adoption: Using reports and audit logs to monitor and analyze G Suite operations, developing strategies to increase G Suite adoption and collaboration within the organization.",
        "Section 6": "Configuring data migration and data governance: Migrating data to G Suite from different sources, setting up data governance policies, and ensuring data protection and compliance."
        }
    },
    "AWS": {
        "AWS Certified Cloud Practitioner": {
            "Section 1": "Cloud Concepts  26%: Define the AWS Cloud and its value proposition. Identify aspects of AWS Cloud economics. List the different cloud architecture design principles.",
            "Section 2": "Security  25%: Define the AWS shared responsibility model. Define AWS Cloud security and compliance concepts. Identify AWS access management capabilities. Identify resources for security support.",
            "Section 3": "Technology  33%: Define methods of deploying and operating in the AWS Cloud. Define the AWS global infrastructure. Identify the core AWS services. Identify resources for technology support.",
            "Section 4": "Billing and Pricing  16%: Compare and contrast the various pricing models for AWS. Recognize the various account structures in relation to AWS billing and pricing. Identify resources available for billing support."
        },
        "AWS Certified Solutions Architect Associate": {
            "Section 1": "Design Resilient Architectures: Choose reliable/resilient storage, Design decoupling mechanisms using AWS services, Choose appropriate resilient network components.",
            "Section 2": "Design HighPerforming Architectures: Select highperforming and scalable storage solutions, Design highperforming IP networking solutions, Choose highperforming database solutions.",
            "Section 3": "Design Secure Applications and Architectures: Design secure application tiers, Choose appropriate data security options.",
            "Section 4": "Design CostOptimized Architectures: Choose costeffective storage solutions, Design costeffective compute and database services.",
            "Section 5": "Operational Excellence: Monitor and log environments, Automate and orchestrate AWS environments."
        },
        "AWS Certified Developer Associate": {
            "Section 1": "Development with AWS Services: Understand how to use AWS SDKs to interact with AWS services and to write applications. Know how to use AWS Elastic Beanstalk to deploy and manage applications.",
            "Section 2": "Security: Implement and manage AWS security features, including authentication, authorization, and encryption. Use AWS Identity and Access Management (IAM) for service authentication.",
            "Section 3": "Deployment and Debugging: Deploy applications using CI/CD pipelines and understand how to use AWS CloudFormation. Troubleshoot application and deployment issues.",
            "Section 4": "Refactoring: Migrate existing applications to AWS and optimize applications to use AWS services and features effectively. Understand serverless development with AWS Lambda.",
            "Section 5": "Monitoring and Troubleshooting: Monitor applications using Amazon CloudWatch and use AWS XRay for debugging and analysis. Understand how to optimize performance.",
            "Section 6": "AWS Services and Architectures: Gain knowledge of key AWS services like Amazon S3, DynamoDB, RDS, EC2, and Lambda. Understand the core AWS architectural best practices."
        },
        "AWS Certified SysOps Administrator Associate": {
            "Section 1": "Monitoring, Logging, and Remediation: Implement and manage monitoring and logging solutions using Amazon CloudWatch, AWS CloudTrail, and AWS Config. Understand how to remediate issues based on monitoring and alerting.",
            "Section 2": "Reliability and Business Continuity: Design and implement backup and restore strategies using AWS services. Understand how to ensure high availability and fault tolerance using Amazon EC2 Auto Scaling and Elastic Load Balancing (ELB).",
            "Section 3": "Deployment, Provisioning, and Automation: Use AWS services such as AWS CloudFormation and AWS OpsWorks for deployment and infrastructure as code (IaC). Automate administrative tasks by using AWS CLI and SDKs.",
            "Section 4": "Security and Compliance: Implement and manage security policies on AWS using IAM, Security Groups, NACLs, and AWS KMS. Understand the shared responsibility model and compliance concepts.",
            "Section 5": "Networking and Content Delivery: Configure and manage VPCs, VPNs, and Direct Connect. Understand how to use Amazon CloudFront for content delivery and how to optimize network performance.",
            "Section 6": "Cost and Performance Optimization: Monitor and identify costoptimization opportunities using AWS Cost Explorer and Trusted Advisor. Implement performance optimization strategies for AWS resources.",
            "Section 7": "Operational Excellence: Follow the AWS WellArchitected Framework to improve systems with a focus on operational excellence. Implement best practices for maintaining AWS environments."
        },
        "AWS Certified Solutions Architect Professional": {
            "Section 1": "Designing for Organizational Complexity: Details on designing multiaccount AWS environments, including considerations for billing, networking, security, and scaling.",
            "Section 2": "Designing New Solutions: Best practices for designing highly available, costefficient, faulttolerant, and scalable systems.",
            "Section 3": "Migration Planning: Strategies for migrating complex, multitier applications on AWS, including selecting the right strategies and understanding the migration process.",
            "Section 4": "Cost Control: Techniques for controlling and optimizing costs in AWS, including the use of Reserved Instances, Savings Plans, and understanding the AWS pricing model.",
            "Section 5": "Continuous Improvement for Existing Solutions: Methods for improving existing solutions, with a focus on enhancing performance, security, and reliability."
        },
        "AWS Certified DevOps Engineer Professional": {
            "Section 1": "SDLC Automation: Implement and manage continuous integration and continuous delivery processes using AWS services.",
            "Section 2": "Configuration Management and Infrastructure as Code: Automate and manage infrastructure provisioning and management using AWS CloudFormation and other AWS tools.",
            "Section 3": "Monitoring and Logging: Deploy, manage, and operate scalable, highly available, and faulttolerant systems on AWS. Implement and control the flow of data to and from AWS.",
            "Section 4": "Policies and Standards Automation: Apply best practices for security, governance, and validation of AWS resource configurations.",
            "Section 5": "Incident and Event Response: Troubleshoot and resolve issues in development and production environments."
        },
        "AWS Certified Security Specialty": {
            "Section 1": "Incident Response: Identify and mitigate threats, and conduct incident analysis by using AWS services.",
            "Section 2": "Logging and Monitoring: Design and implement security monitoring and alerting.",
            "Section 3": "Infrastructure Security: Understand the use of AWS mechanisms to implement a secure infrastructure.",
            "Section 4": "Identity and Access Management: Use AWS identity and access management controls effectively.",
            "Section 5": "Data Protection: Encrypt, manage, and secure data at rest and in transit."
        },
        "AWS Certified Big Data Specialty": {
            "Section 1": "Data Collection: Collect, stream, and process big data using AWS data services.",
            "Section 2": "Storage and Data Management: Implement data storage and database services to manage big data.",
            "Section 3": "Processing: Process and analyze big data using AWS analytics and machine learning services.",
            "Section 4": "Visualization: Use AWS services to visualize and interpret big data.",
            "Section 5": "Security: Secure big data solutions and comply with data protection regulations."
        },
        "AWS Certified Advanced Networking Specialty": {
            "Section 1": "Design and Implement AWS Networks: Design highly available, scalable, and secure networking solutions on AWS.",
            "Section 2": "Network Optimization: Optimize network performance for AWS services.",
            "Section 3": "Automation for AWS Networking Tasks: Automate AWS networking tasks for efficient network operations.",
            "Section 4": "Compliance and Security: Implement and manage security policies within AWS networking infrastructure.",
            "Section 5": "Hybrid Networking Architectures: Design and implement hybrid IT network architectures."
        },
        "AWS Certified Machine Learning Specialty": {
            "Section 1": "Data Engineering: Process, clean, and validate data for machine learning (ML) applications.",
            "Section 2": "Exploratory Data Analysis: Analyze data and model potential solutions using AWS ML services.",
            "Section 3": "Modeling: Design, implement, and deploy ML solutions using AWS.",
            "Section 4": "Machine Learning Implementation and Operations: Automate and operationalize ML workflows and models.",
            "Section 5": "Security and Compliance: Secure ML solutions and ensure compliance with data protection laws."
        },
        "AWS Certified Database Specialty": {
            "Section 1": "Database Design: Design highly available, costefficient, and scalable database solutions.",
            "Section 2": "Deployment and Migration: Automate database solution deployments and migrations.",
            "Section 3": "Management and Operations: Manage, maintain, and troubleshoot AWS database solutions.",
            "Section 4": "Monitoring and Troubleshooting: Implement monitoring, logging, and troubleshooting of database solutions.",
            "Section 5": "Database Security: Secure database solutions, ensure data integrity, and comply with data protection laws."
        },
        "AWS Certified Data Analytics Specialty": {
            "Section 1": "Collection: Collect and store data for analytics.",
            "Section 2": "Storage and Data Management: Design and implement data storage solutions.",
            "Section 3": "Processing and Analysis: Process, analyze, and visualize data using AWS analytics services.",
            "Section 4": "Security: Implement security controls and compliance requirements.",
            "Section 5": "Operational Best Practices: Apply best practices for the deployment and operation of analytics solutions."
        }
    },
    "Microsoft": {
          "Microsoft Certified: Azure Fundamentals": {
            "Section 1": "Cloud Concepts: Understand core cloud services and principles, including aspects of Azure services.",
            "Section 2": "Core Azure Services: Detailed overview of Azure core services, including compute, networking, storage, and database services.",
            "Section 3": "Security and Compliance: Overview of Azure's security tools and features, identity services, and governance methodologies.",
            "Section 4": "Azure Pricing and Support: Understanding Azure subscriptions, planning and managing costs, and Azure support options."
        },
          "Microsoft Certified: Azure Data Fundamentals": {
            "Section 1": "Explore core data concepts: Understand types of core data workloads, and data analytics concepts.",
            "Section 2": "Explore roles and responsibilities in the world of data: Identify different data roles in Azure.",
            "Section 3": "Explore Azure data services: Overview of Azure services related to data management and databases.",
            "Section 4": "Explore relational data in Azure: Understand relational databases in Azure, including Azure SQL.",
            "Section 5": "Explore nonrelational data in Azure: Dive into Azure's nonrelational data services like Cosmos DB.",
            "Section 6": "Explore modern data warehouse analytics in Azure: Introduction to Azure Synapse Analytics and data lake concepts."
        },
         "Microsoft Certified: Azure AI Fundamentals": {
            "Section 1": "Introduction to AI: Understand the basic concepts of AI and machine learning.",
            "Section 2": "Machine Learning on Azure: Explore Azure Machine Learning services and tools.",
            "Section 3": "Computer Vision on Azure: Dive into Azure's computer vision services, including Custom Vision and Face API.",
            "Section 4": "Natural Language Processing on Azure: Overview of Azure services for language understanding, including LUIS and Text Analytics.",
            "Section 5": "Conversational AI on Azure: Introduction to creating bots using Azure Bot Services and QnA Maker."
        },
          "Microsoft Certified: Azure Administrator Associate": {
            "Section 1": "Manage Azure identities and governance: Understand how to manage Azure Active Directory, Azure policies, and subscriptions. This includes user and group management, rolebased access control, and resource tagging.",
            "Section 2": "Implement and manage storage: Focus on managing storage accounts, data in Azure Storage, Azure files, and Azure Blob storage. Learn to secure storage and manage storage costs effectively.",
            "Section 3": "Deploy and manage Azure compute resources: Learn to configure VMs, create and configure containers, and Azure Kubernetes Service. Understand automation and VM management.",
            "Section 4": "Configure and manage virtual networking: Dive into virtual networks, VPN gateway configurations, network security groups, and Azure ExpressRoute for private connections.",
            "Section 5": "Monitor and back up Azure resources: Utilize Azure Monitor, Azure Backup, and other tools for monitoring, alerting, and backing up resources."
        },
         "Microsoft Certified: Azure Developer Associate": {
            "Section 1": "Develop Azure compute solutions: Work with Azure Functions, web apps, containerized applications, and manage compute resources.",
            "Section 2": "Develop for Azure storage: Implement solutions for blob storage, Cosmos DB, storage queues, and data sharing.",
            "Section 3": "Implement Azure security: Understand authentication, authorization, secure cloud solutions, and manage keys, tokens, and certificates.",
            "Section 4": "Monitor, troubleshoot, and optimize Azure solutions: Use monitoring tools, configure application insights, and troubleshoot solutions.",
            "Section 5": "Connect to and consume Azure services and thirdparty services: Integrate APIs, event and messagebased models, and manage API management services."
        },
         "Microsoft Certified: Azure Security Engineer Associate": {
            "Section 1": "Manage identity and access: Configure Azure AD for workloads, secure hybrid identities, and implement conditional access policies.",
            "Section 2": "Implement platform protection: Understand network security, host security, container security, and Azure Resource Manager security.",
            "Section 3": "Manage security operations: Configure security services and policies, manage security alerts, and respond to and remediate security issues.",
            "Section 4": "Secure data and applications: Encrypt data at rest and in transit, manage application security, and secure or isolate databases."
        },
         "Microsoft Certified: Azure AI Engineer Associate": {
            "Section 1": "Plan and manage an Azure Cognitive Services solution: Understand Cognitive Services APIs, create a Cognitive Services resource, and manage keys and endpoints.",
            "Section 2": "Implement computer vision solutions: Use the Computer Vision API and Custom Vision Service to analyze images, detect faces, and recognize objects.",
            "Section 3": "Implement natural language processing: Work with Text Analytics API, Language Understanding (LUIS), and create QnA Maker solutions.",
            "Section 4": "Implement conversational AI solutions: Build bots with the Bot Framework, integrate bots with Cognitive Services, and manage bot resources."
        },
        "Microsoft Certified: Azure Data Scientist Associate": {
            "Section 1": "Data Science and Machine Learning on Azure: Details on how to use Azure services for data science and machine learning tasks.",
            "Section 2": "Implementing and Running Machine Learning Workloads on Azure: Specifics on setting up and running machine learning models, including Azure Machine Learning Service.",
            "Section 3": "Data Processing and Analysis: Techniques and tools for data processing and analysis on Azure.",
            "Section 4": "Monitoring and Optimizing Azure Machine Learning Solutions: Strategies for monitoring and optimizing the performance of machine learning solutions deployed on Azure."
        },
        "Microsoft Certified: Azure Data Engineer Associate": {
            "Section 1": "Designing and Implementing Data Storage: How to design and implement various data storage solutions on Azure.",
            "Section 2": "Managing and Developing Data Processing: Techniques for managing and developing data processing tasks.",
            "Section 3": "Monitoring and Optimizing Data Solutions: Best practices for monitoring and optimizing data solutions on Azure."
        },
        "Microsoft Certified: Azure Database Administrator Associate": {
            "Section 1": "Planning and Implementing Data Platform Resources: Steps for planning and implementing data platform resources on Azure.",
            "Section 2": "Implementing a Secure Environment: Guidance on creating secure environments for database solutions.",
            "Section 3": "Monitoring and Optimizing Operational Resources: Techniques for monitoring and optimizing the performance of operational resources.",
            "Section 4": "Optimizing Query Performance: Strategies for optimizing the performance of database queries."
        },
        "Microsoft Certified: Azure Solutions Architect Expert": {
            "Section 1": "Designing and Implementing a Data Platform Solution: Detailed guidelines on designing and implementing robust data platform solutions on Azure.",
            "Section 2": "Designing for Identity and Security: Best practices for designing solutions with identity and security in mind.",
            "Section 3": "Designing a Business Continuity Strategy: Strategies for ensuring business continuity through disaster recovery and backup solutions.",
            "Section 4": "Designing for Deployment, Migration, and Integration: Considerations for deploying, migrating, and integrating Azure solutions."
        },
        "Microsoft Certified: Azure DevOps Engineer Expert": {
            "Section 1": "Designing and Implementing Microsoft DevOps Solutions: Covers principles of DevOps practices, using Azure Repos for source control, and integrating continuous integration and continuous deployment (CI/CD) pipelines with Azure Pipelines.",
            "Section 2": "Managing Source Control: Focuses on managing Git repositories, implementing branching strategies, and integrating source control with build and release pipelines.",
            "Section 3": "Streamlining Builds and Releases: Details creating and managing build definitions, integrating automated tests, deploying to different environments, and using Azure Artifacts to manage dependencies.",
            "Section 4": "Implementing Continuous Feedback: Covers strategies for monitoring application performance, collecting user feedback, and implementing strategies for reducing technical debt and managing backlogs.",
            "Section 5": "Security and Compliance in DevOps: Discusses managing security in a DevOps workflow, including using Azure Security Center, implementing secure development practices, and compliance monitoring."
        },
        "Microsoft Certified: Security, Compliance, and Identity Fundamentals": {
            "Section 1": "Understanding Microsoft Security, Compliance, and Identity Solutions: Introduces Microsoft's security tools and capabilities across Azure, Microsoft 365, and hybrid environments.",
            "Section 2": "Implementing Microsoft Identity Solutions: Covers the concepts of Azure Active Directory, identity protection, hybrid identity, and managing external identities.",
            "Section 3": "Security Solutions on Azure: Details Azure security features, including network security, host security, container security, and key management strategies.",
            "Section 4": "Compliance and Governance Features: Discusses compliance management in Azure, Microsoft 365 compliance center, information protection, and governance strategies.",
            "Section 5": "Data Protection and Management: Focuses on implementing data loss prevention policies, archiving and retention policies, and understanding Microsoft's information governance solutions."
        },
        "Microsoft Certified: Security Operations Analyst Associate": {
            "Section 1": "Threat Management: Discusses identifying, investigating, and responding to threats using Microsoft Azure Sentinel, Microsoft 365 Defender, and thirdparty security products.",
            "Section 2": "Monitoring and Reporting: Covers configuring security alerts, creating custom dashboards, and reporting on security incidents using Azure Monitor and other tools.",
            "Section 3": "Implementing Security Controls: Details configuring security policies, implementing endpoint protection solutions, and managing security vulnerabilities.",
            "Section 4": "Incident Response: Focuses on developing incident response strategies, understanding attack vectors, and using automation to respond to security incidents.",
            "Section 5": "Understanding Regulatory and Compliance Standards: Covers key compliance standards relevant to security operations, including GDPR, HIPAA, and others, and how to ensure compliance using Microsoft solutions."
        },
        "Microsoft Certified: Identity and Access Administrator Associate": {
            "Section 1": "Plan and implement an identity and access management strategy: Understand Azure Active Directory, identity governance principles, and organizational structures.",
            "Section 2": "Implement an authentication and access management solution: Configure secure authentication methods, access management for apps, and conditional access policies.",
            "Section 3": "Implement access management for apps: Integrate single signon (SSO), secure application registration, and manage API access to Microsoft Graph.",
            "Section 4": "Plan and implement an identity governance strategy: Define and implement entitlement management, access reviews, privileged identity management, and identity protection."
        },
        "Microsoft Certified: Information Protection Administrator Associate": {
            "Section 1": "Implement information protection: Understand data classification, labeling, and data loss prevention in Microsoft 365.",
            "Section 2": "Implement data governance: Manage data governance and retention, inplace records management, and information governance solutions in Microsoft 365.",
            "Section 3": "Manage search and investigation: Conduct content search, audit log investigations, and manage advanced eDiscovery."
        },
        "Microsoft Certified: Windows Server Hybrid Administrator Associate": {
            "Section 1": "Implement Windows Server IaaS VMs: Deploy and manage Windows Server IaaS Virtual Machine on Azure, including storage, networking, and security.",
            "Section 2": "Implement hybrid networking: Understand hybrid networking components, VPN connectivity, and routing solutions between onpremises and Azure.",
            "Section 3": "Implement Windows Server migration, security, and monitoring: Migrate Windows Server workloads, implement Windows Server security solutions, and monitor Windows Server resources in a hybrid environment."
        }
    }
}

# Temporary storage for selected exam details
selected_exam_details = {}

@app.route('/', methods=['GET'])
def home_screen():
    return "Welcome to Certibot!"

@app.route('/companies', methods=['GET'])
def get_companies():
    companies = list(exams_by_company.keys())
    return jsonify(companies)

@app.route('/exams/<company>', methods=['GET'])
def get_exams_for_company(company):
    if company in exams_by_company:
        exams = exams_by_company[company]
        return jsonify(exams)
    else:
        return jsonify({"error": "Company not found"}), 404

@app.route('/exam_selection', methods=['POST'])
def exam_selection():
    global selected_exam_details
    data = request.get_json()
    certifier = data.get('certifier')
    exam_name = data.get('exam_name')
    exam_outline = data.get('exam_outline')

    # Store the selected exam details
    selected_exam_details = {
        "certifier": certifier,
        "exam_name": exam_name,
        "exam_outline": exam_outline
    }

    if certifier in exam_outlines and exam_name in exam_outlines[certifier]:
        exam_scope = exam_outlines[certifier][exam_name]
        # Assuming you want to return the sections and their content
        if exam_outline.lower() == 'sections':
            exam_scope = json.dumps(exam_scope).replace("/n","")
            return exam_scope
        elif exam_outline.lower() == 'topics':
            question_generator = ExamQuestionGenerator(exam_outline=exam_outlines[certifier][exam_name])
            # Retrieve key topics
            full_exam_name = "{} {}".format(certifier, exam_name)
            key_topics = question_generator.retrieve_keytopics(full_exam_name)
            # Return the key topics as a JSON response
            key_topics = key_topics.split(",")
            return jsonify({"key_topics": key_topics})
        else:
            return jsonify({"error": "Selection Unknown"}), 404
    else:
        return jsonify({"error": "Exam outline not found"}), 404

@app.route('/generate_questions_for_sections', methods=['POST'])
def generate_questions_for_sections():
    selected_sections = request.get_json()

    certifier = selected_exam_details.get('certifier')
    exam_name = selected_exam_details.get('exam_name')

    # Navigate the nested structure to get the specific exam's outline
    if certifier in exam_outlines and exam_name in exam_outlines[certifier]:
        exam_outline = exam_outlines[certifier][exam_name]
    else:
        return jsonify({"error": "Exam outline not found"}), 404

    question_generator = ExamQuestionGenerator(exam_outline=exam_outline)

    # Structure to hold the questions for each section
    section_questions = {}

    for section_key in selected_sections.values():
        # Ensure the section exists in the exam outline
        if section_key in exam_outline:
            try:
                # Generate questions for the selected section
                generated_questions = question_generator.based_on_outline(section_key, f"{certifier} {exam_name}")
                # Assuming generated_questions returns clean JSON or a dictionary
                clean_text = generated_questions.replace("```json\n", "").replace("\n```", "").strip()
                clean_text.replace("\\n", "")
                section_questions[section_key] = json.loads(clean_text)
            except ValueError as e:
                # Handle the error appropriately, maybe log it or return an error message
                section_questions[section_key] = "Error generating questions for this section"
        else:
            section_questions[section_key] = "Section not found in the exam outline"

    # Return the structured response as JSON
    return jsonify(section_questions)

@app.route('/generate_questions_for_topics', methods=['POST'])
def generate_questions_for_topics():
    data = request.get_json()
    topics = data.get('topics', [])
    
    exam_name = selected_exam_details.get('exam_name')
    certifier = selected_exam_details.get('certifier')

    question_generator = ExamQuestionGenerator(exam_outline=exam_outlines[certifier][exam_name])
    
    topics_questions = {}

    for topic in topics:
        try:
            # Generate questions for each topic
            generated_questions_str = question_generator.based_on_topics([topic], f"{certifier} {exam_name}")
            generated_questions_json = json.loads(generated_questions_str)
            # Add the generated questions to the topics_questions dict
            topics_questions[topic] = generated_questions_json
        except json.JSONDecodeError as e:
            # Log the error or handle it as needed
            topics_questions[topic] = {"error": f"{e}"}

    # Return the compiled topics and their questions as JSON
    return jsonify(topics_questions)

if __name__ == '__main__':
    app.run(debug=True)
