class HealthScore:
    def calculate_score(self, bp_systolic, bp_diastolic, heart_rate, weight, age):
        score = 100
        
        # Blood pressure scoring
        if bp_systolic > 140 or bp_diastolic > 90:
            score -= 20
        elif bp_systolic > 130 or bp_diastolic > 85:
            score -= 10
        
        # Heart rate scoring
        if heart_rate < 60 or heart_rate > 100:
            score -= 15
        elif heart_rate < 70 or heart_rate > 90:
            score -= 5
        
        # Age adjustment
        if age > 70:
            score -= 5
        elif age > 80:
            score -= 10
        
        return max(0, min(100, score))
    
    def get_rating(self, score):
        if score >= 90:
            return "Excellent", "✅"
        elif score >= 75:
            return "Good", "👍"
        elif score >= 60:
            return "Fair", "⚠️"
        else:
            return "Needs Attention", "🔴"
    
    def get_recommendations(self, score, metrics):
        recommendations = []
        
        if metrics.get('bp_systolic', 0) > 130:
            recommendations.append("Monitor blood pressure regularly")
        
        if metrics.get('heart_rate', 0) > 90:
            recommendations.append("Practice relaxation techniques")
        
        if score < 70:
            recommendations.append("Schedule a doctor's appointment")
        
        return recommendations

health_score = HealthScore()
