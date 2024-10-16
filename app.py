import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Credit Card Transactions Analysis", layout="centered")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv('D:/github projects/Data Analysis/CreditCards.csv/CreditCards_cleaned.csv')
    # Check if the 'Date' column exists and convert it to datetime
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y', errors='coerce')
    return df

df = load_data()

# Function for the home page
def show_home():
    st.header('Welcome to Credit Card Transactions Data Analysis',divider= True)
    st.write("""
        This app provides an in-depth analysis of credit card transactions.
        You can explore various insights such as:
        - Spend by City, Card Type, and Expense Type.
        - Spend by Gender, including male and female-based spending patterns.
        - Monthly spending trends and much more!
        
        Use the sidebar to navigate through different analysis options.
    """)

# Function for the analysis page
def show_analysis():
    options = st.selectbox(
        "Choose Analysis", ['Choose Analysis'] + 
        ['City Spend', 'Card Type Spend', 'Expense Type Spend', 
         'Spend by Gender', 'Spend by Females via Card Type','Spend by Males via Card Type', 
         'Top 5 Cities by Transactions', 'Month-wise Spend', 
         'Men Spend via Expense Type']
    )

    # 1. City Spend
    if options == 'City Spend':
        st.header("Which city has spent the highest amount over the years?")
        if 'City' in df.columns and 'Amount' in df.columns:
            city_spend = df.groupby('City')['Amount'].sum().sort_values(ascending=False).head(10)
            plt.figure(figsize=(12, 5))
            colors = plt.cm.Paired(range(len(city_spend)))
            city_spend.plot(kind='bar', color=colors, title="Top Cities by Total Spend")
            st.pyplot(plt)
            plt.clf()  # Clear the figure
            city_with_highest_spend = city_spend.idxmax()
            st.write(f"**{city_with_highest_spend}** has spent the highest amount over the years.")
        else:
            st.error("Required columns 'City' or 'Amount' not found.")

    # 2. Card Type Spend
    elif options == 'Card Type Spend':
        st.header("Which card type has the highest amount over the years?")
        if 'Card_Type' in df.columns and 'Amount' in df.columns:
            card_spend = df.groupby('Card_Type')['Amount'].sum().sort_values(ascending=False)
            bubble_sizes = (card_spend.values / card_spend.max()) * 1000
            plt.figure(figsize=(8, 5))
            plt.scatter(card_spend.index, card_spend.values, s=bubble_sizes, alpha=0.6, color='green')
            plt.title("Total Spend by Card Type (Bubble Plot)")
            st.pyplot(plt)
            plt.clf()  # Clear the figure
            highest_card_type = card_spend.idxmax()
            st.write(f"**{highest_card_type}** card has the highest amount over the years.")
        else:
            st.error("Required columns 'Card_Type' or 'Amount' not found.")

    # 3. Expense Type Spend
    elif options == 'Expense Type Spend':
        st.header("Which expense type has the highest amount over the years?")
        if 'Exp_Type' in df.columns and 'Amount' in df.columns:
            expense_spend = df.groupby('Exp_Type')['Amount'].sum().sort_values(ascending=False)
            plt.figure(figsize=(10, 6))
            expense_spend.plot(kind='barh', color='orange', title="Total Spend by Expense Type")
            st.pyplot(plt)
            plt.clf()  # Clear the figure
            highest_exp_year = expense_spend.idxmax()
            st.write(f"**{highest_exp_year}** expenses have accounted for the highest amounts over the years.")
        else:
            st.error("Required columns 'Exp_Type' or 'Amount' not found.")

    # 4. Spend by Gender
    elif options == 'Spend by Gender':
        st.header("What is the total amount spent between males and females?")
        if 'Gender' in df.columns and 'Amount' in df.columns:
            gender_spend = df.groupby('Gender')['Amount'].sum()
            plt.figure(figsize=(6, 6))
            plt.pie(gender_spend, labels=gender_spend.index, autopct='%1.1f%%', startangle=90, wedgeprops={'linewidth': 3})
            centre_circle = plt.Circle((0, 0), 0.70, fc='white')
            plt.gca().add_artist(centre_circle)
            plt.title("Total Spend by Gender (Doughnut Chart)")
            st.pyplot(plt)
            plt.clf()  # Clear the figure
            female_spend = gender_spend['F']
            male_spend = gender_spend['M']
            st.write(f"### Total amount spent by females: {female_spend}","(54.1 %)")
            st.write(f"### Total amount spent by males: {male_spend}","(45.9 %)")
        else:
            st.error("Required columns 'Gender' or 'Amount' not found.")

    # 5. Spend by Females via Card Type
    elif options == 'Spend by Females via Card Type':
        st.header("What is the total amount spent by females via Card Type?")
        if 'Gender' in df.columns and 'Card_Type' in df.columns and 'Amount' in df.columns:
            female_spend = df[df['Gender'] == 'F'].groupby('Card_Type')['Amount'].sum().sort_values(ascending=False)
            plt.figure(figsize=(12, 5))
            female_spend.plot(kind='bar', title="Total Spend by Females by Card Type", color=['lightgreen', 'violet', 'grey', 'orange'])
            st.pyplot(plt)
            plt.clf()  # Clear the figure
            st.write(female_spend)
        else:
            st.error("Required columns 'Gender', 'Card_Type', or 'Amount' not found.")

    # 6. What is the total amount spent by males via Card Type?
    elif options == 'Spend by Males via Card Type':
        st.header("What is the total amount spent by females via Card Type?")
        if 'Gender' in df.columns and 'Card_Type' in df.columns and 'Amount' in df.columns:
            male_spend = df[df['Gender'] == 'M'].groupby('Card_Type')['Amount'].sum().sort_values(ascending=False)
            plt.figure(figsize=(12, 5))
            male_spend.plot(kind='bar', title="Total Spend by Males by Card Type", ylabel="Total Spend (in millions)", xlabel="Card Type",color = ['lightblue','violet','gold','orange'])
            st.pyplot(plt)
            plt.clf()
            st.write(male_spend)
        else:
            st.error("Required columns 'Gender', 'Card_Type', or 'Amount' not found.")
        
    # 7. Top 5 Cities by Transactions
    elif options == 'Top 5 Cities by Transactions':
        st.header("Top 5 cities with the maximum transactions")
        if 'City' in df.columns:
            city_transactions = df['City'].value_counts().head(5)
            colors = sns.color_palette("Blues", len(city_transactions))
            city_transactions.plot(kind='bar', title="Top 5 Cities by Number of Transactions", color=colors)
            st.pyplot(plt)
            plt.clf()  # Clear the figure
            st.write(city_transactions)
        else:
            st.error("Required column 'City' not found.")

    # 8. Month-wise Spend
    elif options == 'Month-wise Spend':
        st.header("Month-wise spend across the years in descending order")
        if 'Month' in df.columns and 'Amount' in df.columns:
            monthly_spend = df.groupby('Month')['Amount'].sum().sort_values(ascending=False)
            plt.figure(figsize=(10, 5))
            monthly_spend.plot(kind='line', marker='o', color='purple')
            st.pyplot(plt)
            plt.clf()  # Clear the figure
            st.write(monthly_spend)
        else:
            st.error("Required columns 'Month' or 'Amount' not found.")

    # 9. Men Spend via Expense Type
    elif options == 'Men Spend via Expense Type':
        st.header("Total amount spent by men via expense type")
        if 'Gender' in df.columns and 'Exp_Type' in df.columns and 'Card_Type' in df.columns and 'Amount' in df.columns:
            expense_data = df[df['Gender'] == 'M'].groupby(['Exp_Type', 'Card_Type'])['Amount'].sum().unstack()
            expense_data.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='Set2')
            st.pyplot(plt)
            plt.clf()  # Clear the figure
            st.write(expense_data)
        else:
            st.error("Required columns 'Gender', 'Exp_Type', 'Card_Type', or 'Amount' not found.")

