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
('Default', 'Working','User', '1234567890', 'default@default.com','defaultuser','password','USA','Massachussetts','Boston', 'Student' ),
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
('Emily', 'Rose', 'Bennett', '2345678901', 'emily.bennett@example.com', 'emilybennett', 'password123', 'USA', 'California', 'San Diego', 'System Admin'),
('George', 'Aaron', 'Moore', '3456789012', 'george.moore@example.com', 'georgemoore', 'password123', 'Australia', 'Queensland', 'Gold Coast', 'Hiring Manager'),
('Holly', 'Jane', 'Taylor', '4567890123', 'holly.taylor@example.com', 'hollytaylor', 'password123', 'UK', 'England', 'Liverpool', 'Student'),
('Isaac', 'Michael', 'Wilson', '5678901234', 'isaac.wilson@example.com', 'isaacwilson', 'password123', 'Canada', 'Ontario', 'Ottawa', 'Hiring Manager'),
('Julia', 'Sophia', 'Evans', '6789012345', 'julia.evans@example.com', 'juliaevans', 'password123', 'USA', 'New York', 'Brooklyn', 'System Admin'),
('Kevin', 'Louis', 'Hughes', '7890123456', 'kevin.hughes@example.com', 'kevinhughes', 'password123', 'Australia', 'Victoria', 'Melbourne', 'Student'),
('Lily', 'Grace', 'Campbell', '8901234567', 'lily.campbell@example.com', 'lilycampbell', 'password123', 'UK', 'Scotland', 'Glasgow', 'Hiring Manager');


