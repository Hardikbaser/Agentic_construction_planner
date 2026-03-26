def check_resources(task):
    mock_resources = {
        "labor": True,
        "materials": True,
        "permits": False
    }

    if "permit" in task.lower():
        return "⚠️ Permit not approved yet"
    
    return "✅ Resources available"