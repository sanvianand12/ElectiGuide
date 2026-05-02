

# Create your views here.
from django.shortcuts import render

def home(request):
    polling_stations = {
        "560001": ["City Central Library", "St. Joseph's School", "BBMP Ward Office"],
        "560037": ["HAL Public School", "Marathahalli Community Hall", "Government Primary School"],
        "110001": ["National Museum Gate 2", "Town Hall Plaza", "Central Secretariat Hub"],
        "560076": ["St.Joseph Government School","Hulimavu Area","Near Meenakshi Temple"],
    }

    pincode = request.GET.get('pincode')
    results = polling_stations.get(pincode, [])
    
    # New logic: If pincode exists, we want Step 4 to be open
    open_step = 4 if pincode else None 

    roadmap = [
        {"id": 1, "task": "Eligibility Check", "status": "Requirement"},
        {"id": 2, "task": "Registration Process", "status": "Action Required"},
        {"id": 3, "task": "Research Candidates", "status": "Knowledge"},
        {"id": 4, "task": "Find Polling Place", "status": "Final Step"},
    ]

    return render(request, 'assistant/index.html', {
        'roadmap': roadmap,
        'results': results,
        'searched_pincode': pincode,
        'open_step': open_step # Send this to the HTML
    })
def get_candidates(request):
    topic = request.GET.get('topic')
    # Filter candidates by the topic selected
    candidates = Candidate.objects.filter(focus_area=topic)
    # Return this data to your template...