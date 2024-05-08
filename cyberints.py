cyberints.com
cyberints.com
cyberints.com
cyberints.com


import requests
import argparse

def fuzz():
    
        print("----------------------Dir fuzzing tool created by own -------------------------")
        # Create an ArgumentParser object
        parser = argparse.ArgumentParser(description="URL and Word Argument Parser")

            # Add the URL argument
        parser.add_argument("-url", "--url", required=True, help="The URL to fetch")

            # Add the word argument
        parser.add_argument("-w", "--word", required=True, help="The word to search for")


        args = parser.parse_args()

        url = args.url
        word = args.word
        
        with open(word,"r") as file:
            for line in file:
                    directory = line.strip()
                    url1 =f"{url}/{directory}"
                    
                                
                
                    response = requests.get(url1)

                    # Check the response status code
                    if response.status_code == 200:
                            print(f"Directory found: {url1}")
                    elif response.status_code == 404:
                            print(f"Not Found: {url1}")
                        
                            
             
    
        
if __name__ == "__main__":
    fuzz()
test_lOzu4xm6GkrnWNkBB3iNAhk6Zj4omggan97jrTTp
Sparkpost API Key = beecdc85799231338314bd20292f71fc8cd687e8
AWS API Secret = 426ecdac8e19cdb18f18b3ec05ba393d4c414eea

Sparkpost API Key = 426ecdac8e19cdb18f18b3ec05ba393d4c414eea

Alibaba API = ksWSBrFtl5SIRVpZlwN3NNPQjehA2E

Artifactory API Key = duORpUiYrEpzKIop6iNbjnwKLAKnJ47csTyRACyEmWj0QdUrm5aqNJGHSSEQSUAvNW0ojX0dO

Auth0 OAuth Client Secret = eH7cdAFlNXeVJqWIQ7gW9tY1GJIpUtFb6CmjVyq2VM3u71bOyR8CRihcCgMUYoDNyLXao3

Okta API Token = 00TpugqhmYtVmMO6518mCuRMoOYFldEBl0g187ufoz

Sparkpost API Key = ZEWEcW4SfFNTr4uMNZma0ey4f5lgLrkB0aX0QMow
