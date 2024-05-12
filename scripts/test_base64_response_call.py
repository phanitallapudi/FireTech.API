import json
import base64
import requests

def save_html_from_base64(json_data):
    for index, entry in enumerate(json_data):
        for key, value in entry.items():
            if isinstance(value, str):
                try:
                    decoded_data = base64.b64decode(value)
                    # You can change the file name or path as per your requirement
                    with open(f'output_{index}_{key}.html', 'wb') as html_file:
                        html_file.write(decoded_data)
                    print(f"HTML file for '{key}' in entry {index} saved successfully.")
                except Exception as e:
                    print(f"Error decoding base64 data for '{key}' in entry {index}: {e}")

def fetch_json_data_from_endpoint(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching JSON data from endpoint: {e}")
        return None

# Replace the URL with the actual endpoint URL
data = """
Natural Disaster Incident Report:

Type of Incident: Hurricane
Date: September 15, 2024
Location: Gulf Coast, Anytown, USA

Incident Overview:
On September 15, 2024, a Category 4 hurricane made landfall along the Gulf Coast, impacting the coastal communities of Anytown and surrounding areas. The hurricane, named Hurricane Delta, brought destructive winds exceeding 130 mph and torrential rainfall, resulting in widespread flooding, power outages, and structural damage.

As the storm approached, local authorities issued mandatory evacuation orders for low-lying coastal regions and implemented emergency preparedness measures to safeguard residents and mitigate potential casualties. Despite these efforts, the intensity of Hurricane Delta posed significant challenges to emergency response operations.

        no_injuries="1000",
        minor_injuries="10",
        moderate_injuries="3",
        major_injuries="0",
        injured_civilians="13",
        injured_firefighters="1"

Tactics Used:

Pre-Evacuation Preparations: Emergency management agencies coordinated evacuation efforts by providing transportation assistance and establishing designated evacuation shelters equipped with essential supplies and medical facilities.
Search and Rescue Operations: First responders conducted search and rescue missions in flooded neighborhoods and stranded vehicles, utilizing boats and high-water vehicles to evacuate residents trapped by rising floodwaters.
Infrastructure Protection: Utility crews worked tirelessly to restore power and communication services disrupted by downed power lines and fallen trees. Additionally, structural engineers assessed the integrity of bridges, roads, and public buildings to ensure safety and expedite recovery efforts.
Outcome:

Hurricane Delta inflicted extensive damage to residential and commercial properties, with thousands of homes inundated by floodwaters and roofs torn off by powerful winds.
Despite the severity of the storm, swift evacuation measures and proactive emergency response efforts minimized casualties, with no reported fatalities and only a few minor injuries.
The widespread destruction prompted the activation of federal disaster assistance programs to provide financial aid and resources for debris removal, infrastructure repairs, and temporary housing for displaced residents.
Analysis Feedback and Suggestions:

Evacuation Preparedness: Enhancing public awareness and outreach initiatives regarding evacuation procedures and storm preparedness can improve community resilience and ensure timely evacuation compliance during future hurricane threats.
Critical Infrastructure Resilience: Investing in resilient infrastructure designs, such as storm-resistant buildings and flood mitigation measures, can minimize damage and disruption to essential services during severe weather events.
Interagency Coordination: Strengthening collaboration between local, state, and federal agencies, as well as non-governmental organizations and volunteer groups, enhances resource allocation and response coordination, fostering a more effective and cohesive disaster response framework. Additionally, conducting post-incident debriefings and after-action reviews enables stakeholders to identify areas for improvement and implement lessons learned to enhance future emergency response capabilities.
"""
endpoint_url = f'http://127.0.0.1:8000/generate_charts?data={data}'
# Fetch JSON data from the endpoint
json_data = fetch_json_data_from_endpoint(endpoint_url)

# Proceed if JSON data is successfully fetched
if json_data:
    save_html_from_base64(json_data)
