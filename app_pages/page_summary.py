import streamlit as st


def page_summary_body():

    image_path = "./assets/images/sale-study.jpg"

    st.image(image_path, caption='banner for predicing saleprice',
             use_column_width=True)

    st.write("### Quick Project Summary\n")

    st.write(
        "This project is an ML app specifically developed for the "
        "visualization and prediction of house prices in Ames, Iowa.\n\n"
        "The app offers users the following functionalities:\n"
        "* **Correlation Analysis:** The application allows users to identify "
        "the correlation between house attributes and the sale price.\n"
        "* **Sale Price Prediction:** The application provides a predictive "
        "model that enables users to obtain accurate estimates for "
        "the sale price.\n"
    )
    # text based on README file - "Dataset Content" section
    st.info("""
    **Project Terms & Jargons**\n

    - **Variables**: These refer to various attributes of a house, such as
     floor area, basement, and garage.
    - **Target Variable**: In this study, the target variable is
     'SalePrice', representing the price at which a house was sold.\n

    **Project Dataset**\n

    - The dataset comprises properties sold in Ames, Iowa. It includes details
     for 24 distinct features for each property, which have the potential
     to affect the price. These features cover different aspects of
     the houses, including floor area, basement, garage, kitchen, and
     year built. We use this dataset for studying correlated features,
     training our machine learning model, and predicting sale prices of
     properties in the area.\n
    - The dataset encompasses houses built from 1872 to 2010 and is
     sourced from
     [Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data).
    """
            )
    # Link to README file, users can have access to full project documentation
    st.write(
        f"For additional information, please visit and **read** the "
        f"** [Project's README file]"
        f"(https://github.com/Frangidha/PP5-Housing"
        f"-issue/blob/main/README.md)**."
    )

    # copied from README file - "Business Requirements" section
    st.success(
        "**Project Business Requirements:**\n\n"
        "1. The client is keen to understand how the various attributes "
        "of houses relate to their sale prices. "
        "As a result, they require data visualizations that depict the "
        "correlations between these attributes and the sale prices.\n\n"
        "2. The client also wishes to predict the sale price of her four "
        "inherited houses and any other house in Ames, Iowa."
    )