-- Insert 5 sample companies into the 'companies' table
INSERT INTO companies (
    companyName, industry, headquarters, companySize, headAddress, website, 
    openPositions, registeredAT, updatedAT
) VALUES
('Roblox', 'Technology', 'San Mateo, CA', 2400, '970 Park Place, Suite 100', 'https://roblox.com', 2, NOW(), NOW()),
('MarketX Digital', 'Marketing', 'New York, NY', 250, '456 Market St, Suite 200', 'https://www.marketx.com', 5, NOW(), NOW()),
('DataSolutions Inc.', 'Data Science', 'Chicago, IL', 500, '789 Data Blvd, Floor 3', 'https://www.datasolutions.com', 8, NOW(), NOW()),
('DesignWorks Agency', 'Design', 'Los Angeles, CA', 50, '321 Design Park, Suite 201', 'https://www.designworks.com', 3, NOW(), NOW()),
('HRPartners LLC', 'Human Resources', 'Dallas, TX', 100, '654 HR Lane, Office 405', 'https://www.hrpartners.com', 12, NOW(), NOW()),
('TechNova Solutions', 'Technology', 'San Francisco, CA', 150, '101 Silicon Ave, Suite 500', 'https://www.technova.com', 4, NOW(), NOW()),
('GreenSky Industries', 'Renewable Energy', 'Denver, CO', 200, '202 Green St, Suite 305', 'https://www.greensky.com', 6, NOW(), NOW()),
('FinSecure Technologies', 'Finance', 'New York, NY', 120, '333 Wall St, 7th Floor', 'https://www.finsecure.com', 10, NOW(), NOW()),
('HealthPrime Innovations', 'Healthcare', 'Austin, TX', 300, '456 Wellness Blvd, Suite 700', 'https://www.healthprime.com', 15, NOW(), NOW()),
('CloudSync Solutions', 'Cloud Computing', 'Seattle, WA', 400, '789 Cloud Rd, Suite 1200', 'https://www.cloudsync.com', 9, NOW(), NOW()),
('SmartHome Inc.', 'Technology', 'Chicago, IL', 500, '123 Home St, Floor 4', 'https://www.smarthome.com', 8, NOW(), NOW()),
('RetailMax Corporation', 'Retail', 'Los Angeles, CA', 800, '432 Market St, Suite 900', 'https://www.retailmax.com', 20, NOW(), NOW()),
('ByteWave Studios', 'Entertainment', 'Hollywood, CA', 150, '678 Studio Rd, Suite 250', 'https://www.bytewave.com', 7, NOW(), NOW()),
('FleetWorks Logistics', 'Logistics', 'Dallas, TX', 600, '234 Logistics Dr, Suite 1000', 'https://www.fleetworks.com', 14, NOW(), NOW()),
('NextGen Labs', 'Biotechnology', 'San Diego, CA', 200, '876 Lab Park, Floor 5', 'https://www.nextgenlabs.com', 4, NOW(), NOW()),
('CitySmart Technologies', 'Smart City Solutions', 'New York, NY', 350, '123 Urban St, Suite 800', 'https://www.citysmart.com', 12, NOW(), NOW()),
('EduConnect Solutions', 'Education', 'Toronto, ON', 100, '456 Learning Ave, Suite 300', 'https://www.educonnect.com', 5, NOW(), NOW()),
('MediPro Health', 'Healthcare', 'Vancouver, BC', 250, '789 Health Rd, Suite 200', 'https://www.mediprohealth.com', 6, NOW(), NOW()),
('NextWave Digital', 'Marketing', 'Miami, FL', 150, '123 Digital Blvd, Suite 450', 'https://www.nextwavedigital.com', 3, NOW(), NOW()),
('CyberGuard Security', 'Cybersecurity', 'San Jose, CA', 500, '234 Security St, Suite 600', 'https://www.cyberguard.com', 10, NOW(), NOW()),
('QuantumTech Innovations', 'Technology', 'Boston, MA', 400, '500 Quantum Blvd, Suite 200', 'https://www.quantumtech.com', 5, NOW(), NOW()),
('EcoLife Solutions', 'Environmental', 'San Francisco, CA', 150, '100 Green Lane, Suite 100', 'https://www.ecolife.com', 3, NOW(), NOW()),
('BrightPath Education', 'Education', 'New York, NY', 80, '250 Bright Ave, Suite 300', 'https://www.brightpath.com', 4, NOW(), NOW()),
('Vanguard Ventures', 'Finance', 'Los Angeles, CA', 350, '150 Capital Blvd, Suite 500', 'https://www.vanguardventures.com', 6, NOW(), NOW()),
('BlueWave Industries', 'Renewable Energy', 'Houston, TX', 200, '800 BlueWave Rd, Suite 700', 'https://www.bluewaveindustries.com', 7, NOW(), NOW()),
('FusionLabs', 'Biotechnology', 'San Diego, CA', 100, '220 Fusion St, Floor 4', 'https://www.fusionlabs.com', 3, NOW(), NOW()),
('AeroTech Dynamics', 'Aerospace', 'Phoenix, AZ', 500, '350 Aero Park, Suite 900', 'https://www.aerotechdynamics.com', 10, NOW(), NOW()),
('MedicarePlus', 'Healthcare', 'Chicago, IL', 800, '400 Health St, Suite 600', 'https://www.medicareplus.com', 12, NOW(), NOW()),
('AgriMax Solutions', 'Agriculture', 'Dallas, TX', 150, '789 Farm Rd, Suite 200', 'https://www.agrimaxsolutions.com', 5, NOW(), NOW()),
('SkyNet Technologies', 'Technology', 'Seattle, WA', 300, '600 Sky Rd, Suite 500', 'https://www.skynet.com', 9, NOW(), NOW()),
('GreenSprout Innovations', 'Environmental', 'Portland, OR', 120, '800 GreenSprout Ave, Suite 100', 'https://www.greensprout.com', 4, NOW(), NOW()),
('NextStep Robotics', 'Technology', 'Austin, TX', 250, '450 Robot St, Floor 5', 'https://www.nextsteprobotics.com', 6, NOW(), NOW()),
('UrbanGrid Solutions', 'Urban Development', 'Chicago, IL', 200, '500 Urban Grid Rd, Suite 100', 'https://www.urbangridsolutions.com', 8, NOW(), NOW()),
('MetaCloud Systems', 'Cloud Computing', 'San Jose, CA', 400, '1200 MetaCloud Dr, Suite 700', 'https://www.metacloudsystems.com', 11, NOW(), NOW()),
('BrightFuture Innovations', 'Technology', 'Los Angeles, CA', 150, '300 BrightFuture Blvd, Suite 400', 'https://www.brightfuture.com', 7, NOW(), NOW()),
('SolarTech Industries', 'Renewable Energy', 'Denver, CO', 250, '123 Solar Way, Suite 150', 'https://www.solartech.com', 5, NOW(), NOW()),
('CodeCraft Studios', 'Software Development', 'Austin, TX', 100, '789 Code St, Suite 350', 'https://www.codecraft.com', 4, NOW(), NOW()),
('SmartAgri Solutions', 'Agriculture Technology', 'Des Moines, IA', 300, '234 Agri Rd, Floor 2', 'https://www.smartagri.com', 8, NOW(), NOW()),
('Visionary Films', 'Entertainment', 'Los Angeles, CA', 120, '567 Vision Blvd, Suite 200', 'https://www.visionaryfilms.com', 3, NOW(), NOW()),
('Quantum Logistics', 'Logistics', 'Memphis, TN', 400, '901 Quantum Ave, Suite 600', 'https://www.quantumlogistics.com', 10, NOW(), NOW()),
('BioCare Pharma', 'Pharmaceuticals', 'Boston, MA', 500, '789 Care Rd, Suite 900', 'https://www.biocarepharma.com', 6, NOW(), NOW()),
('NextGen AI', 'Artificial Intelligence', 'San Francisco, CA', 150, '450 AI Blvd, Suite 300', 'https://www.nextgenai.com', 9, NOW(), NOW()),
('EnviroWave Tech', 'Environmental Technology', 'Portland, OR', 200, '678 Green Lane, Suite 150', 'https://www.envirowave.com', 7, NOW(), NOW()),
('CyberDefend Solutions', 'Cybersecurity', 'San Jose, CA', 500, '321 Cyber Dr, Suite 800', 'https://www.cyberdefend.com', 12, NOW(), NOW()),
('MegaRetail Corp', 'Retail', 'New York, NY', 1000, '150 Retail Park, Suite 500', 'https://www.megaretail.com', 20, NOW(), NOW()),
('CleanEnergy Tech', 'Renewable Energy', 'Denver, CO', 220, '234 Clean Blvd, Suite 300', 'https://www.cleanenergy.com', 5, NOW(), NOW()),
('FutureMeds Inc.', 'Healthcare', 'Houston, TX', 400, '567 Med Rd, Suite 200', 'https://www.futuremeds.com', 11, NOW(), NOW()),
('UrbanConnect Solutions', 'Smart City Solutions', 'Chicago, IL', 350, '123 Urban Ave, Suite 400', 'https://www.urbanconnect.com', 6, NOW(), NOW()),
('BioTech Advanced', 'Biotechnology', 'San Diego, CA', 450, '789 Bio Park, Floor 3', 'https://www.biotechadvanced.com', 4, NOW(), NOW()),
('EcomWorks', 'E-commerce', 'Seattle, WA', 300, '567 Ecom Rd, Suite 700', 'https://www.ecomworks.com', 9, NOW(), NOW()),
('FinancePros', 'Finance', 'New York, NY', 600, '456 Wall St, Suite 600', 'https://www.financepros.com', 12, NOW(), NOW()),
('EduBridge Tech', 'Education Technology', 'Toronto, ON', 200, '345 Bridge Ave, Suite 100', 'https://www.edubridge.com', 3, NOW(), NOW()),
('Wellness Solutions', 'Healthcare', 'Vancouver, BC', 250, '789 Wellness Rd, Suite 250', 'https://www.wellnesssolutions.com', 8, NOW(), NOW()),
('GreenEarth Industries', 'Environmental', 'San Francisco, CA', 150, '300 Green Blvd, Suite 100', 'https://www.greenearth.com', 5, NOW(), NOW()),
('TechFlow Innovations', 'Technology', 'Austin, TX', 100, '567 Flow Blvd, Suite 150', 'https://www.techflow.com', 2, NOW(), NOW()),
('BrightVision Media', 'Marketing', 'Miami, FL', 80, '123 Vision Blvd, Suite 200', 'https://www.brightvision.com', 6, NOW(), NOW()),
('SecureNet Systems', 'Cybersecurity', 'San Jose, CA', 500, '890 Security Ave, Suite 600', 'https://www.securenetsystems.com', 7, NOW(), NOW()),
('EcoSmart Innovations', 'Environmental', 'Portland, OR', 200, '789 Eco St, Suite 300', 'https://www.ecosmart.com', 4, NOW(), NOW()),
('BlueSky Aviation', 'Aerospace', 'Phoenix, AZ', 300, '567 Sky Ave, Suite 200', 'https://www.blueskyaviation.com', 9, NOW(), NOW()),
('RetailHub Corporation', 'Retail', 'Los Angeles, CA', 800, '450 Retail Blvd, Suite 400', 'https://www.retailhub.com', 15, NOW(), NOW());

