# Random Video Clip Generator Cloud service 

Generate a list (text file) of your music videos (locally downloaded), upload it, and then download a playlist (xml) for VLC to play random clips locally! 


## FAQ 

Q: Where are the instructions to use this service? <br />
A: In the main page: www.randomvideoclipgenerator.com  

Q: Where is the code to fork the project? <br />
A: https://github.com/marq4/Random-Video-Clip-Generator 



## Terminology

* List: the text document that the user (DJ) generates locally by running any of the available scripts (like Windows PowerShell), and then uploads to the webpage. 
* Crate: a user (DJ) account will always have at least one crate. A new account will be created with an empty default crate. A crate holds a list of videos. 
* Playlist: the XSPF (XML) text file that contains the information for the random video clips. The user generates and downloads it by pressing a single button on the webpage. When the playlist is available locally the user can double-click it to display the video clips on VLC media player. 
* VLC: free open-source video player for any OS. 


## AWS Services
* S3: to host the downloadable scripts to generate the text list.
* VPC: custom VPC where the EC2 instances will live. SG allows SSH, HTTP from everywhere for now. Route Table with default route to the IGW.
* Subnet: 2 public for the ASG for resilience against AZ failure. 
* IAM: Role to allow Apache/Python to talk to AWS. 
* EC2:
   1. Execute the computation of the random clip generation (Python).
   2. Serve the Web content (PHP).
   3. Communicate with DynamoDB (boto3). 
* ASG: to scale out up to a second instance "if needed". 
* ELB: ALB for the ASG.
* SNS: sends me emails when ASG scales in/out. 
* Route53: what is the price for a domain? Domain to purchase: www.randomvideoclipgenerator.com. 
* CloudWatch: to monitor the resources. 
* CloudTrail: to see the API calls: when ASG spins 2nd instance up, when boto3 commits changes to DynamoDB. 
* DynamoDB: Table: Crates. Schema: Key: {Owner, CrateID}, CrateName, VideoList: {Path, Duration}. 
* Cognito: username & password functionality. 
* Inspector: run A security benchmark agains EC2 ONCE. 
* Shield: to protect from DDoS. 
* WAF: protect the webpage from OWASP top 10 exploits. Cost??
* Health Dashboard: see general status of my services.
* Cost Explorer & Budgets. 

## Use cases 
* The user (DJ) creates an account by specifying a username and password.
* The user (DJ) updates their username.
* The user (DJ) updated their password.
* The user (DJ) locally generates the video list after reviewing the instructions using Bash or PowerShell.
* The user (DJ) creates a new (empty) crate.
* The user (DJ) renames any crate.
* The user (DJ) uploads a video list to an empty crate to populate it.
* The user (DJ) uploads a video list to a non-empty crate and selects replace or merge option.
* The user (DJ) empties a crate.
* The user (DJ) manually removes a video from any crate.
* The user (DJ) generates and downloads an xml playlist from any crate.
* The user (DJ) sets the desired number of clips for any crate.
* The user (DJ) sets min and max duration of the clips for any crate.
* The user (DJ) shares this service on their social media.
* The user (DJ) signs out.
* The user (DJ) deletes their account.
* The user (DJ) reviews instructions, downloads PowerShell or Bash script, clicks link to Suggested Music Videos list. 