def show_about_dataset():
    st.title('About Dataset')
    st.subheader('Overview of Dataset:')
    st.write("""
        It contains 9 columns and 26,052 rows of credit card transactions.
        The 9 columns are as follows:
        - **Index**: Serial No for each transaction.
        - **City**: Place where the transaction took place.
        - **Date**: Day the transaction took place (Start Date is 4th Oct 2013, End Date is 26th May 2015).
        - **Card Type**: Category/Type of Card (Silver, Signature, Platinum, Gold).
        - **Exp Type**: Type of expense the card was used for (Fuel, Food, Entertainment, Grocery, Bills, Travel).
        - **Gender**: F for Female, M for Male.
        - **Amount**: Amount spent on each transaction.
        - **Year**: Year of the transaction.
        - **Month**: Month of the transaction.
""")
    st.write("""
        ### **Data Cleaning**:
        There were null values or missing values in the dataset, which were dropped using `dropna()`. 
        Two changes were made to the column names:
        - `Card Type` was changed to **Card_Type**
        - `Exp Type` was changed to **Exp_Type** for Data analysis purposes.

        ### **Data Analysis**:
        The idea behind doing the analysis was to find patterns or insights that could help the credit card company in formulating strategies for decision-making purposes. 
        The questions for the analysis were formulated based on this objective.
""")



