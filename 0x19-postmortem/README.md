Postmortem: July 18, 2024, 07:15 Eastern Time to 09:15
Incident Overview:

In the early hours of July 18th, while most of us were still enjoying our morning coffee, Microsoft Windows users were hit by a security update so effective, it secured them out of their own systems! Error messages abounded, and users were suddenly reminded of the good old days when "Have you tried turning it off and on again?" was the solution to all tech woes.

Impact:

Among the unfortunate victims were airlines, hospitals, healthcare providers, 911 call centers, banks, and more. Essentially, anyone with something important to do that day was caught in the digital crossfire. The system was down for everyone—no exceptions. If you weren't impacted, you probably weren't logged in.

Detection:

The chaos was detected at 07:15 Eastern Time, and a team member named Redmond (no relation to Microsoft, we think) quickly flagged that something was amiss with US cloud services. It was initially suspected to be a Microsoft issue—because, well, who wouldn’t blame Microsoft first? But it turned out that a faulty channel file in CrowdStrike's Falcon sensor product was the real culprit.

Response:

CrowdStrike, with the efficiency of a seasoned firefighter, rolled back the update within just over an hour. The error was traced back to a template containing some "problematic" data—think of it as the digital equivalent of forgetting to add sugar to your cake batter, only this time it crashed systems worldwide.

Collaborative Effort:

Microsoft, not one to let a good crisis go to waste, deployed hundreds of engineers to assist in the recovery effort. They teamed up with CrowdStrike, Google Cloud, AWS, and probably a few tech-savvy baristas, to bring systems back online. By the end of July, 97% of the affected Falcon sensors were recovered, though some may have needed a bit of coaxing.


Preventive Measures:

To prevent a repeat performance, CrowdStrike promised more rigorous testing—think developer, update, rollback, stability, and stress testing (and perhaps a mandatory session of "tech crisis yoga" to keep everyone calm). They also introduced staggered updates with canary deployments, ensuring that any future hiccups only affect a few users at a time—because misery loves company, but not too much of it.

Security Warnings:

In the aftermath, CrowdStrike and national cyber security agencies warned of phishing and social engineering attacks, urging everyone to only trust official channels. So, if you get an email promising to fix everything with one click, just remember: if it sounds too good to be true, it’s probably phishing.

Ongoing Investigation:

CrowdStrike is continuing its investigation into the incident and promises to keep everyone in the loop. They’re committed to full transparency and have assured us that they’ll be taking steps to prevent this from happening again—because once is enough, right?

