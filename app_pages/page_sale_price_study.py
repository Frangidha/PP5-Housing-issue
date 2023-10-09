from src.data_management import load_house_prices_data
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


def page_sale_price_study_body():

    # load data
    df = load_house_prices_data()

    # hard copied from correlation study notebook
    important_variables = ['OverallQual', 'GrLivArea',
                           'GarageArea', 'TotalBsmtSF',
                           '1stFlrSF', 'YearBuilt']

    st.write("### House Sale Prices Study")

    st.info(
        f"#### Business Requirement 1\n"
        f"* The client is interested in discovering how the house "
        f"attributes correlate with the sale price. Therefore, the "
        f"client expects data visualizations of the correlated "
        f"variables against the sale price to show that."
    )

    # inspect data
    if st.checkbox("Inspect House Prices Dataset"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows.")

        st.write(df.head(10))

    st.write("---")

    # Correlation Study Summary
    st.write(
        f"* A study of the data was conducted in the notebook to better to "
        f"understand how the variables are correlated to `SalePrice`.\n\n"
        f"The most correlated variables are: **{important_variables}**"
    )

    # Text based on "Sale Price Study" notebook - "Conclusions" section
    st.info(
        "Through a thorough analysis of correlation coefficients and careful"
        "examination of plots, we have unveiled insights into factors"
        "influencing house sale prices:\n\n"
        "- **OverallQual**: Higher quality ratings relate to "
        "higher sale prices.\n"
        "- **GrLivArea**: Larger living areas correspond to higher prices.\n"
        "- **GarageArea**: More garage space is associated "
        "with higher prices.\n"
        "- **TotalBsmtSF**: Larger basements tend to "
        "result in higher prices.\n"
        "- **YearBuilt**: Newer houses generally command higher prices.\n"
        "- **1stFlrSF**: More first-floor space tends to lead "
        "to higher prices."
    )

    st.write(
        "Scatter plots illustrate the correlation between each"
        "variable and 'SalePrice':")

    # Copied from "Sale Price Study" notebook - "EDA on selected variables"
    df_eda = df.filter(important_variables + ['SalePrice'])

    # Individual plots per variable
    if st.checkbox("Sale Price Correlation Per Variable"):
        sale_price_per_variable(df_eda, important_variables)

    st.write(
        f"* Heatmap showing the correlation between the relevant variables: "
    )

    # Plotting Heatmap
    if st.checkbox("Show Correlation Heatmap"):
        plot_heatmap(df_eda, important_variables)

    st.success(
        """
**Finding:**\n\n

Our comprehensive analysis, including correlation assessments
 and plot examinations,
 provides valuable insights into the first business question concerning house
 attributes and their impact on typical Sale Price:\n

- It is evident that Sale Price tends to be higher for houses with
 specific attributes, making these attributes crucial in
 determining property value.\n

- Remarkably, the attribute with the most substantial correlation to Sale
 Price is Overall Quality. This implies that houses with superior quality
 ratings generally command higher prices, underlining the significance of
 quality in the real estate market.\n

- Additionally, variables such as Above Ground Living Area, Garage Area,
 Total Basement Square Footage, and First Floor Square Footage exhibit
 robust positive correlations with Sale Price.
 These attributes play a pivotal role in influencing property prices.\n

- Year Built, while not as strongly correlated as some attributes,
 still demonstrates moderate positive correlations with Sale Price,
 signifying that newer houses tend to fetch higher
 prices in comparison to older properties.\n
"""

    )


# Iterate over each relevant variable and plot its relationship with SalePrice
def sale_price_per_variable(df_eda, important_variables):
    target_var = 'SalePrice'
    for col in important_variables:
        plot_numerical(df_eda, col, target_var)
        st.write("\n\n")


# function created using "Sale Price Study" notebook - "Analyzing Correlations"
def plot_numerical(df_eda, col, target_var):

    fig = plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df_eda, x=col, y='SalePrice')
    plt.title(f"{col} vs SalePrice", fontsize=20, y=1.05)
    plt.xlabel(col)
    plt.ylabel('SalePrice')
    st.pyplot(fig)  # Display the matplotlib plot using Streamlit


def plot_heatmap(df_eda, important_variables):

    # Create a new DataFrame with the selected variables
    heatmap_vars = df_eda.copy()

    # Calculate the correlation matrix
    correlation_matrix = heatmap_vars.corr()

    # Plot the heat map
    fig = plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True)
    plt.title("Correlation Matrix", fontsize=20)
    st.pyplot(fig)