-- Insert data into the 'hiring_managers' table
INSERT INTO hiring_managers (
    hiringManager_id, company_id, jobTitle, experience, university, registeredAT, updatedAT
) VALUES
(1, 1, 'Senior Recruitment Manager', 8, 'Stanford University', NOW(), NOW()),
(2, 2, 'Marketing Director', 10, 'Harvard University', NOW(), NOW()),
(3, 3, 'Chief Data Scientist', 12, 'University of Chicago', NOW(), NOW()),
(4, 4, 'Creative Director', 7, 'California Institute of the Arts', NOW(), NOW()),
(5, 5, 'HR Manager', 5, 'University of Texas', NOW(), NOW()),
(6, 6, 'Lead Engineer', 9, 'Massachusetts Institute of Technology', NOW(), NOW()),
(7, 7, 'Operations Director', 15, 'University of Michigan', NOW(), NOW()),
(8, 8, 'Product Development Manager', 6, 'University of California, Berkeley', NOW(), NOW()),
(9, 9, 'Sales Executive', 4, 'University of Pennsylvania', NOW(), NOW()),
(10, 10, 'Cybersecurity Specialist', 8, 'Carnegie Mellon University', NOW(), NOW()),
(11, 11, 'Logistics Manager', 10, 'Texas A&M University', NOW(), NOW()),
(12, 12, 'Customer Relations Manager', 7, 'University of Washington', NOW(), NOW()),
(13, 13, 'Innovation Strategist', 6, 'University of Colorado', NOW(), NOW()),
(14, 14, 'Chief Operations Officer', 20, 'Cornell University', NOW(), NOW()),
(15, 15, 'Healthcare Consultant', 9, 'University of Southern California', NOW(), NOW()),
(16, 16, 'Software Engineering Manager', 11, 'University of Illinois', NOW(), NOW()),
(17, 17, 'Data Analytics Lead', 10, 'Columbia University', NOW(), NOW()),
(18, 18, 'Cloud Architect', 12, 'Duke University', NOW(), NOW()),
(19, 19, 'Environmental Scientist', 8, 'Yale University', NOW(), NOW()),
(20, 20, 'Creative Advertising Manager', 5, 'Princeton University', NOW(), NOW()),
(21, 21, 'Financial Analyst', 6, 'University of California, Los Angeles', NOW(), NOW()),
(22, 22, 'HR Specialist', 3, 'University of Florida', NOW(), NOW()),
(23, 23, 'Biotech Research Manager', 14, 'Johns Hopkins University', NOW(), NOW()),
(24, 24, 'Marketing Analyst', 5, 'New York University', NOW(), NOW()),
(25, 25, 'Retail Manager', 7, 'Boston University', NOW(), NOW()),
(26, 26, 'Robotics Engineer', 8, 'Georgia Institute of Technology', NOW(), NOW()),
(27, 27, 'Urban Planning Manager', 10, 'University of Toronto', NOW(), NOW()),
(28, 28, 'Quality Assurance Lead', 6, 'University of Waterloo', NOW(), NOW()),
(29, 29, 'AI Specialist', 13, 'University of California, San Diego', NOW(), NOW()),
(30, 30, 'Aerospace Engineer', 15, 'Purdue University', NOW(), NOW()),
(31, 31, 'Healthcare Operations Manager', 10, 'University of North Carolina', NOW(), NOW()),
(32, 32, 'Supply Chain Coordinator', 8, 'McGill University', NOW(), NOW()),
(33, 33, 'Education Specialist', 9, 'University of British Columbia', NOW(), NOW()),
(34, 34, 'Cloud Computing Consultant', 11, 'University of Maryland', NOW(), NOW()),
(35, 35, 'Renewable Energy Analyst', 7, 'University of Alberta', NOW(), NOW()),
(36, 36, 'Entertainment Manager', 5, 'University of California, Irvine', NOW(), NOW()),
(37, 37, 'Chief Financial Officer', 18, 'Wharton School of Business', NOW(), NOW()),
(38, 38, 'Public Relations Specialist', 4, 'University of Western Ontario', NOW(), NOW()),
(39, 39, 'Chief Marketing Officer', 14, 'Northwestern University', NOW(), NOW()),
(40, 40, 'Agricultural Consultant', 8, 'University of Saskatchewan', NOW(), NOW());


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
'2024-12-01', '2024-12-05'),

(6, 6, 'Product Management Intern', 'Assist the product management team in researching market trends, creating product roadmaps, and collaborating with cross-functional teams.', 'Austin, TX', 'Internship', 28.00, 
'Health insurance, Stock options, Paid time off', '2024-02-01', '2024-07-01', 'https://example.com/apply/product-management-intern', 'hiring.manager6@example.com', 
'Currently pursuing a degree in Business, Marketing, or a related field. Strong communication and organizational skills required.', 
'Product management, Market research, Cross-functional collaboration', '2024-12-01', '2024-12-05'),

(7, 7, 'Sales Intern', 'Help the sales team with customer outreach, lead generation, and managing the sales pipeline.', 'Miami, FL', 'Internship', 18.50, 
'Health benefits, Commission-based incentives, Paid sick leave', '2024-03-01', '2024-08-01', 'https://example.com/apply/sales-intern', 'hiring.manager7@example.com', 
'Currently pursuing a degree in Business, Marketing, or related field. Strong interpersonal skills and an interest in sales.', 
'Sales, Customer outreach, Lead generation', '2024-12-02', '2024-12-05'),

(8, 8, 'Operations Assistant', 'Assist the operations team in optimizing processes, managing inventory, and tracking shipments.', 'Houston, TX', 'Full-time', 21.00, 
'Health insurance, Paid time off, Retirement plan', '2024-02-15', '2024-08-15', 'https://example.com/apply/operations-assistant', 'hiring.manager8@example.com', 
'Strong organizational skills, Proficiency in Microsoft Excel, Attention to detail.', 
'Logistics, Inventory management, Process optimization', '2024-11-18', '2024-12-05'),

(9, 9, 'Content Writer Intern', 'Join our content team to help with writing blogs, articles, and social media content.', 'Denver, CO', 'Internship', 20.00, 
'Health insurance, Paid time off, Free snacks', '2024-04-01', '2024-09-01', 'https://example.com/apply/content-writer', 'hiring.manager9@example.com', 
'Strong writing and editing skills. Experience in content creation or journalism is preferred.', 
'Content writing, Editing, Research', '2024-11-22', '2024-12-01'),

