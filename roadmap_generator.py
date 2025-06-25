import json

def load_templates(path="templates.json"):
    with open(path, "r") as f:
        return json.load(f)

def generate_timeline(goal, interests, current_skills, templates):
    goal_template = templates.get(goal)
    if not goal_template:
        return ["❌ Sorry, no roadmap available for this goal."]

    timeline = []
    step = 1
    learned_skills = [skill.strip().lower() for skill in current_skills.split(",")]

    for stage in goal_template["timeline"]:
        skill = stage["skill"]
        if skill.lower() in learned_skills:
            continue
        if stage.get("area") and stage["area"] not in interests:
            continue

        entry = f"🪜 Step {step}:\n🔹 Learn: {skill}"
        if stage.get("project"):
            entry += f"\n📌 Project: {stage['project']}"
        if stage.get("course"):
            entry += f"\n🎓 Course: {stage['course']}"
        timeline.append(entry)
        step += 1

    return timeline if timeline else ["🎉 You’ve already covered all the basics! Time to level up!"]
