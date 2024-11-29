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
    payWeekly DECIMAL(3, 2),
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
CREATE TABLE co_op_postings (
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
    FOREIGN KEY (coopPosting_id) REFERENCES co_op_postings (coopPosting_id) ON UPDATE CASCADE ON DELETE CASCADE,
    INDEX idx_student_id (student_id),
    INDEX idx_coopPosting_id (coopPosting_id)
);


-- This is the table for feedback posts --
CREATE TABLE feedback_posts (
    feedbackPost_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    studentEmployee_id INT NOT NULL,
    coopPosting_id INT NOT NULL,
    createdAT DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updatedAT DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    writtenReview TEXT NOT NULL,
    skillsLearned TEXT NOT NULL,
    challenges TEXT NOT NULL,
    roleSuggestions TEXT NOT NULL,
    returnOffer ENUM('Yes', 'No') NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students (student_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (studentEmployee_id) REFERENCES student_employees (studentEmployee_id) ON UPDATE CASCADE ON DELETE
        CASCADE,
    FOREIGN KEY (coopPosting_id) REFERENCES co_op_postings (coopPosting_id) ON UPDATE CASCADE ON DELETE CASCADE,
    INDEX idx_student_id (student_id),
    INDEX idx_studentEmployee_id (studentEmployee_id),
    INDEX idx_coopPosting_id (coopPosting_id)
);



-- Examples: --
/*
-- Examples for users: --
INSERT INTO users (email, username, password, userRole)
    VALUES ('browns@northeastern.edu', 'sammyb', 'sAm435*', 'Student'),
           ('myersk@northeastern.edu', 'myersk', 'horrorMovies97', 'System Admin'),
           ('emilyda@gmail.com', 'emilyDA', '37782', 'Hiring Manager'),
           ('brownda@gmail.com', 'davidBrown', '332182', 'Hiring Manager'),
           ('dannysky@northeastern.edu', 'dannysky', 'SkyIsLimit9', 'System Admin'),
           ('zuben@northeastern.edu', 'zuben', 'birdFlies', 'Student');
 */


/*
-- Examples for students: --
INSERT INTO students (nu_id, graduationYear, gpa, transcript, resume)
    VALUES ('002233442', '2027', '3.45', 'A, A, C+', 'AI Club, Volunteering'),
           ('002132442', '2025', '3.02', 'B, B, C+', 'Robotics Club');
 */


/*
-- Examples for departments: --
INSERT INTO departments (departmentName)
    VALUES ('Khoury College of Computer Sciences'),
           ('College of Arts, Media and Design');
 */


/*
-- Examples for majors: --
INSERT INTO majors (student_id, department_id, name)
    VALUES (1, 1,'Data Science'),
           (2, 2,'Game Design');
 */


/*
-- Examples for minors: --
INSERT INTO minors (student_id, department_id, name)
    VALUES (1, 1, 'Computer Science'),
           (2, 2,'Theatre');
 */


/*
-- Examples for companies: --
INSERT INTO companies (companyName, industry, website)
    VALUES ('Google', 'Technology', 'https://about.google'),
           ('Boston Center for the Arts', 'Performance Arts', 'https://bostonarts.org');
 */


/*
-- Examples for hiring_managers: --
INSERT INTO hiring_managers (hiringManager_id, company_id, jobTitle, experience)
    VALUES (3, 1, 'Hiring Manager for the Software Team at Google', 22),
           (4, 2,'Hiring Manager for the Theatre Group at BCA', 7);
 */


/*
-- Examples for student_employees --
INSERT INTO student_employees (student_id, hiringManager_id, wayOfWorking)
    VALUES (1, 3, 'Hybrid'),
           (2, 4, 'On-site');
 */


/*
-- Examples for application_metrics --
INSERT INTO application_metrics(metricName)
    VALUES ('Total Student User Count'),
           ('Average Student GPA across All Grades');
 */


/*
-- Examples for system_admin --
INSERT INTO system_admin(systemAdmin_id, role)
    VALUES (2, 'Developer for NUworks'),
           (5, 'Primary Error Patcher');
 */


/*
-- Examples for system_diagnostics --
INSERT INTO system_diagnostics(appMetrics_id, status)
    VALUES (1, 'Operational'),
           (2, 'Warning');
 */


/*
-- Examples for co_op_postings --
INSERT INTO co_op_postings(company_id)
    VALUES (1),
           (2);
*/


/*
-- Examples for feedback_posts --
INSERT INTO feedback_posts(studentEmployee_id, coopPosting_id, writtenReview, skillsLearned, challenges,
                           roleSuggestions, returnOffer)
    VALUES (1, 1, 'I had a great time working for Google.',
            'Advanced MySql', 'The communication between colleagues was sometimes difficult.',
            'Do not stress! There is a two-week transition period.', 'Yes'),
           (2, 2, 'I learned about the intricacies of performance arts.',
            'Play Dancing', 'It is very tiring.',
            'Only apply if you are willing to dance for hours on end.', 'No');
 */