(10, 10, 'Software Developer Intern', 'Work with the development team to design, implement, and test software solutions for various applications.', 'Seattle, WA', 'Internship', 25.00, 
'Health benefits, Stock options, Paid vacation', '2024-06-01', '2024-12-01', 'https://example.com/apply/software-developer-intern', 'hiring.manager10@example.com', 
'Currently pursuing a degree in Computer Science or related field. Proficiency in at least one programming language (Java, Python, C++).', 
'Java, Python, C++, Software development, Problem-solving', '2024-11-23', '2024-12-02'),

(11, 11, 'UI/UX Design Intern', 'Assist the design team in creating user-friendly and visually appealing interfaces for web and mobile applications.', 'Chicago, IL', 'Internship', 22.00, 
'Health insurance, Paid holidays, Career development workshops', '2024-05-01', '2024-10-01', 'https://example.com/apply/ui-ux-design-intern', 'hiring.manager11@example.com', 
'Experience with design tools like Figma or Sketch. A portfolio showcasing UI/UX design projects is preferred.', 
'UI design, UX design, Figma, Sketch', '2024-12-01', '2024-12-05'),

(12, 12, 'Business Analyst Intern', 'Support the business analysis team by gathering requirements, analyzing business processes, and creating reports to improve operational efficiency.', 'Los Angeles, CA', 'Internship', 23.00, 
'Health insurance, Professional development allowance, Paid time off', '2024-03-15', '2024-08-15', 'https://example.com/apply/business-analyst-intern', 'hiring.manager12@example.com', 
'Currently pursuing a degree in Business, Economics, or related field. Strong analytical and problem-solving skills.', 
'Business analysis, Reporting, Process improvement', '2024-11-25', '2024-12-02'),

(13, 13, 'Financial Analyst Intern', 'Assist the finance team with financial modeling, budget forecasting, and data analysis for business performance insights.', 'Boston, MA', 'Internship', 26.00, 
'Health benefits, 401k matching, Paid sick leave', '2024-06-01', '2024-12-01', 'https://example.com/apply/financial-analyst-intern', 'hiring.manager13@example.com', 
'Currently pursuing a degree in Finance, Accounting, or related field. Proficiency in Excel and financial analysis tools is a plus.', 
'Financial modeling, Excel, Budget forecasting', '2024-11-20', '2024-12-01'),

(14, 14, 'Legal Assistant Intern', 'Assist the legal team in conducting legal research, preparing documents, and supporting case management.', 'San Diego, CA', 'Internship', 24.00, 
'Health insurance, Paid vacation, Legal mentorship opportunities', '2024-07-01', '2024-12-01', 'https://example.com/apply/legal-assistant-intern', 'hiring.manager14@example.com', 
'Currently pursuing a degree in Law or related field. Strong research and writing skills required.', 
'Legal research, Document preparation, Case management', '2024-12-01', '2024-12-05'),

(15, 15, 'Customer Support Intern', 'Support our customer service team by assisting with customer inquiries, troubleshooting issues, and providing feedback for improvements.', 'Phoenix, AZ', 'Internship', 18.00, 
'Health benefits, Paid time off, Career growth opportunities', '2024-05-01', '2024-10-01', 'https://example.com/apply/customer-support-intern', 'hiring.manager15@example.com', 
'Strong communication and problem-solving skills. Previous customer service experience is a plus.', 
'Customer support, Problem-solving, Communication', '2024-12-02', '2024-12-05'),

(16, 16, 'Operations Intern', 'Assist the operations team with data analysis, project management, and operational efficiency improvements.', 'New York, NY', 'Internship', 21.00, 
'Health insurance, Paid time off, Training sessions', '2024-08-01', '2024-12-01', 'https://example.com/apply/operations-intern', 'hiring.manager16@example.com', 
'Currently pursuing a degree in Business Administration, Operations Management, or related field. Strong analytical and organizational skills.', 
'Operations management, Project management, Data analysis', '2024-11-28', '2024-12-05'),

(17, 17, 'Research Intern', 'Join our research team to assist in gathering data, conducting experiments, and analyzing results for various projects.', 'Boston, MA', 'Internship', 22.00, 
'Health benefits, Paid sick leave, Academic conference opportunities', '2024-04-01', '2024-09-01', 'https://example.com/apply/research-intern', 'hiring.manager17@example.com', 
'Currently pursuing a degree in Science, Engineering, or related field. Strong research and problem-solving skills required.', 
'Research, Data collection, Experimentation', '2024-11-23', '2024-12-01'),

(18, 18, 'Operations Research Intern', 'Assist in modeling, analyzing, and optimizing business processes and operational workflows.', 'Dallas, TX', 'Internship', 23.00, 
'Health benefits, Paid time off, Tuition reimbursement', '2024-06-01', '2024-11-01', 'https://example.com/apply/operations-research-intern', 'hiring.manager18@example.com', 
'Currently pursuing a degree in Operations Research, Industrial Engineering, or related field. Experience with optimization tools is a plus.', 
'Operations research, Optimization, Process modeling', '2024-11-21', '2024-12-02'),

(20, 20, 'Cybersecurity Intern', 'Assist the cybersecurity team with monitoring network traffic, conducting vulnerability assessments, and developing security protocols.', 'Atlanta, GA', 'Internship', 30.00, 
'Health insurance, Paid time off, Security certifications', '2024-06-15', '2024-11-15', 'https://example.com/apply/cybersecurity-intern', 'hiring.manager20@example.com', 
'Currently pursuing a degree in Cybersecurity, Computer Science, or related field. Familiarity with security tools such as firewalls and encryption techniques is a plus.', 
'Cybersecurity, Vulnerability assessment, Network monitoring', '2024-12-01', '2024-12-05'),

(21, 21, 'Video Production Intern', 'Assist in the production and editing of video content for marketing, training, and internal communications.', 'San Francisco, CA', 'Internship', 23.50, 
'Health insurance, Paid holidays, Creative freedom', '2024-03-01', '2024-08-01', 'https://example.com/apply/video-production-intern', 'hiring.manager21@example.com', 
'Experience with video editing software like Adobe Premiere Pro or Final Cut Pro. A portfolio of past work is preferred.', 
'Video editing, Storyboarding, Production', '2024-11-19', '2024-12-02'),

