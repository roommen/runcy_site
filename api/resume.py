def resume():
            return {"Name": "Runcy Oommen", "URL": "https://runcy.me", 
                    "Email": "runcy.oommen@gmail.com", "Location": "Bangalore, India",
                    "Summary": "An accomplished software engineer with strong SDLC experience \
                    and a string of projects primarily in the security domain.",
                    "Description": "Runcy strives constantly to build better software with \
                    extra focus on data security kept throughout life-cycle and not just \
                    an after-thought. Considers himself to be a perfectionist yet remains \
                    practical, knowing where to draw the line and stop. Runcy advocates strong \
                    data privacy and possessing a natural penchant for security, he began working \
                    full time on CloudBrew to minimize data breaches in this mass surveillance world, \
                    which continues now as an open source project.",
                    "Social": []
                    }

def lambda_handler(event, context):
    return resume()
