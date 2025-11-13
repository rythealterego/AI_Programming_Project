def generate_student_summary(students):
    """Return a clean summary of the students."""
    if not students:
        return "No students recorded."

    summary = ""
    for s in students:
        summary += (
            f"Name: {s['name']}\n"
            f"Student ID: {s['student_id']}\n"
            f"Favorite AI Tool: {s['favorite_ai_tool']}\n"
            "-------------------------------\n"
        )
    return summary
