def calculate_sip_future_value(yearly_investments, annual_interest_rate, years):
    future_value = 0
    total_months = years * 12
    
    for year in range(1, years + 1):
        # SIP amount for this year
        current_monthly_investment = yearly_investments[year - 1]
        num_months = min(12, total_months)  # Number of months to account for in this year
        total_months -= num_months
        
        # Future value of monthly contributions made during this year
        for month in range(num_months):
            future_value += current_monthly_investment * (1 + annual_interest_rate / 12) ** (total_months + num_months - month)
    
    return future_value

def format_number(number):
    number_str = str(number)
    # Split the number into two parts: the last three digits and the rest
    last_three = number_str[-3:]
    rest = number_str[:-3]
    
    # Reverse the rest to insert commas easily
    rest_reversed = rest[::-1]
    
    # Insert commas every two digits in the reversed string
    chunks = [rest_reversed[i:i+2] for i in range(0, len(rest_reversed), 2)]
    rest_with_commas = ','.join(chunks)[::-1]
    
    # Combine the formatted rest and the last three digits
    formatted_number = f'{rest_with_commas},{last_three}'
    return formatted_number

def generate_yearly_investments(initial_amount, annual_increment, years, max_increment_year):
    investments = []
    current_amount = initial_amount
    
    for year in range(1, years + 1):
        investments.append(current_amount)
        
        if year < max_increment_year:
            current_amount += annual_increment
    
    return investments

# Parameters
initial_amount = 40000        # Initial SIP amount for the first year
annual_increment = 10000      # Amount by which the SIP increases each year
years = 38                  # Total number of years
max_increment_year = 11      # Year after which the SIP amount will not increase
annual_interest_rate = 0.09  # Annual interest rate (12% annual interest rate)

yearly_investments = generate_yearly_investments(initial_amount, annual_increment, years, max_increment_year)
years = len(yearly_investments)  # Total number of years

# Calculate future value

print(yearly_investments)
print(f"Total Investment { format_number(sum(yearly_investments) * 12)}")
future_value = calculate_sip_future_value(yearly_investments, annual_interest_rate, years)
# Format and print the result
formatted_number = format_number(int(future_value))
print(f"Returns {format_number(int(future_value-(sum(yearly_investments) * 12)))}")
print(f"Future Value of SIP: {formatted_number}")