(22, 22, 'Public Relations Intern', 'Assist the PR team in managing media relations, writing press releases, and organizing public events.', 'New York, NY', 'Internship', 24.00, 
'Health insurance, Paid time off, PR agency exposure', '2024-07-01', '2024-12-01', 'https://example.com/apply/pr-intern', 'hiring.manager22@example.com', 
'Currently pursuing a degree in Public Relations, Communications, or related field. Strong writing and interpersonal skills are required.', 
'Public relations, Media relations, Writing', '2024-11-21', '2024-12-05'),

(23, 23, 'Event Planning Intern', 'Assist in the coordination and execution of corporate events, including logistics, vendor management, and client communication.', 'Los Angeles, CA', 'Internship', 22.00, 
'Health insurance, Event tickets, Networking opportunities', '2024-05-01', '2024-10-01', 'https://example.com/apply/event-planning-intern', 'hiring.manager23@example.com', 
'Strong organizational skills and attention to detail. Prior experience in event coordination is a plus.', 
'Event coordination, Vendor management, Logistics', '2024-11-20', '2024-12-02'),

(24, 24, 'Database Administrator Intern', 'Assist the DBA team in maintaining and optimizing databases, ensuring data security, and performing backups and restores.', 'Houston, TX', 'Internship', 26.00, 
'Health benefits, Paid sick leave, Learning resources', '2024-06-01', '2024-12-01', 'https://example.com/apply/db-admin-intern', 'hiring.manager24@example.com', 
'Currently pursuing a degree in Computer Science, Information Systems, or related field. Familiarity with SQL and database management tools is a plus.', 
'Database management, SQL, Data security', '2024-11-24', '2024-12-05'),

(25, 25, 'Cloud Engineering Intern', 'Help the cloud team with designing, deploying, and maintaining cloud-based infrastructure and services.', 'Seattle, WA', 'Internship', 28.00, 
'Health insurance, Stock options, Paid time off', '2024-04-15', '2024-09-15', 'https://example.com/apply/cloud-engineering-intern', 'hiring.manager25@example.com', 
'Currently pursuing a degree in Cloud Computing, Computer Science, or related field. Experience with cloud platforms like AWS or Azure is preferred.', 
'Cloud computing, AWS, Azure, Infrastructure management', '2024-12-01', '2024-12-05'),

(26, 26, 'Content Marketing Intern', 'Assist the marketing team with content creation, campaign management, and performance analysis for digital marketing initiatives.', 'Chicago, IL', 'Internship', 21.00, 
'Health benefits, Free snacks, Paid time off', '2024-08-01', '2024-12-01', 'https://example.com/apply/content-marketing-intern', 'hiring.manager26@example.com', 
'Strong writing skills, Familiarity with SEO principles, Experience in social media marketing preferred.', 
'Content marketing, SEO, Social media', '2024-11-18', '2024-12-01'),

(27, 27, 'Business Development Intern', 'Assist the business development team in identifying growth opportunities, researching new markets, and generating leads for expansion.', 'Austin, TX', 'Internship', 23.00, 
'Health insurance, Paid vacation, Training programs', '2024-06-01', '2024-11-01', 'https://example.com/apply/business-development-intern', 'hiring.manager27@example.com', 
'Currently pursuing a degree in Business Administration, Marketing, or related field. Strong analytical and communication skills.', 
'Business development, Market research, Lead generation', '2024-12-02', '2024-12-05'),

(28, 28, 'Human Resources Assistant', 'Assist the HR team in employee recruitment, onboarding, and performance management tasks.', 'San Diego, CA', 'Full-time', 20.00, 
'Health insurance, Paid time off, Employee discounts', '2024-01-01', '2024-06-01', 'https://example.com/apply/hr-assistant', 'hiring.manager28@example.com', 
'Strong communication skills, Ability to handle sensitive information, HR software knowledge a plus.', 
'Human resources, Recruitment, Onboarding', '2024-11-23', '2024-12-01'),

(29, 29, 'Product Design Intern', 'Support the product team with designing user interfaces, wireframes, and prototypes for new product features.', 'Denver, CO', 'Internship', 25.00, 
'Health benefits, Paid time off, Design team exposure', '2024-04-15', '2024-09-15', 'https://example.com/apply/product-design-intern', 'hiring.manager29@example.com', 
'Currently pursuing a degree in Product Design, Interaction Design, or related field. Familiarity with design tools such as Figma or Adobe XD is a plus.', 
'Product design, Figma, Prototyping', '2024-11-21', '2024-12-02'),

(30, 30, 'Quality Assurance Intern', 'Assist the QA team in testing software applications, identifying bugs, and ensuring product quality before release.', 'Miami, FL', 'Internship', 22.00, 
'Health insurance, Paid sick leave, Testing certifications', '2024-07-01', '2024-12-01', 'https://example.com/apply/quality-assurance-intern', 'hiring.manager30@example.com', 
'Currently pursuing a degree in Computer Science, Software Engineering, or related field. Familiarity with testing tools like Selenium is a plus.', 
'Quality assurance, Software testing, Bug tracking', '2024-12-02', '2024-12-05'),

(31, 31, 'Social Media Intern', 'Help manage social media accounts, create engaging content, and track campaign performance for the company’s social media presence.', 'Chicago, IL', 'Internship', 20.00, 
'Health benefits, Paid time off, Creative flexibility', '2024-05-15', '2024-10-15', 'https://example.com/apply/social-media-intern', 'hiring.manager31@example.com', 
'Strong understanding of social media platforms and trends. Experience with social media management tools is a plus.', 
'Social media, Content creation, Campaign management', '2024-11-20', '2024-12-01'),

(32, 32, 'Supply Chain Intern', 'Assist in optimizing the supply chain by analyzing data, improving processes, and managing supplier relationships.', 'San Francisco, CA', 'Internship', 24.00, 
'Health insurance, Paid holidays, Supply chain conferences', '2024-08-01', '2024-12-01', 'https://example.com/apply/supply-chain-intern', 'hiring.manager32@example.com', 
'Currently pursuing a degree in Supply Chain Management, Business, or related field. Proficiency in Microsoft Excel is required.', 
'Supply chain management, Data analysis, Process optimization', '2024-12-02', '2024-12-05');

