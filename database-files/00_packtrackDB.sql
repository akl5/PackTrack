DROP DATABASE IF EXISTS pack_track;
-- Creating the database, which will be called pack_track --
CREATE DATABASE pack_track;

-- Using the database we just made (pack_track) --
USE pack_track;

-- This is the table for users --
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(50),
    middleName VARCHAR(50),
    lastName VARCHAR(50),
    mobile VARCHAR(15),
    email VARCHAR(75) UNIQUE NOT NULL,
    username VARCHAR(30) UNIQUE,
    password VARCHAR(150) NOT NULL,
    country VARCHAR(150),
    state VARCHAR(100),
    town VARCHAR(100),
    registeredAT DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updatedAT DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    profile TEXT,
    accountStatus BOOLEAN DEFAULT TRUE,
    userRole ENUM('Student', 'Hiring Manager', 'System Admin') NOT NULL,
    INDEX idx_mobile (mobile),
    INDEX idx_email (email)
);


-- This is the table for students --
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    nu_id INT UNIQUE NOT NULL,
    enrollmentDate DATE,
    graduationYear INT,
    gpa DECIMAL(3, 2) CHECK (gpa BETWEEN 0.00 AND 4.00) NOT NULL,
    transcript TEXT NOT NULL,
    resume MEDIUMTEXT NOT NULL,
    coverLetter MEDIUMTEXT,
    FOREIGN KEY (student_id) REFERENCES users (id) ON UPDATE CASCADE ON DELETE CASCADE,
    INDEX idx_nu_id (nu_id),
    INDEX idx_gpa (gpa)
);


-- This is the table for departments --
CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    departmentName VARCHAR (300) NOT NULL
);


