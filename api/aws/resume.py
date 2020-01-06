def resume():
            return {
                "Name": "Runcy Oommen", "URL": "https://runcy.me", 
                "Email": "runcy.oommen@gmail.com", "Location": "Bangalore, India",
                "Summary": "An accomplished software engineer with strong SDLC experience and a string of projects primarily in the security domain.",
                "Description": "Runcy strives constantly to build better software with extra focus on data security kept throughout life-cycle and not just an after-thought. Considers himself to be a perfectionist yet remains practical, knowing where to draw the line and stop. Runcy advocates strong data privacy and possessing a natural penchant for security, he began working full time on CloudBrew to minimize data breaches in this mass surveillance world, which continues now as an open source project.",
                "Social": {
                        "LinkedIn": "https://www.linkedin.com/in/runcyoommen",
                        "GitHub": "https://github.com/roommen",
                        "Twitter": "https://twitter.com/runcyoommen",
                        "Meetup": "https://www.meetup.com/members/227859610",
                        "Slideshare": "https://www.slideshare.net/RuncyOommen/presentations"
                        },
                "Experience": [{
                        "Company": "SonicWALL",
                        "Title": "Principal Software Engineer",
                        "Duration": "Dec '19 - Present | Dec '07 - May '16",
                        "Roles & Responsibilities": {
                                "1": "Over the course of my tenure, Runcy was part of the Email Security, SSL-VPN and UTM (Firewall) teams with focus on network and application security.",
                                "2": "Currently working on a cloud native and AWS based solution for GMS."
                                }
                        },{
                        "Company": "Bridgei2i",
                        "Title": "Cloud Architect",
                        "Duration": "Jun '17 - Present",
                        "Roles & Responsibilities": {
                                "1": "Leading the team for creating a cloud first and AI enabled sales assistant that deliver deal level recommendations",
                                "2": "Primarily responsible for designing the architecture from grounds up with emphasis on secure development.",
                                "3": "Responsibilities involve development of the components either in a containerized or serverless manner for effective scaling.",
                                "4": "Design and development of the licensing and subscription services from scratch."
                                }
                        },{
                        "Company": "CloudBrew",
                        "Title": "Founder",
                        "Duration": "Nov '15 - May '17",
                        "Roles & Responsibilities": {
                                "1": "Building the core library that does the encryption, split, decryption and merge of files, identifying the algorithm and optimization for production readiness.",
                                "2": "Implemented the final packaging mechanism that combined the web, GUI and library components, deployment and easy environment replication.",
                                "3": "Help arrive at the grand vision with an eye on the finer details by elevating the user experience and identifying the gaps.",
                                "4": "Conducted design reviews, integration of the GUI and core library components, end-user testing, performance and security enhancements."
                                }
                        },{
                        "Company": "McAfee",
                        "Title": "Software QA Engineer",
                        "Duration": "May '05 - Dec '07"
                        },{
                        "Company": "Infosys",
                        "Title": "Associate Software Engineer",
                        "Duration": "Jul '03 - Apr '05"
                        }],
                "Education": [{
                        "Institute": "XLRI",
                        "Course": "Post Graduate Certificate in Business Management",
                        "Year": "2006 - 2008",
                        "Details": "CGPA 8.0 - Specialized in Business Management, Finance, Software Project Management, Costing and Marketing."
                        },{
                        "Institute": "Bharathiar University",
                        "Course": "Bachelor Degree in Software Systems",
                        "Year": "2000 - 2003",
                        "Details": "Distinction - Specialized in Programming, Computer Science, Databases, Software Life-cycle, Architecture, Design and Implementation."
                        }],
                "Certifications": [{
                        "Name": "Certified Software Quality Analyst (CSQA)",
                        "Year": "2005"
                        },{
                        "Name": "Graduate from National Institute of Information Technology (GNIIT)",
                        "Year": "2000 - 2003"
                        }],
                "Hackathons": {
                        "1": "Top 6 team finish from 6500+ participants at Rajasthan IT Day 4.0 (Mar ’18)",
                        "2": "3rd Prize at UNiSYS 20/20 (Dec ’17)",
                        "3": "2nd Prize at Unilever MUSE (Oct ’17)",
                        "4": "Special Jury Award at Accenture HackForward (Jul ’17)"
                },
                "Community": {
                        "1": "Co-organizer of Google Cloud Developer Community, Bangalore",
                        "2": "Co-organizer of AWS User Group, Bangalore",
                        "3": "Co-organizer of Container Devs and Serverless Architects, Bangalore"
                },
                "Awards": {
                        "1": "Presented with the Brand Ambassador Award by Bridgei2i for being a community influencer and increasing the brand equity of the company. Apr ’18",
                        "2": "Received the Gold Award by Dell for contribution done towards Mobile Connect and in improving the stability of the SSL-VPN firmware. Aug ’15",
                        "3": "Given the Star Award thrice from SonicWall as recognition and success towards the engineering team and company. Nov ’11, May ’10 & Feb ’09",
                        "4": "Awarded Catch of the Month by McAfee for discovering business critical defects in the product with an impact on revenue. Apr ’07"
                },
                "Recognition": {
                        "1": "CloudBrew selected as the top 13 start-up from over 5000 in UberPITCH, India finals. Dec ’16",
                        "2": "CloudBrew granted $20,000 in credits by Google as part of their GCP Sparks package. Jul ’16"
                },
                "Skills": {
                        "Programming": "C, C++, Python, Shell Script, HTML, Javascript",
                        "Technical Specialities": "Knowledge of SDLC around Software Dev, QA and Automation. Linux, Virtualization, Cloud (AWS, GCP), Docker, TCP/IP Networking, Software Security, Perforce, Git, Apache, Bugzilla and MySQL.",
                        "Natural Languages": "English (full professional proficiency), Malayalam (mother tongue), Hindi (working proficiency) and French(beginner)."
                }
                }

def lambda_handler(event, context):
    return resume()
