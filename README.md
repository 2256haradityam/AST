# AST
WORKING DIRECTORY STRUCTURE

<pre>
AST/
├── job_project/        # Django project root
│   ├── job/            # Django app
│   ├── job_project/    # Django project settings
│   └── manage.py        # Django management script
│
├── .gitignore          # Ignore unnecessary files (Optional)
├── requirements.txt    # Project dependencies
├── runtime.txt        # Python version specification (Optional)
├── Procfile            # Render deployment command
├── render.yaml        # Render configuration (Optional)
└── README.md          # Project documentation
</pre>

WEBSITE IS RUNNING LIVE AT https://ast-577j.onrender.com.

USERNAME : harad, PASSWORD : mongoadmin

CLICK ON JOBS NOT JOB TO SEE LIST OF JOBS

JOBS FETCHED USING APIFY.COM(INDEED SCRAPPER) -> LATEST DATA

TO SEE AVERAGE SALARY FILL LOCATION AND CLICK ON BUTTON. 

EXAMPLE LOCATION : Chicago

TO RUN PROJECT LOCAL MAINTAIN ABOVE FOLDER STRUCTURE.
**MAKE SURE IN settings.py ADD 'localhost' IN ALLOWED_HOST.**
cd job_project (AST->job_project)
THEN TYPE COMMAND IN TERMINAL 
python manage.py runserver
ENTER CREDENTIALS AND GET LOGIN
THEN CLICK ON Job
YOU WOULD SEE THE SAME LIST
