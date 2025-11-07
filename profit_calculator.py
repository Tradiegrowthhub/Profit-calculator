
import streamlit as st

# Display logo (replace with actual logo URL if available)
st.image("https://tradiegrowthhub.com.au/logo.png", width=150)

# Welcome message
st.title("Profit Acceleration Calculator")
st.markdown("### G'day! I'm here to help you discover how small tweaks to your business can massively boost your profit. Ready to see what's possible?")

# Step 1: Annual Revenue
revenue = st.number_input("Annual Revenue ($)", value=750000, format="%d")
st.info("💡 This is your total income before any costs - basically all the money coming into your business each year")

# Step 2: Gross Profit Margin
gross_margin = st.number_input("Gross Profit Margin (%)", value=50)
st.info("💡 Gross profit is what's left after you pay for materials and direct job costs (like subbies). If you charge $1000 for a job and materials cost $450, your gross profit is $550, or 55%. Most tradies run between 40-60%")

# Step 3: Net Profit Margin
net_margin = st.number_input("Net Profit Margin (%)", value=15)
st.info("💡 Net profit is what you actually have left after ALL expenses - wages, vehicle costs, insurances, tools, rent, everything. If you're making 10-20% you're doing very well. Many tradies are below 10%. If you are not sure just use your best guess.")

# Step 4: Improvement Areas
st.markdown("### Now the fun part! Let's look at 5 key areas where small improvements create BIG results.")
st.info("💡 I recommend starting conservative - just 3-5% improvements in each area. You can always go back and change the numbers later to see what else might be possible.")

cost_decrease = st.number_input("Cost Decrease (%)", value=3)
pricing_increase = st.number_input("Quote Accuracy & Pricing Increase (%)", value=3)
additional_products = st.number_input("Additional Products/Services (%)", value=3)
quote_win_rate = st.number_input("Quote Win Increase (%)", value=3)
job_mix_improvement = st.number_input("Job Mix Improvement (%)", value=3)

# Calculate results
current_profit = revenue * (net_margin / 100)
improved_revenue = revenue * (1 + (pricing_increase + additional_products + quote_win_rate + job_mix_improvement) / 100)
reduced_costs = revenue * (cost_decrease / 100)
improved_profit = (improved_revenue - reduced_costs) * (gross_margin / 100)

# Display results
st.markdown("## Your Business Profit Transformation")
st.markdown("### Here's what happens when you make just a few small improvements...")
st.write(f"**Current Situation**
Annual Revenue: ${revenue:,.0f}
Net Profit: ${current_profit:,.0f}")
st.write(f"**With Improvements**
New Annual Revenue: ${improved_revenue:,.0f}
New Net Profit: ${improved_profit:,.0f}")

st.markdown("### Breakdown of Improvements")
st.write(f"Cost Reduction ({cost_decrease}%): ${reduced_costs:,.0f}")
st.write(f"Pricing Increase ({pricing_increase}%): ${revenue * (pricing_increase / 100):,.0f}")
st.write(f"Additional Products ({additional_products}%): ${revenue * (additional_products / 100):,.0f}")
st.write(f"Quote Win Rate ({quote_win_rate}%): ${revenue * (quote_win_rate / 100):,.0f}")
st.write(f"Higher Profit Jobs ({job_mix_improvement}%): ${revenue * (job_mix_improvement / 100):,.0f}")

st.markdown("## 🔥 Additional Possibilities")
st.write(f"Additional Revenue per Year: ${improved_revenue - revenue:,.0f} ({((improved_revenue - revenue) / revenue) * 100:.1f}% increase)")
st.write(f"Additional Profit per Year: ${improved_profit - current_profit:,.0f} ({((improved_profit - current_profit) / current_profit) * 100:.1f}% increase)")

st.markdown("## Here's What Most Tradies Miss...")
st.write("These are just small tweaks and improvements in a few areas, and require little or no extra actual work by you or your team. Imagine the results if we did this across the 20 - 30 other areas of your business or if we focused on a few and achieved 10 - 15 or 20% plus improvements!!")
st.write("Most tradie businesses are leaking thousands of profits in key areas without even realising it. Small leaks that are costing you thousands - each and every month.")

st.markdown("### Want to find YOUR biggest Profit Leaks?")
st.write("Book a free 20 minute 'Profit Leak Finder Call' where we will:")
st.write("✅ Identify 2-3 of your biggest profit leaks
✅ Show you exactly how much they are costing you
✅ Give you step by step tools to immediately plug them
No sales pitch. No fluff. Just actionable advice you can use straight away.")

st.button("Book my Profit Leak Finder Call")
st.button("Send me my results")
st.button("Try different numbers")
