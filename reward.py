def reward_function(params):
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']

    # Calculate 3 markers that are at varying distance away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to the center line and vice versa
    if distance_from_center <= marker_1:
        reward =1.0
    elif distance_from_center <=marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else: 
        reward = 1e-3 #likely crashed/close to off track
    
    return float(reward)



def reward_function(params):
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    progress = params['progress']

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to the center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # Likely crashed/close to off track

    # Add a reward based on progress (percentage of track completed)
    progress_reward = progress * 100.0  # Convert progress to a reward in the range of 0-100
    reward += progress_reward

    return float(reward)


def reward_function(params):
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    progress = params['progress']
    speed = params['speed']
    waypoints = params['waypoints']

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to the center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # Likely crashed/close to off track

    # Add a reward based on progress (percentage of track completed)
    progress_reward = progress * 100.0  # Convert progress to a reward in the range of 0-100
    reward += progress_reward

    # Add a reward based on speed
    speed_reward = speed * 2.0  # Scaling speed to a reward in the range of 0-10
    reward += speed_reward

    # Calculate the distance to the next waypoint
    next_waypoint = waypoints[min(params['closest_waypoints'])]
    distance_to_next_waypoint = abs(params['x'] - next_waypoint[0]) + abs(params['y'] - next_waypoint[1])

    # Add a reward based on reaching the next waypoint
    waypoint_reward = 1.0 / (1.0 + distance_to_next_waypoint)  # Inverse of the distance for reward
    reward += waypoint_reward

    return float(reward)






def reward_function(params):
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    progress = params['progress']
    speed = params['speed']
    waypoints = params['waypoints']
    steering_angle = abs(params['steering_angle'])  # Using absolute value for penalization

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Penalize large steering angles for smoother turns
    steering_reward = 1.0 - (steering_angle / 30.0)  # Scale the reward inversely with steering angle
    reward = steering_reward

    # Give higher reward if the car is closer to the center line and vice versa
    if distance_from_center <= marker_1:
        reward += 1.0
    elif distance_from_center <= marker_2:
        reward += 0.5
    elif distance_from_center <= marker_3:
        reward += 0.1
    else:
        reward += 1e-3  # Likely crashed/close to off track

    # Add a reward based on progress (percentage of track completed)
    progress_reward = progress * 100.0  # Convert progress to a reward in the range of 0-100
    reward += progress_reward

    # Add a reward based on speed
    speed_reward = speed * 2.0  # Scaling speed to a reward in the range of 0-10
    reward += speed_reward

    # Calculate the distance to the next waypoint
    next_waypoint = waypoints[min(params['closest_waypoints'])]
    distance_to_next_waypoint = abs(params['x'] - next_waypoint[0]) + abs(params['y'] - next_waypoint[1])

    # Add a reward based on reaching the next waypoint
    waypoint_reward = 1.0 / (1.0 + distance_to_next_waypoint)  # Inverse of the distance for reward
    reward += waypoint_reward

    # Penalize off-track and crashes
    if params['is_offtrack']:
        reward -= 1.0

    if params['is_crashed']:
        reward -= 1.0

    # Penalize reverse driving
    if params['is_reversed']:
        reward -= 1.0

    return float(reward)






def reward_function(params):
    # Extract parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    progress = params['progress']
    speed = params['speed']
    waypoints = params['waypoints']
    steering_angle = abs(params['steering_angle'])  # Using absolute value for penalization
    is_on_track = params['all_wheels_on_track']  # Added parameter for all wheels being on track

    # Calculate markers for distance from center
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Penalize large steering angles for smoother turns
    steering_reward = 1.0 - (steering_angle / 30.0)  # Scale the reward inversely with steering angle

    # Reward for being on track
    on_track_reward = 1.0 if is_on_track else -1.0  # Reward if on track, penalize if off track

    # Calculate rewards based on distance from center
    if distance_from_center <= marker_1:
        center_reward = 1.0
    elif distance_from_center <= marker_2:
        center_reward = 0.5
    elif distance_from_center <= marker_3:
        center_reward = 0.1
    else:
        center_reward = 1e-3  # Likely crashed/close to off track

    # Calculate reward based on progress
    progress_reward = progress * 100.0

    # Calculate reward based on speed
    speed_reward = speed * 2.5

    # Calculate distance to next waypoint and reward
    next_waypoint = waypoints[min(params['closest_waypoints'])]
    distance_to_next_waypoint = abs(params['x'] - next_waypoint[0]) + abs(params['y'] - next_waypoint[1])
    waypoint_reward = 1.0 / (1.0 + distance_to_next_waypoint)

    # Calculate final reward with appropriate scaling
    reward = (
        steering_reward +
        on_track_reward +
        center_reward +
        progress_reward +
        speed_reward +
        waypoint_reward
    )

    return float(reward)




