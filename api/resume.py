def resume():
            return {"Name": "Runcy Oommen", "URL": "https://runcy.me", 
                    "Email": "runcy.oommen@gmail.com", "Location": "Bangalore, India"}

def lambda_handler(event, context):
    return resume()