INSERT INTO students (nu_id, enrollmentDate, graduationYear, gpa, transcript, resume, coverLetter) VALUES
#THIS IS THE USER FOR SIMULATION FOR WRITING REVIEW
(1, '2020-09-01', 2024, 3.85, 'Transcript content', 'Resume content', 'Cover letter content'),
(2, '2020-09-01', 2024, 3.85, 'Transcript content', 'Resume content', 'Cover letter content'),
(3, '2019-09-01', 2023, 3.90, 'Transcript content', 'Resume content', 'Cover letter content'),
(4, '2021-09-01', 2025, 3.60, 'Transcript content', 'Resume content', 'Cover letter content'),
(5, '2020-09-01', 2024, 3.75, 'Transcript content', 'Resume content', 'Cover letter content'),
(6, '2019-09-01', 2023, 3.95, 'Transcript content', 'Resume content', 'Cover letter content'),
(7, '2021-09-01', 2025, 3.80, 'Transcript content', 'Resume content', 'Cover letter content'),
(8, '2020-09-01', 2024, 3.65, 'Transcript content', 'Resume content', 'Cover letter content'),
(9, '2019-09-01', 2023, 3.70, 'Transcript content', 'Resume content', 'Cover letter content'),
(10, '2021-09-01', 2025, 3.88, 'Transcript content', 'Resume content', 'Cover letter content'),
(11, '2020-09-01', 2024, 3.90, 'Transcript content', 'Resume content', 'Cover letter content'),
(12, '2019-09-01', 2023, 3.80, 'Transcript content', 'Resume content', 'Cover letter content'),
(13, '2021-09-01', 2025, 3.85, 'Transcript content', 'Resume content', 'Cover letter content'),
(14, '2020-09-01', 2024, 3.92, 'Transcript content', 'Resume content', 'Cover letter content'),
(15, '2019-09-01', 2023, 3.78, 'Transcript content', 'Resume content', 'Cover letter content'),
(16, '2021-09-01', 2025, 3.75, 'Transcript content', 'Resume content', 'Cover letter content'),
(17, '2020-09-01', 2024, 3.95, 'Transcript content', 'Resume content', 'Cover letter content'),
(18, '2019-09-01', 2023, 3.60, 'Transcript content', 'Resume content', 'Cover letter content'),
(19, '2021-09-01', 2025, 3.90, 'Transcript content', 'Resume content', 'Cover letter content'),
(20, '2020-09-01', 2024, 3.85, 'Transcript content', 'Resume content', 'Cover letter content'),
(21, '2019-09-01', 2023, 3.68, 'Transcript content', 'Resume content', 'Cover letter content'),
(22, '2021-09-01', 2025, 3.50, 'Transcript content', 'Resume content', 'Cover letter content'),
(23, '2020-09-01', 2024, 3.78, 'Transcript content', 'Resume content', 'Cover letter content'),
(24, '2019-09-01', 2023, 3.82, 'Transcript content', 'Resume content', 'Cover letter content'),
(25, '2021-09-01', 2025, 3.65, 'Transcript content', 'Resume content', 'Cover letter content'),
(26, '2020-09-01', 2024, 3.77, 'Transcript content', 'Resume content', 'Cover letter content'),
(27, '2019-09-01', 2023, 3.92, 'Transcript content', 'Resume content', 'Cover letter content'),
(28, '2021-09-01', 2025, 3.80, 'Transcript content', 'Resume content', 'Cover letter content'),
(29, '2020-09-01', 2024, 3.85, 'Transcript content', 'Resume content', 'Cover letter content'),
(30, '2019-09-01', 2023, 3.76, 'Transcript content', 'Resume content', 'Cover letter content'),
(31, '2021-09-01', 2025, 3.70, 'Transcript content', 'Resume content', 'Cover letter content'),
(32, '2020-09-01', 2024, 3.88, 'Transcript content', 'Resume content', 'Cover letter content'),
(33, '2019-09-01', 2023, 3.83, 'Transcript content', 'Resume content', 'Cover letter content'),
(34, '2021-09-01', 2025, 3.72, 'Transcript content', 'Resume content', 'Cover letter content'),
(35, '2020-09-01', 2024, 3.91, 'Transcript content', 'Resume content', 'Cover letter content'),
(36, '2019-09-01', 2023, 3.85, 'Transcript content', 'Resume content', 'Cover letter content'),
(37, '2021-09-01', 2025, 3.95, 'Transcript content', 'Resume content', 'Cover letter content'),
(38, '2020-09-01', 2024, 3.65, 'Transcript content', 'Resume content', 'Cover letter content'),
(39, '2019-09-01', 2023, 3.70, 'Transcript content', 'Resume content', 'Cover letter content'),
(40, '2021-09-01', 2025, 3.80, 'Transcript content', 'Resume content', 'Cover letter content');

INSERT INTO departments (departmentName) VALUES ('College of Science');
INSERT INTO departments (departmentName) VALUES ('Business');
INSERT INTO departments (departmentName) VALUES ('College of Social Sciences');
INSERT INTO departments (departmentName) VALUES ('Engineering');
INSERT INTO departments (departmentName) VALUES ('Computer Science');
INSERT INTO departments (departmentName) VALUES ('Physics');
INSERT INTO departments (departmentName) VALUES ('Mathematics');
INSERT INTO departments (departmentName) VALUES ('Chemistry');
INSERT INTO departments (departmentName) VALUES ('Biology');
INSERT INTO departments (departmentName) VALUES ('English');
INSERT INTO departments (departmentName) VALUES ('History');
INSERT INTO departments (departmentName) VALUES ('Philosophy');
INSERT INTO departments (departmentName) VALUES ('Linguistics');
INSERT INTO departments (departmentName) VALUES ('Psychology');
INSERT INTO departments (departmentName) VALUES ('Political Science');
INSERT INTO departments (departmentName) VALUES ('Sociology');
INSERT INTO departments (departmentName) VALUES ('Economics');
INSERT INTO departments (departmentName) VALUES ('Education');
INSERT INTO departments (departmentName) VALUES ('Law');
INSERT INTO departments (departmentName) VALUES ('Public Health');
INSERT INTO departments (departmentName) VALUES ('Nursing');
INSERT INTO departments (departmentName) VALUES ('Environmental Science');
INSERT INTO departments (departmentName) VALUES ('Art History');
INSERT INTO departments (departmentName) VALUES ('Architecture');
INSERT INTO departments (departmentName) VALUES ('Music');
INSERT INTO departments (departmentName) VALUES ('Theatre');
INSERT INTO departments (departmentName) VALUES ('Dance');
INSERT INTO departments (departmentName) VALUES ('Anthropology');
INSERT INTO departments (departmentName) VALUES ('Geography');
INSERT INTO departments (departmentName) VALUES ('Civil Engineering');
INSERT INTO departments (departmentName) VALUES ('Mechanical Engineering');
INSERT INTO departments (departmentName) VALUES ('Electrical Engineering');
INSERT INTO departments (departmentName) VALUES ('Chemical Engineering');
INSERT INTO departments (departmentName) VALUES ('Aerospace Engineering');
INSERT INTO departments (departmentName) VALUES ('Computer Engineering');
INSERT INTO departments (departmentName) VALUES ('Biomedical Engineering');
INSERT INTO departments (departmentName) VALUES ('Industrial Engineering');
INSERT INTO departments (departmentName) VALUES ('Information Technology');
INSERT INTO departments (departmentName) VALUES ('Cognitive Science');
INSERT INTO departments (departmentName) VALUES ('Marketing');
INSERT INTO departments (departmentName) VALUES ('Finance');
INSERT INTO departments (departmentName) VALUES ('Management');
INSERT INTO departments (departmentName) VALUES ('Accounting');
INSERT INTO departments (departmentName) VALUES ('Entrepreneurship');


