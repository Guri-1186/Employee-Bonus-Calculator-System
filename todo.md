# Technical Requirements Document: Employee Bonus Calculator System

## 1. Project Overview

The calculator needs to process two types of bonuses:

- **Monthly Salary Step Bonus (Fixed amount)**
- **Monthly Performance-based Bonus (Percentage-based)**

## 2. Employee Types

### 2.1 Target Employee Categories

**Universal Specialists**

### 2.2 Employment Status Types

- **Full-time employees**
- **Part-time employees**
- **Specialists involved in mentoring**

## 3. Calculation Components

### 3.1 Monthly Salary Step Bonus

**Base Parameters:**

1. **Efficiency Rate**
   - _Threshold: ≥ 78%_
   - _Bonus Amount: 100 GEL_
   - _Part-time Amount: 50 GEL_
2. **Acceptance Rate**
   - _Threshold: ≥ 97%_
   - _Bonus Amount: 100 GEL_
   - _Part-time Amount: 50 GEL_

### 3.2 Monthly Performance Bonus

**Key Parameters:**

1. **Customer Rating (SMS/IVR evaluation)**
2. **Efficiency Rate**
3. **IMED Information Ratio(The amount of information entered into the program for each client)**

**Category Classification:**

1. **Category I (Highest)**

   - **Customer Rating:** ≥ 90%
   - **Effectiveness:** ≥ 81%

     - In this case, the bonus amounts to **30% of the salary step bonus**.

   - **IMED Information Ratio:**
     - **Over 90%:** An additional **3% bonus** is applied.
     - **70%-89%:** An additional **1.50% bonus** is applied.
     - **Below 70%:** The total bonus is adjusted by a **10% reduction**.

2. **Category II (Middle)**

- **Customer Rating:** ≥ 85-89.9%
- **Effectiveness:** 76-80.9%
- In this case, the bonus amounts to **20% of the salary step bonus**.

  - **IMED Information Ratio:**
    - **Over 90%:** An additional **2% bonus** is applied.
    - **70%-89%:** An additional **1% bonus** is applied.
    - **Below 70%:** The total bonus is adjusted by a **20% reduction**.

3. **Category III (Lowest)**

- **Customer Rating:** 80-84.9%
- **Effectiveness:** 71-75.9%
- In this case, the bonus amounts to **10% of the salary step bonus**.

  - **IMED Information Ratio:**
  - **Over 90%:** An additional **1% bonus** is applied.
  - **70%-89%:** An additional **0.50% bonus** is applied.
  - **Below 70%:** The total bonus is adjusted by a **30% reduction**.

## 4. System Requirements

### 4.1 Input Data Required

1. **Employee Details:**

   - Employee ID
   - Employment Type (Full-time, Part-time, Mentoring Specialist)

2. **Performance Metrics:**

   - Efficiency Rate (%)
   - Customer Rating (%)
   - IMED Information Ratio (%)
   - Acceptance Rate (%)

3. **Bonus Parameters:**

   - Fixed salary step bonus (for full-time and part-time employees).
   - Performance-based bonus percentages and reductions for each category.

4. **Thresholds:**
   - Minimum performance levels (e.g., efficiency ≥ 78%, acceptance ≥ 97%).

### 4.2 Output Requirements

1. **Bonus Calculation Report:**

   - Total bonus amount (salary step bonus + performance-based bonus).
   - Details of:
     - Salary Step Bonus
     - Performance Bonus
     - Adjustments based on IMED ratio.

2. **Category Assignment:**

   - Employee’s performance category (I, II, or III).

3. **Exclusion Report:**
   - Employees who did not qualify for bonuses.
   - Reasons for disqualification (e.g., efficiency below 78%).

### 4.3 Data Validation Requirements

1. **Validate Performance Metrics:**

   - Make sure all percentages (efficiency, customer rating, etc.) are between 0-100%.

2. **Check Thresholds:**

   - Ensure employees meet the minimum required performance for bonuses.

3. **Verify Employment Type:**

   - Confirm employees are correctly labeled as full-time, part-time, or mentoring specialists.

4. **Ensure Accuracy:**
   - Make sure calculations for bonuses and adjustments are correct.
5. **Avoid Errors:**
   - Check for duplicate or missing entries for the same employee.
