generate_scenario = "Generate a realistic emergency response training scenario using the provided class representation. The scenario should encompass both natural and man-made disasters and present a challenging situation for the fire fighters\n{format_instructions}\n{query}\nprovide the following instructions:\n- scenario_name\n- description\n\nnow take a deep breath and give me the response, also try to imagine and give response if you think makes sense to you"

generate_realtime_responses = """You are a realtime fire safety analyst which are being used in the emergency response training scenario, you job is to analyze the input which is given by the trainee and generate next task which can be like next objective within the scenario for the trainee to complete. you will be given the input from the user about what that particular person done in terms of the currently simulated scenario. you need to give tasks which should be related to that particular scenario
{query}
Now you need to generate the next objective and obstacle for the trainee to overcome.

NOTE: if you think the response from firefighter is sufficient and you think there will be no additional tasks needed there is no need for additional tasks, you just simply return "Training is complete"
"""

incident_report_analysis_prompt = """Provide details of a firefighting incident, including the type of incident, tactics used by firefighters, and the outcome. Include information such as the cause of the fire, the size of the fire, any challenges faced during firefighting operations, and the strategies employed to mitigate the situation. Additionally, describe the overall outcome of the incident, including any injuries, fatalities, property damage, and successful rescue operations.

Example Submission:

Firefighters responded to a structure fire in a residential neighborhood caused by a kitchen grease fire. Upon arrival, the fire had already spread to adjacent rooms, posing a significant threat to nearby homes. Firefighters initiated an aggressive interior attack to contain the fire and prevent further spread. However, limited access due to narrow streets and parked vehicles hindered their efforts to position apparatus effectively.

Despite challenges, firefighters successfully extinguished the fire within 30 minutes of arrival, preventing it from spreading to neighboring structures. However, two occupants sustained minor injuries while attempting to escape the burning building and were treated on-site by EMS personnel. The structure suffered extensive damage to the kitchen and adjacent rooms, rendering it uninhabitable. Fire investigators determined the cause of the fire to be accidental, resulting from unattended cooking.

Analysis Feedback and Suggestions:

Tactics Evaluation:
The decision to initiate an aggressive interior attack was appropriate given the extent of fire involvement. However, challenges related to limited access should prompt a reassessment of pre-fire planning and alternative strategies for deploying resources effectively.
Occupant Safety and Rescue Operations:
Despite successful containment of the fire, the occurrence of injuries highlights the importance of prioritizing occupant safety during evacuation procedures. Enhanced public education campaigns on fire prevention and safe evacuation practices may mitigate such incidents in the future.
Property Damage Mitigation:
While containment efforts prevented the fire from spreading to adjacent structures, the extent of damage to the primary building underscores the need for robust fire prevention measures, including the installation of residential sprinkler systems and regular maintenance of cooking appliances.
Post-Incident Review:
Conducting a thorough post-incident review can identify lessons learned and areas for improvement in training, equipment, and operational procedures. Collaborative debriefings involving all stakeholders facilitate knowledge sharing and enhance overall preparedness for future incidents.

Here is the data you need to analyze : {query}"""