# MoodAF
Statistics show that 1 in 4 people feel they have no one to confide in, and even after sharing their feelings, 70% of them have held back how they truly felt when opening up. To address this issue, our team has risen to this challenge by developing a webapp that identifies emotions from a user’s journal entries and lists mediations.

MoodAF is an innovative solution that uses Cohere Classify and Generate API to create a safe space for individuals to share their experiences and emotions through journaling, with the goal of reducing stigma, improving understanding, and providing accessibility for medical professionals to understand their patients. 

# Table of Contents  
[Inspiration](#Inspiration)  
[Interface](#Interface)  
[Levels](#Levels)  
[Challenges Encoutered](#Challenges-We-Encountered)  
[Accomplishments](#accomplishments)
[What We Learned](#What-we-learned)
[What's Next?](#What's-Next-for-MoodAF)   
 

## Inspiration

The inspiration for creating MoodAF (Mood, Analytics, and Feedback) that raises awareness about mental health through journaling stems from the recognition that mental health issues are a widespread and significant problem that affect millions of people. This project aims to provide a platform for individuals to share their experiences and emotions through journaling, with the goal of reducing stigma and promoting empathy and understanding. Overall, this project seeks to promote mental health awareness, reduce stigma, and provide individuals with the tools they need to manage their emotions and achieve a better quality of life through daily journaling activities.

## Interface
At the home page, users can click new entry to navigate to the journal entry page. Returning users can also login to view old entries.
![image](https://user-images.githubusercontent.com/43208342/236710437-ff8ade43-4abb-4c0e-a864-82a07ee9f989.png)

Users can enter their jounral entries while listening to some relaxing music. After submitting, the user input is put through the Cohere Classify API to determine what emotion the user is experiencing.
![image](https://user-images.githubusercontent.com/43208342/236710598-2878fd82-e889-41ec-8f89-95ad4da02ef8.png)

With the context of the journal entry and the mood it is written in, this information is then put through the Cohere Generate API to produce a list of ways to mediate these emotions, such as through mindfulness exercises or connecting with support groups. By making this information easily accessible, the project aims to empower individuals to take control of their mental health and seek out effective coping strategies. Users can also cosent to sharing their entry and entry recommendations with a Profession if they wish.
![image](https://user-images.githubusercontent.com/43208342/236710683-fb1f8414-6650-4339-a4c8-f5c7a1d0b821.png)

After submitting multiple entries, users can review their mood trends overtime in the personalized summarization page. They can view their old entries (in black) and MoodAF's suggestion (in blue).
![image](https://user-images.githubusercontent.com/43208342/236710492-2d221887-6058-4051-b525-f792e83a8bd0.png)

Everyday, the community page is refreshed for users to see how everyone else on MoodAF is feeling, assuring them that they are not alone. Using the journal entries of all the users, a Mental Health Tip of the Day is generated with the Cohere Generate API.
![image](https://user-images.githubusercontent.com/43208342/236710715-eaae6c2d-f0a0-46f6-96f8-fb0e10178227.png)


## Challenges We Encountered

It was difficult working with Django's built-in database system, django.db, for the first time, as we were unfamiliar with the framework. Some of the challenges we faced included learning the new syntax for querying the database, configuring the database settings, and understanding how the database schema is created and managed.

## Accomplishments

As a team, we are extremely proud of successfully implementing two powerful APIs, Cohere Classify and Cohere Generate, into our project. These APIs have allowed us to leverage the latest advances in Natural Language Processing (NLP) to provide advanced functionality and insights to our users.

## What We learned

As a team comprised of individuals from different universities, we were faced with the challenge of collaborating and working together effectively. However, we are proud to say that we successfully learned how to collaborate as a team and work towards a common goal. We quickly identified the strengths and weaknesses of each team member, and delegated tasks accordingly, ensuring that everyone was able to contribute their skills and knowledge. We are proud of what we have accomplished as a team, and we look forward to continuing to work together in the future.

## What's Next for MoodAF

As we look to the future of MoodAF, one of our key priorities is to implement a voice-to-text aspect of the project. This will allow users to speak their journal entries rather than typing them out, which can be especially useful for individuals who may have difficulty with typing or prefer to speak their thoughts out loud.
