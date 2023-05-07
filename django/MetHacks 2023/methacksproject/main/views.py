from django.shortcuts import render
from django.http import HttpResponse
from .models import PatientData
from .forms import PatientForm
from django.contrib import messages
from django.db.models import Q
from methacksproject.globals import GLOBAL_FNAME, GLOBAL_LNAME
import cohere
from cohere.responses.classify import Example


#Where ALL the python functions are written

def home(request):
    return render(request, 'index.html', {})


def form(request):
    if request.method == "POST":
        submission = PatientForm(request.POST or None)
        if submission.is_valid():
            submission.save()
            patientfName = request.POST['fname']
            patientlName = request.POST['lname']
            date = request.POST['date']
            global GLOBAL_FNAME
            global GLOBAL_LNAME
            if GLOBAL_FNAME == None and GLOBAL_LNAME == None:
                GLOBAL_FNAME = patientfName
                GLOBAL_LNAME = patientlName
            return analyzeEntry(request, patientfName, patientlName, date)
        else:
            return render(request, 'form.html', {})
    else:
        return render(request, 'form.html', {})
    

def analyzeEntry(request, fname, lname, date):
    all_entries = PatientData.objects.filter(Q(fname__icontains = fname) | Q(lname__icontains = lname) | Q(date__icontains = date))
    #COHERE CODE, OR LINK FUNCTION THAT CLASSIFIES IT
    dayEntry = ""
    for index, entry in enumerate(all_entries):
        dayEntry += str(entry)
        if len(all_entries) > 1 and index != len(all_entries)-1:
            dayEntry += ". "
    cohereClassification = responseEval(dayEntry)
    return render(request, "postForm.html", {'entries': all_entries, 'cohere': cohereClassification})
    #return all_entries
        

def postForm(request, originalEntries, analyzedEntries):
    return render(request, "postForm.html", {'entries': originalEntries, 'analyzed': analyzedEntries})


#Function for all entries from login page
def summary(request):
    patientfName = request.POST['fname']
    patientlName = request.POST['lname']
    global GLOBAL_FNAME
    GLOBAL_FNAME = patientfName
    global GLOBAL_LNAME
    GLOBAL_LNAME = patientlName

    #PUT COHERE'ED RETURNS
    all_entries = PatientData.objects.filter(Q(fname__icontains = GLOBAL_FNAME) | Q(lname__icontains = GLOBAL_LNAME))
    return render(request, 'summary.html', {'entries': all_entries, 'first': GLOBAL_FNAME, 'last': GLOBAL_LNAME})


def viewEntries(request):
    if GLOBAL_LNAME == None and GLOBAL_FNAME == None:
        return HttpResponse("No Entries")
    else:
        all_entries = PatientData.objects.filter(Q(fname__icontains = GLOBAL_FNAME) | Q(lname__icontains = GLOBAL_LNAME))
        #PUT COHERE'ED RETURNS
        return render(request, 'summary.html', {'entries': all_entries, 'first': GLOBAL_FNAME, 'last': GLOBAL_LNAME})


