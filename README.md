# SanCap Cleaning Calculator

A Python-based console application designed to estimate house cleaning costs based on property size, cleaning type, and optional add-on services.  
Originally created to support a small cleaning business, this tool demonstrates practical application of programming logic, data structures, and user interaction for business automation.

## Features

- Calculates estimates for four property sizes: **Small**, **Medium**, **Large**, and **Estate**  
- Supports multiple cleaning types, including:
  - First Time Clean
  - Deep Clean
  - Move In/Out
  - Maintenance
- Allows users to select optional add-ons such as:
  - Inside Fridge
  - Inside Oven
  - Windows (Interior)
  - Blinds Dusting
- Displays a **low-to-high price range** based on base rates and uplift percentages
- Performs input validation and error handling for a smooth user experience
- Runs continuously until the user chooses to exit

## How It Works

1. User enters the **square footage** of the property.  
2. Selects a **cleaning type** from the provided list.  
3. Optionally adds **extra services** from a menu of add-ons.  
4. The calculator computes a **price range** using base rates and percentage uplifts.  
5. The user can view the breakdown and choose to **start over or exit**.
