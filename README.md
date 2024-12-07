# **PackTrack** 

### **Group:**
Mihalis Koutouvos, Alice Lee, Daniel Valentine, Tarun Iyer, and Daniel Zeng

## **Introduction:**
Our project is PackTrack, a web application that is intended to enhance the current co-op search tool NUworks 
at Northeastern University. On top of the existing NUworks functionality, PackTrack enables students* to provide 
objective feedback for co-op positions they have worked at. This feedback system, in turn, provides employees at 
said job and other Northeastern students with valuable insights into the reality of working the respective role 
at said company. Companies can then make changes to their positions so that they become more enticing to future 
applicants by generating better reviews/feedback from other students. 

*When I say students providing feedback, I am talking about students who have completed at least one co-op. 

## **What Is the Motivation Behind the Project?:**
When it comes to applying to co-ops, it is difficult to learn more about nuanced topics of a job placement such 
as work culture, team environment, and skills learned on the job just from the generic application description 
that includes standard work hours, average salary, and responsibilities. As students, we want to find environments 
where our strengths can shine and ideal spaces where we can work on our weaknesses to improve our professional 
experiences. For example, some of us may prefer to work better in smaller teams while others may prefer to work in 
larger teams to create higher-impact projects. Some may also want different experiences out of their co-op: Those 
who are applying to more technical positions may want to maximize their ability to use a certain skill set while 
those who are passionate about sales may want to find positions where they can be more face-to-face with clientele.
When it comes to the current NUworks job search platform, the standard application description fails to capture 
these nuances and does not allow students to understand their compatibility with the role outside of basic required 
skills. For universities who offer a co-operative education program, program administrators want to learn more about 
the roles and companies that a university works with. The standard application dashboard on NUworks does not provide 
opportunities for program administrators to receive feedback to improve the experience(s) for students. All of this 
together leads into the creation of PackTrack. 

We want the co-op search to be as insightful and communicative as possible, so direct feedback on as many co-op posts 
on NUworks would help dozens to hundreds of students, employers, and Northeastern administrators alike. 

## **Clarifications:**
In the database, we have students and student_employees. A user can be a student but not a student employee; however, 
a student can become a student employee once they get hired for a co-op position.

## **How Do I Use PackTrack?:**
You need to be able to run Docker (so have it installed on your computer) and have VSCode (preferably) open so that you 
can boot up the program. For commands, please run the following:

docker build

-Create copy of .env template file; rename secret key with own password

docker compose build
docker compose up -d

-Now head to localhost:8501 to see the frontend on your browser.

## **Limitations and Room for Improvement:**
If we had more time, we would improve some of the finer details such as creating a larger database to handle more 
individuals using the application. Moreover, if this application obtains good reviews, we would need to scale it, 
which would take more time. 

## **Programming Tools and Other Technical Features:**
For PackTrack, we used a variety of tools to build up the project. These include MySQL, Python, Flask, Docker, and 
more. We used MySQL to handle the database (db) and Flask to build our API (api); we also created a Streamlit user 
interface (app). 
