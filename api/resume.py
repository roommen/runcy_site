def resume():
            return {"name": "Runcy Oommen", "website": "https://runcy.me", 
                    "email": "runcy.oommen@gmail.com", "location": "Bangalore, India"}

def lambda_handler(event, context):
    return resume()
