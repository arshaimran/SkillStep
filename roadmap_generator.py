import json

def load_templates(path="templates.json"):
    with open(path, "r") as f:
        return json.load(f)

def generate_timeline(goal, interests, current_skills, templates):
    goal_template = templates.get(goal)
    if not goal_template:
        return ["❌ Sorry, no roadmap available for this goal."]

    learned_skills = [skill.strip().lower() for skill in current_skills.split(",")]
    timeline = []
    step = 1

    # Group stages by level
    levels = ["Beginner", "Intermediate", "Advanced"]
    level_stages = {level: [] for level in levels}

    for stage in goal_template["timeline"]:
        level = stage.get("level", "Beginner")
        if stage["skill"].lower() not in learned_skills and (not stage.get("area") or stage["area"] in interests):
            level_stages[level].append(stage)

    for level in levels:
        for stage in level_stages[level]:
            entry = f"🪜 Step {step}:\n🔹 Learn: {stage['skill']}"
            if stage.get("level"):
                entry += f"\n🎯 Level: {stage['level']}"
            if stage.get("project"):
                entry += f"\n📌 Project: {stage['project']}"
            if stage.get("course"):
                entry += f"\n🎓 Course: {stage['course']}"
            timeline.append(entry)
            step += 1

        if not level_stages[level]:  # If no stages at this level, skip to next
            continue

        # Stop suggesting higher levels if current level not yet cleared
        if level_stages[level]:
            break

    if not timeline:
        return ["🎉 You’ve already covered all the basics! Time to level up!"]
    return timeline
