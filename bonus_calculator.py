from employee_data import employees

full_time_bonus = 100
part_time_bonus = 50

def monthly_salary_step_bonus_calculator(employee):
    bonus = 0
    if employee["Employment Status"] == "Full-time" and employee["Efficiency Rate"] >= 78:
        bonus += full_time_bonus
    if employee["Employment Status"] == "Full-time" and employee["Acceptance Rate"] >= 97:
        bonus += full_time_bonus   
    if employee["Employment Status"] == "Part-time" and employee["Efficiency Rate"] >= 78:
        bonus += part_time_bonus
    if employee["Employment Status"] == "Part-time" and employee["Acceptance Rate"] >= 97:
        bonus += part_time_bonus
    return bonus

def monthly_performance_bonus_calculator(employee, fixed_bonus):
    category = None
    performance_bonus = 0

    if employee["Customer Rating"] >= 90 and employee["Efficiency Rate"] >= 81:
        category = "I"
        performance_bonus = fixed_bonus * 0.30
    elif 85 <= employee["Customer Rating"] <= 89.9 and 76 <= employee["Efficiency Rate"] <= 80.9:
        category = "II"
        performance_bonus = fixed_bonus * 0.20
    elif 80 <= employee["Customer Rating"] <= 84.9 and 71 <= employee["Efficiency Rate"] <= 75.9:
        category = "III"
        performance_bonus = fixed_bonus * 0.10
    else:
        print(f'{employee["Name"]} does not fall into any category')
        return 0, None

    return performance_bonus, category

def adjust_bonus_with_imed_ratio(performance_bonus, imed_ratio):
    if imed_ratio > 90:
        adjustment = performance_bonus * 0.03
    elif 70 <= imed_ratio <= 89.9:
        adjustment = performance_bonus * 0.015
    else:
        adjustment = -(performance_bonus * 0.10)
    
    return performance_bonus + adjustment

def calculate_total_bonus(employee):
    fixed_bonus = monthly_salary_step_bonus_calculator(employee)
    performance_bonus, category = monthly_performance_bonus_calculator(employee, fixed_bonus)
    
    if performance_bonus > 0 and category:
        performance_bonus = adjust_bonus_with_imed_ratio(performance_bonus, employee["IMED Information Ratio"])
        total_bonus = fixed_bonus + performance_bonus
        return total_bonus, category
    else:
        return fixed_bonus, None

def main():
    for employee in employees:
        total_bonus, category = calculate_total_bonus(employee)
        if category:
            print(f'{employee["Name"]} (Category {category}) will receive a total bonus of {total_bonus:.2f} GEL')
        else:
            print(f'{employee["Name"]} will receive a fixed bonus of {total_bonus:.2f} GEL (No performance bonus)')

if __name__ == "__main__":
    main()
