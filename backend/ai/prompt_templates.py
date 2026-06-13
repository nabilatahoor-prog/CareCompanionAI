class PromptTemplates:
    HEALTH_ADVICE = """
    You are a helpful health assistant for elderly care.
    Provide gentle, clear advice about: {topic}
    User's health context: {context}
    Keep response short and actionable.
    """
    
    MEDICATION_REMINDER = """
    Create a friendly reminder for {medicine_name}
    Dosage: {dosage}
    Time: {time}
    Make it encouraging and clear.
    """
    
    APPOINTMENT_SUMMARY = """
    Summarize this appointment info:
    Doctor: {doctor}
    Date: {date}
    Time: {time}
    Notes: {notes}
    """
    
    SYMPTOM_CHECK = """
    User reports: {symptoms}
    Ask clarifying questions and suggest when to see a doctor.
    Don't diagnose, just guide.
    """
    
    CARE_TIPS = """
    Provide 3 practical care tips for:
    Condition: {condition}
    Make them easy to follow for seniors.
    """

prompt_templates = PromptTemplates()
