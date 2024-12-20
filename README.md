# Random Video Clip Generator Cloud Service 

Generate a list of your videos (text file), upload it, and then generate a playlist for VLC to play random clips. 

* To fork the project: https://github.com/marq4/Random-Video-Clip-Generator
* The recommended way to display random video clips: https://github.com/marq4/Random-Video-Clip-Generator-Docker 

## FAQ 

Q: What is the advantage of using this Cloud service over the Python or Docker version? <br />
A: None. This project’s main goal is for me to practice Cloud. 


## Terminology

* List: the text document that the user (DJ) generates locally by running any of the available scripts passing the folder that contains the video.mp4 files as a parameter, and then uploads to the webpage.
* Crate: a user (DJ) account will always have at least one crate. A new account will be created with an empty default crate. Crates can be renamed by the user. A crate holds a list of “video title”:duration pairs.
* Playlist: the xspf (xml) file that contains the information for the random video clips. The user generates and downloads it by pressing a single button on the webpage. When the playlist is available locally the user can double-click it to display the video clips on VLC.
* VLC: free open-source video player for any OS. 


## AWS Services
For now I’ll just list all services that I MAY use for this project.
* S3: to host the downloadable scripts to generate the text list.
* VPC: default VPC where the EC2 instance(s) will live. SG? NACLs? Route Table? IGW? EIP? NATGW? Route53 Resolver DNS FW?
* IAM?
* EC2: one of the options to execute the computation of the random clip generation (xml playlist), the other being Lambda?
* ASG: to scale out up to a second instance? (just for practice)
* ELB: ALB? to randomly choose between the EC2 instance and Lambda compute options (just for practice).
* Route53: what is the price for a domain? Is this domain available: www.randomvideoclipgenerator.com?
* CloudWatch: to monitor the resources.
* Lambda: will sit behind an ALB that will choose between this and the EC2 ASG? to compute the random clips.
* CloudTrail: to see the API calls between my services.
* API GW: will sit between the frontend and the backend. Will load & save user create content (lists of video titles: duration) from/to the DB.
* DocumentDB VS DynamoDB: I need to decide which one to store the user crates as JSON documents.
* ECR: to host the Docker image that users with Docker can pull to generate the list (txt).
* ECS: it is also possible to have a third option for compute: containers. I need to check the price.
* Cognito: this will handle the username/password. DB needed?
* Detective: to see if the system got compromised. What’s the cost?
* Inspector: run security benchmarks agains EC2 instance(s). Cost??
* Macie: should tell me if there are secrets leaked to S3. Cost??
* Shield: to protect from DDoS.
* WAF: protect the webpage from OWASP top 10 exploits.
* Health Dashboard: see general status of my services. 

## Use cases 
* The user (DJ) creates an account by specifying a username and password.
* The user (DJ) updates their username.
* The user (DJ) updated their password.
* The user (DJ) locally generates the video list after reviewing the instructions using Docker, Bash, Python, or PowerShell.
* The user (DJ) creates an additional (empty) crate.
* The user (DJ) renames any crate.
* The user (DJ) uploads a video list to an empty crate to populate it.
* The user (DJ) uploads a video list to a non-empty crate and selects replace or merge option.
* The user (DJ) empties a crate.
* The user (DJ) manually adds a video to any crate.
* The user (DJ) manually removes a video from any crate.
* The user (DJ) generates and downloads an xml playlist from any crate.
* The user (DJ) sets the desired number of clips for any crate.
* The user (DJ) sets min and max duration of the clips for any crate.
* The user (DJ) sets the local path of the folder associated with any crate.
* The user (DJ) shares this service on their social media.
* The user (DJ) signs out.
* The user (DJ) deletes their account.

