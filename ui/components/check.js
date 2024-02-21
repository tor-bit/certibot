
export const topics_questions = {
    "BigQuery": {
        "questions": [
            {
                "options": {
                    "A": "Use BigQuery's Data Loss Prevention API to scan and de-identify PII before loading the data into BigQuery.",
                    "B": "Configure column-level security on the PII fields and grant specific roles to authorized users only.",
                    "C": "Implement row-level security to filter out any rows that contain PII from being accessed by unauthorized users.",
                    "D": "Use the Dynamic Data Masking feature to define masking policies on PII columns."
                },
                "question": "You are working with a BigQuery dataset that contains sensitive user data. You need to ensure that personally identifiable information (PII) is masked before analysts can query the data. Which feature should you use and how should it be implemented?",
                "solution": {
                    "correct": "B",
                    "explanation": "Column-level security allows you to restrict access to specific columns containing sensitive data like PII and ensure that only users with the necessary roles can access them."
                }
            },
            {
                "options": {
                    "A": "Partition the large table based on the query patterns and only scan relevant partitions.",
                    "B": "Duplicate the large table and keep only the frequently accessed columns, ensuring they are indexed.",
                    "C": "Create a materialized view that selects only the frequently accessed columns from the large table.",
                    "D": "Store the frequently accessed columns in a separate native BigQuery storage format for faster access."
                },
                "question": "You are designing a data warehouse in BigQuery and have a requirement to optimize for high-frequency, low-latency reads on a few columns from a large table. Which approach could minimize costs while meeting this requirement?",
                "solution": {
                    "correct": "C",
                    "explanation": "Creating a materialized view that projects the frequently accessed columns can streamline read performance and possibly reduce costs by caching the results and preventing full table scans."
                }
            },
            {
                "options": {
                    "A": "The source table schema referenced by the view has been changed, resulting in an invalid view.",
                    "B": "The account used to query the view has lost the necessary permissions.",
                    "C": "BigQuery views have an expiration time set, and the view has expired.",
                    "D": "The query that defines the view is using a non-deterministic function which is not allowed in BigQuery views."
                },
                "question": "Your company's BigQuery data warehouse has multiple views created for department-specific usage. The Engineering department's view has recently started to return errors when queried. What could be a possible cause?",
                "solution": {
                    "correct": "A",
                    "explanation": "If the schema of the underlying source table changes (e.g., columns are removed or renamed), the view's SQL query may reference columns that no longer exist, causing errors."
                }
            },
            {
                "options": {
                    "A": "Use the EXPORT DATA statement to create smaller tables that contain only the necessary data and join them instead.",
                    "B": "Enable the BI Engine on BigQuery tables to cache the results and speed up query execution.",
                    "C": "Use the query plan explanation to identify the most resource-intensive stages and optimize the join keys and join types in the query.",
                    "D": "Increase the slot allocation for the BigQuery project to allocate more computational resources to the query execution."
                },
                "question": "You are conducting a performance optimization on a BigQuery SQL query which joins several large tables. Despite your efforts to minimize the data processed using filters and partitioned tables, the query still consumes a significant amount of resources. What can you do to potentially improve the query's performance?",
                "solution": {
                    "correct": "C",
                    "explanation": "By using the query plan explanation, you can identify bottlenecks and optimize the joins by selecting the correct join keys and perhaps changing join types (from CROSS JOIN to INNER JOIN, for example) to reduce resource consumption."
                }
            },
            {
                "options": {
                    "A": "Use the bq command-line tool's extract command to export the table directly to Cloud Storage in Avro format.",
                    "B": "Split the table into multiple smaller tables, export them separately to Cloud Storage, and concatenate later.",
                    "C": "Export the data into a single CSV file by setting the destination format in the BigQuery extraction API.",
                    "D": "Export the table using a wildcard to create multiple sharded files in Cloud Storage."
                },
                "question": "You have been tasked with exporting a large BigQuery table into Google Cloud Storage for further processing with Dataproc. The table is approximately 5 TB in size. What approach should you take to efficiently handle this export?",
                "solution": {
                    "correct": "D",
                    "explanation": "Using a wildcard in the export path, you can export a large table to multiple sharded files in Cloud Storage. This approach allows for parallelism and efficient handling of large exports."
                }
            }
        ],
        "topic": "BigQuery"
    },
    "Cloud Storage": {
        "questions": [
            {
                "options": {
                    "A": "Multi-Regional Storage",
                    "B": "Regional Storage",
                    "C": "Nearline Storage",
                    "D": "Coldline Storage"
                },
                "question": "A company is looking to store large sets of immutable data for their data analysis workflows. This data will be frequently accessed by their analytics team within the first 30 days of creation but will be rarely accessed thereafter. Cost-effectiveness and data retrieval times are important for the company. Which storage class should the company use for this scenario?",
                "solution": {
                    "answer": "C",
                    "explanation": "Nearline Storage is cost-effective for storing infrequently accessed data, with retrieval times suitable for the required use case."
                }
            },
            {
                "options": {
                    "A": "Object Versioning",
                    "B": "Storage Transfer Service",
                    "C": "Cross-Region Replication",
                    "D": "Multi-Regional Storage"
                },
                "question": "An organization is designing a disaster recovery plan and needs to ensure that their data stored in Cloud Storage can be quickly mirrored to another region in case of regional failure. Which feature should they implement?",
                "solution": {
                    "answer": "C",
                    "explanation": "Cross-Region Replication will automatically and asynchronously replicate objects to a bucket in another region, thus serving the need for a disaster recovery plan."
                }
            },
            {
                "options": {
                    "A": "Use Cloud Storage with Customer-Managed Encryption Keys (CMEK)",
                    "B": "Enable Cloud Storage Bucket Versioning",
                    "C": "Store data using the Coldline Storage class",
                    "D": "Deploy the application in a VPC Service Control perimeter"
                },
                "question": "A healthcare application is deployed on Google Cloud Platform and requires HIPAA-compliant storage for storing sensitive patient records. Which of the following configurations should be ensured?",
                "solution": {
                    "answer": "A",
                    "explanation": "Using Customer-Managed Encryption Keys (CMEK) in Cloud Storage provides an additional layer of security by allowing customers to control the encryption keys, which helps in complying with regulations like HIPAA."
                }
            },
            {
                "options": {
                    "A": "Use Cloud Functions triggered by Cloud Storage events to call the Vision API",
                    "B": "Set up a Compute Engine instance to poll the storage bucket and process images using the Vision API",
                    "C": "Use Cloud Dataflow to batch process images at intervals and analyze them with the Vision API",
                    "D": "Directly connect Cloud Storage with the Vision API without using any intermediary services"
                },
                "question": "Your application stores images uploaded by users on Google Cloud Storage and needs to perform image recognition. What's the most effective method to integrate storage with the Cloud Vision API for processing these images on the fly?",
                "solution": {
                    "answer": "A",
                    "explanation": "Using Cloud Functions with Cloud Storage triggers is an event-driven and cost-effective way to process images as they are uploaded without managing infrastructure."
                }
            },
            {
                "options": {
                    "A": "Create a lifecycle management rule that checks for objects older than 365 days and has metadata 'permanent' not equal to 'true'",
                    "B": "Use a daily Cloud Function to check each object's age and metadata, and delete if appropriate",
                    "C": "Implement a Cloud Scheduler job that runs a custom script to filter and delete objects",
                    "D": "Enable versioning, and then run a script to delete non-permanent objects older than 365 days"
                },
                "question": "A company wants to employ Object Lifecycle Management on their Cloud Storage bucket to reduce costs. They aim to delete objects that are older than 365 days but want to ensure that objects marked 'permanent' in the metadata are not deleted. What should they do?",
                "solution": {
                    "answer": "A",
                    "explanation": "The lifecycle management policy can include conditions on object age and custom metadata, allowing automated deletion with the specified criteria."
                }
            }
        ],
        "topic": "Cloud Storage"
    }
}