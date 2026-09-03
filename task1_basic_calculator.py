"""
Task 1 - Basic Stress and Strain Calculator
Member 1
"""

applied_force_newtons = float(input("Enter the applied force (N): "))
cross_sectional_area_m2 = float(input("Enter the cross-sectional area (m^2): "))
original_length_m = float(input("Enter the original length (m): "))
change_in_length_m = float(input("Enter the change in length (m): "))

stress_pascals = applied_force_newtons / cross_sectional_area_m2
strain = change_in_length_m / original_length_m

print('we did it')