INSERT INTO majors (student_id, department_id, name) VALUES
(1, 5, 'Computer Science'),
(2, 2, 'Marketing'),
(3, 3, 'Data Science'),
(4, 4, 'Mechanical Engineering'),
(5, 3, 'Human Resources'),
(6, 1, 'Physics'),
(7, 5, 'Electrical Engineering'),
(8, 6, 'Philosophy'),
(9, 7, 'Sociology'),
(10, 8, 'Psychology'),
(11, 9, 'Political Science'),
(12, 10, 'History'),
(13, 11, 'Biology'),
(14, 12, 'Law'),
(15, 13, 'Nursing'),
(16, 14, 'Environmental Science'),
(17, 15, 'Art History'),
(18, 16, 'Architecture'),
(19, 17, 'Music'),
(1, 18, 'Dance'),
(2, 19, 'Economics'),
(3, 20, 'Geography'),
(4, 1, 'Mechanical Engineering'),
(5, 2, 'Civil Engineering'),
(6, 3, 'Aerospace Engineering');

INSERT INTO minors (student_id, department_id, name) VALUES
(1, 2, 'Business Administration'),
(2, 3, 'Psychology'),
(3, 1, 'Statistics'),
(4, 3, 'Law'),
(5, 2, 'Finance'),
(6, 4, 'Environmental Studies'),
(7, 5, 'Mechanical Engineering'),
(8, 6, 'Ethics'),
(9, 7, 'International Relations'),
(10, 8, 'Creative Writing'),
(11, 9, 'Marketing'),
(12, 10, 'Public Health'),
(13, 11, 'Chemistry'),
(14, 12, 'Theatre'),
(15, 13, 'Public Policy'),
(16, 14, 'Geographic Information Systems'),
(17, 15, 'Art History'),
(18, 16, 'Sociology'),
(19, 17, 'Music Theory'),
(1, 18, 'Psychology of Learning'),
(2, 19, 'Entrepreneurship'),
(3, 20, 'Humanities'),
(4, 1, 'Statistics'),
(6, 3, 'Economics');

INSERT INTO application_metrics (student_id, metricName, obtainedAt) VALUES
(1, 'GPA', '2024-01-01'),
(2, 'Resume Score', '2024-02-01'),
(3, 'Interview Performance', '2024-03-01'),
(4, 'GPA', '2024-04-01'),
(5, 'Resume Score', '2024-05-01'),
(6, 'GPA', '2024-06-01'),
(7, 'Resume Score', '2024-07-01'),
(8, 'Interview Performance', '2024-08-01'),
(9, 'GPA', '2024-09-01'),
(10, 'Resume Score', '2024-10-01'),
(11, 'Interview Performance', '2024-11-01'),
(12, 'GPA', '2024-12-01'),
(13, 'Resume Score', '2025-01-01'),
(14, 'Interview Performance', '2025-02-01'),
(15, 'GPA', '2025-03-01'),
(16, 'Resume Score', '2025-04-01'),
(17, 'Interview Performance', '2025-05-01'),
(18, 'GPA', '2025-06-01'),
(19, 'Resume Score', '2025-07-01'),
(20, 'Interview Performance', '2025-08-01'),
(21, 'GPA', '2025-09-01'),
(22, 'Resume Score', '2025-10-01'),
(23, 'Interview Performance', '2025-11-01'),
(24, 'GPA', '2025-12-01'),
(25, 'Resume Score', '2026-01-01'),
(26, 'Interview Performance', '2026-02-01'),
(27, 'GPA', '2026-03-01'),
(28, 'Resume Score', '2026-04-01'),
(29, 'Interview Performance', '2026-05-01'),
(6, 'GPA', '2026-06-01'),
(7, 'Resume Score', '2026-07-01'),
(8, 'Interview Performance', '2026-08-01'),
(9, 'GPA', '2026-09-01'),
(10, 'Resume Score', '2026-10-01');