#classification 
co = cohere.Client('yhlIG1WYyeUVrAJ2NzhQwYKnghq6sbs8DfWCPulm') # This is your trial API key
def responseEval(msg):
  response = co.classify(
  model='large',
  inputs=[msg],
  examples=[Example("Today, I woke up feeling empty and hopeless. I don\'t know what\'s wrong with me, but I can\'t shake this feeling of sadness. I tried to distract myself by doing things I enjoy, but nothing seems to help.", "Melancholy"), 
            Example("I got some bad news today, and I\'m devastated. It feels like everything is falling apart around me. I don\'t know how to process this information, and I don\'t know who to turn to for support. I just want to curl up in a ball and cry.", "Melancholy"), 
            Example("I\'m so tired of feeling this way. It\'s like a dark cloud has been following me around for weeks, and I can\'t seem to shake it. I don\'t know how to lift myself out of this funk, and I\'m afraid I\'ll be stuck here forever.", "Melancholy"), 
            Example("I had a panic attack today, and it was terrifying. I felt like I was going to die, and I couldn\'t catch my breath. Even after it was over, I couldn\'t calm down. I\'m afraid it will happen again, and I don\'t know how to prevent it.", "Anxiety"), 
            Example("Today, my anxiety was at an all-time high. I woke up with a knot in my stomach, and I couldn\'t shake the feeling of impending doom. Every little thing felt like a threat, and I couldn\'t stop worrying about everything.", "Anxiety"), 
            Example("I\'m so anxious about the future. I keep thinking about all the things that could go wrong, and I can\'t seem to stop. It\'s like my mind is stuck in a loop, and I can\'t break free.", "Anxiety"), 
            Example("I\'m so angry right now, I could scream. I feel like everything is going wrong, and there\'s nothing I can do to fix it. I\'m tired of feeling helpless and frustrated all the time.", "Anger"), 
            Example("I\'m angry at myself for letting things get this bad. I should have known better, but I ignored all the warning signs. Now I\'m paying the price, and it feels like there\'s no way out.", "Anger"), 
            Example("The world feels so unfair right now, and it\'s making me angry. There are so many injustices happening every day, and it feels like no one is doing anything about it. I don\'t know how to channel this anger into something productive.", "Anger"), 
            Example("I\'m so confused about what I want to do with my life. I thought I had everything figured out, but now I\'m not so sure. I don\'t know if I should keep pursuing my current path or if I should try something new.", "Confusion"), 
            Example("I\'m confused about my relationships. I don\'t know if the people in my life are good for me or if I should distance myself. I\'m afraid of hurting them, but I\'m also afraid of staying in toxic situations.", "Confusion"), 
            Example("Today, I\'m grateful for my health. I woke up feeling energized and ready to take on the day, and I know that\'s not something everyone gets to experience.", "Gratitude"), 
            Example("I\'m thankful for my supportive friends and family. They have been there for me through thick and thin, and I know I wouldn\'t be where I am today without them.", "Gratitude"), 
            Example("I\'m grateful for my job. It\'s not always easy, but it provides me with stability and the opportunity to grow and learn new things.", "Gratitude"), 
            Example("Today was an amazing day! I woke up feeling refreshed and energized, ready to tackle the challenges of the day. I had a productive morning and was able to complete all of the tasks on my to-do list. What made the day even better was that I received an email from my dream job saying that they were interested in interviewing me. I feel hopeful and excited about what the future holds!", "Hopefulness"), 
            Example("Today, I went for a walk in the park and it was such a beautiful day. The sun was shining and the flowers were in full bloom. I felt a sense of peace and calm that I haven\'t felt in a long time. As I walked, I thought about all of the possibilities that the future holds and felt hopeful that everything will work out in the end. I am grateful for moments like this that remind me to appreciate the present and look forward to the future.", "Hopefulness"), 
            Example("Today was a day of new beginnings. I started a new job that I am really excited about and feel hopeful about the opportunities it will bring. I met some great people and feel like I am already starting to fit in. After work, I went for a run and felt a sense of accomplishment and pride. I am starting to see the results of all the hard work I have been putting in and it feels great. Today was a reminder that with hard work and dedication, anything is possible.", "Hopefulness"), 
            Example("I ran into an old friend today and found out that they had just bought a new house. As they showed me pictures of the beautiful home with a huge backyard and spacious rooms, I couldn\'t help but feel a tinge of envy. I\'ve been struggling to make ends meet and the thought of owning a home seems like an impossible dream. Seeing someone else achieve what I\'ve been striving for only made me feel worse.", "Envy"), 
            Example("Today, I saw a coworker get promoted to a position that I\'ve been working hard for. While I am happy for them and know that they deserve the promotion, I couldn\'t help but feel a sense of envy. I\'ve been working just as hard and feel like I\'ve been overlooked. I know I shouldn\'t compare myself to others, but it\'s hard not to feel envious when someone else gets something you want.", "Envy"), 
            Example(" I saw pictures on social media of an old classmate who is now traveling the world, visiting exotic places and experiencing new cultures. As I scrolled through the pictures, I felt envious of their freedom and adventure. I\'ve been stuck in the same routine and feel like I\'m missing out on all the excitement. Seeing someone else living the life I want only made me feel more envious and resentful.", "Envy"), 
            Example("Today was a simple, yet wonderful day. I spent the morning reading a good book and drinking a cup of coffee. In the afternoon, I went for a walk in the park and enjoyed the fresh air and sunshine. As I reflect on the day, I feel content and grateful for the little things in life that bring me joy. It\'s moments like these that make me appreciate the present and feel content with where I am in life.", "Content"), 
            Example("Today, I spent the day with my family, just enjoying each other\'s company. We had a barbecue, played games, and talked about our lives. As I watched my kids running around and laughing, I felt a deep sense of contentment. It\'s times like these that I realize how lucky I am to have a loving family and how much they mean to me.", "Content"), 
            Example("Today, I accomplished a goal that I\'ve been working towards for a long time. I finally finished writing a book that I\'ve been working on for years. As I hit the \"send\" button to submit the manuscript, I felt a sense of contentment and pride. It\'s a great feeling to achieve something that I\'ve worked so hard for and to see the fruits of my labor.", "Content"), 
            Example("Today was one of those days where everything seemed to go wrong. I woke up late, spilled coffee on my shirt, and missed an important meeting at work. The rest of the day was spent playing catch-up and trying to fix my mistakes. As I sit here, exhausted and stressed, I can\'t help but feel like everything is falling apart.", "Stressed"), 
            Example("Today, I received some unexpected bills in the mail that I wasn\'t prepared for. I\'ve been struggling financially and the added stress of these bills is overwhelming. I feel like I\'m drowning in debt and can\'t seem to catch a break. The weight of these financial burdens is taking a toll on my mental and physical health, and I\'m not sure how to cope.", "Stressed"), 
            Example("The holidays are supposed to be a time of joy and celebration, but for me, it\'s just another source of stress. I have a long list of gifts to buy, parties to attend, and family obligations to fulfill. The thought of all of these commitments is overwhelming and I feel like I can\'t keep up. Instead of feeling excited for the holidays, I\'m filled with stress and anxiety.", "Stressed")])
  return response.classifications[0].prediction

#generate
co = cohere.Client('ry6dvHIzlf5GYi40NXpn5lvZAlmeIEhijbUjpasT') # This is your trial API key
def generateFeedback(msg):
    response = co.generate(
    model='command-xlarge-nightly',
    prompt=msg,
    max_tokens=300,
    temperature=0.9,
    k=0,
    stop_sequences=[],
    return_likelihoods='NONE')
    print('Prediction: {}'.format(response.generations[0].text))
    return response.generations[0].text
#EXTRAS
#TODO: Personalizable journal entries page? (this would be cool but IDK how to do this at all)
#TODO: Google map API to gather location information for healthcare research purposes
#TODO: voice entry for children (attached to the form, not sure how to do this though)
#TODO: 'Make an Account' page, where the patient makes their account, or we can just do, when a new name is submitted in the form, a new 'Patient' is entered