def reward_function(params):
    # Extract parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    progress = params['progress']
    speed = params['speed']
    waypoints = params['waypoints']
    steering_angle = abs(params['steering_angle'])  # Using absolute value for penalization
    is_on_track = params['all_wheels_on_track']  # Added parameter for all wheels being on track

    # Calculate markers for distance from center
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Penalize large steering angles for smoother turns
    steering_reward = 1.0 - (steering_angle / 30.0)  # Scale the reward inversely with steering angle

    # Reward for being on track
    on_track_reward = 1.0 if is_on_track else -1.8  # Reward if on track, penalize if off track

    # Calculate rewards based on distance from center
    if distance_from_center <= marker_1:
        center_reward = 1.5
    elif distance_from_center <= marker_2:
        center_reward = 1.0
    elif distance_from_center <= marker_3:
        center_reward = 0.5
    else:
        center_reward = 1e-5  # Likely crashed/close to off track

    # Calculate reward based on progress
    progress_reward = progress * 100.0

    # Adjusted speed reward with penalty for going too slow
    SPEED_THRESHOLD = 2.5  # Set the speed threshold based on your action space
    if speed < SPEED_THRESHOLD:
        speed_penalty = -1.5  # Penalty for going too slow
    else:
        speed_penalty = 0.0
    speed_reward = speed * 4.5 + speed_penalty  # Incorporate speed penalty

    # Calculate distance to next waypoint and reward
    next_waypoint = waypoints[min(params['closest_waypoints'])]
    distance_to_next_waypoint = abs(params['x'] - next_waypoint[0]) + abs(params['y'] - next_waypoint[1])
    waypoint_reward = 2.0 / (1.0 + distance_to_next_waypoint)

    # Calculate final reward with appropriate scaling
    reward = (
        steering_reward +
        on_track_reward +
        center_reward +
        progress_reward +
        speed_reward +
        waypoint_reward
    )

    return float(reward)







def reward_function(params):
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    progress = params['progress']
    speed = params['speed']
    waypoints = params['waypoints']
    steering_angle = abs(params['steering_angle'])  # Using absolute value for penalization
    is_on_track = params['all_wheels_on_track']  # Added parameter for all wheels being on track

    # Calculate markers for distance from center
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Penalize large steering angles for smoother turns
    steering_reward = 1.0 - (steering_angle / 30.0)  # Scale the reward inversely with steering angle

    # Reward for being on track
    on_track_reward = 1.0 if is_on_track else -0.5  # Reward if on track, penalize if off track

    # Calculate rewards based on distance from center
    if distance_from_center <= marker_1:
        center_reward = 1.5
    elif distance_from_center <= marker_2:
        center_reward = 1.0
    elif distance_from_center <= marker_3:
        center_reward = 0.5
    else:
        center_reward = 1e-5  # Likely crashed/close to off track

    # Calculate reward based on progress
    progress_reward = progress * 100.0
    SPEED_THRESHOLD = 2.5
    if speed < SPEED_THRESHOLD:
        speed_penalty = -1.5
    else:
        speed_penalty = 0.0

    # Adjusted speed reward with a higher scaling factor
    speed_reward = speed * 4.0  # Scaling speed to a reward in the range of 0-20

    # Calculate distance to next waypoint and reward
    next_waypoint = waypoints[min(params['closest_waypoints'])]
    distance_to_next_waypoint = abs(params['x'] - next_waypoint[0]) + abs(params['y'] - next_waypoint[1])
    
    # Higher waypoint reward for accurate waypoint following
    waypoint_reward = 3.0 / (1.0 + distance_to_next_waypoint)

    # Calculate final reward with appropriate scaling
    reward = (
        steering_reward +
        on_track_reward +
        center_reward +
        progress_reward +
        speed_reward +
        waypoint_reward
    )

    return float(reward)