INSERT INTO system_admin (systemAdmin_id, appMetrics_id, role, departmentBranch, permissionList) VALUES
(1, 1, 'Admin', 'Engineering', 'Read, Write, Execute'),
(2, 2, 'Admin', 'Marketing', 'Read, Write'),
(3, 3, 'Admin', 'Data Science', 'Read, Execute'),
(4, 4, 'Admin', 'Design', 'Write'),
(5, 5, 'Admin', 'HR', 'Read'),
(6, 12, 'Admin', 'Marketing', 'Write, Execute'),
(7, 13, 'Admin', 'Data Science', 'Read, Write'),
(8, 14, 'Admin', 'Design', 'Read, Execute'),
(9, 15, 'Admin', 'HR', 'Write'),
(10, 16, 'Admin', 'Engineering', 'Execute'),
(11, 17, 'Admin', 'Marketing', 'Read, Execute'),
(12, 18, 'Admin', 'Data Science', 'Write'),
(13, 19, 'Admin', 'Design', 'Read'),
(14, 20, 'Admin', 'HR', 'Execute'),
(15, 21, 'Admin', 'Engineering', 'Write'),
(16, 22, 'Admin', 'Marketing', 'Read, Write, Execute'),
(17, 23, 'Admin', 'Data Science', 'Execute'),
(18, 24, 'Admin', 'Design', 'Write, Execute'),
(19, 25, 'Admin', 'HR', 'Read, Write'),
(20, 26, 'Admin', 'Engineering', 'Read'),
(21, 27, 'Admin', 'Marketing', 'Write'),
(22, 28, 'Admin', 'Data Science', 'Read, Write, Execute'),
(23, 29, 'Admin', 'Design', 'Execute'),
(24, 29, 'Admin', 'HR', 'Write, Execute'),
(25, 27, 'Admin', 'Engineering', 'Write, Execute'),
(26, 12, 'Admin', 'Marketing', 'Read, Execute'),
(27, 3, 'Admin', 'Data Science', 'Write, Execute'),
(28, 4, 'Admin', 'Design', 'Read, Write'),
(29, 5, 'Admin', 'HR', 'Execute');

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
(2, 2, 1, '2024-11-12 11:30:00', '2024-12-05 14:00:00',
    'I had an amazing time working as a Software Development Intern. My tasks involved writing and debugging code, as well as assisting with feature implementation and testing. I had the opportunity to work with a talented team of developers who helped me improve my coding and problem-solving skills. I learned how to navigate version control systems like Git and got hands-on experience working with modern software development tools and practices. The work was challenging but fulfilling, and I felt that my contributions truly impacted the team’s progress.',
    'Java, Software Development, Git, Debugging, Problem-solving',
    'One of the challenges I faced was integrating new features into an existing codebase, especially when the code was complex and undocumented. There were times when it was difficult to identify the root cause of bugs, and working with legacy code required a bit more time than I expected. Additionally, working under tight deadlines and prioritizing tasks efficiently was an ongoing challenge.',
    'I would suggest providing more training on internal tools and frameworks that are used in development. A deeper understanding of the company’s coding standards and architecture early on would help new interns feel more prepared to contribute effectively from the beginning.',
    'Yes'
),
(3, 2, 2, '2024-11-12 09:30:00', '2024-12-04 15:30:00', 
    'This internship provided me with an incredible opportunity to learn about the fast-paced world of digital marketing. I had the chance to work on various campaigns, create content for social media, and assist with market research. I gained hands-on experience in content creation, audience targeting, and performance analysis. The best part was working closely with senior marketers, who provided valuable insights into strategic decision-making. I also had the opportunity to contribute to some high-visibility projects, which was a great learning experience.',
    'Content Creation, Social Media Strategy, Market Research, Google Analytics',
    'One of the biggest challenges was managing multiple projects with tight deadlines. Sometimes it felt like I had too many tasks to juggle at once, and it was difficult to prioritize effectively. Also, some campaigns had last-minute changes, which made it hard to keep everything on track. Despite this, I managed to adapt and learned how to work efficiently under pressure.',
    'I believe that having more structured timelines for each project would help interns manage expectations and workload more effectively. It would also be helpful to have a more clear onboarding process to get up to speed with the marketing tools and platforms the company uses.',
    'No'
),
(4, 3, 3, '2024-11-14 10:45:00', '2024-12-03 17:00:00',
    'My time as a Data Analyst Intern was a truly valuable experience. I worked on a variety of data-related tasks, including cleaning datasets, performing analysis using statistical software, and creating visualizations to present our findings. The team was extremely collaborative, and I had the opportunity to learn new techniques in data wrangling and visualization. I was also involved in interpreting data for client reports, which gave me a deeper understanding of how data analysis can influence business decisions.',
    'Excel, Data Visualization, Data Cleaning, SQL',
    'The most challenging aspect was dealing with extremely large datasets that sometimes contained inconsistencies or missing values. Cleaning and preparing the data for analysis was time-consuming, and it was difficult to ensure that the data was completely accurate. Additionally, while I had some experience with statistical software, the learning curve was steep, and I often had to spend extra time figuring out how to use advanced features.',
    'More hands-on training with statistical tools like R or Python would have been helpful, especially for interns who might not be familiar with these technologies. A clearer structure for data cleaning tasks and more guidance on data accuracy could also help to streamline the process.',
    'Yes'
),
(5, 4, 4, '2024-11-18 11:00:00', '2024-12-02 14:45:00',
    'As a Graphic Design Intern, I had the opportunity to work on a variety of creative projects, from designing social media graphics to creating print advertisements. The best part was working alongside a talented design team that provided constructive feedback and helped me improve my skills. I was also responsible for creating visual concepts for new campaigns, which required me to think creatively and develop ideas that aligned with the company’s branding strategy. Overall, it was an incredibly fulfilling experience, and I feel much more confident in my design abilities.',
    'Adobe Photoshop, Adobe Illustrator, Typography, Branding',
    'The biggest challenge I faced was trying to meet the expectations for design work while working under tight deadlines. At times, I struggled with balancing creativity and practicality, especially when there were last-minute changes to the project scope. Additionally, I found it difficult to manage my time between multiple ongoing design tasks, which sometimes caused stress and delays.',
    'I would recommend having a clearer timeline and more structured feedback sessions, so that designers can refine their concepts without feeling rushed. Additionally, it would be helpful to have more collaboration between the design team and other departments to ensure alignment on project objectives from the start.',
    'Yes'
),
(6, 5, 5, '2024-11-20 08:15:00', '2024-12-01 13:30:00',
    'Working in HR as an intern was an eye-opening experience. I had the chance to assist with a range of tasks, including recruitment, employee onboarding, and preparing training materials. I learned a great deal about the importance of maintaining employee relations and the intricacies of handling sensitive HR issues. The most valuable part of the experience was seeing how HR decisions directly impact employee satisfaction and retention. I also had the chance to sit in on meetings with senior HR leaders, which helped me gain a better understanding of strategic HR practices.',
    'Recruitment, Employee Onboarding, HRIS Systems, Conflict Resolution',
    'The most challenging aspect of this internship was managing multiple tasks that required a great deal of attention to detail. For example, during the recruitment process, it was essential to keep track of many applicants and ensure that all documentation was up to date. Additionally, I had to learn how to navigate the company’s HRIS system, which had a steep learning curve.',
    'It would be helpful to provide more training on the company’s HR systems early in the internship. Additionally, having more opportunities to shadow senior HR staff during interviews or meetings would have given me more insights into the strategic decision-making process.',
    'No'
);