-- This is the table for majors --
CREATE TABLE majors (
    student_id INT NOT NULL,
    department_id INT NOT NULL,
    PRIMARY KEY(student_id, department_id),
    name VARCHAR(150) NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students (student_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (department_id) REFERENCES departments (department_id) ON UPDATE CASCADE ON DELETE CASCADE
);


-- This is the table for minors --
CREATE TABLE minors (
   student_id INT NOT NULL,
   department_id INT NOT NULL,
   PRIMARY KEY (student_id, department_id),
   name VARCHAR(150) NOT NULL,
   FOREIGN KEY (student_id) REFERENCES students (student_id) ON UPDATE CASCADE ON DELETE CASCADE,
   FOREIGN KEY (department_id) REFERENCES departments (department_id) ON UPDATE CASCADE ON DELETE CASCADE
);


-- This is the table for companies --
CREATE TABLE companies (
   company_id INT AUTO_INCREMENT PRIMARY KEY,
   companyName VARCHAR(200) NOT NULL,
   industry VARCHAR(200) NOT NULL,
   headquarters VARCHAR(200),
   companySize INT,
   headAddress VARCHAR(200),
   website VARCHAR(200) UNIQUE NOT NULL,
   openPositions INT,
   registeredAT DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
   updatedAT DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
   INDEX idx_companyName (companyName),
   INDEX idx_industry (industry)
);


-- This is the table for hiring managers --
CREATE TABLE hiring_managers (
    hiringManager_id INT PRIMARY KEY,
    company_id INT,
    jobTitle VARCHAR(300) NOT NULL,
    experience INT NOT NULL,
    university VARCHAR(150),
    registeredAT DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updatedAT DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (hiringManager_id) REFERENCES users (id),
    FOREIGN KEY (company_id) REFERENCES companies (company_id),
    INDEX idx_company_id (company_id),
    INDEX idx_jobTitle (jobTitle)
);


-- This is the table for student employees --
CREATE TABLE student_employees (
    studentEmployee_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    hiringManager_id INT NOT NULL,
    jobTitle VARCHAR(200),
    startDATE DATE NULL,
    endDATE DATE NULL,
    payWeekly DECIMAL,
    hoursWeekly INT,
    wayOfWorking ENUM('On-site', 'Hybrid', 'Remote') NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students (student_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (hiringManager_id) REFERENCES hiring_managers (hiringManager_id) ON UPDATE CASCADE ON DELETE CASCADE,
    INDEX idx_student_id (student_id),
    INDEX idx_hiringManager_id (hiringManager_id),
    INDEX idx_jobTitle (jobTitle)
);


-- This is the table for application metrics --
CREATE TABLE application_metrics (
   appMetrics_id INT AUTO_INCREMENT PRIMARY KEY,
   student_id INT,
   metricName VARCHAR(150) NOT NULL,
   obtainedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
   FOREIGN KEY (student_id) REFERENCES students (student_id),
   INDEX idx_student_id (student_id),
   INDEX idx_metricName (metricName)
);


-- This is the table for system administrators --
CREATE TABLE system_admin (
    systemAdmin_id INT PRIMARY KEY,
    appMetrics_id INT,
    role VARCHAR(200) NOT NULL,
    departmentBranch VARCHAR(200),
    permissionList MEDIUMTEXT,
    FOREIGN KEY (systemAdmin_id) REFERENCES users (id),
    FOREIGN KEY (appMetrics_id) REFERENCES application_metrics (appMetrics_id),
    INDEX idx_appMetrics_id (appMetrics_id),
    INDEX idx_role (role)
);


-- This is the table for system diagnostics --
CREATE TABLE system_diagnostics (
    systemDiagnostics_id INT AUTO_INCREMENT PRIMARY KEY,
    appMetrics_id INT,
    status ENUM('Operational', 'Warning', 'Error') NOT NULL,
    metric VARCHAR(100),
    errorCount INT,
    responseTimeToFix DECIMAL(10, 2),
    coopPostSpeed DECIMAL (10, 2),
    FOREIGN KEY (appMetrics_id) REFERENCES application_metrics (appMetrics_id),
    INDEX appMetrics_id (appMetrics_id)
);


-- This is the table for co-op postings --
CREATE TABLE coop_postings (
    coopPosting_id INT AUTO_INCREMENT PRIMARY KEY,
    company_id INT NOT NULL,
    hiringManager_id INT,
    jobTitle VARCHAR(200),
    jobDescription TEXT,
    location VARCHAR(200),
    jobType VARCHAR(50),
    pay DECIMAL(4, 2),
    companyBenefits TEXT,
    startDate DATE,
    endDate DATE,
    linkToApply VARCHAR(200),
    hiringManagerEmail VARCHAR(150),
    requirements TEXT,
    preferredSkills TEXT,
    createdAT DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updatedAT DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies (company_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (hiringManager_id) REFERENCES hiring_managers (hiringManager_id) ON UPDATE CASCADE ON DELETE CASCADE,
    INDEX idx_company_id (company_id),
    INDEX idx_hiringManager_id (hiringManager_id),
    INDEX idx_location (location),
    INDEX idx_jobType (jobType)
);

-- This is the table for applications for co-ops --
CREATE TABLE applications (
    application_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    coopPosting_id INT NOT NULL,
    applicationDueDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    resume MEDIUMTEXT NOT NULL,
    coverLetter MEDIUMTEXT,
    status ENUM('Accepted', 'Denied', 'Waiting') NOT NULL,
    createdAT DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updatedAT DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students (student_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (coopPosting_id) REFERENCES coop_postings (coopPosting_id) ON UPDATE CASCADE ON DELETE CASCADE,
    INDEX idx_student_id (student_id),
    INDEX idx_coopPosting_id (coopPosting_id)
);


-- This is the table for feedback posts --
CREATE TABLE feedback_posts (
    feedbackPost_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    studentEmployee_id INT NOT NULL,
    coopPosting_id INT NOT NULL,
    createdAT DATETIME NOT NULL,
    updatedAT DATETIME ON UPDATE CURRENT_TIMESTAMP,
    writtenReview TEXT NOT NULL,
    skillsLearned TEXT NOT NULL,
    challenges TEXT NOT NULL,
    roleSuggestions TEXT NOT NULL,
    returnOffer ENUM('Yes', 'No') NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students (student_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (studentEmployee_id) REFERENCES student_employees (studentEmployee_id) ON UPDATE CASCADE ON DELETE
        CASCADE,
    FOREIGN KEY (coopPosting_id) REFERENCES coop_postings (coopPosting_id) ON UPDATE CASCADE ON DELETE CASCADE,
    INDEX idx_student_id (student_id),
    INDEX idx_studentEmployee_id (studentEmployee_id),
    INDEX idx_coopPosting_id (coopPosting_id)
);

-- **************** INSERTING DUMMY DATA **********************
INSERT INTO users (firstName, middleName, lastName, mobile, email, username, password, country, state, town, userRole) VALUES
('John', 'Michael', 'Doe', '1234567890', 'john.doe@example.com', 'johndoe', 'password123', 'USA', 'California', 'Los Angeles', 'Hiring Manager'),
('Jane', 'Marie', 'Smith', '2345678901', 'jane.smith@example.com', 'janesmith', 'password123', 'USA', 'Texas', 'Dallas', 'Hiring Manager'),
('Alice', 'Lee', 'Johnson', '3456789012', 'alice.johnson@example.com', 'alicejohnson', 'password123', 'Canada', 'Ontario', 'Toronto', 'Hiring Manager'),
('Bob', 'David', 'Williams', '4567890123', 'bob.williams@example.com', 'bobwilliams', 'password123', 'UK', 'England', 'London', 'Hiring Manager'),
('Charlie', 'James', 'Brown', '5678901234', 'charlie.brown@example.com', 'charliebrown', 'password123', 'USA', 'Florida', 'Miami', 'Hiring Manager'),
('David', 'Ryan', 'Miller', '6789012345', 'david.miller@example.com', 'davidmiller', 'password123', 'Australia', 'Victoria', 'Melbourne', 'Hiring Manager'),
('Eva', 'Grace', 'Wilson', '7890123456', 'eva.wilson@example.com', 'evawilson', 'password123', 'USA', 'Florida', 'Miami', 'System Admin'),
('Frank', 'Edward', 'Moore', '8901234567', 'frank.moore@example.com', 'frankmoore', 'password123', 'Canada', 'Quebec', 'Montreal', 'Student'),
('Grace', 'Isabel', 'Taylor', '9012345678', 'grace.taylor@example.com', 'gracetaylor', 'password123', 'USA', 'Nevada', 'Las Vegas', 'Hiring Manager'),
('Hannah', 'Sophia', 'Anderson', '0123456789', 'hannah.anderson@example.com', 'hannahanderson', 'password123', 'UK', 'Scotland', 'Edinburgh', 'System Admin'),
('Ian', 'Samuel', 'Thomas', '1230987654', 'ian.thomas@example.com', 'ianthomas', 'password123', 'USA', 'Arizona', 'Phoenix', 'Student'),
('Jack', 'Alexander', 'Jackson', '2341098765', 'jack.jackson@example.com', 'jackjackson', 'password123', 'Australia', 'Queensland', 'Brisbane', 'Hiring Manager'),
('Katherine', 'Ellen', 'White', '3452109876', 'katherine.white@example.com', 'katherinewhite', 'password123', 'Canada', 'Alberta', 'Calgary', 'System Admin'),
('Liam', 'Benjamin', 'Harris', '4563210987', 'liam.harris@example.com', 'liamharris', 'password123', 'USA', 'Illinois', 'Chicago', 'Student'),
('Megan', 'Isabella', 'Clark', '5674321098', 'megan.clark@example.com', 'meganclark', 'password123', 'UK', 'Wales', 'Cardiff', 'Hiring Manager'),
('Noah', 'Lucas', 'Lewis', '6785432109', 'noah.lewis@example.com', 'noahlewis', 'password123', 'USA', 'Michigan', 'Detroit', 'System Admin'),
('Olivia', 'Charlotte', 'Walker', '7896543210', 'olivia.walker@example.com', 'oliviawalker', 'password123', 'Australia', 'New South Wales', 'Sydney', 'Student'),
('Paul', 'Christian', 'Hall', '8907654321', 'paul.hall@example.com', 'paulhall', 'password123', 'Canada', 'Manitoba', 'Winnipeg', 'Hiring Manager'),
('Quinn', 'Eliza', 'Young', '9018765432', 'quinn.young@example.com', 'quinnyoung', 'password123', 'USA', 'Oregon', 'Portland', 'System Admin'),
('Riley', 'John', 'King', '0129876543', 'riley.king@example.com', 'rileyking', 'password123', 'UK', 'Northern Ireland', 'Belfast', 'Student'),
('Samantha', 'Rose', 'Scott', '1230987612', 'samantha.scott@example.com', 'samanthascott', 'password123', 'Australia', 'South Australia', 'Adelaide', 'Hiring Manager'),
('Thomas', 'Patrick', 'Green', '2341098723', 'thomas.green@example.com', 'thomasgreen', 'password123', 'Canada', 'Nova Scotia', 'Halifax', 'System Admin'),
('Ursula', 'Riley', 'Adams', '3452109834', 'ursula.adams@example.com', 'ursulaadams', 'password123', 'USA', 'Ohio', 'Cleveland', 'Student'),
('Victor', 'George', 'Nelson', '4563210945', 'victor.nelson@example.com', 'victornelson', 'password123', 'UK', 'England', 'Manchester', 'Hiring Manager'),
('William', 'David', 'Carter', '5674321056', 'william.carter@example.com', 'williamcarter', 'password123', 'Canada', 'British Columbia', 'Vancouver', 'System Admin'),
('Xander', 'Ian', 'Evans', '6785432167', 'xander.evans@example.com', 'xanderevans', 'password123', 'USA', 'Washington', 'Seattle', 'Student'),
('Yvonne', 'Elena', 'Perez', '7896543278', 'yvonne.perez@example.com', 'yvonneperez', 'password123', 'Australia', 'Western Australia', 'Perth', 'Hiring Manager'),
('Zachary', 'Jared', 'Morris', '8907654389', 'zachary.morris@example.com', 'zacharymorris', 'password123', 'Canada', 'Ontario', 'Ottawa', 'System Admin'),
('Abigail', 'Victoria', 'Rodriguez', '9018765490', 'abigail.rodriguez@example.com', 'abigailrodriguez', 'password123', 'USA', 'California', 'San Francisco', 'Student'),
('Benjamin', 'Henry', 'Martinez', '0129876654', 'benjamin.martinez@example.com', 'benjaminmartinez', 'password123', 'UK', 'England', 'Birmingham', 'Hiring Manager'),
('Clara', 'Josephine', 'Gonzalez', '1230987656', 'clara.gonzalez@example.com', 'claragonzalez', 'password123', 'Australia', 'Tasmania', 'Hobart', 'System Admin'),
('Daniel', 'Aiden', 'Perez', '2341098760', 'daniel.perez@example.com', 'danielperez', 'password123', 'Canada', 'Ontario', 'Ottawa', 'Student'),
('Emma', 'Grace', 'Roberts', '3452109879', 'emma.roberts@example.com', 'emmaroberts', 'password123', 'USA', 'Tennessee', 'Nashville', 'Hiring Manager');

-- Insert 5 sample companies into the 'companies' table
INSERT INTO companies (
    companyName, industry, headquarters, companySize, headAddress, website, 
    openPositions, registeredAT, updatedAT
) VALUES
('Roblox', 'Technology', 'San Mateo, CA', 2400, '970 Park Place, Suite 100', 'https://roblox.com', 2, NOW(), NOW()),

('MarketX Digital', 'Marketing', 'New York, NY', 250, '456 Market St, Suite 200', 'https://www.marketx.com', 5, NOW(), NOW()),

('DataSolutions Inc.', 'Data Science', 'Chicago, IL', 500, '789 Data Blvd, Floor 3', 'https://www.datasolutions.com', 8, NOW(), NOW()),

('DesignWorks Agency', 'Design', 'Los Angeles, CA', 50, '321 Design Park, Suite 201', 'https://www.designworks.com', 3, NOW(), NOW()),

('HRPartners LLC', 'Human Resources', 'Dallas, TX', 100, '654 HR Lane, Office 405', 'https://www.hrpartners.com', 12, NOW(), NOW());


-- Insert data into the 'hiring_managers' table
INSERT INTO hiring_managers (
    hiringManager_id, company_id, jobTitle, experience, university, registeredAT, updatedAT
) VALUES
(1, 1, 'Senior Recruitment Manager', 8, 'Stanford University', NOW(), NOW()),

(2, 2, 'Marketing Director', 10, 'Harvard University', NOW(), NOW()),

(3, 3, 'Chief Data Scientist', 12, 'University of Chicago', NOW(), NOW()),

(4, 4, 'Creative Director', 7, 'California Institute of the Arts', NOW(), NOW()),

(5, 5, 'HR Manager', 5, 'University of Texas', NOW(), NOW());


INSERT INTO coop_postings (
    company_id, hiringManager_id, jobTitle, jobDescription, location, jobType, pay, 
    companyBenefits, startDate, endDate, linkToApply, hiringManagerEmail, 
    requirements, preferredSkills, createdAT, updatedAT
) VALUES 
(1, 1, 'Software Engineer Intern', 'As a software engineering intern, you will assist in developing cutting-edge software applications.', 'San Francisco, CA', 'Internship', 25.00, 
'Health insurance, 401k matching, Paid time off', '2024-01-15', '2024-06-15', 'https://example.com/apply/software-engineer', 'hiring.manager1@example.com', 
'Currently enrolled in a computer science or related field program. Basic knowledge of programming languages such as Java, Python, or C++ is required.', 
'Java, Python, C++, Problem-solving skills', '2024-12-01', '2024-12-05'),

(2, 2, 'Marketing Assistant', 'Assist in creating and managing digital marketing campaigns, content creation, and social media strategy.', 'New York, NY', 'Full-time', 20.00, 
'Health insurance, Paid sick leave, Free gym membership', '2024-02-01', '2024-08-01', 'https://example.com/apply/marketing-assistant', 'hiring.manager2@example.com', 
'Strong communication skills, Familiarity with social media platforms like Instagram, Facebook, and Twitter. Experience in marketing preferred.', 
'Digital marketing, Content creation, Social media management', '2024-11-26', '2024-12-02'),

(3, 3, 'Data Analyst Intern', 'We are looking for a data analyst intern to help with data processing, statistical analysis, and visualization projects.', 'Chicago, IL', 'Internship', 22.50, 
'Health benefits, Transportation stipend, Paid vacation', '2024-03-01', '2024-07-01', 'https://example.com/apply/data-analyst', 'hiring.manager3@example.com', 
'Currently pursuing a degree in data science, mathematics, or statistics. Familiarity with data analysis tools like Excel or Tableau is a plus.', 
'Excel, Tableau, Data analysis, Statistical modeling', '2024-11-20', '2024-11-25'),

(4, 4, 'Graphic Design Intern', 'Join our creative team and assist in creating engaging visuals, web designs, and brand assets.', 'Los Angeles, CA', 'Internship', 18.00, 
'Creative freedom, Health benefits, Paid holidays', '2024-04-01', '2024-09-01', 'https://example.com/apply/graphic-design', 'hiring.manager4@example.com', 
'Experience with Adobe Creative Suite (Photoshop, Illustrator, InDesign). A strong portfolio showcasing design skills is preferred.', 
'Adobe Photoshop, Adobe Illustrator, Graphic design, Branding', '2024-11-10', '2024-11-15'),

(5, 5, 'Human Resources Intern', 'Assist with recruitment, employee onboarding, and HR administrative tasks within the organization.', 'Dallas, TX', 'Internship', 20.00, 
'Health insurance, Paid time off, Professional development opportunities', '2024-05-15', '2024-08-15', 'https://example.com/apply/hr-intern', 'hiring.manager5@example.com', 
'Currently pursuing a degree in Human Resources or related field. Strong organizational skills and attention to detail.', 
'Human resources, Recruitment, Employee onboarding', '2024-11-15', '2024-11-18'),

(1, 1, 'Machine Learning Intern', 'As a Machine Learning Intern, you will assist in developing machine learning models, analyzing datasets, and applying AI techniques to real-world problems.', 
'San Francisco, CA', 'Internship', 30.00, 'Health insurance, 401k matching, Paid time off', '2024-01-15', '2024-06-15', 
'https://example.com/apply/machine-learning-intern', 'hiring.manager1@example.com', 
'Currently enrolled in a computer science, data science, or related field program. Basic knowledge of machine learning algorithms, data preprocessing, and Python is required.', 
'Python, TensorFlow, Scikit-learn, Data preprocessing, Machine learning algorithms', 
'2024-12-01', '2024-12-05');


INSERT INTO students (nu_id, enrollmentDate, graduationYear, gpa, transcript, resume, coverLetter) VALUES
(1001, '2020-09-01', 2024, 3.85, 'Transcript content', 'Resume content', 'Cover letter content'),
(1002, '2019-09-01', 2023, 3.90, 'Transcript content', 'Resume content', 'Cover letter content'),
(1003, '2021-09-01', 2025, 3.60, 'Transcript content', 'Resume content', 'Cover letter content'),
(1004, '2020-09-01', 2024, 3.75, 'Transcript content', 'Resume content', 'Cover letter content'),
(1005, '2019-09-01', 2023, 3.95, 'Transcript content', 'Resume content', 'Cover letter content');

INSERT INTO departments (departmentName) VALUES ('College of Science');
INSERT INTO departments (departmentName) VALUES ('Business');
INSERT INTO departments (departmentName) VALUES ('College of Social Sciences');
INSERT INTO departments (departmentName) VALUES ('Engineering');
INSERT INTO departments (departmentName) VALUES ('Computer Science');

INSERT INTO majors (student_id, department_id, name) VALUES
(1, 5, 'Computer Science'),
(2, 2, 'Marketing'),
(3, 3, 'Data Science'),
(4, 4, 'Mechanical Engineering'),
(5, 3, 'Human Resources');

INSERT INTO minors (student_id, department_id, name) VALUES
(1, 2, 'Business Administration'),
(2, 3, 'Psychology'),
(3, 1, 'Statistics'),
(4, 3, 'Law'),
(5, 2, 'Finance');

INSERT INTO application_metrics (student_id, metricName, obtainedAt) VALUES
(1, 'GPA', '2024-01-01'),
(2, 'Resume Score', '2024-02-01'),
(3, 'Interview Performance', '2024-03-01'),
(4, 'GPA', '2024-04-01'),
(5, 'Resume Score', '2024-05-01');

INSERT INTO system_admin (systemAdmin_id, appMetrics_id, role, departmentBranch, permissionList) VALUES
(7, 1, 'Admin', 'Engineering', 'Read, Write, Execute'),
(8, 2, 'Admin', 'Marketing', 'Read, Write'),
(9, 3, 'Admin', 'Data Science', 'Read, Execute'),
(10, 4, 'Admin', 'Design', 'Write'),
(11, 5, 'Admin', 'HR', 'Read');

INSERT INTO system_diagnostics (appMetrics_id, status, metric, errorCount, responseTimeToFix, coopPostSpeed) VALUES
(1, 'Operational', 'CPU Load', 0, 0.5, 1.2),
(2, 'Warning', 'Memory Usage', 2, 2.5, 1.0),
(3, 'Error', 'Disk Space', 5, 5.0, 0.8),
(4, 'Operational', 'Network Latency', 0, 0.2, 1.5),
(5, 'Warning', 'Database Connections', 3, 3.0, 1.1);

INSERT INTO student_employees (student_id, hiringManager_id, jobTitle, startDATE, endDATE, payWeekly, hoursWeekly, wayOfWorking) VALUES
(1, 1, 'Software Engineer Intern', '2024-01-15', '2024-06-15', 300.00, 20, 'Hybrid'),
(2, 2, 'Marketing Assistant', '2024-02-01', '2024-08-01', 200.00, 15, 'On-site'),
(3, 3, 'Data Analyst Intern', '2024-03-01', '2024-07-01', 225.00, 18, 'Remote'),
(4, 4, 'Graphic Design Intern', '2024-04-01', '2024-09-01', 180.00, 20, 'Hybrid'),
(5, 5, 'HR Intern', '2024-05-15', '2024-08-15', 200.00, 18, 'On-site');

INSERT INTO student_employees (student_id, hiringManager_id, jobTitle, startDATE, endDATE, payWeekly, hoursWeekly, wayOfWorking) VALUES
(1, 1, 'Software Engineer Intern', '2024-01-15', '2024-06-15', 300.00, 20, 'Hybrid'),
(2, 2, 'Marketing Assistant', '2024-02-01', '2024-08-01', 200.00, 15, 'On-site'),
(3, 3, 'Data Analyst Intern', '2024-03-01', '2024-07-01', 225.00, 18, 'Remote'),
(4, 4, 'Graphic Design Intern', '2024-04-01', '2024-09-01', 180.00, 20, 'Hybrid'),
(5, 5, 'HR Intern', '2024-05-15', '2024-08-15', 200.00, 18, 'On-site');

INSERT INTO applications (student_id, coopPosting_id, resume, coverLetter, status) VALUES
(1, 1, 'Resume content for software engineer', 'Cover letter content for software engineer', 'Waiting'),
(2, 2, 'Resume content for marketing assistant', 'Cover letter content for marketing assistant', 'Accepted'),
(3, 3, 'Resume content for data analyst', 'Cover letter content for data analyst', 'Denied'),
(4, 4, 'Resume content for graphic designer', 'Cover letter content for graphic designer', 'Waiting'),
(5, 5, 'Resume content for HR intern', 'Cover letter content for HR intern', 'Accepted');

INSERT INTO feedback_posts (student_id, studentEmployee_id, coopPosting_id, createdAT, updatedAT, writtenReview, skillsLearned, challenges, roleSuggestions, returnOffer) VALUES
(1, 1, 1, '2024-11-10 10:00:00', '2024-12-05 12:00:00',
    'I had a fantastic experience working with the development team during my internship. The team was very supportive, and I learned a great deal about software development processes. I worked on a variety of projects, including debugging existing code, implementing new features, and collaborating with team members to resolve issues. The work was challenging but rewarding, and I felt like my contributions were genuinely valued. The exposure to real-world software engineering practices was incredibly valuable, and I am excited to apply what I learned in future projects.',
    'Java, Problem-solving, Software Development, Git',
    'One of the biggest challenges I faced was understanding the full scope of some of the projects, especially those with complex codebases that had been built over time. Additionally, dealing with tight deadlines and balancing multiple tasks simultaneously was a bit overwhelming at times. However, the team was always there to help when I needed guidance.',
    'I think it would be helpful to provide more initial training on the company’s internal systems and tools. Having a better understanding of the architecture upfront would have made it easier to contribute more quickly to the team’s projects. Overall, the experience was very positive, and I feel I was able to grow significantly as a developer.',
    'Yes'
),
(2, 2, 1, '2024-11-12 11:30:00', '2024-12-05 14:00:00',
    'I had an amazing time working as a Software Development Intern. My tasks involved writing and debugging code, as well as assisting with feature implementation and testing. I had the opportunity to work with a talented team of developers who helped me improve my coding and problem-solving skills. I learned how to navigate version control systems like Git and got hands-on experience working with modern software development tools and practices. The work was challenging but fulfilling, and I felt that my contributions truly impacted the team’s progress.',
    'Java, Software Development, Git, Debugging, Problem-solving',
    'One of the challenges I faced was integrating new features into an existing codebase, especially when the code was complex and undocumented. There were times when it was difficult to identify the root cause of bugs, and working with legacy code required a bit more time than I expected. Additionally, working under tight deadlines and prioritizing tasks efficiently was an ongoing challenge.',
    'I would suggest providing more training on internal tools and frameworks that are used in development. A deeper understanding of the company’s coding standards and architecture early on would help new interns feel more prepared to contribute effectively from the beginning.',
    'Yes'
),
(2, 2, 2, '2024-11-12 09:30:00', '2024-12-04 15:30:00', 
    'This internship provided me with an incredible opportunity to learn about the fast-paced world of digital marketing. I had the chance to work on various campaigns, create content for social media, and assist with market research. I gained hands-on experience in content creation, audience targeting, and performance analysis. The best part was working closely with senior marketers, who provided valuable insights into strategic decision-making. I also had the opportunity to contribute to some high-visibility projects, which was a great learning experience.',
    'Content Creation, Social Media Strategy, Market Research, Google Analytics',
    'One of the biggest challenges was managing multiple projects with tight deadlines. Sometimes it felt like I had too many tasks to juggle at once, and it was difficult to prioritize effectively. Also, some campaigns had last-minute changes, which made it hard to keep everything on track. Despite this, I managed to adapt and learned how to work efficiently under pressure.',
    'I believe that having more structured timelines for each project would help interns manage expectations and workload more effectively. It would also be helpful to have a more clear onboarding process to get up to speed with the marketing tools and platforms the company uses.',
    'No'
),
(3, 3, 3, '2024-11-14 10:45:00', '2024-12-03 17:00:00',
    'My time as a Data Analyst Intern was a truly valuable experience. I worked on a variety of data-related tasks, including cleaning datasets, performing analysis using statistical software, and creating visualizations to present our findings. The team was extremely collaborative, and I had the opportunity to learn new techniques in data wrangling and visualization. I was also involved in interpreting data for client reports, which gave me a deeper understanding of how data analysis can influence business decisions.',
    'Excel, Data Visualization, Data Cleaning, SQL',
    'The most challenging aspect was dealing with extremely large datasets that sometimes contained inconsistencies or missing values. Cleaning and preparing the data for analysis was time-consuming, and it was difficult to ensure that the data was completely accurate. Additionally, while I had some experience with statistical software, the learning curve was steep, and I often had to spend extra time figuring out how to use advanced features.',
    'More hands-on training with statistical tools like R or Python would have been helpful, especially for interns who might not be familiar with these technologies. A clearer structure for data cleaning tasks and more guidance on data accuracy could also help to streamline the process.',
    'Yes'
),
(4, 4, 4, '2024-11-18 11:00:00', '2024-12-02 14:45:00',
    'As a Graphic Design Intern, I had the opportunity to work on a variety of creative projects, from designing social media graphics to creating print advertisements. The best part was working alongside a talented design team that provided constructive feedback and helped me improve my skills. I was also responsible for creating visual concepts for new campaigns, which required me to think creatively and develop ideas that aligned with the company’s branding strategy. Overall, it was an incredibly fulfilling experience, and I feel much more confident in my design abilities.',
    'Adobe Photoshop, Adobe Illustrator, Typography, Branding',
    'The biggest challenge I faced was trying to meet the expectations for design work while working under tight deadlines. At times, I struggled with balancing creativity and practicality, especially when there were last-minute changes to the project scope. Additionally, I found it difficult to manage my time between multiple ongoing design tasks, which sometimes caused stress and delays.',
    'I would recommend having a clearer timeline and more structured feedback sessions, so that designers can refine their concepts without feeling rushed. Additionally, it would be helpful to have more collaboration between the design team and other departments to ensure alignment on project objectives from the start.',
    'Yes'
),
(5, 5, 5, '2024-11-20 08:15:00', '2024-12-01 13:30:00',
    'Working in HR as an intern was an eye-opening experience. I had the chance to assist with a range of tasks, including recruitment, employee onboarding, and preparing training materials. I learned a great deal about the importance of maintaining employee relations and the intricacies of handling sensitive HR issues. The most valuable part of the experience was seeing how HR decisions directly impact employee satisfaction and retention. I also had the chance to sit in on meetings with senior HR leaders, which helped me gain a better understanding of strategic HR practices.',
    'Recruitment, Employee Onboarding, HRIS Systems, Conflict Resolution',
    'The most challenging aspect of this internship was managing multiple tasks that required a great deal of attention to detail. For example, during the recruitment process, it was essential to keep track of many applicants and ensure that all documentation was up to date. Additionally, I had to learn how to navigate the company’s HRIS system, which had a steep learning curve.',
    'It would be helpful to provide more training on the company’s HR systems early in the internship. Additionally, having more opportunities to shadow senior HR staff during interviews or meetings would have given me more insights into the strategic decision-making process.',
    'No'
);