def show_about():
    st.title('Conclusion & Analysis ')
    st.subheader('Key Insights from Credit Card Transaction Analysis')
    st.write(
    """

    1. **City Spending Patterns**:
       - **Greater Mumbai** leads in total spending; however, the difference in spending amounts is minimal compared to **Bengaluru, Ahmedabad**, and **Delhi**. 
       - This suggests a competitive market where targeted strategies could enhance engagement in other cities.

    2. **Card Type Preferences**:
       - **Females** favor **Silver Cards**, while **Males** prefer **Platinum Cards**, with **Gold Cards** being the least popular among men. 
       - The limited difference in spending across card types for males indicates potential for promoting Gold Cards through targeted marketing campaigns to increase awareness and usage.

    3. **Expense Categories**:
       - **Bills** account for the highest expenditures, whereas **Travel** represents the lowest. 
       - The lack of data on food spending (offline and online) presents an opportunity for collaboration with food delivery services and restaurants to increase engagement through discounts, rewards, and cashback offers.

    4. **Gender Spending Analysis**:
       - **Females** have a total spending of **₹2,205,311,030**, representing **54.1%** of transactions, while **Males** spent **₹1,869,522,343**, or **45.9%** of transactions. 
       - This suggests that females are more engaged in higher-value transactions, which credit card companies could leverage for tailored promotions and features aimed at female consumers. Conversely, strategies to boost spending among males may help close this gap.

    5. **Monthly Spending Trends**:
       - Spending peaks in **January**, followed by **October** and **December**, likely due to holiday-related purchases. 
       - Conversely, spending declines during **June**, **July**, and **September**, indicating a potential for targeted promotions during these slower months to enhance engagement.

    6. **Usage Patterns by Card Type**:
       - Males predominantly utilize **Gold** and **Platinum Cards** for **Fuel** and **Entertainment** expenses, while **Silver Cards** demonstrate consistent usage across categories. 
       - The lower travel spending suggests an opportunity for credit card companies to enhance travel-related incentives, potentially increasing engagement among male users.

    ### **Conclusion**
    The analysis reveals notable trends and opportunities for credit card companies to optimize their marketing strategies and enhance user engagement. By tailoring promotions based on gender-specific spending habits, focusing on underperforming categories, and addressing seasonal spending variations, companies can effectively maximize their outreach and engagement.

    """
)



def show_contact():
    st.title('Contact Me')
    st.markdown("""
    ### Get in touch:
    
    - Email: [anirudhr2509@gmail.com](mailto:anirudhr2509@gmail.com)
    - LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/anirudh-r-4b5038278)
    - GitHub: [GitHub Profile](https://github.com/Anirudh-sys)
    - Portfolio: [My Portfolio Website](https://your-portfolio.com)
    
    Feel free to reach out if you have any questions or collaboration ideas!
    """)

# Main function to handle page navigation

def main():

    nav_container = st.sidebar

    # Default page
    if 'page' not in st.session_state:
        st.session_state.page = "Home"

    with nav_container:
        st.title("Select Page")  
        if st.button("Home"):
            st.session_state.page = "Home"
        if st.button("Analysis"):
            st.session_state.page = "Analysis"
        if st.button("About Dataset"):
            st.session_state.page = "About Dataset"
        if st.button("Conclusion & Analysis"):
            st.session_state.page = "Conclusion & Analysis"
        if st.button("Contact"):
            st.session_state.page = "Contact"

    # Render the selected page
    if st.session_state.page == "Home":
        show_home()
    elif st.session_state.page == "Analysis":
        show_analysis()
    elif st.session_state.page == "About Dataset":
        show_about_dataset()
    elif st.session_state.page == "Conclusion & Analysis":
        show_about()
    elif st.session_state.page == "Contact":
        show_contact()

if __name__ == "__main__":
    main()
