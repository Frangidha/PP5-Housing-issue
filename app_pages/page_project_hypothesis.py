import streamlit as st


def page_project_hypothesis_body():

    st.write("### Project Hypothesis")

    st.info(
        f"Based on our comprehensive data analysis, where we examined various "
        f" variables and conducted correlation studies,"
        f"we have found strong evidence supporting the following hypotheses:"
    )

    # conclusions taken from "02 - Sale Price Study" notebook
    st.success("""
        Hypotheses for House Sale Prices
        These hypotheses are based on the observed correlations and provide
         insights
         into key factors influencing house sale prices during data
         visualization.\n

        Hypothesis 1: Overall Quality\n
        - **Hypothesis**: Quality significantly impacts selling price.\n
        - **Explanation**: Strong correlation; higher quality
         commands higher prices.\n

        Hypothesis 2: Above Ground Living Area\n
        - **Hypothesis**: Living area affects selling price.\n
        - **Explanation**: Robust positive correlation; larger spaces
         mean higher prices. \n

        Hypothesis 3: Year Built
        - **Hypothesis**: Year built moderately impacts price.\n
        - **Explanation**: Moderate positive correlation; newer
         houses command higher prices.\n

        Hypothesis 4: Garage Area\n
        - **Hypothesis**: Garage size plays a role.\n
        - **Explanation**: Strong correlation; larger garages
         mean higher selling prices.\n
        """)

    st.info(
        f"**Key Findings**: Factors Influencing Houses Prices\n\n"
        f"Overall, by analyzing these correlations and considering the top "
        f"correlated variables, we have confirmed our hypotheses that the "
        f"quality of the house and the size of the property and addition of a"
        f"garage play significant"
        f"roles in determining the sale price. Additionally, newer houses tend"
        f" to command higher prices compared to older ones. The correlation "
        f" This makes sense because newer houses are often of higher quality "
        f" coefficients and visualizations provide robust evidence to support"
        f" these findings."
    )
