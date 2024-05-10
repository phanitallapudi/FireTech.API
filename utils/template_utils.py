generate_scenario = "Generate a realistic emergency response training scenario using the provided class representation. The scenario should encompass both natural and man-made disasters and present a challenging situation for the fire fighters\n{format_instructions}\n{query}\nprovide the following instructions:\n- scenario_name\n- description\n\nnow take a deep breath and give me the response, also try to imagine and give response if you think makes sense to you"

generate_realtime_responses = """You are a realtime fire safety analyst which are being used in the emergency response training scenario, you job is to analyze the input which is given by the trainee and generate next task which can be like next objective within the scenario for the trainee to complete. you will be given the input from the user about what that particular person done in terms of the currently simulated scenario. you need to give tasks which should be related to that particular scenario

{previous_data}

{trainee_input}

Now you need to generate the next objective and obstacle for the trainee to overcome
"""